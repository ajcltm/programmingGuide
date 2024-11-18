
- SpringBootTest
~~~java
package org.hgtech.guidearchiveweb.controller;
  
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;    
  
@SpringBootTest
public class DownloadTest {  
  
    @Test  
    public void test() {  
		...
    }  
}
~~~

- MockMvc
~~~java
package org.hgtech.guidearchiveweb.controller;  
  
import org.junit.jupiter.api.Test;  

import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;  
  
@SpringBootTest  
@AutoConfigureMockMvc  
public class DownloadTest {
  
    @Autowired  
    private MockMvc mockMvc;  
  
    @Test  
    public void testRegister() throws Exception{  
        mockMvc.perform(get("/guide/download").param("id", "71"))  
                .andExpect(status().isOk());  
    }  
}
~~~

- controller 테스트
~~~java
package org.hgtech.guidearchiveweb.controller;  
  
import org.junit.jupiter.api.Test;

import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;

import org.springframework.mock.web.MockMultipartFile;
  
@SpringBootTest  
@AutoConfigureMockMvc  
public class RegisterTest {  
  
    @Autowired  
    private MockMvc mockMvc;  
  
    @Test  
    public void testRegister() throws Exception{  
        MockMultipartFile file = new MockMultipartFile("files", "test.text", "text/plain", "This is content".getBytes());  
        mockMvc.perform(multipart("/guide/register")  
                .file(file).file(file)  
                .param("title", "controller register test title")  
                .param("content", "controller register test content"))  
                .andExpect(status().isFound())  
                .andExpect(redirectedUrl("/guide/list"));  
    }  
}
~~~

- dao test
~~~java
package org.hgtech.guidearchiveweb.dao;  
  
import org.hgtech.guidearchiveweb.domain.GuideVO;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.boot.test.context.SpringBootTest;  
  
import java.time.LocalDateTime;  
import java.util.ArrayList;  
import java.util.List;  
import java.util.UUID;  
  
@SpringBootTest  
public class GuideDaoTest {  
  
    @Autowired  
    GuideDao guideDao;  
  
    private GuideVO getGuideVO(){  
        LocalDateTime currentDateTime = LocalDateTime.now();  
        GuideVO guideVO = GuideVO.builder().reg_date(currentDateTime).mod_date(currentDateTime).title("test title").content("test content!").build();  
        return guideVO;  
    }  
  
    private GuideVO getGuideVO(String title){  
        LocalDateTime currentDateTime = LocalDateTime.now();  
        GuideVO guideVO = GuideVO.builder().reg_date(currentDateTime).mod_date(currentDateTime).title(title).content("test content!").build();  
        return guideVO;  
    }  
  
    private GuideVO getGuideVO(String title, String content){  
        LocalDateTime currentDateTime = LocalDateTime.now();  
        GuideVO guideVO = GuideVO.builder().reg_date(currentDateTime).mod_date(currentDateTime).title(title).content(content).build();  
        return guideVO;  
    }  
  
    private List<GuideVO> getGuideVOList(int length) {  
        List<GuideVO> guideVOList = new ArrayList<>();  
  
        for (int i=0; i<length; i++) {  
            guideVOList.add(getGuideVO());  
        }  
        return guideVOList;  
    }  
  
    private String getUniqueTitle() {  
        String uuid = UUID.randomUUID().toString();  
        String title = uuid + "_title";  
        return title;  
    }  
  
    @Test  
    public void insertTest() {  
        GuideVO guideVO = getGuideVO();  
        guideDao.insert(guideVO);  
    }  
  
    @Test  
    public void selectAllTest() {  
  
        List<String> titleList = new ArrayList();  
        int length = 10;  
        for (int i=0; i<length; i++) {  
            String title = getUniqueTitle();  
            GuideVO vo = getGuideVO(title);  
            titleList.add(title);  
            guideDao.insert(vo);  
        }  
  
        List<GuideVO> selectedAllList = guideDao.selectAll();  
        Assertions.assertEquals(selectedAllList.get(selectedAllList.size()-1).getTitle(), titleList.get(length-1));  
        Assertions.assertEquals(selectedAllList.get(selectedAllList.size()-3).getTitle(), titleList.get(length-3));  
    }  
  
    @Test  
    public void selectLastTest() {  
        String title = getUniqueTitle();  
        GuideVO guideVO = getGuideVO(title);  
        guideDao.insert(guideVO);  
  
        GuideVO lastVO = guideDao.selectLast();  
        Assertions.assertEquals(title, lastVO.getTitle());  
    }  
  
    @Test  
    public void selectByIdTest() {  
        String title = getUniqueTitle();  
        GuideVO guideVO = getGuideVO(title);  
        guideDao.insert(guideVO);  
  
        GuideVO lastVO = guideDao.selectLast();  
        GuideVO selectedByIdVO = guideDao.selectById(lastVO.getGid());  
        Assertions.assertEquals(lastVO.getTitle(), selectedByIdVO.getTitle());  
    }  
  
    @Test  
    public void deleteTest() {  
        GuideVO unDeletedVO = getGuideVO(getUniqueTitle(), "undeleted content!");  
        GuideVO deletedVo = getGuideVO(getUniqueTitle(), "deleted content!");  
  
        guideDao.insert(unDeletedVO);  
        guideDao.insert(deletedVo);  
  
        int deletedId = guideDao.selectLast().getGid();  
        guideDao.delete(deletedId);  
        Assertions.assertNull(guideDao.selectById(deletedId));  
        Assertions.assertEquals(guideDao.selectLast().getTitle(), unDeletedVO.getTitle());  
    }  
  
    @Test  
    public void updateTest() {  
        GuideVO guideVO = getGuideVO(getUniqueTitle(), "not updated content yet!");  
        guideDao.insert(guideVO);  
  
        GuideVO beforeUpdateVO = guideDao.selectLast();  
        String updatedTitle = getUniqueTitle();  
        beforeUpdateVO.setTitle(updatedTitle);  
        beforeUpdateVO.setContent("content updated!");  
        guideDao.update(beforeUpdateVO);  
        GuideVO afterUpdateVO = guideDao.selectById(beforeUpdateVO.getGid());  
        Assertions.assertEquals(afterUpdateVO.getTitle(), updatedTitle);  
    }  
}
~~~