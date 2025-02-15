
#### DTO

~~~java
package org.hgtech.pnpsecure.DTO;  
  
  
import lombok.*;  
  
import java.util.List;  
  
@Getter  
@Setter  
@ToString  
@Builder  
@AllArgsConstructor  
@NoArgsConstructor  
public class BoardPaginationDTO {  
    int currentPage;  
    int size;  
    int nationSize;  
    int total;  
    int maxPage;  
    List<BoardDTO> dataList;  
    int dataStart;  
    int dataEnd;  
    int pageStart;  
    int pageEnd;  
    Integer prevPage;  
    Integer nextPage;  
}
~~~

#### Service
---
~~~java
package org.hgtech.pnpsecure.service;  
  
import org.hgtech.pnpsecure.DTO.BoardDTO;  
import org.hgtech.pnpsecure.DTO.BoardPaginationDTO;  
import org.hgtech.pnpsecure.domain.BoardVO;  
import org.hgtech.pnpsecure.repository.BoardRepository;  
import org.modelmapper.ModelMapper;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
  
import java.util.List;  
import java.util.stream.Collectors;  
  
@Service  
public class BoardPaginationService {  
  
    @Autowired  
    BoardRepository repository;  
  
    ModelMapper mapper = new ModelMapper();  
  
    int currentPage;  
    int size;  
    int nationSize;  
  
    int total;  
    int maxPage;  
    List<BoardDTO> dataList;  
    int dataStart;  
    int dataEnd;  
    int pageStart;  
    int pageEnd;  
    Integer prevPage;  
    Integer nextPage;  
  
    private void calculate(int currentPage, int size, int nationSize) {  
        this.total = repository.totalSize();  
        this.maxPage = (int) Math.ceil((double) total / size) -1;  
        this.currentPage = currentPage;  
        this.size = size;  
        this.nationSize = nationSize;  
        calculDataStart();  
        calculDataEnd();  
        selectData();  
        calculPageStart();  
        calculPageEnd();  
        calculPrevPage();  
        calculNextPage();  
    }  
  
    private void calculDataStart() {  
        this.dataStart = currentPage*size;  
    }  
    private void calculDataEnd() {  
        int dataEnd = dataStart+size-1;  
        if (dataEnd > this.total-1) {  
            this.dataEnd = this.total-1;  
        } else {  
            this.dataEnd = dataEnd;  
        }  
    }  
  
    private void selectData(){  
        List<BoardVO> boardVOList = repository.selectFrom(this.dataStart, this.size);  
        this.dataList = boardVOList.stream().map(vo -> mapper.map(vo, BoardDTO.class)).collect(Collectors.toList());  
    }  
  
    private void calculPageStart() {  
        int pageStart = (Integer)(currentPage / nationSize) * nationSize;  
        if (pageStart > this.maxPage) {  
            this.pageStart = this.maxPage;  
        } else {  
            this.pageStart = pageStart;  
        }  
    }  
  
    private void calculPageEnd() {  
        int pageEnd = this.pageStart + nationSize -1;  
        if (pageEnd > this.maxPage) {  
            this.pageEnd = this.maxPage;  
        } else {  
            this.pageEnd = pageEnd;  
        }  
    }  
  
    private void calculPrevPage() {  
        this.prevPage = (this.pageStart-1>=0) ? this.pageStart-1 : null;  
    }  
  
    private void calculNextPage() {  
        this.nextPage = (this.pageEnd+1<=this.maxPage) ? this.pageEnd+1 : null;  
    }  
  
    public BoardPaginationDTO getPagination(int currentPage, int size, int nationSize){  
        this.calculate(currentPage, size, nationSize);  
        BoardPaginationDTO boardPagenationDTO = BoardPaginationDTO.builder()  
                .currentPage(this.currentPage)  
                .size(this.size)  
                .nationSize(this.nationSize)  
                .total(this.total)  
                .maxPage(this.maxPage)  
                .dataList(this.dataList)  
                .dataStart(this.dataStart)  
                .dataEnd(this.dataEnd)  
                .pageStart(this.pageStart)  
                .pageEnd(this.pageEnd)  
                .prevPage(this.prevPage)  
                .nextPage(this.nextPage)  
                .build();  
        return boardPagenationDTO;  
    }  
}
~~~

### Repository
---
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.pnpsecure.repository.BoardRepository">   
	<select id="selectFrom" resultType="org.hgtech.pnpsecure.domain.BoardVO">  
	    SELECT * FROM tbl_pnpsecure_board ORDER BY id LIMIT #{size} OFFSET #{start}  
	</select>  
	  
	<select id="totalSize">  
	    SELECT COUNT(*) AS total_count FROM tbl_pnpsecure_board  
	</select>
</mapper>
~~~

~~~java
package org.hgtech.board.repository;  
  
import org.apache.ibatis.annotations.Mapper;  
import org.hgtech.board.domain.BoardVO;  
import org.hgtech.board.domain.ReplyVO;  
  
import java.util.List;  
  
@Mapper  
public interface BoardRepository {  
    List<BoardVO> selectFrom(int start, int size);  
    int totalSize();  
}
~~~

### Repository Test
---
~~~java
package org.hgtech.pnpsecure.service;  
  
import org.junit.jupiter.api.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.boot.test.context.SpringBootTest;  
  
@SpringBootTest  
public class BoardPaginationTest {  
    @Autowired  
    BoardPaginationService service;  
  
    @Test  
    public void getPagenationTest(){  
        System.out.println("================== getPagenationTest ==================");  
        System.out.println(service.getPagination(1, 5, 5));  
    }  
}
~~~