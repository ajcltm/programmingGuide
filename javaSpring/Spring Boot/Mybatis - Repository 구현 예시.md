
- repository
~~~java
package org.hgtech.pnpsecure.repository;  
  
import org.apache.ibatis.annotations.Mapper;  
import org.hgtech.pnpsecure.domain.BoardVO;  
  
import java.util.List;  
  
@Mapper  
public interface BoardRepository {  
    int insert(BoardVO boardVO);  
    List<BoardVO> selectAll();  
    BoardVO selectLast();  
    BoardVO selectById(String id);  
    BoardVO selectByCategory(String category);  
    BoardVO selectLike(String keyword);  
    int delete(String id);  
    int update(BoardVO boardVO);  
}
~~~

- xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.pnpsecure.repository.BoardRepository">  
    <insert id="insert">  
        insert into tbl_pnpsecure_board (id, regDate, modDate, title, content, category) values (#{id}, #{regDate}, #{modDate}, #{title}, #{content}, #{category})  
    </insert>  
  
    <select id="selectAll" resultType="org.hgtech.pnpsecure.domain.BoardVO">  
        select * from tbl_pnpsecure_board  
    </select>  
  
    <select id="selectById" resultType="org.hgtech.pnpsecure.domain.BoardVO">  
        select * from tbl_pnpsecure_board where id = #{id}  
    </select>  
  
    <select id="selectByCategory" resultType="org.hgtech.pnpsecure.domain.BoardVO">  
        select * from tbl_pnpsecure_board where category = #{category}  
    </select>  
  
    <select id="selectLike" resultType="org.hgtech.pnpsecure.domain.BoardVO">  
        select * from tbl_pnpsecure_board where title like concat('%', #{keyword}, '%') or content like concat('%', #{keyword}, '%')  
    </select>  
  
    <select id="selectLast" resultType="org.hgtech.pnpsecure.domain.BoardVO">  
        select * from tbl_pnpsecure_board order by id desc limit 1  
    </select>  
  
    <delete id="delete">  
        delete from tbl_pnpsecure_board where id = #{id}  
    </delete>  
  
    <update id="update">  
        update tbl_pnpsecure_board set regDate = #{regDate}, modDate = #{modDate}, title = #{title}, content = #{content}, category = #{category} where id = #{id}  
    </update>  
</mapper>
~~~

- test
~~~java
package org.hgtech.pnpsecure.repository;  
  
import org.hgtech.pnpsecure.domain.BoardVO;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.boot.test.context.SpringBootTest;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.Random;  
import java.util.UUID;  
  
@SpringBootTest  
public class BoardRepositoryTest {  
  
    @Autowired  
    BoardRepository repository;  
  
    public BoardVO createVO() {  
//      VO 객체 생성  
        BoardVO vo = BoardVO.builder()  
                .id(createId())  
                .regDate(createRandomDatetime())  
                .modDate(createRandomDatetime())  
                .title(createRandomString())  
                .content(createRandomString())  
                .category(createRandomString())  
                .build();  
        return vo;  
    }  
  
    public String createId() {  
        int newNum = 10000;  
        if (repository.selectLast() != null) {  
            newNum = Integer.parseInt(repository.selectLast().getId().substring(3))+1 ;  
        }  
        return "bd-"+newNum;  
    }  
    public String createRandomString() {  
        return UUID.randomUUID().toString();  
    }  
  
    public int createRandomNumber() {  
        Random random = new Random();  
        return random.nextInt(1000);  
    }  
  
    public LocalDateTime createRandomDatetime() {  
        LocalDateTime now = LocalDateTime.now();  
        return now;  
    }  
  
    public LocalDate createRandomDate() {  
        LocalDate now = LocalDate.now();  
        return now;  
    }  
  
  
    @Test  
    public void insertTest() {  
        int result = repository.insert(createVO());  
        Assertions.assertEquals(result,1);  
    }  
  
    @Test  
    public void selectLastTest() {  
        int result = repository.insert(createVO());  
        System.out.println("================== selectLastTest ====================");  
        System.out.println(repository.selectLast());  
    }  
  
    @Test  
    public void selectAllTest () {  
        repository.insert(createVO());  
        repository.insert(createVO());  
        System.out.println("================== selectAllTest ====================");  
        System.out.println(repository.selectAll());  
    }  
  
    @Test  
    public void selectByIdTest () {  
        repository.insert(createVO());  
//      id 속성 이름 확인 필요  
        System.out.println("================== selectByIdTest ====================");  
        System.out.println(repository.selectById(repository.selectLast().getId()));  
    }  
  
    @Test  
    public void selectByCategoryTest() {  
        repository.insert(createVO());  
//      id 속성 이름 확인 필요  
        System.out.println("================== selectByCategoryTest ====================");  
        System.out.println(repository.selectByCategory(repository.selectLast().getCategory()));  
    }  
  
    @Test  
    public void selectLikeTest() {  
        repository.insert(createVO());  
//      id 속성 이름 확인 필요  
        System.out.println("================== selectLikeTest ====================");  
        System.out.println(repository.selectLike(repository.selectLast().getTitle()));  
    }  
  
    @Test  
    public void deleteTest() {  
        repository.insert(createVO());  
        int result = repository.delete(repository.selectLast().getId());  
        Assertions.assertEquals(result,1);  
    }  
  
    @Test  
    public void updateTest(){  
        repository.insert(createVO());  
//      수정하고자 하는 속성 이름과 해당 객체 확인 필요  
        BoardVO updatedVO = repository.selectLast();  
        updatedVO.setContent(createRandomString()+"  ### updated!!! ###  ");  
        int result = repository.update(updatedVO);  
        Assertions.assertEquals(result,1);  
        System.out.println("================== updateTest ====================");  
        System.out.println(repository.selectLast());  
    }  
}
~~~
