- dependency
~~~
Lombok
Spring Boot DevTools
Spring Web
Thymeleaf
MariaDB Driver
MyBatis Framework
~~~

- build.gradle
~~~
dependencies {  
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'  
    implementation 'org.springframework.boot:spring-boot-starter-web'  
    implementation 'org.mybatis.spring.boot:mybatis-spring-boot-starter:3.0.3'  
    compileOnly 'org.projectlombok:lombok'  
    developmentOnly 'org.springframework.boot:spring-boot-devtools'  
    runtimeOnly 'org.mariadb.jdbc:mariadb-java-client'  
    annotationProcessor 'org.projectlombok:lombok'  
    testImplementation 'org.springframework.boot:spring-boot-starter-test'  
    testImplementation 'org.mybatis.spring.boot:mybatis-spring-boot-starter-test:3.0.3'  
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
    
    // modelmapper 추가 수동 입력
    implementation group: 'org.modelmapper', name: 'modelmapper', version: '3.0.0'  
}
~~~

- application.properies
~~~
spring.application.name=webDevSys

#/repository
spring.datasource.driver-class-name=org.mariadb.jdbc.Driver
spring.datasource.url=jdbc:mariadb://localhost:3306/webdb
spring.datasource.username=webuser
spring.datasource.password=webuser
  
# log
logging.level.org.springframework=info
logging.level.org.hgtech=info
  
# file
spring.servlet.multipart.max-file-size=1000MB
spring.servlet.multipart.max-request-size=1000MB
  
# mybatis
mybatis.mapper-locations=classpath:mappers/*.xml
~~~

- project structure
~~~
-src
	|-main
		|-java
			|-org.hgtect.webdevsys
				|-config
				|-controller
				|-converter
				|-domain
				|-DTO
				|-filter
				|-reposipory
				|-service
				|-WebDevSysApplication
		|-resources
			|-mappers
				|-webInfo.xml
			|-static # 브라우저에서 /로 접근 가능. public 폴더도 동일 (ex: /css/style.css)
				|-css
					|-styles.css
				|-images
					|-img1.jpg
				|-js
					|-javascripts.js
			|-templates
				|-index.html
			|-application.properties
	|-test
		|-java
			|-org.hgtect.webdevsys
				|-controllerTests
				|-reposiporyTests
				|-serviceTests
				|-WebDevSysApplicationTestss
~~~
