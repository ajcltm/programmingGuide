
- RegisterDTO
~~~java
package org.hgtech.worksystem.domain;  
  
import lombok.*;  
  
import java.time.LocalDateTime;  
  
@Getter  
@Setter  
@ToString  
@Builder  
@AllArgsConstructor  
@NoArgsConstructor  
public class FileVO {
    Integer wfId;
    LocalDateTime wfRegDate;
    LocalDateTime wfModDate;
    String wfName;
    String wfPath;
    String wfType;
    Integer wfWkId;
    Integer wfLgId;
}
~~~

- FileIO Controller
~~~java
package org.hgtech.worksystem.controller;  
  
import org.hgtech.worksystem.service.FileIOService;  
import org.hgtech.worksystem.service.FileService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.core.io.FileSystemResource;  
import org.springframework.core.io.Resource;  
import org.springframework.http.HttpHeaders;  
import org.springframework.http.HttpStatus;  
import org.springframework.http.ResponseEntity;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.*;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Paths;  
import java.util.List;  
  
@Controller  
@RequestMapping("/workSystem/files")  
public class FileIOController {  
  
    @Autowired  
    FileIOService fileIOService;  
  
    @Autowired  
    FileService fileService;  
  
    @PostMapping("/upload")  
    public ResponseEntity<String> uploadFile(@RequestParam List<MultipartFile> files, Integer wfWkId) throws IOException {  
        for (MultipartFile file : files) {  
            fileIOService.save(file, wfWkId);  
            }  
        return ResponseEntity.ok("Files uploaded");  
    }  
  
    @GetMapping("/download")  
    public ResponseEntity<Resource> downloadFile(@RequestParam int wfId) throws IOException {  
        File file = fileIOService.load(wfId);  
        Resource resource = new FileSystemResource(file);  
        String contentType = Files.probeContentType(Paths.get(file.getPath()));  
        if(contentType == null) {  
            contentType = "application/octet-stream";  
        }  
  
        return ResponseEntity.ok()  
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + file.getName() + "\"")  
                .header(HttpHeaders.CONTENT_TYPE, contentType)  
                .body(resource);  
    }  
  
    @GetMapping("/remove")  
    public ResponseEntity<String> remove(@RequestParam int wfId) {  
        fileIOService.remove(wfId);  
        return ResponseEntity.status(HttpStatus.CREATED).body("removed : " + wfId);  
    }
}
~~~

- FileIO service
~~~java
package org.hgtech.worksystem.service;  
  
import org.hgtech.worksystem.DTO.FileDTO;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Paths;  
import java.util.UUID;  
  
@Service  
public class FileIOService {  
    final private String fileDir = "c://Users/ajcltm/uploads/workSystem/";  
  
    @Autowired  
    FileService fileService;  
  
    public void save(MultipartFile file, Integer wfWkId, Integer wfLgId) throws IOException {
        String uuid = UUID.randomUUID().toString();
        String fileName = file.getOriginalFilename();
        String saveName = uuid + "_" + fileName;
        String filePath = fileDir + saveName;
        String fileType = Files.probeContentType(Paths.get(fileDir).resolve(fileName).normalize());
  
//        파일저장
        file.transferTo(new File(filePath));
  
//        파일 정보 db 기록  
        FileDTO fileDTO = FileDTO.builder().wfName(fileName).wfPath(filePath).wfType(fileType).wfWkId(wfWkId).wfLgId(wfLgId).build();  
        fileService.register(fileDTO);  
    }
    
    public File load(int id) {  
//        파일 기록 가져오기  
        FileDTO fileDTO = fileService.getByWfId(id);
//        파일 불러오기  
        File file = new File(fileDTO.getWfPath());
        System.out.println("file exists : " + file.exists());
        return file;
  
    }  
  
    public void remove(int id) {  
        //        파일 기록 가져오기
        FileDTO fileDTO = fileService.getByWfId(id);
//        파일 불러오기  
        File file = new File(fileDTO.getWfPath());
        System.out.println(file.exists());
        if (file.exists()) {
            file.delete();
        }  
        fileService.remove(id);
    }
}
~~~