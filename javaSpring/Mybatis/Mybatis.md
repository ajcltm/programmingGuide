- pom.xml
	- maven install 필요(Run as - 6.maven install)
~~~xml
<!-- https://mvnrepository.com/artifact/org.apache.commons/commons-dbcp2 -->
<dependency>
	<groupId>org.apache.commons</groupId>
	<artifactId>commons-dbcp2</artifactId>
	<version>2.10.0</version>
</dependency>

<!-- https://mvnrepository.com/artifact/com.mysql/mysql-connector-j -->
<dependency>
	<groupId>com.mysql</groupId>
	<artifactId>mysql-connector-j</artifactId>
	<version>8.2.0</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.mybatis/mybatis -->
<dependency>
	<groupId>org.mybatis</groupId>
	<artifactId>mybatis</artifactId>
	<version>3.5.13</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.mybatis/mybatis-spring -->
<dependency>
	<groupId>org.mybatis</groupId>
	<artifactId>mybatis-spring</artifactId>
	<version>1.3.2</version>
</dependency>

<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-jdbc</artifactId>
	<version>${org.springframework-version}</version>
</dependency>
~~~

- root-context.xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:mybatis="http://mybatis.org/schema/mybatis-spring"
xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
http://mybatis.org/schema/mybatis-spring http://mybatis.org/schema/mybatis-spring.xsd">

<!-- Root Context: defines shared resources visible to all other web components -->
<bean id="dataSource" class="org.apache.commons.dbcp2.BasicDataSource" destroy-method="close">
	<property name="driverClassName" value="com.mysql.cj.jdbc.Driver" />
	<property name="url" value="jdbc:mysql://localhost/testdb" />
	<property name="username" value="root" />
	<property name="password" value="3795264Ab!" />
</bean>

<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
	<property name="dataSource" ref="dataSource" />
	<property name="configLocation" value="classpath://mapper/mybatis-config.xml" />
</bean>

<mybatis:scan base-package="com.laonsys.laspd.webconsole.dao" />

</beans>
~~~

- mybatis-config.xml
	-  src/main/resources/mapper/mybatis-config.xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE configuration PUBLIC "//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd" >

<configuration>
<mappers>
	<mapper resource="/mapper/TimeMapper.xml"/>
</mappers>
</configuration>
~~~

- TimeMapper.xml
	-  src/main/resources/mapper/mybatis-config.xml
~~~xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.laonsys.laspd.webconsole.dao.TimeMapper">
	<select id="getTime2" resultType="String">
	select sysdate() from dual
	</select>
</mapper>
~~~

- dao interface
~~~java
package com.laonsys.laspd.webconsole.dao;

import org.apache.ibatis.annotations.Select;

public interface TimeMapper {
	@Select("SELECT SYSDATE() FROM DUAL")
	public String getTime();
	public String getTime2();
}
~~~

