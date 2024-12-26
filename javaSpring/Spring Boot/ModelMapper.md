
### ModelMapper란?

**ModelMapper**는 Java 객체 간의 매핑을 간단하고 직관적으로 수행하는 라이브러리입니다. 주로 DTO(Data Transfer Object)와 Entity 간의 변환을 위해 사용되며, 매핑 코드의 중복을 줄여줍니다.

---

### 기본 설정

#### build.gradle
~~~
dependencies {  
    // modelmapper 추가 수동 입력
    implementation group: 'org.modelmapper', name: 'modelmapper', version: '3.0.0'  
}
~~~

#### config 설정파일
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

### 기본 사용법

#### 1. ModelMapper 객체 생성

```java
import org.modelmapper.ModelMapper;

ModelMapper modelMapper = new ModelMapper();
```

#### 2. 간단한 매핑

Entity와 DTO 간의 필드 이름이 동일한 경우 자동으로 매핑됩니다.

```java
// 예제 클래스
public class User {
    private Long id;
    private String name;
    private String email;
    // Getter/Setter
}

public class UserDTO {
    private String name;
    private String email;
    // Getter/Setter
}

// 매핑
User user = new User(1L, "John Doe", "john@example.com");
UserDTO userDTO = modelMapper.map(user, UserDTO.class);

System.out.println(userDTO.getName());  // 출력: John Doe
System.out.println(userDTO.getEmail()); // 출력: john@example.com
```

---

### 고급 사용법

#### 1. 프로퍼티 이름이 다른 경우

필드 이름이 다를 때는 매핑 규칙을 지정해야 합니다.

```java
import org.modelmapper.PropertyMap;

// 예제 클래스
public class Source {
    private String fullName;
    // Getter/Setter
}

public class Destination {
    private String name;
    // Getter/Setter
}

// 커스텀 매핑
PropertyMap<Source, Destination> propertyMap = new PropertyMap<>() {
    @Override
    protected void configure() {
        map().setName(source.getFullName());
    }
};
modelMapper.addMappings(propertyMap);

Source source = new Source();
source.setFullName("John Doe");

Destination destination = modelMapper.map(source, Destination.class);
System.out.println(destination.getName()); // 출력: John Doe
```

#### 2. 컬렉션 매핑

리스트 또는 배열도 매핑할 수 있습니다.

```java
import java.util.List;
import java.util.stream.Collectors;

List<User> userList = List.of(
    new User(1L, "Alice", "alice@example.com"),
    new User(2L, "Bob", "bob@example.com")
);

List<UserDTO> userDTOList = userList.stream()
    .map(user -> modelMapper.map(user, UserDTO.class))
    .collect(Collectors.toList());
```

---

### 매핑 전략 설정

ModelMapper는 기본적으로 필드 이름과 타입을 기반으로 매핑합니다. 하지만 더 세부적인 설정이 필요할 때 전략을 지정할 수 있습니다.

#### 1. 매핑 전략 변경

- **STANDARD**: 기본 전략
- **STRICT**: 필드 타입과 이름이 정확히 일치해야 매핑
- **LOOSE**: 느슨한 매핑, 일부 필드가 누락되어도 동작

```java
import org.modelmapper.convention.MatchingStrategies;

modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
```

#### 2. null 값 처리

`null` 값 무시 설정으로 매핑 시 대상 객체의 기존 값을 유지할 수 있습니다.

```java
modelMapper.getConfiguration().setSkipNullEnabled(true);
```

---

### 양방향 매핑

#### 1. DTO → Entity

```java
UserDTO userDTO = new UserDTO("Alice", "alice@example.com");
User user = modelMapper.map(userDTO, User.class);
```

#### 2. Entity → DTO

```java
User user = new User(1L, "Bob", "bob@example.com");
UserDTO userDTO = modelMapper.map(user, UserDTO.class);
```

---

### 커스텀 컨버터 사용

#### 1. 간단한 컨버터

```java
import org.modelmapper.Converter;
import org.modelmapper.spi.MappingContext;

// 커스텀 컨버터 정의
Converter<String, Integer> stringToInteger = new Converter<>() {
    @Override
    public Integer convert(MappingContext<String, Integer> context) {
        return Integer.valueOf(context.getSource());
    }
};

// 컨버터 추가
modelMapper.addConverter(stringToInteger);

// 사용
String source = "123";
Integer destination = modelMapper.map(source, Integer.class);
System.out.println(destination); // 출력: 123
```

#### 2. 복잡한 컨버터

```java
Converter<UserDTO, User> userConverter = new Converter<>() {
    @Override
    public User convert(MappingContext<UserDTO, User> context) {
        UserDTO source = context.getSource();
        User destination = new User();
        destination.setName(source.getName());
        destination.setEmail(source.getEmail());
        destination.setAge(30); // 추가 작업
        return destination;
    }
};

modelMapper.addConverter(userConverter);
```

---

### Spring Boot와 통합

#### 1. ModelMapper Bean 등록

```java
import org.modelmapper.ModelMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {
    @Bean
    public ModelMapper modelMapper() {
        return new ModelMapper();
    }
}
```

#### 2. 사용

```java
import org.springframework.beans.factory.annotation.Autowired;

@Service
public class UserService {
    @Autowired
    private ModelMapper modelMapper;

    public UserDTO convertToDTO(User user) {
        return modelMapper.map(user, UserDTO.class);
    }
}
```

---

ModelMapper는 기본 매핑에서부터 커스텀 매핑까지 강력한 기능을 제공하며, Spring Boot와 함께 사용할 때 특히 유용합니다. 적절히 설정하여 효율적인 매핑을 구현하세요!

