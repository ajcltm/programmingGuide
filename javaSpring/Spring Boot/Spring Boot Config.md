
- spring initializer
~~~
Lombok
Spring Boot DevTools
Spring Web
Thymeleaf
MariaDB Driver
MyBatis Framework
// Spring Boot 3.2.6 버전으로 해야 MyBatis Framework 선택이 활성화됨
~~~

- applicatioin.properties
~~~java
spring.application.name=economicSys
  
spring.datasource.driver-class-name=org.mariadb.jdbc.Driver
spring.datasource.url=jdbc:mariadb://localhost:3306/webdb
spring.datasource.username=webuser
spring.datasource.password=webuser

logging.level.org.springframework=info
logging.level.org.hgtech=debug
  
spring.servlet.multipart.max-file-size=1000MB
spring.servlet.multipart.max-request-size=1000MB

mybatis.mapper-locations=classpath:mappers/*.xml
~~~

-  업데이트 자동 반영
~~~
[Edit Configurations] - [Modify options] - [On 'Update' action] - [Update classes and resources]

[Edit Configurations] - [Modify options] - [On frame deactivation] - [Update classes and resources]
~~~

- 파일 경로
~~~
-projectName
|-src
	|-main
		|-java
			|-controller-package
			|-domain-package
			|-repository-package
			|-service-package
		|-resources
			|-mappers
			|-static
				|-css
					|-styles.css
				|-js
					|-scripts.js
			|-templates
				|-index.html
			|-application.properties
	|-test
~~~