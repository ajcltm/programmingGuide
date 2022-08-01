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
---
~~~sql
drop database databaseName;
~~~

### **database 선택**
---
~~~sql
use dasebaseName;
~~~

### **table 생성**
---
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
---
~~~sql
DROP table tabelName;
~~~

### **data 입력**
---
~~~sql
INSERT INTO test (name, email) VALUES("Lee", "seed@gmail.com");
~~~

### **data 삭제**
---
~~~sql
DELETE FROM tableName WHERE id = 0;
DELETE FROM tableName     # tableName 내 모든 data 삭제
~~~

### **data 수정**
---
~~~sql
UPDATE tableName SET email='example@gmail.com' WHERE name='Lee';
~~~

### **query 순서**
---
~~~sql
<문법 작성 순서>
1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY
---
<실행 작동 순서>
1. FROM
2. ON
3. JOIN
4. WHERE
5. GROUP BY
6. CUBE | ROLLUP
7. HAVING
8. SELECT
9. DISTINCT
10. ORDER BY
11. TOP
~~~

### **DATEDIFF / TIMESTAMPDIFF**
---
- **DATEDIFF**
~~~sql
DATEDIFF(날짜1, 날짜2);
DATEDIFF('2018-03-28 23:59:59', '2017-03-01 00:00:00');
~~~
- **TIMESTAMPDIFF**
~~~sql
TIMESTAMPDIFF(단위, 날짜1, 날짜2);
TIMESTAMPDIFF(QUARTER, '2017-03-01', '2018-03-28');
~~~
symbol |unit
---    |--- 
SECOND | 초
MINUTE | 분
HOUR   | 시
DAY    | 일
WEEK   | 주
MONTH  | 월
QUARTER| 분기
YEAR   | 연

### **LAG** / **PATITION**
---
~~~sql
SELECT 
	employee_id, 
	fiscal_year, 
	salary,
	previous_salary,
	CONCAT(ROUND(( salary - previous_salary ) * 100 /previous_salary,0),'%')  YoY
FROM
	( SELECT 
		employee_id, 
		fiscal_year, 
		salary,
		LAG(salary,1,0) OVER (
			PARTITION BY employee_id 
			ORDER BY fiscal_year) previous_salary
	FROM
		basic_pays
	) t;   
~~~
