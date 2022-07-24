### **database 생성**
---
- 아래 모두 database를 생상하는 동일한 쿼리임
~~~sql
CREATE SCHEMA schemaName DEFAULT CHARACTER SET utf8;
~~~

~~~sql
CREATE database databaseName DEFAULT CHARACTER SET utf8;
~~~

### **database 삭제**
~~~sql
drop database databaseName;
~~~

### **database 선택**
~~~sql
use dasebaseName;
~~~

### **table 생성**
~~~sql
CREATE TABLE test (
id int(11) not null auto_increment,
name varchar(10) not null,
email varchar(30),
primary key(id),
index name_index(name(10))  # name 필드를 name_index라는 이름으로 인덱스함
)
~~~

### **table 삭제**
~~~sql
DROP table tabelName;
~~~

### **data 입력**
~~~sql
INSERT INTO test (name, email) VALUES("Lee", "seed@gmail.com");
~~~

### **data 삭제**
~~~sql
DELETE FROM tableName WHERE id = 0;
DELETE FROM tableName     # tableName 내 모든 data 삭제
~~~

### **data 수정**
~~~sql
UPDATE tableName SET email='example@gmail.com' WHERE name='Lee';
~~~