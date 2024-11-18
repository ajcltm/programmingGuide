- LOMBOK
~~~java
package org.hgtech.webdevsys.domain;  
  
import lombok.*;  
  
import java.time.LocalDateTime;  
  
@Data  
@ToString  
@Builder  
@AllArgsConstructor  
@NoArgsConstructor  
public class WebInfoVO {  
    int id;  
    LocalDateTime regDate;  
    LocalDateTime modDate;  
    String title;  
    String content;  
    String comment;  
    int parentId;  
}
~~~
