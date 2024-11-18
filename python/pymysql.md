## **pymysql**
---
### **create Schema**
---
~~~python
### MySQL Workbench query 창에서 입력 후 ctrl+enter 키실행

CREATE SCHEMA naverland DEFAULT CHARACTER SET utf8mb4;
~~~

### **data type**
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

---

<br><br>

### **Connect DB**
---
~~~python
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8mb4')
~~~

### **Create Table**
---
~~~python
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8mb4')
sql = "CREATE TABLE IF NOT EXISTS corpCode(\
                corp_code VARCHAR(8),\
                corp_name VARCHAR(100),\
                stock_code VARCHAR(6),\
                modify_date TIMESTAMP\
            )"
db.cursor().execute(sql)
db.commit()
~~~
~~~python
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8mb4')
sql = "CREATE TABLE IF NOT EXISTS consolidatedData(\
        rceptNo VARCHAR(14),\
        consolidatedEquity BIGINT,\
        consolidatedliability BIGINT,\
        consolidatedNetIncome BIGINT,\
        consolidatedGrossProfit BIGINT,\
        consolidatedOperatingProfit BIGINT,\
        consolidatedConprehensiveNetIncome BIGINT,\
        consolidatedConprehensiveGrossProfit BIGINT,\
        consolidatedConprehensiveOperatingProfit BIGINT,\
        consolidatedOperatingActivities BIGINT\
        )"
db.cursor().execute(sql)
db.commit()
~~~
### **insert data**
---
~~~python
def get_values_part(self, data : dataclass):
    dic = data.dict()
    values = dic.values()

    values_part_lst = [self.get_string_format(value) for value in values]
    values_part = ', '.join(values_part_lst)
    return values_part

values_part = get_values_part(data)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8')
sql = f"insert into corpCode values ({values_part})"
db.cursor().execute(sql)
db.commit()
~~~
### **query data**
---
~~~python
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8')
c = db.cursor()
sql = 'select * from article_info'
c.execute(sql)
for data in c.fetchall()
  print(data)
~~~
