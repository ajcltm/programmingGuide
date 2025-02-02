
### 경로
---

~~~
-project
 |-src
  |-main
   |-java
    |-config
     |-WebConfig
    |-converter
     |-CustomConverter
~~~

### converter 구현
---

~~~java
// Spring의 `Converter<S, T>` 인터페이스는 소스 타입(S)을 타겟 타입(T)으로 변환하는 역할
public interface Converter<S, T> {
    T convert(S source);
}
~~~

~~~java
package org.hgtech.worksystem.converter;
import org.springframework.core.convert.converter.Converter;
import org.springframework.stereotype.Component;
  
import java.time.LocalDate;  
import java.time.LocalDateTime;  

@Component  
public class StringToLocalDateTimeConverter implements Converter<String, LocalDateTime> {
    @Override
    public LocalDateTime convert(String source) {
        if (source != null && source.matches("\\d{4}-\\d{2}-\\d{2}")) {
            // yyyy-MM-dd 형식 처리
            return LocalDate.parse(source).atStartOfDay();
        } else if (source != null && source.matches("\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}")) {
            // yyyy-MM-dd'T'HH:mm:ss 형식 처리
            return LocalDateTime.parse(source);
        }
    }
}
~~~

### webconfig 등록 설정
---
- @component 이노테이션을 달면 별도로 등록하지 않아도 됨(자동등록)
~~~java
package org.hgtech.worksystem.config;  
  
import org.hgtech.worksystem.converter.StringToLocalDateTimeConverter;  
import org.springframework.context.annotation.Configuration;  
import org.springframework.format.FormatterRegistry;  
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;  
  
@Configuration  
public class WebConfig implements WebMvcConfigurer {  
  
    @Override  
    public void addFormatters(FormatterRegistry registry) {  
        registry.addConverter(new StringToLocalDateTimeConverter());  
    }  
}
~~~
