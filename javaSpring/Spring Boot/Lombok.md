Lombok은 자바에서 보일러플레이트 코드를 줄여주는 라이브러리입니다. 반복적으로 작성해야 하는 `getter`, `setter`, `toString`, 생성자, 빌더 패턴 등을 어노테이션으로 간단히 처리할 수 있습니다.

### Lombok 설치

1. **Maven**
    
    ```xml
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.18.30</version> <!-- 최신 버전 확인 필요 -->
        <scope>provided</scope>
    </dependency>
    ```
    
2. **Gradle**
    
    ```gradle
    dependencies {
        compileOnly 'org.projectlombok:lombok:1.18.30'
        annotationProcessor 'org.projectlombok:lombok:1.18.30'
    }
    ```
    
3. **IDE 설정**  
    Lombok이 IntelliJ IDEA 또는 Eclipse에서 제대로 작동하려면 플러그인을 설치해야 합니다.
    
    - **IntelliJ IDEA**: `Settings > Plugins > Marketplace`에서 "Lombok" 설치
    - **Eclipse**: Lombok 공식 사이트에서 JAR 파일을 다운로드하여 IDE에 통합

---

### Lombok 어노테이션 사용법

#### @Getter와 @Setter

- 각 필드에 대해 getter/setter 메서드를 자동 생성합니다.
- 클래스에 적용하면 모든 필드에 일괄 적용됩니다.

```java
@Getter
@Setter
public class User {
    private String name;
    private int age;
}
```

#### @ToString

- `toString()` 메서드를 자동 생성합니다.
- 특정 필드만 포함하거나 제외하려면 `@ToString.Exclude` 또는 `of` 속성을 사용합니다.

```java
@ToString
public class User {
    private String name;
    private int age;

    @ToString.Exclude
    private String password;
}
```

#### @EqualsAndHashCode

- `equals()`와 `hashCode()` 메서드를 자동 생성합니다.
- 식별자 기반 비교를 원할 경우 `@EqualsAndHashCode.Include`를 활용합니다.

```java
@EqualsAndHashCode
public class User {
    private Long id;

    @EqualsAndHashCode.Include
    private String email;
}
```

#### @NoArgsConstructor, @AllArgsConstructor

- 기본 생성자와 모든 필드를 포함한 생성자를 자동 생성합니다.

```java
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private String name;
    private int age;
}
```

#### @RequiredArgsConstructor

- `final` 또는 `@NonNull` 필드만 포함한 생성자를 생성합니다.

```java
@RequiredArgsConstructor
public class User {
    private final String name;
    private int age;
}
```

#### @Builder

- 빌더 패턴을 자동 생성합니다.

```java
@Builder
public class User {
    private String name;
    private int age;
}
```

사용 예:

```java
User user = User.builder()
               .name("John")
               .age(25)
               .build();
```

#### @Data

- `@Getter`, `@Setter`, `@ToString`, `@EqualsAndHashCode`, `@RequiredArgsConstructor`를 한꺼번에 적용합니다.
- DTO와 같은 단순 데이터 클래스에 적합합니다.

```java
@Data
public class User {
    private String name;
    private int age;
}
```

#### @Value

- 불변 객체를 생성합니다. 모든 필드는 `final`로 선언되고, setter는 생성되지 않습니다.

```java
@Value
public class Address {
    private String city;
    private String street;
    private String zipcode;
}
```

#### @NonNull

- 특정 필드가 `null`이 될 수 없음을 명시합니다.  
    해당 필드에 대해 `@Setter` 또는 생성자를 통해 null 값이 들어오면 `NullPointerException`이 발생합니다.

```java
public class User {
    @NonNull
    private String name;

    private int age;
}
```

---

### Lombok 사용 시 주의사항

1. **Entity 클래스에 남용하지 않기**  
    Entity에서는 JPA와의 호환성을 위해 `@Data`보다는 `@Getter`와 `@Setter`를 개별적으로 사용하는 것이 좋습니다.
    
2. **DTO와 Entity 분리**  
    DTO는 `@Builder`, `@Data`를 사용해도 좋지만 Entity는 `@NoArgsConstructor`, `@AllArgsConstructor`와 조합하는 것이 일반적입니다.
    
3. **코드 가독성 검토**  
    Lombok 어노테이션만으로 구현하면 코드의 구조를 파악하기 어려울 수 있으므로, 꼭 필요한 곳에서만 사용하세요.
    
4. **디버깅**  
    Lombok이 생성하는 코드는 컴파일 타임에 추가되므로, 디버깅 시 메서드가 보이지 않아 불편할 수 있습니다. IDE 설정에서 Lombok 플러그인으로 생성된 코드를 확인하세요.
    

Lombok을 활용하면 개발 속도가 빨라지지만, 남용하면 코드 유지보수가 어려워질 수 있습니다. 상황에 맞게 적절히 사용하세요!