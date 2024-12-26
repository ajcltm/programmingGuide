- service
~~~java
package org.hgtech.webdevsys.service;  
  
import org.hgtech.webdevsys.DTO.WebInfoDTO;  
import org.hgtech.webdevsys.domain.WebInfoVO;  
import org.hgtech.webdevsys.repository.WebInfoRepository;  
import org.modelmapper.ModelMapper;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
  
import java.util.List;  
import java.util.stream.Collectors;  
  
@Service  
public class WebInfoService {  
  
    @Autowired  
    WebInfoRepository webInfoRepository;  
  
    @Autowired  
    ModelMapper modelMapper;  
  
    public void register(WebInfoDTO webInfoDTO) {  
        WebInfoVO webInfoVO = modelMapper.map(webInfoDTO, WebInfoVO.class);  
        webInfoRepository.insert(webInfoVO);  
    }  
  
    public List<WebInfoDTO> getAll() {  
        List<WebInfoVO> webInfoVOList = webInfoRepository.selectAll();  
        List<WebInfoDTO> webInfoDTOList = webInfoVOList.stream().map(vo -> modelMapper.map(vo, WebInfoDTO.class)).collect(Collectors.toList());  
        return webInfoDTOList;  
    }  
  
    public WebInfoDTO getLast() {  
        WebInfoVO webInfoVO = webInfoRepository.selectLast();  
        WebInfoDTO webInfoDTO = modelMapper.map(webInfoVO, WebInfoDTO.class);  
        return webInfoDTO;  
    }  
  
    public WebInfoDTO getById(int id) {  
        WebInfoVO webInfoVO = webInfoRepository.selectById(id);  
        if (webInfoVO==null){  
            return null;  
        }  
        WebInfoDTO webInfoDTO = modelMapper.map(webInfoVO, WebInfoDTO.class);  
        return webInfoDTO;  
    }  
  
    public List<WebInfoDTO> getByParentId(int id) {  
        List<WebInfoVO> webInfoVOList = webInfoRepository.selectByParentId(id);  
        List<WebInfoDTO> webInfoDTOList = webInfoVOList.stream().map(vo -> modelMapper.map(vo, WebInfoDTO.class)).collect(Collectors.toList());  
        return webInfoDTOList;  
    }  
  
    public void remove(int id) {  
        webInfoRepository.delete(id);  
    }  
  
    public void modify(WebInfoDTO webInfoDTO) {  
        WebInfoVO webInfoVO = modelMapper.map(webInfoDTO, WebInfoVO.class);  
        webInfoRepository.update(webInfoVO);  
    }  
}
~~~

- test
~~~java
package org.hgtech.webdevsys.serviceTest;  
  
import org.hgtech.webdevsys.DTO.WebInfoDTO;  
import org.hgtech.webdevsys.service.WebInfoService;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.boot.test.context.SpringBootTest;  
  
import java.time.LocalDateTime;  
import java.util.ArrayList;  
import java.util.List;  
import java.util.Random;  
import java.util.UUID;  
  
@SpringBootTest  
public class WebInfoServiceTest {  
  
    @Autowired  
    WebInfoService webInfoService;  
  
    private WebInfoDTO createWebInfoDTO() {  
        LocalDateTime dateTime = LocalDateTime.now();  
        String randomText = UUID.randomUUID().toString();  
        WebInfoDTO webInfoDTO = WebInfoDTO.builder().regDate(dateTime).modDate(dateTime).title(randomText + "_title").content(randomText + "content").comment(randomText + "_comment").build();  
        return webInfoDTO;  
    }  
  
    public WebInfoDTO createWebInfoDTO(int parentId) {  
        LocalDateTime now = LocalDateTime.now();  
        String randomText = UUID.randomUUID().toString();  
        WebInfoDTO webInfoDTO = WebInfoDTO.builder().regDate(now).modDate(now).title(randomText+"_title").content(randomText+"_content").comment(randomText+"comment").parentId(parentId).build();  
        return webInfoDTO;  
    }  
  
    private WebInfoDTO getTargetDTO() {  
        WebInfoDTO webInfoDTO = createWebInfoDTO();  
        webInfoService.register(webInfoDTO);  
        WebInfoDTO target = webInfoService.getLast();  
        return target;  
    }  
  
    public List<WebInfoDTO> getTargetDTO(int parentId) {  
        for (int i=0; i<5; i++) {  
            WebInfoDTO webInfoDTO = createWebInfoDTO(parentId);  
            webInfoService.register(webInfoDTO);  
        }  
        List<WebInfoDTO> webInfoDTOList = webInfoService.getAll();  
        List<WebInfoDTO> targetDTO = webInfoDTOList.subList(webInfoDTOList.size()-5, webInfoDTOList.size());  
        return targetDTO;  
    }  
  
    private List<WebInfoDTO> getTargetDTOList(int size) {  
        List<WebInfoDTO> targetDTOList = new ArrayList<>();  
        for (int i = 0; i < size; i++) {  
            WebInfoDTO webInfoDTO = createWebInfoDTO();  
            webInfoService.register(webInfoDTO);  
            WebInfoDTO targetDTO = webInfoService.getLast();  
            targetDTOList.add(targetDTO);  
        }  
        return targetDTOList;  
    }  
  
    @Test  
    public void registerTest() {  
        WebInfoDTO webInfoDTO = createWebInfoDTO();  
        webInfoService.register(webInfoDTO);  
    }  
  
    @Test  
    public void getLastTest() {  
        WebInfoDTO target = createWebInfoDTO();  
        webInfoService.register(target);  
        WebInfoDTO test = webInfoService.getLast();  
        Assertions.assertEquals(target.getTitle(), test.getTitle());  
    }  
  
    @Test  
    public void getAllTest() {  
        int size = 10;  
        List<WebInfoDTO> target = getTargetDTOList(size);  
        List<WebInfoDTO> test = webInfoService.getAll();  
        Assertions.assertEquals(target.get(size - 1).getTitle(), test.get(test.size() - 1).getTitle());  
        Assertions.assertEquals(target.get(size - 3).getTitle(), test.get(test.size() - 3).getTitle());  
    }  
  
    @Test  
    public void getByIdTest() {  
        WebInfoDTO target = getTargetDTO();  
        WebInfoDTO test = webInfoService.getById(target.getId());  
        Assertions.assertEquals(target.getTitle(), test.getTitle());  
    }  
  
    @Test  
    public void getByParentIdTest() {  
        Random random = new Random();  
        int parentId = random.nextInt(1000);  
        List<WebInfoDTO> target = getTargetDTO(parentId);  
        List<WebInfoDTO> test = webInfoService.getByParentId(parentId);  
        Assertions.assertEquals(target.get(0).getTitle(), test.get(0).getTitle());  
    }  
  
    @Test  
    public void removeTest() {  
        WebInfoDTO target = getTargetDTO();  
        webInfoService.remove(target.getId());  
        WebInfoDTO test = webInfoService.getById(target.getId());  
        Assertions.assertNull(test);  
    }  
  
    @Test  
    public void modifyTest(){  
        WebInfoDTO target = getTargetDTO();  
        String modified = UUID.randomUUID()+"modified";  
        target.setTitle(modified);  
        webInfoService.modify(target);  
        WebInfoDTO test = webInfoService.getById(target.getId());  
        Assertions.assertEquals(target.getTitle(), test.getTitle());  
    }  
}
~~~
