- project 생성
	- File - New - Project - Maven Project - Filter : [입력] org.apahe.maven - [클릭] Artifact Id: maven-archetype-webapp - Group Id: [입력] 회사이름 - [입력] Artifact Id: project name - Finish
	- 설치 프로세스가 진행 될때, y를 한번 입력해줘야 한다.

- project properties 설정
	- Maven - Project Facets
		- Dynamic Web Module 체크
		- Java - [tab] Runtimes  - apache-tomcat-9.0.71 체크
	- Deployment Assembly
		- Add... 클릭 - Java Build Path Entries - [Next] - Maven Dependencies - [Finish] 
		- (Dynamic Web Moudule 체크 설정이 되어 있어야만 project properties 설정에 Deployment Assembly 설정 매뉴가 나타난다)

- tomcat 서버에 프로젝트 추가
	- Maven 인터페이스 하단에 [tab] Servers - Tomcat v9.0 Server at localhost [마우스 오른쪽 클릭] - Add and Remove... [클릭] - 프로젝트 [Add >] 

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
		|-webapp
			|-META-INF
				|-MANIFEST.MF
			|-WEB-INF
				|-lib
				|-spring
					|-appServlet
						|-servlet-context.xml
					|-root-context.xml
				|-views
					|-home.jsp
					|-welcome.jsp
				|-resources
					|-css
						|-cssfile.css
				|-web.xml
	|-test
|-target
|-pom.xml
~~~

- pom.xml 설정
	- properties 추가

	~~~xml
	<properties>
		<!--springframework-version 추가 -->
		<org.springframework-version>5.3.19</org.springframework-version>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<maven.compiler.source>1.7</maven.compiler.source>
		<maven.compiler.target>1.7</maven.compiler.target>
	</properties>
	~~~

	- dependency 추가
		- spring dependency
		~~~xml
		<!-- Spring -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-context</artifactId>
			<version>${org.springframework-version}</version>
			<exclusions>
				<!-- Exclude Commons Logging in favor of SLF4j -->
				<exclusion>
					<groupId>commons-logging</groupId>
					<artifactId>commons-logging</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-webmvc</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>
		~~~

		- servlet dependency
		~~~xml
		<!-- Servlet -->
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>servlet-api</artifactId>
			<version>2.5</version>
			<scope>provided</scope>
		</dependency>
		<dependency>
			<groupId>javax.servlet.jsp</groupId>
			<artifactId>jsp-api</artifactId>
			<version>2.1</version>
			<scope>provided</scope>
		</dependency>
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>jstl</artifactId>
			<version>1.2</version>
		</dependency>
		~~~

		- build plugin 추가
		~~~xml
		<build>
			<plugins>
				<plugin>
					<artifactId>maven-eclipse-plugin</artifactId>
					<version>2.9</version>
					<configuration>
						<additionalProjectnatures>
							<projectnature>org.springframework.ide.eclipse.core.springnature</projectnature>
						</additionalProjectnatures>
						<additionalBuildcommands>
							<buildcommand>org.springframework.ide.eclipse.core.springbuilder</buildcommand>
						</additionalBuildcommands>
						<downloadSources>true</downloadSources>
						<downloadJavadocs>true</downloadJavadocs>
					</configuration>
				</plugin>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-compiler-plugin</artifactId>
					<version>2.5.1</version>
					<configuration>
						<source>1.6</source>
						<target>1.6</target>
						<compilerArgument>-Xlint:all</compilerArgument>
						<showWarnings>true</showWarnings>
						<showDeprecation>true</showDeprecation>
					</configuration>
				</plugin>
				<plugin>
					<groupId>org.codehaus.mojo</groupId>
					<artifactId>exec-maven-plugin</artifactId>
					<version>1.2.1</version>
					<configuration>
						<mainClass>org.test.int1.Main</mainClass>
					</configuration>
				</plugin>
			</plugins>
		</build>
		~~~

- web.xml 설정
	- 네임스페이스 설정
	~~~xml
	<?xml version="1.0" encoding="UTF-8"?>
	<web-app version="2.5" xmlns="http://java.sun.com/xml/ns/javaee"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee https://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">
	</web-app>
	~~~

	- context-param설정
	~~~xml
	<!-- The definition of the Root Spring Container shared by all Servlets and Filters -->
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/spring/root-context.xml</param-value>
	</context-param>
	~~~

	- listener 설정
	~~~xml
	<!-- Creates the Spring Container shared by all Servlets and Filters -->
	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>
	~~~

	- servlet 설정
	~~~xml
	<!-- Processes application requests -->
	<servlet>
		<servlet-name>appServlet</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		<init-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
		</init-param>
		<load-on-startup>1</load-on-startup>
	</servlet>
	~~~

	- servlet-mapping 설정
	~~~xml
	<servlet-mapping>
		<servlet-name>appServlet</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>
	~~~

	- url 한글 인코딩
	~~~xml
	<filter>
        <filter-name>encodingFilter</filter-name>
        <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
        <init-param>
            <param-name>encoding</param-name>
            <param-value>UTF-8</param-value>
        </init-param>
    </filter>
    <filter-mapping>
        <filter-name>encodingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
	~~~

- servlet-context 설정
	- 네임스페이스 설정
	~~~xml
	<?xml version="1.0" encoding="UTF-8"?>
	<beans:beans xmlns="http://www.springframework.org/schema/mvc"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xmlns:beans="http://www.springframework.org/schema/beans"
		xmlns:context="http://www.springframework.org/schema/context"
		xsi:schemaLocation="http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd
			http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
			http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">
	</beans:beans>
	~~~

	- annotation 설정
	~~~xml
	<!-- Enables the Spring MVC @Controller programming model -->
	<annotation-driven />
	~~~

	- resource mapping 설정
	~~~xml
	<!-- Handles HTTP GET requests for /resources/** by efficiently serving up static resources in the ${webappRoot}/resources directory -->
	<resources mapping="/resources/**" location="/resources/" />
	~~~

	- resolver 설정
	~~~xml
	<!-- Resolves views selected for rendering by @Controllers to .jsp resources in the /WEB-INF/views directory -->
	<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<beans:property name="prefix" value="/WEB-INF/views/" />
		<beans:property name="suffix" value=".jsp" />
	</beans:bean>
	~~~

	- conmponent-scan 설정
	~~~xml
	<context:component-scan base-package="org.hgtect.mvc" />
	~~~

	- root-context 설정
	~~~xml
	<?xml version="1.0" encoding="UTF-8"?>
	<beans xmlns="http://www.springframework.org/schema/beans"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd">
		
		<!-- Root Context: defines shared resources visible to all other web components -->	
	</beans>
	~~~