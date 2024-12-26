
- repository
~~~java
package org.hgtech.webdevsys.repository;  
  
import org.apache.ibatis.annotations.Mapper;  
import org.hgtech.webdevsys.domain.WebInfoVO;  
import java.util.List;  
  
@Mapper  
public interface WebInfoRepository {  
  
    void insert(WebInfoVO webInfoVO);  
  
    List<WebInfoVO> selectAll();  
  
    WebInfoVO selectLast();  
  
    List<WebInfoVO> selectByParentId(int parentId);  
  
    WebInfoVO selectById(int id);  
  
    void delete(int id);  
  
    void update(WebInfoVO webInfoVO);  
}
~~~

- xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.webdevsys.repository.WebInfoRepository">  
    <insert id="insert">  
        insert into tbl_webInfo (regDate, modDate, title, content, comment, parentId) values (#{regDate}, #{modDate}, #{title}, #{content}, #{comment}, #{parentId})  
    </insert>  
  
    <select id="selectAll" resultType="org.hgtech.webdevsys.domain.WebInfoVO">  
        select * from tbl_webInfo  
    </select>  
  
    <select id="selectById" resultType="org.hgtech.webdevsys.domain.WebInfoVO">  
        select * from tbl_webInfo where id = #{id}  
    </select>  
  
    <select id="selectByParentId" resultType="org.hgtech.webdevsys.domain.WebInfoVO">  
        select * from tbl_webInfo where parentId = #{parentId}  
    </select>  
  
    <select id="selectLast" resultType="org.hgtech.webdevsys.domain.WebInfoVO">  
        select * from tbl_webInfo order by id desc limit 1  
    </select>  
  
    <delete id="delete">  
        delete from tbl_webInfo where id = #{id}  
    </delete>  
  
    <update id="update">  
        update tbl_webInfo set regDate = #{regDate}, modDate = #{modDate}, title = #{title}, content = #{content}, comment = #{comment}, parentId = #{parentId} where id= #{id}  
    </update>  
</mapper>
~~~

- test
~~~java
package org.hgtech.webdevsys.repositoryTest;  
  
import org.hgtech.webdevsys.domain.WebInfoVO;  
import org.hgtech.webdevsys.repository.WebInfoRepository;  
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
public class WebInfoRepositoryTest {  
  
    @Autowired  
    WebInfoRepository webInfoRepository;  
  
    public WebInfoVO createWebInfoVO() {  
        LocalDateTime now = LocalDateTime.now();  
        String randomText = UUID.randomUUID().toString();  
        WebInfoVO webInfoVO = WebInfoVO.builder().regDate(now).modDate(now).title(randomText+"_title").content(randomText+"_content").comment(randomText+"comment").build();  
        return webInfoVO;  
    }  
  
    public WebInfoVO createWebInfoVO(int parentId) {  
        LocalDateTime now = LocalDateTime.now();  
        String randomText = UUID.randomUUID().toString();  
        WebInfoVO webInfoVO = WebInfoVO.builder().regDate(now).modDate(now).title(randomText+"_title").content(randomText+"_content").comment(randomText+"comment").parentId(parentId).build();  
        return webInfoVO;  
    }  
  
    public WebInfoVO getTargetVO() {  
        WebInfoVO webInfoVO = createWebInfoVO();  
        webInfoRepository.insert(webInfoVO);  
        WebInfoVO targetVO = webInfoRepository.selectLast();  
        return targetVO;  
    }  
  
    public List<WebInfoVO> getTargetVO(int parentId) {  
        for (int i=0; i<5; i++) {  
            WebInfoVO webInfoVO = createWebInfoVO(parentId);  
            webInfoRepository.insert(webInfoVO);  
        }  
        List<WebInfoVO> webInfoVOList = webInfoRepository.selectAll();  
        List<WebInfoVO> targetVO = webInfoVOList.subList(webInfoVOList.size()-5, webInfoVOList.size());  
        return targetVO;  
    }  
  
    public List<WebInfoVO> getTargetVOList(int size) {  
        List<WebInfoVO> targetVOList = new ArrayList<>();  
        for (int i=0; i < size; i++) {  
            WebInfoVO webInfoVO = createWebInfoVO();  
            webInfoRepository.insert(webInfoVO);  
            WebInfoVO targetVO = webInfoRepository.selectLast();  
            targetVOList.add(targetVO);  
        }  
        return targetVOList;  
    }  
  
    @Test  
    public void insertTest() {  
        WebInfoVO webInfoVO = createWebInfoVO();  
        webInfoRepository.insert(webInfoVO);  
    }  
  
    @Test  
    public void selectLastTest() {  
        WebInfoVO target = createWebInfoVO();  
        webInfoRepository.insert(target);  
        WebInfoVO test = webInfoRepository.selectLast();  
        Assertions.assertEquals(target.getTitle(), test.getTitle());  
    }  
  
    @Test  
    public void selectAllTest () {  
        int size = 10;  
        List<WebInfoVO> target = getTargetVOList(size);  
        List<WebInfoVO> test = webInfoRepository.selectAll();  
        Assertions.assertEquals(target.get(size-1).getTitle(), test.get(test.size()-1).getTitle());  
        Assertions.assertEquals(target.get(size-3).getTitle(), test.get(test.size()-3).getTitle());  
    }  
  
    @Test  
    public void selectByIdTest () {  
        WebInfoVO target = getTargetVO();  
        WebInfoVO test = webInfoRepository.selectById(target.getId());  
        Assertions.assertEquals(target.getTitle(), test.getTitle());  
    }  
  
    @Test  
    public void selectByParentIdTest() {  
        Random random = new Random();  
        int parentId = random.nextInt(1000);  
        List<WebInfoVO> target = getTargetVO(parentId);  
        List<WebInfoVO> test = webInfoRepository.selectByParentId(parentId);  
        Assertions.assertEquals(target.get(0).getTitle(), test.get(0).getTitle());  
    }  
  
    @Test  
    public void deleteTest() {  
        WebInfoVO target = getTargetVO();  
        webInfoRepository.delete(target.getId());  
        WebInfoVO test = webInfoRepository.selectById(target.getId());  
        Assertions.assertNull(test);  
    }  
  
    @Test  
    public void updateTest(){  
        WebInfoVO target = getTargetVO();  
        String updated = UUID.randomUUID()+"updated";  
        target.setTitle(updated);  
        webInfoRepository.update(target);  
        WebInfoVO test = webInfoRepository.selectById(target.getId());  
        Assertions.assertEquals(target.getTitle(), test.getTitle());  
    }  
}
~~~
