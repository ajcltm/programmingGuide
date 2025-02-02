
- repository
~~~java
package org.hgtech.board.repository;  
  
import org.apache.ibatis.annotations.Mapper;  
import org.hgtech.board.domain.MemberVO;  
  
import java.util.List;  
  
@Mapper  
public interface MemberRepository {  
    int insert(MemberVO memberVO);  
    List<MemberVO> selectAll();  
    MemberVO selectLast();  
    MemberVO selectByMbId(String mbId);  
    MemberVO selectByIdpw(String mbUserId, String mbUserPw);  
    MemberVO selectByMbUUID(String mbUUID);  
    int delete(String mbId);  
    int update(MemberVO memberVO);  
}
~~~

- xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.board.repository.MemberRepository">  
    <insert id="insert">  
        insert into tbl_boardMember (mbId, mbRegDate, mbModDate, mbName, mbBirth, mbUserId, mbUserPw, mbUUID) values (#{mbId}, #{mbRegDate}, #{mbModDate}, #{mbName}, #{mbBirth}, #{mbUserId}, #{mbUserPw}, #{mbUUID})  
    </insert>  
  
    <select id="selectAll" resultType="org.hgtech.board.domain.MemberVO">  
        select * from tbl_boardMember  
    </select>  
  
    <select id="selectByMbId" resultType="org.hgtech.board.domain.MemberVO">  
        select * from tbl_boardMember where mbId = #{mbId}  
    </select>  
  
    <select id="selectByIdpw" resultType="org.hgtech.board.domain.MemberVO">  
        select * from tbl_boardMember where mbUserId = #{mbUserId} and mbUserPw = #{mbUserPw}  
    </select>  
  
    <select id="selectByMbUUID" resultType="org.hgtech.board.domain.MemberVO">  
        select * from tbl_boardMember where mbUUID = #{mbUUID}  
    </select>  
  
    <select id="selectLast" resultType="org.hgtech.board.domain.MemberVO">  
        select * from tbl_boardMember order by mbId desc limit 1  
    </select>  
  
    <delete id="delete">  
        delete from tbl_boardMember where mbId = #{mbId}  
    </delete>  
  
    <update id="update">  
        update tbl_boardMember set mbRegDate = #{mbRegDate}, mbModDate = #{mbModDate}, mbName = #{mbName}, mbBirth = #{mbBirth}, mbUserId = #{mbUserId}, mbUserPw = #{mbUserPw}, mbUUID = #{mbUUID} where mbId= #{mbId}  
    </update>  
</mapper>
~~~

- test
~~~java
package org.hgtech.board.repository;  
  
import org.hgtech.board.domain.MemberVO;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.boot.test.context.SpringBootTest;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.Random;  
import java.util.UUID;  
  
@SpringBootTest  
public class memberRepositoryTest {  
    @Autowired  
    MemberRepository repository;  
  
    public MemberVO createVO() {  
//      VO 객체 생성  
        MemberVO vo = MemberVO.builder()  
                .mbId(createId())  
                .mbRegDate(createRandomDate())  
                .mbModDate(createRandomDate())  
                .mbName(createRandomString())  
                .mbBirth(createRandomDate())  
                .mbUserId(createRandomString())  
                .mbUserPw(createRandomString())  
                .mbUUID(createRandomString())  
                .build();  
        return vo;  
    }  
  
    public String createId() {  
        int newNum = 10000;  
        if (repository.selectLast() != null) {  
            newNum = Integer.parseInt(repository.selectLast().getMbId().substring(3))+1 ;  
        }  
        return "mb-"+newNum;  
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
        repository.insert(createVO());  
        System.out.println(repository.selectLast());  
    }  
  
    @Test  
    public void selectAllTest () {  
        repository.insert(createVO());  
        repository.insert(createVO());  
        System.out.println(repository.selectAll());  
    }  
  
    @Test  
    public void selectByIdTest () {  
        repository.insert(createVO());  
//      id 속성 이름 확인 필요  
        Assertions.assertEquals(repository.selectLast().getMbId(), repository.selectByMbId(repository.selectLast().getMbId()).getMbId());  
    }  
  
    @Test  
    public void selectByIdpwTest () {  
        repository.insert(createVO());  
//      id 속성 이름 확인 필요  
        Assertions.assertEquals(repository.selectLast().getMbId(), repository.selectByIdpw(repository.selectLast().getMbUserId(), repository.selectLast().getMbUserPw()).getMbId());  
    }  
  
    @Test  
    public void selectByUUID () {  
        repository.insert(createVO());  
//      id 속성 이름 확인 필요  
        Assertions.assertEquals(repository.selectLast().getMbId(), repository.selectByMbUUID(repository.selectLast().getMbUUID()).getMbId());  
    }  
  
    @Test  
    public void deleteTest() {  
        repository.insert(createVO());  
        int result = repository.delete(repository.selectLast().getMbId());  
        Assertions.assertEquals(result,1);  
    }  
  
    @Test  
    public void updateTest(){  
        repository.insert(createVO());  
//      수정하고자 하는 속성 이름과 해당 객체 확인 필요  
        String input = repository.selectLast().getMbUserId();  
        MemberVO vo = repository.selectLast();  
        vo.setMbUserId(createRandomString());  
        repository.update(vo);  
        Assertions.assertNotEquals(input, repository.selectLast().getMbUserId());  
    }  
}
~~~
