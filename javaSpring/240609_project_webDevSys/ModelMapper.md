
- build.gradle
~~~
dependencies {  
    // modelmapper 추가 수동 입력
    implementation group: 'org.modelmapper', name: 'modelmapper', version: '3.0.0'  
}
~~~

- config
~~~java
package org.hgtech.webdevsys.config;  
  
import org.modelmapper.ModelMapper;  
import org.modelmapper.convention.MatchingStrategies;  
import org.springframework.context.annotation.Bean;  
import org.springframework.context.annotation.Configuration;  
  
@Configuration  
public class RootConfig {  
  
    @Bean  
    public ModelMapper getMapper() {  
        ModelMapper modelMapper = new ModelMapper();  
        modelMapper.getConfiguration()  
                .setFieldMatchingEnabled(true)  
                .setFieldAccessLevel(org.modelmapper.config.Configuration.AccessLevel.PRIVATE)  
                .setMatchingStrategy(MatchingStrategies.LOOSE);  
        return modelMapper;  
    }  
}
~~~

