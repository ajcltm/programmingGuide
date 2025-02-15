- service
~~~java
package org.hgtech.pnpsecure.service;  
  
import org.hgtech.pnpsecure.DTO.BoardDTO;  
import org.hgtech.pnpsecure.domain.BoardVO;  
import org.hgtech.pnpsecure.repository.BoardRepository;  
import org.modelmapper.ModelMapper;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.List;  
import java.util.stream.Collectors;  
  
@Service  
public class BoardService {  
    @Autowired  
    BoardRepository repository;  
  
    ModelMapper mapper = new ModelMapper();  
  
    public String createId() {  
        int newNum = 10000;  
        if (getLast() != null) {  
            newNum = Integer.parseInt(getLast().getId().substring(3))+1 ;  
        }  
        return "mb-"+newNum;  
    }  
  
    public int register(BoardDTO boardDTO) {  
        boardDTO.setId(createId());  
        boardDTO.setRegDate(LocalDateTime.now());  
        boardDTO.setModDate(LocalDateTime.now());  
        return repository.insert(mapper.map(boardDTO, BoardVO.class));  
    }  
  
    public BoardDTO getLast() {  
        if (repository.selectLast() != null) {  
            return mapper.map(repository.selectLast(), BoardDTO.class);  
        }  
        return null;  
    }  
  
    public List<BoardDTO> getAll() {  
        if (repository.selectAll() != null) {  
            return repository.selectAll().stream().map(vo -> mapper.map(vo, BoardDTO.class)).collect(Collectors.toList());  
        }  
        return null;  
    }  
  
    public BoardDTO getById(String id) {  
        if (repository.selectById(id) != null) {  
            return mapper.map(repository.selectById(id), BoardDTO.class);  
        }  
        return null;  
    }  
  
    public BoardDTO getByCategory(String category) {  
        if (repository.selectByCategory(category) != null) {  
            return mapper.map(repository.selectByCategory(category), BoardDTO.class);  
        }  
        return null;  
    }  
  
    public BoardDTO getLike(String keyword) {  
        if (repository.selectLike(keyword) != null) {  
            return mapper.map(repository.selectLike(keyword), BoardDTO.class);  
        }  
        return null;  
    }  
  
    public int remove(String id) {  
        return repository.delete(id);  
    }  
  
    public int modify(BoardDTO boardDTO) {  
        boardDTO.setModDate(LocalDateTime.now());  
        return repository.update(mapper.map(boardDTO, BoardVO.class));  
    }  
}
~~~

- test
~~~java
package org.hgtech.pnpsecure.service;  
  
import org.hgtech.pnpsecure.DTO.BoardDTO;  
import org.hgtech.pnpsecure.domain.BoardVO;  
import org.junit.jupiter.api.Assertions;  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  
import java.util.Random;  
import java.util.UUID;  
import org.springframework.boot.test.context.SpringBootTest;  
  
@SpringBootTest  
public class BoardServiceTest {  
    @Autowired  
    BoardService service;  
  
    public BoardDTO createDTO() {  
//      VO 객체 생성  
        BoardDTO dto = BoardDTO.builder()  
                .id(createRandomString())  
                .regDate(createRandomDatetime())  
                .modDate(createRandomDatetime())  
                .title(createRandomString())  
                .content(createRandomString())  
                .category(createRandomString())  
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
    public void getLastTest() {  
        service.register(createDTO());  
        System.out.println("================== getLastTest ====================");  
        System.out.println(service.getLast());  
    }  
  
    @Test  
    public void getAllTest () {  
        service.register(createDTO());  
        service.register(createDTO());  
        System.out.println("================== getAllTest ====================");  
        System.out.println(service.getAll());  
    }  
  
    @Test  
    public void getByIdTest () {  
        service.register(createDTO());  
//      id 속성 이름 확인 필요  
        System.out.println("================== getByIdTest ====================");  
        System.out.println(service.getById(service.getLast().getId()));  
    }  
  
    @Test  
    public void getByCategoryTest () {  
        service.register(createDTO());  
//      id 속성 이름 확인 필요  
        System.out.println("================== getByCategoryTest ====================");  
        System.out.println(service.getByCategory(service.getLast().getCategory()));  
    }  
  
    @Test  
    public void getLikeTest () {  
        service.register(createDTO());  
//      id 속성 이름 확인 필요  
        System.out.println("================== getLikeTest ====================");  
        System.out.println(service.getLike(service.getLast().getTitle()));  
    }  
  
    @Test  
    public void removeTest() {  
        service.register(createDTO());  
        int result = service.remove(service.getLast().getId());  
        Assertions.assertEquals(result,1);  
    }  
  
    @Test  
    public void modifyTest(){  
        service.register(createDTO());  
//      수정하고자 하는 속성 이름과 해당 객체 확인 필요  
        BoardDTO updatedDTO = service.getLast();  
        updatedDTO.setContent(createRandomString()+"  ### modified!!! ###  ");  
        int result = service.modify(updatedDTO);  
        Assertions.assertEquals(result,1);  
        System.out.println("================== modifyTest ====================");  
        System.out.println(service.getLast());  
    }  
}
~~~
