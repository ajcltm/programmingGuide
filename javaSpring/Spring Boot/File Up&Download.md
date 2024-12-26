### upload
- RegisterDTO
~~~java
package org.hgtech.guidearchiveweb.DTO;  
  
import lombok.Data;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.util.List;  
  
@Data  
public class RegisterDTO {  
    String title;  
    String content;  
    List<MultipartFile> files;  
}
~~~
- Controller
~~~java
package org.hgtech.guidearchiveweb.controller;  
  
import lombok.extern.log4j.Log4j2;  
  
import org.hgtech.guidearchiveweb.DTO.FileDTO;  
import org.hgtech.guidearchiveweb.DTO.RegisterDTO;  
import org.hgtech.guidearchiveweb.DTO.SaveFileResultDTO;  
import org.hgtech.guidearchiveweb.service.FileInfoService;  
import org.hgtech.guidearchiveweb.service.FileService;  
import org.hgtech.guidearchiveweb.service.GuideService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.http.MediaType;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.*;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.IOException;  
import java.util.List;  
  
@Controller  
@Log4j2  
@RequestMapping("/guide")  
public class RegisterController {  
  
    @Autowired  
    private FileService fileService;  
  
    @Autowired  
    private FileInfoService fileInfoService;  
  
    @Autowired  
    private GuideService guideService;  
  
    @GetMapping("/register")  
    public String getRegister() {  
        return "register";  
    }  
  
    @PostMapping(value = "/register", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)  
    public String postRegister(RegisterDTO registerDTO) throws IOException {  
        log.info("title : " + registerDTO.getTitle());  
  
        guideService.register(registerDTO.getTitle(), registerDTO.getContent());  
        int foreign_id = guideService.getLast().getGid();  
        List<MultipartFile> files = registerDTO.getFiles();  
        for (MultipartFile file : files) {  
            SaveFileResultDTO resultDTO = fileService.saveFile(file);  
            FileDTO fileDTO = FileDTO.builder().foreign_id(foreign_id).file_name(resultDTO.getFileName()).file_path(resultDTO.getFilePath()).file_type(resultDTO.getFileType()).build();  
            fileInfoService.register(fileDTO);  
        }  
        return "redirect:/guide/list";  
    }  
}
~~~

- file service
~~~java
package org.hgtech.guidearchiveweb.service;  
  
import org.hgtech.guidearchiveweb.DTO.FileDTO;  
import org.hgtech.guidearchiveweb.DTO.SaveFileResultDTO;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Path;  
import java.nio.file.Paths;  
import java.util.List;  
import java.util.UUID;  
  
@Service  
public class FileService {  
  
    final private String fileDir = "c://Users/ajcltm/uploads/guide/";  
  
    @Autowired  
    FileInfoService fileInfoService;  
  
    public SaveFileResultDTO saveFile(MultipartFile file) throws IOException {  
  
        String uuid = UUID.randomUUID().toString();  
        String fileName = file.getOriginalFilename();  
        String saveName = uuid + "_" + fileName;  
        String filePath = fileDir + saveName;  
        file.transferTo(new File(filePath));  
        String fileType = Files.probeContentType(Paths.get(fileDir).resolve(fileName).normalize());  
  
        SaveFileResultDTO saveFileResultDTO = SaveFileResultDTO.builder().fileName(fileName).saveName(saveName).filePath(filePath).fileType(fileType).build();  
        return saveFileResultDTO;  
    }
}
~~~

- saveFileResultDTO
~~~java
package org.hgtech.guidearchiveweb.DTO;  
  
import lombok.Builder;  
import lombok.Data;  
  
@Data  
@Builder  
public class SaveFileResultDTO {  
    String uuid;  
    String fileName;  
    String saveName;  
    String filePath;  
    String fileType;  
}
~~~

- file info DTO
~~~java
package org.hgtech.guidearchiveweb.DTO;  
  
import lombok.*;  
  
@Data  
@Builder  
@ToString  
@AllArgsConstructor  
@NoArgsConstructor  
public class FileDTO {  
    int id;  
    int foreign_id;  
    String file_name;  
    String file_path;  
    String file_type;  
}
~~~

### Download

- controller

~~~java
package org.hgtech.guidearchiveweb.controller;  
  
import org.hgtech.guidearchiveweb.service.FileService;  
import org.springframework.core.io.FileSystemResource;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.core.io.Resource;  
import org.springframework.http.HttpHeaders;  
import org.springframework.http.ResponseEntity;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestParam;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Paths;  
  
@Controller  
@RequestMapping("/guide")  
public class DownloadController {  
  
    @Autowired  
    FileService fileService;  
  
    @GetMapping("/download")  
    public ResponseEntity<Resource> downloadFile(@RequestParam int id) throws IOException {  
  
        File file = fileService.downloadFile(id);  
        System.out.println("[download] filePath"+file.getPath()); 
        String fileName = fileInfoService.getById(id).getFileName();
  
        if(!file.exists()) {  
            return ResponseEntity.notFound().build();  
        }
  
        Resource resource = new FileSystemResource(file);  
        String contentType = Files.probeContentType(Paths.get(file.getPath()));  
  
        if(contentType == null) {  
            contentType = "application/octet-stream";  
        }  
  
        return ResponseEntity.ok()  
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + fileName + "\"")  
                .header(HttpHeaders.CONTENT_TYPE, contentType)  
                .body(resource);  
    }  
  
}
~~~

- file service
~~~java
package org.hgtech.guidearchiveweb.service;  
  
import org.hgtech.guidearchiveweb.DTO.FileDTO;  
import org.hgtech.guidearchiveweb.DTO.SaveFileResultDTO;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Path;  
import java.nio.file.Paths;  
import java.util.List;  
import java.util.UUID;  
  
@Service  
public class FileService {  
  
    final private String fileDir = "c://Users/ajcltm/uploads/guide/";  
  
    @Autowired  
    FileInfoService fileInfoService;  
  
    public File downloadFile(int id) {  
        FileDTO fileDTO = fileInfoService.getById(id);  
        File file = new File(fileDTO.getFile_path());  
        return file;  
    }    
}
~~~

- file remove
~~~java
package org.hgtech.guidearchiveweb.service;  
  
import org.hgtech.guidearchiveweb.DTO.FileDTO;  
import org.hgtech.guidearchiveweb.DTO.SaveFileResultDTO;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Path;  
import java.nio.file.Paths;  
import java.util.List;  
import java.util.UUID;  
  
@Service  
public class FileService {  
  
    final private String fileDir = "c://Users/ajcltm/uploads/guide/";  
  
    @Autowired  
    FileInfoService fileInfoService;  
  
    public void removeFile(int id) {  
        FileDTO fileDTO = fileInfoService.getById(id);  
        File file = new File(fileDTO.getFile_path());  
        file.delete();  
    }  
  
}
~~~
