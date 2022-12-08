## **sqlite3**
---
### **create DB file & table**
---
- variable type : text, integer, real, date, number(size), varchar2(size), char(size) 등 
~~~python
fileName = 'test.db'
fileDir = Path.home().joinpath('Desktop', fileName)
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
cur.execute('create table test_table (id integer primary key autoincrement, name text, num integer, value real)')
conn.commit()

conn.close()
~~~
- [참고] 테이블 삭제 방법
~~~python
fileName = 'test.db'
fileDir = Path.home().joinpath('Desktop', fileName)
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
cur.execute('drop table test_table)')
conn.commit()

conn.close()
~~~
### **insert values**
---
~~~python
fileName = 'test.db'
fileDir = Path.home().joinpath('Desktop', fileName)
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
cur.execute('''insert into test_table values (1004, 'LEE', 10, 24.2)''')
cur.execute('''insert into test_table values (?, ?, ?, ?)''', (1002, 'PARK', 88, 9.78))
cur.executemany('insert into test_table values (?, ?, ?, ?)', [(1006, 'KIM', 50, 29.9), (1003, 'LEE', 12, 29.11)])
conn.commit()

conn.close()
~~~

### **Pandas를 이용하여 테이블 및 데이터 추가**
---
~~~python
fileName = 'test.db'
fileDir = Path.home().joinpath('Desktop', fileName)

dic = {'name' : '송효주' , 'age' : 11, 'dog' : '송다루'}
df = pd.DataFrame(dic, index=[0])
con = sqlite3.connect(fileDir)
df.to_sql(f'test_table', con, index=False, if_exists='append')
~~~

### **데이터 출력**
---
- 하나씩 출력 (itteration 이용)
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
cur.execute('select * from article_info')
print(cur.fetchone())
print(cur.fetchone())
conn.close()
~~~
- 전체 출력
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
cur.execute('select * from article_info')

for row in cur.fetchall():
    print(row)
conn.close()
~~~ 

- Pandas 이용하여 데이터 읽기(dataFrame)
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
sql = f'select * from article_info'
df = pd.read_sql(sql, conn, index_col=None)
print(df)
~~~

### **Where Clause**
---
- where clause : in (?, ?, ?)
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
sql = f'select * from article_info where articleNo in (?, ?)'
args = ['2201917900', '2201919206']
cur.execute(sql, args)

for row in cur.fetchall():
     print(row)
conn.close() 
~~~

- where clause : date
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
sql = f"select * from article_info where aptUseApproveYmd > date('2020-01-01')"
cur.execute(sql)

for row in cur.fetchall():
     print(row)
conn.close() 
~~~

- where clause 함수형 v1
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
args=['2201917900', '2201919206']
formated = ','.join(args)
sql = f'select * from article_info where articleNo in ({formated})'
cur.execute(sql)
for row in cur.fetchall():
    print(row) 
conn.close()
~~~ 
- where clause 함수형 v2
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()
args=['2201917900', '2201919206']
sql="select * from article_info where articleNo in ({seq})".format(seq=','.join(['?']*len(args)))
cur.execute(sql, args)
for row in cur.fetchall():
    print(row) 
conn.close()
~~~
- multiple where + order by   
 ! order by 사용시 컬럼 뒤에 asc 또는 desc를 붙이면 각각 오름, 내림차순으로 정렬함
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select articleNo, articleName, dealPrice from article_info'
where_1 = f'where articleNo in ({ids_formated})'
where_2 = f'and dealPrice < 350000'
order = f'order by dealPrice desc, aptName asc'
sql = ' '.join([select, where_1, where_2, order])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()
~~~

- where clause : Pandas version
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
args=['2201917900', '2201919206']
formated = ','.join(args)
sql = f'select * from article_info where articleNo in ({formated})'

df = pd.read_sql(sql, conn, index_col=None)
print(df)
~~~

### **Join Clause**
---
- inner join ; left table과 right table에서 특정 조건을 만족하는 공통 요소만 불러옴
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

sql = f'select articleNo, articleName, aptName, aptHouseholdCount, dealPrice, complex_article.complexNo from article_info inner join complex_article on article_info.articleNo = complex_article.idNo'

lst = list(cur.execute(sql).fetchall())
print(lst[:5])
conn.close()

[out]
[('2201917900', 'LG개포자이 103동', 'LG개포자이', '212', 300000, '8928'), ('2201919206', 'LG개포자이 104동', 'LG개포자이', '212', 320000, '8928'), ('2201295075', 'LG개포자이 102동', 'LG개포자이', '212', 350000, '8928'), ('2201077766', 'LG개포자이 102동', 'LG개포자이', '212', 350000, '8928'), ('2202228480', 'LG개포자이 104동', 'LG개포자이', '212', 280000, '8928')]
~~~

- left outer join ; left table의 행은 그대로 두고 right table 중 특정 조건을 만족하는 요소를 가지고옴   
! right outer join은 반대이며, full outer join은 양쪽 table의 모든 행을 합침
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

sql = f'select articleNo, articleName, aptName, aptHouseholdCount, dealPrice, complex_article.complexNo from article_info left outer join complex_article on article_info.articleNo = complex_article.idNo'

lst = list(cur.execute(sql).fetchall())
print(lst[:5])
conn.close()
~~~
- multiple join ; 작성된 코드 순서대로 join함
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

sql = f'select articleNo, articleName, aptName, aptHouseholdCount, dealPrice, complex_article.complexNo, dong_complex.name from article_info left outer join complex_article on article_info.articleNo = complex_article.idNo inner join dong_complex on complex_article.complexNo = dong_complex.idNo'

lst = list(cur.execute(sql).fetchall())
print(lst[:5])
conn.close()
~~~

### **join + where + order by**
---
- join, where, order by 순으로 query해야함
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

cols = 'articleNo, articleName, aptName, aptHouseholdCount, dealPrice, complex_article.complexNo, dong_complex.name'

select_table = 'article_info'
select = f'select {cols} from {select_table}'
outer_join_table = 'complex_article'
on = f'on {select_table}.articleNo = {outer_join_table}.idNo'
left_outer = f' left outer join {outer_join_table} {on}'

inner_join_table = 'dong_complex'
on = f'{outer_join_table}.complexNo = {inner_join_table}.idNo'
inner = f' inner join {inner_join_table} on {on}'

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
where_1 = f' where articleNo in ({ids_formated})'

where_2 = f'and dealPrice < 350000'

order = f' order by dealPrice desc, aptName asc'

sql = select + left_outer + inner + where_1 + where_2 + order

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()
~~~

### **Regex**
---
- python의 sqlite3 library에는 정규표현식을 사용할 수 있는 함수가 내장되어 있지 않아서 직접 함수를 설정해주아야함

~~~python
def regexp(expr, item):         # 별도 함수를 만들어줌
    reg = re.compile(expr)
    return reg.search(item) is not None

time_str = '(20220204-002000)'
fileName = f'naverLand{time_str}'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
conn.create_function("REGEXP", 2, regexp)  # 사용자 함수를 등록함
conn.row_factory = sqlite3.Row
cur = conn.cursor()

sql = f'''select idNo from article_info where idNo REGEXP '^[201]' '''
~~~

### **Group By**
---
- avg(*) + group by
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select aptName, AVG(dealPrice) from article_info'
where = f'where articleNo in ({ids_formated})'
groupBy = f'group by aptName'
sql = ' '.join([select, where, groupBy])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이', 320000.0), ('서희스타힐스', 73000.0), ('장안푸르미에(도시형)', 13300.0)]
~~~

- sum(*) + group by
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select aptName, SUM(roomCount) from article_info'
where = f'where articleNo in ({ids_formated})'
groupBy = f'group by aptName'
sql = ' '.join([select, where, groupBy])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이', 20), ('서희스타힐스', 3), ('장안푸르미에(도시형)', 1)]
~~~

- min(*) + group by  ; max도 동일한 방식으로 사용 가능함
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select aptName, MIN(dealPrice) from article_info'
where = f'where articleNo in ({ids_formated})'
groupBy = f'group by aptName'
sql = ' '.join([select, where, groupBy])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이', 280000), ('서희스타힐스', 73000), ('장안푸르미에(도시형)', 13300)]
~~~

- count(*) + group by   
 ! where 절과 함께 사용시에는 select 컬럼 from table where 조건 group by 컬럼 형식으로 순서를 지키서 입력해야함
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select aptName, COUNT(*) from article_info'
where = f'where articleNo in ({ids_formated})'
groupBy = f'group by aptName'
sql = ' '.join([select, where, groupBy])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이', 5), ('서희스타힐스', 1), ('장안푸르미에(도시형)', 1)]
~~~

~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select articleName, aptName, COUNT(*) from article_info'
where = f'where articleNo in ({ids_formated})'
groupBy = f'group by articleName, aptName'
sql = ' '.join([select, where, groupBy])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이 102동', 'LG개포자이', 2), ('LG개포자이 103동', 'LG개포자이', 1), ('LG개포자이 104동', 'LG개포자이', 2), ('서희스타힐스 1동', '서희스타힐스', 1), ('장안푸르미에(도시형) 1동', '장안푸르미에(도시형)', 1)]
~~~
- group by + having   
 ! haveing은 group by문이 끝나고 추가적인 필터 조건을 입력하기 위해 사용함(group by 다음에 나와야함)
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['2201917900', '2201919206', '2201295075', '2201077766', '2202228480', '2200666701', '2134477322']
ids_formated = ','.join(args)
select = f'select articleName, aptName, COUNT(*) from article_info'
where = f'where articleNo in ({ids_formated})'
groupBy = f'group by articleName, aptName'
having = f'having count(*) >= 2'
sql = ' '.join([select, where, groupBy, having])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이 102동', 'LG개포자이', 2), ('LG개포자이 104동', 'LG개포자이', 2)]
~~~

### **컬럼 병합**
---
~~~python
[in]
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args = ['8928', '8967', '14947', '104277', '8971']
ids_formated = ','.join(args)
select = f'select name, (cortarAddress || " " || detailAddress) as fullAddress from dong_complex'
where = f'where idNo in ({ids_formated})'
sql = ' '.join([select, where])

lst = list(cur.execute(sql).fetchall())
print(lst)
conn.close()

[out]
[('LG개포자이', '서울시 강남구 개포동 12-2'), ('개포현대5차', '서울시 강남구 개포동 172-3'), ('더샵그린', '서울시 강남구 개포동 1167'), ('논현대우멤버스카운티', '서울시 강남구 논현동 30-2'), ('논현동양파라곤', '서울시 강남구 논현동 245')]
~~~


### **SQL to Python object**
---
- to list
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
cur = conn.cursor()

args=['2201917900', '2201919206']
formated = ','.join(args)
sql = f'select * from article_info where articleNo in ({formated})'

cur.execute(sql)

lst = list(cur.fetchall())
print(lst)
conn.close()
~~~

- to dictionary   
! conn.row_factory = sqlite3.Row 설정을 하면, 결과가 row object 형태로 반환되며, 파이썬 dictionary 처럼 keys() 메서드를 사용할 수 있음. 단, values()나 items() 메서드는 제공하지 않음
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

args=['2201917900', '2201919206']
formated = ','.join(args)
sql = f'select * from article_info where articleNo in ({formated})'

cur.execute(sql)

lst = []
for row in cur.fetchall():
    lst.append({key : row[key] for key in row.keys()})
print(lst)
conn.close()
~~~

### **DB FILE backup**
---
- (검증이 필요함)
~~~python
fileName = 'naverLand(20220122-181419)'
fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}.db'
conn = sqlite3.connect(fileDir)
with conn:
    dump_fileDir = Path.cwd() / 'naverLand' / 'db' / f'{fileName}_dump.db'
    with open(dump_fileDir, "w", encoding='utf-8') as f:
        for line in conn.iterdump():
            f.write("%s\n" % line)
        print("Dump Print Complet")
conn.close()
~~~
<br><br><br>
