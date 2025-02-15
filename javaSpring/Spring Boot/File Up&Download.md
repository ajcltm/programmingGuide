
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
package org.hgtech.pnpsecure.controller;  
  
import org.hgtech.pnpsecure.service.FileIOService;  
import org.hgtech.pnpsecure.service.FileService;  
import org.springframework.stereotype.Controller;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.core.io.FileSystemResource;  
import org.springframework.core.io.Resource;  
import org.springframework.http.HttpHeaders;  
import org.springframework.http.HttpStatus;  
import org.springframework.http.ResponseEntity;  
import org.springframework.web.bind.annotation.*;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Paths;  
import java.util.List;  
  
@Controller  
public class FileIOController {  
    @Autowired  
    FileIOService fileIOService;  
  
    @Autowired  
    FileService fileService;  
  
    @PostMapping("/upload")  
    public ResponseEntity<String> uploadFile(@RequestParam List<MultipartFile> files, String foreignId) throws IOException {  
        for (MultipartFile file : files) {  
            fileIOService.save(file, foreignId);  
        }  
        return ResponseEntity.ok("Files uploaded");  
    }  
  
    @GetMapping("/download")  
    public ResponseEntity<Resource> downloadFile(@RequestParam String foreignId) throws IOException {  
        File file = fileIOService.load(foreignId);  
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
    public ResponseEntity<String> remove(@RequestParam String foreignId) {  
        fileIOService.remove(foreignId);  
        return ResponseEntity.status(HttpStatus.CREATED).body("removed : " + foreignId);  
    }  
}
~~~

- FileIO service
~~~java
package org.hgtech.pnpsecure.service;  
  
import org.hgtech.pnpsecure.DTO.FileDTO;  
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
    final private String fileDir = "c://Users/ajcltm/uploads/pnpsecure/";  
  
    @Autowired  
    FileService fileService;  
  
    public void save(MultipartFile file, String foreignId) throws IOException {  
        String uuid = UUID.randomUUID().toString();  
        String fileName = file.getOriginalFilename();  
        String saveName = uuid + "_" + fileName;  
        String filePath = fileDir + saveName;  
        String fileType = Files.probeContentType(Paths.get(fileDir).resolve(fileName).normalize());  
  
//        파일저장  
        file.transferTo(new File(filePath));  
  
//        파일 정보 db 기록  
        FileDTO fileDTO = FileDTO.builder().name(fileName).path(filePath).type(fileType).foreignId(foreignId).build();  
        fileService.register(fileDTO);  
    }  
  
    public File load(String id) {  
//        파일 기록 가져오기  
        FileDTO fileDTO = fileService.getById(id);  
//        파일 불러오기  
        File file = new File(fileDTO.getPath());  
        System.out.println("file exists : " + file.exists());  
        return file;  
  
    }  
  
    public void remove(String id) {  
        //        파일 기록 가져오기  
        FileDTO fileDTO = fileService.getById(id);  
//        파일 불러오기  
        File file = new File(fileDTO.getPath());  
        System.out.println(file.exists());  
        if (file.exists()) {  
            file.delete();  
        }  
        fileService.remove(id);  
    }  
}
~~~