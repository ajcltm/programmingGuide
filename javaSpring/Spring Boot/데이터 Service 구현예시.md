- service
~~~java
package org.hgtech.board.service;  
  
import org.hgtech.board.DTO.MemberDTO;  
import org.hgtech.board.domain.MemberVO;  
import org.hgtech.board.repository.MemberRepository;  
import org.modelmapper.ModelMapper;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.List;  
import java.util.stream.Collectors;  
  
@Service  
public class MemberService {  
  
    @Autowired  
    MemberRepository repository;  
  
    ModelMapper mapper = new ModelMapper();  
  
    public String createId() {  
        int newNum = 10000;  
        if (getLast() != null) {  
            newNum = Integer.parseInt(getLast().getMbId().substring(3))+1 ;  
        }  
        return "mb-"+newNum;  
    }  
  
    public int register(MemberDTO memberDTO) {  
        memberDTO.setMbId(createId());  
        memberDTO.setMbRegDate(LocalDate.now());  
        memberDTO.setMbModDate(LocalDate.now());  
        return repository.insert(mapper.map(memberDTO, MemberVO.class));  
    }  
  
    public MemberDTO getLast() {  
        if (repository.selectLast() != null) {  
            return mapper.map(repository.selectLast(), MemberDTO.class);  
        }  
        return null;  
    }  
  
    public List<MemberDTO> getAll() {  
        if (repository.selectAll() != null) {  
            return repository.selectAll().stream().map(vo -> mapper.map(vo, MemberDTO.class)).collect(Collectors.toList());  
        }  
        return null;  
    }  
  
    public MemberDTO getByMbId(String id) {  
        if (repository.selectByMbId(id) != null) {  
            return mapper.map(repository.selectByMbId(id), MemberDTO.class);  
        }  
        return null;  
    }  
  
    public MemberDTO getByIdpw(String mbUserId, String mbUserPw) {  
        if (repository.selectByIdpw(mbUserId, mbUserPw) != null) {  
            return mapper.map(repository.selectByIdpw(mbUserId, mbUserPw), MemberDTO.class);  
        }  
        return null;  
    }  
  
    public MemberDTO getByMbUUID(String mbUUID) {  
        if (repository.selectByMbUUID(mbUUID) != null) {  
            return mapper.map(repository.selectByMbUUID(mbUUID), MemberDTO.class);  
        }  
        return null;  
    }  
  
    public int remove(String id) {  
        return repository.delete(id);  
    }  
  
    public int modify(MemberDTO memberDTO) {  
        memberDTO.setMbModDate(LocalDate.now());  
        return repository.update(mapper.map(memberDTO, MemberVO.class));  
    }  
}
~~~

- test
~~~java
package org.hgtech.board.service;  
  
import org.hgtech.board.DTO.MemberDTO;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.Random;  
import java.util.UUID;  
import org.springframework.boot.test.context.SpringBootTest;  
  
@SpringBootTest  
public class MemberServiceTest {  
    @Autowired  
    MemberService service;  
  
    public MemberDTO createDTO() {  
//      VO 객체 생성  
        MemberDTO dto = MemberDTO.builder()  
                .mbId(createRandomString())  
                .mbRegDate(createRandomDate())  
                .mbModDate(createRandomDate())  
                .mbName(createRandomString())  
                .mbBirth(createRandomDate())  
                .mbUserId(createRandomString())  
                .mbUserPw(createRandomString())  
                .mbUUID(createRandomString())  
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
    public void getByMbIdpwTest () {  
        service.register(createDTO());  
//      id 속성 이름 확인 필요  
        Assertions.assertEquals(service.getLast().getMbId(), service.getByIdpw(service.getLast().getMbUserId(), service.getLast().getMbUserPw()).getMbId());  
    }  
  
    @Test  
    public void getByUUIDTest () {  
        service.register(createDTO());  
//      id 속성 이름 확인 필요  
        Assertions.assertEquals(service.getLast().getMbId(), service.getByMbUUID(service.getLast().getMbUUID()).getMbId());  
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
