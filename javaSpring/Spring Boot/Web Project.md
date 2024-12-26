
### 첨부파일 업로드

- controller
~~~java
package org.hgtech.economicsys.controller;  
  
import org.hgtech.economicsys.service.FileService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.core.io.FileSystemResource;  
import org.springframework.core.io.Resource;  
import org.springframework.http.HttpHeaders;  
import org.springframework.http.ResponseEntity;  
import org.springframework.web.bind.annotation.*;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Path;  
import java.nio.file.Paths;  
  
@RestController  
public class FileController {  
  
    @Autowired  
    FileService fileService;  
  
    @PostMapping("/upload")  
    public String handleFileUpload(@RequestParam MultipartFile file) throws IOException {  
        String result = fileService.uploadFile(file);  
        return result;  
    }
~~~

- service
~~~java
package org.hgtech.economicsys.service;  
 
import org.springframework.stereotype.Service;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
  
@Service  
public class FileService {  
  
    private final String uploadDir = "c://Users/ajcltm/uploads/";  
  
    public String uploadFile(MultipartFile file) throws IOException {  
        String fileName = file.getOriginalFilename();  
        String filePath = uploadDir + fileName;  
  
        File dest = new File(filePath);  
        file.transferTo(dest);  
  
        return "upload complete : " + filePath;  
    }  
  
}
~~~

### 첨부파일 다운로드

- controller
~~~java
package org.hgtech.economicsys.controller;  
  
import org.hgtech.economicsys.service.FileService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.core.io.FileSystemResource;  
import org.springframework.core.io.Resource;  
import org.springframework.http.HttpHeaders;  
import org.springframework.http.ResponseEntity;  
import org.springframework.web.bind.annotation.*;  
import org.springframework.web.multipart.MultipartFile;  
  
import java.io.File;  
import java.io.IOException;  
import java.nio.file.Files;  
import java.nio.file.Path;  
import java.nio.file.Paths;  
  
@RestController  
public class FileController {  
  
    @Autowired  
    FileService fileService;  
  
    @GetMapping("/download/{filename}")  
    public ResponseEntity<Resource> downloadFile(@PathVariable String filename) throws IOException{  
        String uploadDir = "c://Users/ajcltm/uploads/";  
        Path filePath = Paths.get(uploadDir).resolve(filename).normalize();  
        File file = filePath.toFile();  
  
        if(!file.exists()) {  
            return ResponseEntity.notFound().build();  
        }  
  
        Resource resource = new FileSystemResource(file);  
        String contentType = Files.probeContentType(filePath);  
  
        if(contentType == null) {  
            contentType = "application/octet-stream";  
        }  
  
        return ResponseEntity.ok()  
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + resource.getFilename() + "\"")  
                .header(HttpHeaders.CONTENT_TYPE, contentType)  
                .body(resource);  
    }  
}
~~~
