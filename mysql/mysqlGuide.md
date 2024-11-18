### **database 생성**
---
- 아래 모두 database를 생상하는 동일한 쿼리임
~~~sql
CREATE SCHEMA schemaName DEFAULT CHARACTER SET utf8mb4;
~~~

~~~sql
CREATE database databaseName DEFAULT CHARACTER SET utf8mb4;
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

### **INDEX**
---

- 인덱스 생성
~~~sql
CREATE INDEX 인덱스이름 ON 테이블이름 (필드이름1, 필드이름2, ...)
~~~

- UNIQUE 인덱스 생성
~~~sql
CREATE UNIQUE INDEX 인덱스이름 ON 테이블이름 (필드이름1, 필드이름2, ...)
~~~

- 인덱스 추가
~~~sql
ALTER TABLE 테이블명 ADD INDEX 인덱스명 (필드이름1, 필드이름2, ...)
~~~

- 인덱스 삭제
~~~sql
ALTER TABLE 테이블명 DROP INDEX 인덱스명
~~~

- 인덱스 정보 보기
~~~sql
SHOW INDEX FROM 테이블이름
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

Data Type
---

- basic type

|데이터 형식|바이트 수|설명|
|---|---|---|
|CHAR(n)	|1 ~ 255	|고정길이 문자형 n을 1부터 255까지 지정 그냥 CHAR만 쓰면 CHAR(1)과 동일
|VARCHAR(n)	|1 ~ 65535	|가변길이 문자형 n을 사용하면 1부터 65535까지 지정
|BINARY(n)	|1 ~ 255	|고정길이의 이진 데이터 값
|VARBINARY(n)	|1 ~ 255	|가변길이의 이진 데이터 값
|TINYTEXT	|1 ~ 255	|255 크기의 TEXT 데이터 값
|TEXT	|1 ~ 65535	|N 크기의 TEXT 데이터 값
|MEDIUMTEXT	|1 ~ 16777215	|16777215 크기의 TEXT 데이터 값
|LONGTEXT	|1 ~ 4294967295	|최대 4GB 크기의 TEXT 데이터 값
|TINYBLOB	|1 ~ 255	|255 크기의 BLOB 데이터 값
|BLOB	|1 ~ 65535	|N 크기의 BLOB 데이터 값
|MEDIUMBLOB	|1 ~ 16777215	|16777215 크기의 BLOB 데이터 값
|LONGBLOB	|1 ~ 4294967295	|최대 4GB 크기의 BLOB 데이터 값
|ENUM(값들...)	|1 또는 2	|최대 65535개의 열거형 데이터 값
|SET(값들...)	|1, 2, 3, 4, 8	|최대 64개의 서로 다른 데이터 값

- Number type 

|데이터 형식	|바이트 수	|숫자설명| 설명|
|---|---|---|---|
|BIT(N)|	N/8|	 	|1~64Bit 표현, b'0000'형식으로 표현
|TINYINT|	1|	-128 ~ 127	|정수
|MEDIUMINT|	3|	-8,388,608 ~ 8,388,607	|정수
|INT, INTEGER|	4|	약-21억 ~ +21억	|정수
|BIGINT|	8|	약 -900경 ~ +900경	|정수
|FLOAT|	4|	-3.40E+38 ~ -1.17E-38	|소수점 아래 7자리까지 표현
|DOUBLE, REAL|	8|	-1.22E-308 ~ 1.79E+308	|소수점 아래 15자리까지 표현
|DECIMAL(m,[d]), NUMBER(m,[d])|	5~17|	-10^38+1 ~ 10^38-1	|전체 자릿수(m)와 소수점 이하 자릿수(d)를 가진 숫자형 예) decimal(5,2)는 전체 자릿수를 5자리로 하되, 그 중 소수점 이하를 2자리로 함
