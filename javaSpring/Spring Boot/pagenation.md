
#### DTO

~~~java
package org.hgtech.board.DTO;
  
  
import lombok.Getter;
import lombok.ToString;
import org.hgtech.board.service.BoardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
  
import java.util.List
  
@Component
@ToString
@Getter
public class BoardPagenationDTO {  

    @Autowired
    BoardService boardService;

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
  
    public void calculate(int currentPage, int size, int nationSize) {
        this.total = boardService.totalSize();
        this.maxPage = total/size;
        this.currentPage = currentPage;
        this.size = size;
        this.nationSize = nationSize;
        calculDataStart();
        calculDataEnd();
        selectData();
        calculPageStart();
        calculPageEnd();
    }
  
    public void calculDataStart() {
        this.dataStart = currentPage*size;
    }
    public void calculDataEnd() {
        int dataEnd = dataStart+size-1;
        if (dataEnd > this.total-1) {
            this.dataEnd = this.total-1;
        } else {
            this.dataEnd = dataEnd;
        }
    }
  
    public void selectData(){
        this.dataList = boardService.getFrom(this.dataStart, this.size);
    }  
  
    public void calculPageStart() {
        int pageStart = (Integer)(currentPage / nationSize) * nationSize;
        if (pageStart > this.maxPage) {
            this.pageStart = this.maxPage;
        } else {
            this.pageStart = pageStart;
        }
    }
  
    public void calculPageEnd() {
        int pageEnd = this.pageStart + nationSize -1;
        if (pageEnd > this.maxPage) {
            this.pageEnd = this.maxPage;
        } else {
            this.pageEnd = pageEnd;
        }
    }
}
~~~

#### Service
---
~~~java
package org.hgtech.board.service;

import org.hgtech.board.DTO.BoardPagenationDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BoardPagenationService {
  
    @Autowired
    BoardPagenationDTO boardPagenationDTO;

    public BoardPagenationDTO getPagenation(int currentPage, int size, int nationSize){ 
        boardPagenationDTO.calculate(currentPage, size, nationSize);
        return boardPagenationDTO;
    }
}
~~~
