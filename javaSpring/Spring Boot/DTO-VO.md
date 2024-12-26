### **DTO**
~~~java
package org.hgtech.webdevsys.domain;  
  
import lombok.*;  
  
import java.time.LocalDateTime;  
  
@Data  
@ToString 
@Builder
@AllArgsConstructor  
@NoArgsConstructor  
public class someDTO {  
    int id;  
    LocalDateTime regDate;  
    LocalDateTime modDate;  
    String title;  
    String content;  
    String comment;  
    int parentId;  
}
~~~

### **VO**

~~~java
package org.hgtech.webdevsys.domain;  
  
import lombok.*;  
  
import java.time.LocalDateTime;  

@Getter
@ToString
@Builder
@AllArgsConstructor  
@NoArgsConstructor  
public class someDTO {  
    int id;  
    LocalDateTime regDate;  
    LocalDateTime modDate;  
    String title;  
    String content;  
    String comment;  
    int parentId;  
}
~~~

### **DTO, VO, Entity의 차이**

- **DTO (Data Transfer Object)**  
DTO는 계층 간 데이터 전송을 위해 사용하는 객체로, 주로 컨트롤러와 서비스 간 데이터 전달에 활용됩니다. 비즈니스 로직이 없어야 하며, 데이터를 담는 단순한 역할만 합니다.  
예: 클라이언트에서 서버로 요청 데이터를 전달하거나, 서버에서 클라이언트로 응답 데이터를 전달할 때 사용.


- **VO (Value Object)**  
VO는 변하지 않는 데이터의 값을 표현하는 객체입니다. 주로 값을 비교하거나 데이터 무결성을 보장하는 데 사용됩니다.  
예: 특정 값이 같은 경우 동일 객체로 간주해야 할 때 사용하며, `equals`와 `hashCode` 메서드가 중요합니다.

- **Entity**  
Entity는 데이터베이스 테이블과 직접 매핑되는 객체입니다. JPA, Hibernate와 같은 ORM 프레임워크를 사용할 때 주로 사용되며, 데이터베이스와의 CRUD 작업을 처리하는 데 활용됩니다.  
예: 테이블의 각 필드와 매핑되며, 실제 저장소와의 연동에서 핵심적인 역할을 합니다.