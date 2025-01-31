- service
~~~java
package org.hgtech.worksystem.service;  
  
import org.hgtech.worksystem.DTO.MemberDTO;  
import org.hgtech.worksystem.DTO.WorkDTO;  
import org.hgtech.worksystem.domain.MemberVO;  
import org.hgtech.worksystem.domain.WorkVO;  
import org.hgtech.worksystem.repository.MemberRepository;  
import org.hgtech.worksystem.repository.WorkRepository;  
import org.modelmapper.ModelMapper;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  

import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;
  
@Service
public class MemberService {
    @Autowired
    MemberRepository repository;
  
    ModelMapper mapper = new ModelMapper();
  
	public int register(MemberDTO memberDTO) {  
	    int newNum = 10000;  
	    MemberDTO last = getLast();  
	    if (last != null) {  
	        newNum = Integer.parseInt(last.getMbId().substring(3))+1 ;  
	    }  
	  
	    memberDTO.setMbId("mb-"+newNum);  
	    memberDTO.setMbRegDate(LocalDate.now());  
	    memberDTO.setMbModDate(LocalDate.now());  
	    return repository.insert(mapper.map(memberDTO, MemberVO.class));  
	}
  
    public MemberDTO getLast() {
        return mapper.map(repository.selectLast(), MemberDTO.class);
    }

    public List<MemberDTO> getAll() {
        return repository.selectAll().stream().map(vo -> mapper.map(vo, MemberDTO.class)).collect(Collectors.toList());
    }
  
    public MemberDTO getByMbId(int id) {
        return mapper.map(repository.selectByMbId(id), MemberDTO.class);
    }

    public int remove(int id) {
        return repository.delete(id);
    }

    public int modify(MemberDTO memberDTO) {
        memberDTO.setMbModDate(LocalDateTime.now());
        return repository.update(mapper.map(memberDTO, MemberVO.class));
    }
}
~~~

- test
~~~java
package org.hgtech.worksystem.serviceTest;  
  
import org.hgtech.worksystem.DTO.MemberDTO;  
import org.hgtech.worksystem.service.MemberService;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.boot.test.context.SpringBootTest;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.Random;  
import java.util.UUID;  

@SpringBootTest
public class MemberServiceTest {
    @Autowired
    MemberService service;
  
    public MemberDTO createDTO() {
//      VO 객체 생성
        MemberDTO dto = MemberDTO.builder()
                .mbRegDate(createRandomDatetime())
                .mbModDate(createRandomDatetime())
                .mbUserName(createRandomString())
                .mbUserBirth(createRandomDate())
                .mbUserId(createRandomString())
                .mbUserPw(createRandomString())
                .build();
        return dto;
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
    public void registerTest() {
        int result = service.register(createDTO());
        Assertions.assertEquals(result,1);
    }  
  
    @Test  
    public void selectLastTest() {  
        service.register(createDTO());  
        System.out.println(service.getLast());  
    }  
  
    @Test  
    public void selectAllTest () {
        service.register(createDTO());
        service.register(createDTO());
        System.out.println(service.getAll());
    }
  
    @Test  
    public void selectByIdTest () {
        service.register(createDTO());
//      id 속성 이름 확인 필요
        Assertions.assertEquals(service.getLast().getMbId(), service.getByMbId(service.getLast().getMbId()).getMbId());
    }
  
    @Test  
    public void deleteTest() {
        service.register(createDTO());
        int result = service.remove(service.getLast().getMbId());
        Assertions.assertEquals(result,1);
    }  
  
    @Test  
    public void updateTest(){
        service.register(createDTO());
//      수정하고자 하는 속성 이름과 해당 객체 확인 필요
        String input = service.getLast().getMbUserId();
        MemberDTO dto = service.getLast();
        dto.setMbUserId(createRandomString());
        service.modify(dto);
        Assertions.assertNotEquals(input, service.getLast().getMbUserId());
    }  
}
~~~
