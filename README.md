## **Dictionary**
---
### **dictionary 기본**
---
- dictionary 생성
  
~~~python
[in]
dic = {}
for i in range(0,4) :
    dic[f'key_{i}'] = i
dic

[out]
{'key_0': 0, 'key_1': 1, 'key_2': 2, 'key_3': 3}
~~~
~~~python
[in]
withdrawal = {}

symbols = ['AAPL', 'NVDA', 'AMZN']
for symbol in symbols:
    withdrawal[symbol] = {'unitPrice': 0, 'amounts': 0}
withdrawal

[out]
{'AAPL': {'unitPrice': 0, 'amounts': 0}, 'NVDA': {'unitPrice': 0, 'amounts': 0}, 'AMZN': {'unitPrice': 0, 'amounts': 0}}
~~~

- 요소 삭제
~~~python
[in]
dic = {1: 'a', 'name':'pey', 3:[1,2,3]}

del dic[1]
dic

[out]
{'name': 'pey', 3: [1, 2, 3]}
~~~

- dic.keys()
~~~python
[in]
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic.keys())
print(list(dic.keys()))

[out]
dict_keys(['name', 'phone', 'birth'])
['name', 'phone', 'birth']
~~~

- dic.values()
~~~python
[in]
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic.values()

[out]
dict_values(['pey', '0119993323', '1118'])
~~~

- key, value 쌍 얻기(items)
~~~python
[in]
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic.items()

[out]
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
~~~

- Dictionnary 결합
~~~python
[in]
dic1 = {1:10, 2:20}
dic2 = {1:100, 3:300}

dic1.update(dic2)

[out]
{1: 100, 2: 20, 3: 300}
~~~


- Key: Value 쌍 모두 지우기(clear)
~~~python
[in]
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic.clear()
dic

[out]
{}
~~~

- Key로 Value얻기(get)  
  ! dic.get('name')은 dic['name']을 사용했을 때와 동일한 결괏값이지만, 해당키가 없을시 에러 대신 None값을 반환  
  ! 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용
~~~python
[in]
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic.get('name'))
print(dic.get('nokey'))

[out]
pey
None
~~~
~~~python
[in]
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
dic.get('foo', 'bar')

[out]
bar
~~~

- 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
~~~python
[in]
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in dic)
print('email' in dic)

[out]
True
False
~~~

<br><br><br>



## **Pandas**
---
### **DataFrame & Series**
---
- pd.DataFrame()에서 row의 length가 하나일때 발생하는 error  
  ! 주의 : 아래 예시는 np.random.randint(0,10,size=(1,5))의 return값이 array([[3, 9, 6, 5, 9]])으로 2차원 배열이기 때문에 배열의 각 원소를 value로 인식하지 않고 array([[3, 9, 6, 5, 9]]) 전체를 하나의 원소(scalar)로 취급하기 때문에 index에러가 발생함. 1차원 배열을 입력해야 의도한 대로 5행 2열의 DataFrame을 얻을 수 있음
  
~~~python
[in]
data = {
    'col1' : np.random.randint(0,10,size=(1,5)),
    'col2' : np.random.randint(0,10,size=(1,5))
}

df = pd.DataFrame(data)
df

[out]
[...]
ValueError: If using all scalar values, you must pass an index
~~~
~~~python
[in]
data = {
    'col1' : np.random.randint(0,10,size=(5)),
    'col2' : np.random.randint(0,10,size=(5))
}

df = pd.DataFrame(data)
df

[out]
	col1	col2
0	1      	1
1	5      	2
2	7      	3
3	6      	6
4	3      	9
~~~

### **Data 조회**
---
- loc와 iloc의 차이
~~~python
df
	col1	col2
0	1      	1
1	5      	2
2	7      	3
3	6      	6
4	3      	9
~~~

~~~python
[in]
df.iloc[2:3]

[out]
	col1	col2
2	7      	3
~~~
~~~python
[in]
df.loc[2:3]

[out]
	col1	col2
2	7      	3
3	6      	6
~~~

### **Series.str**
---
- Series.str.strip()
  : 맨 왼쪽과 오른쪽의 공백문자 제거(가운데 공백문자는 제거 하지 않음)
~~~python
df = pd.DataFrame(
    np.random.randn(3, 2), columns=[" Column A ", " Column B "], index=range(3)
)
df
    Column A    Column B
0   -0.020580    0.461255
1   -1.251339   -1.173025
2   -0.445028   -0.658810
~~~

~~~python
[in]
df.columns.str.strip()

[out]
Index(['Column A', 'Column B'], dtype='object')
~~~

- Series.str.replace()
  : 특정 문자를 다른 문자로 대체함(공백문자 제거에 활용할 수 있음)
~~~python
s = pd.Series(["ab c", "c de ", np.nan, " f g h "], dtype="string")
s
0       ab c
1      c de
2       <NA>
3     f g h
~~~

~~~python
[in]
s.str.replace(' ','')

[out]
0     abc
1     cde
2    <NA>
3     fgh
~~~

- Series.str.cat()
  : series의 각 원소를 하나의 str로 합침
~~~python
df = pd.DataFrame({'ticker':['005930', '000829'],
                    'name':['samsung', 'dongsan']})
df
   ticker     name
0  005930  samsung
1  000829  dongsan
~~~

~~~python
[in]
df.apply(lambda row: row.str.cat(sep='&'), axis=1)

[out]
0    005930&samsung
1    000829&dongsan
~~~

- Series.str.contains(string/pattern, case=True/False, regex=True/False)  
  : case는 대소문자 구별여부, regex는 정규식 표현 여부임
~~~python
df
  col1 col2
0  1   apple
1  2   abcde
2  3   lelele
3  4   Ppa
4  5   xyzab
5  6   123
~~~

~~~python
[in]
con = df.col2.str.contains('pp', case=False, regex=False)
df.loc[con]

[out]
	col1	col2
0	1      	apple
3	4      	Ppa
~~~
~~~python
[in]
con = df.col2.str.contains('a+', case=False, regex=True)
df.loc[con]

[out]
	col1	col2
0	1      	apple
1	2      	abcde
3	4      	Ppa
4	5      	xyzab
~~~

- Series.str.extract() : 정규식으로 표현된 그룹을 추출하여 새로운 열로 반환
~~~python
[in]
df.col2.str.extract(r"(a+)")

[out]
	0
0	a
1	a
2	NaN
3	a
4	a
5	NaN
~~~

### **groupby**
---
- groupby + transform()
~~~python
[in]
df = DataFrame({'group_1': ['a', 'a', 'a', 'a', 'b'], 
                       'group_2': ['c', 'c', 'd', 'd','e'], 
                       'col': [1, np.NaN, 4, 5, 6]})
                    
df['count_col'] = df.groupby(['group_1', 'group_2']).col.transform('count')
df

[out]
	group_1	group_2	col	count_col
0	a	       c	1.0	       1
1	a	       c	NaN	       1
2	a	       d	4.0	       2
3	a	       d	5.0	       2
4	b	       e	6.0	       1
~~~
~~~python
[in]
df['sum_col'] = df.groupby(['group_1', 'group_2']).col.transform('sum')
df

[out]
	group_1	group_2	col	sum_col
0	a	       c	1.0    1.0
1	a	       c	NaN    1.0
2	a	       d	4.0    9.0
3	a	       d	5.0    9.0
4	b	       e	6.0    6.0
~~~
~~~python
[in]
df['max_col'] = df.groupby(['group_1', 'group_2']).col.transform('max')
df

[out]
	group_1	group_2	col	max_col
0	a	       c	1.0    1.0
1	a	       c	NaN    1.0
2	a	       d	4.0    5.0
3	a	       d	5.0    5.0
4	b	       e	6.0    6.0
~~~

- groupby + pct_change()
~~~python
[in]
df = pd.DataFrame({'country' : ['kor']*3 + ['jap']*3,
                    'value' : [100,105,109,100,101,100]})
                    
df['pct_change'] = df.groupby(['country']).value.pct_change()
df

[out]
  country value pct_change
0 kor     100   NaN
1 kor     105   0.050000
2 kor     109   0.038095
3 jap     100   NaN
4 jap     101   0.010000
5 jap     100  -0.009901
~~~

- groupby + pct_change() + transform() + cumprod()
~~~python
[in]
df = pd.DataFrame({'country' : ['kor']*3 + ['jap']*3,
                    'value' : [100,105,109,100,101,100]})
df['pct_change']=df.groupby(['country']).value.pct_change()
df['cumulativeReturn']=df.groupby(['country'])['pct_change'].transform(lambda x : x+1)
df['cumulativeReturn']=df.groupby(['country'])['cumulativeReturn'].cumprod()
df

# df.groupby(['country']).value.pct_change().transform(lambda x : x+1).cumprod()  -> 이렇게 하지 않도록 주의!

[out]
       country	value	cumulativeReturn
0	kor	       100	       NaN
1	kor	       105	       1.05
2	kor	       109	       1.09
3	jap	       100	       NaN
4	jap	       101	       1.01
5	jap	       100	       1.00
~~~


<br><br><br>



## **Numpy**
---
### **random**
---
- np.random.rand() : [0.0, 1.0] 임의값 반환하며 shape으로 입력 시 array 반환(미입력 시 scalar)

~~~python
[in]
np.random.rand(2, 3)

[out]
array([[0.41140371, 0.98738577, 0.42903107],
       [0.93806615, 0.45240497, 0.12544594]])
~~~

- np.random.random() : [0.0, 1.0) 임의값 반환하며, shape를 튜플로 입력해야함(미입력 시 scalar)
~~~python
[in]
np.random.random((2,3))

[out]
array([[0.41140371, 0.98738577, 0.42903107],
       [0.93806615, 0.45240497, 0.12544594]])
~~~

- np.random.randn() : 평균이 0이고 표준편차가 1인 정규분포의 임의값 반환 (가우시안 분포), shape으로 입력 시 array 반환(미입력 시 scalar)
~~~python
[in]
np.random.randn(2,3)

[out]
array([[ 0.40054939,  0.30965968, -0.50036237],
       [ 0.64300747,  1.56065243, -0.33234598]])
~~~

- np.random.randint() : 입력값들 사이의 정수를 반환함 (균등 분포), 인자는 다음과 같음 -> low : int, high:int (optional), size : int or tuple 
~~~python
[in]
np.random.randint(-100, 100, size=(2,3))

[out]
array([[-62,  10,  -8],
       [ 70,  36, -68]])
~~~
<br><br><br>

## **Time**
---
### **datetime**
---

- 현재 일자 및 시각 생성
~~~python
[in]
datetime.now()

[out]
datetime.datetime(2021, 10, 15, 17, 27, 57, 116839)
~~~

- 특정 일자 생성
~~~python
[in]
datetime.datetime(1923, 8, 29)

[out]
datetime.datetime(1923, 8, 29, 0, 0)
~~~

- datetime object를 str로 변환
~~~python
[in]
date = datetime.datetime(1923, 8, 29)
date.strftime(format='%Y-%m-%d')

[out]
'1923-08-29'
~~~


- str을 datetime object로 변환  
! 주의 : 인자를 format='%Y-%m-%d'이라고 쓰면 안됨
~~~python
[in]
date = '1923-8-29'
datetime.datetime.strptime(date, '%Y-%m-%d')

[out]
datetime.datetime(1923, 8, 29, 0, 0)
~~~

- 기간 리스트 만들기
~~~python
[in]
start = datetime.datetime.strptime("1923-08-29", "%Y-%m-%d")
end = datetime.datetime.strptime("1923-09-03", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dayList = []
for date in date_generated:
    dayList.append(date.strftime("%Y%m%d"))

dayList

[out]
['19230829', '19230830', '19230831', '19230901', '19230902']
~~~

- datetime에 3개월 더하는 방법 (timedelta는 시간, 일, 주 단위 연산만 가능)
~~~python
[in]
from dateutil.relativedelta import relativedelta

date = datetime.datetime(1923, 8, 29)
date + relativedelta(months=3)

[out]
datetime.datetime(1923, 11, 29, 0, 0)
~~~


### **Pandas에서 시간 다루기**
---
- 특정열을 datetime 포맷으로 변경

~~~python
[in]
date = ['1923-08-29','1923-08-30','1923-09-01','1923-09-02']
df = pd.DataFrame(date, columns=['date'])
pd.to_datetime(df['date'], format='%Y-%m-%d')

[out]
0   1923-08-29
1   1923-08-30
2   1923-09-01
3   1923-09-02
Name: date, dtype: datetime64[ns]
~~~


- 분기 str format을 period[M] format으로 변환 (datetime은 분기 연산은 다루지 않음)
~~~python
[in]
quater = ['1923-1','1923-2','1923-3','1923-4']
df = pd.DataFrame(quater, columns=['quater'])

df['quater'].apply(lambda x:pd.Period(x[:-1] + "Q" + x[-1:], freq="M"))

[out]
# 월로 변환되었음(1923-3 -> 1923-07)
0    1923-01 
1    1923-04
2    1923-07
3    1923-10
Name: quater, dtype: period[M]
~~~
<br><br><br>



## **Web Scrapping**
---
### **requests**
---
- get(url)
~~~python
[in]
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita'

r = requests.get(url)
html = r.text
html

[out]
'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title>List of countries by GDP (PPP) per capita - [...] ;</script>\n</body></html>'
~~~

- get(url, params)  
;params에 딕셔너리를 입력하면 필요할 경우 url을 인코딩해줌
~~~python
[in]
url = 'https://finance.naver.com/item/coinfo.naver?'
parm = {'code': '005930'}

r = requests.get(url, params=parm)
html = r.text
html

[out]
'<!--  global include -->\n\n\t\n\t\n<html lang=\'ko\'>\n<head>\n\n\n\t\n\t\t<title>삼성전자 : [...]'
~~~

- post(url, data)
~~~python
[in]
url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
data = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT01901',
        'mktId': 'STK',
        'share': '1',
        'csvxls_isNo': 'false'
}
r = requests.post(url, data = data)
html = r.text
html

[out]
'{"OutBlock_1":[{"ISU_CD":"KR7095570008","ISU_SRT_CD":"095570","ISU_NM":"AJ네트웍스보통주","ISU_ABBRV":"AJ네트웍스", [...] :"2021.10.19 AM 12:19:07"}'
~~~

- json()
~~~python
[in]
url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
data = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT01901',
        'mktId': 'STK',
        'share': '1',
        'csvxls_isNo': 'false'
}
r = requests.post(url, data = data)
json = r.json()
json

[out]
'{'OutBlock_1': [{'ISU_CD': 'KR7095570008',
   'ISU_SRT_CD': '095570',
   'ISU_NM': 'AJ네트웍스보통주',
   'ISU_ABBRV': 'AJ네트웍스', 
   [...]
}'
~~~

~~~python
# json format -> pandas dataframe
[in]
pd.DataFrame(r.json()['OutBlock_1'])

[out]

       ISU_CD	       ISU_SRT_CD	ISU_NM	       ISU_ABBRV     [...]
0	KR7095570008	095570	       AJ네트웍스보통주	AJ네트웍스	[...]
1	KR7006840003	006840	       AK홀딩스보통주	AK홀딩스      [...]
[...]

~~~

- content (한글 파일 다운로드)
~~~python
[in]
mainUrl = 'https://www.alio.go.kr'
fileNo = 129887
addUrl = f'/rulefiledown.dn?fileNo={fileNo}'

r = requests.get(mainUrl+addUrl)

path = Path.home().joinpath('Desktop')

with open(path/'download_file.hwp', 'wb') as f:
    f.write(r.content)
~~~

### **BeautifulSoup**
---
- select()
~~~python
[in]
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/coinfo.naver?'
parm = {'code': '005930'}

r = requests.get(url, params=parm)
html = r.text

soup = BeautifulSoup(html, 'html.parser')
table = soup.select('table.lwidth')[0]  # tag : table / class : lwidth  
table

[out]
<table class="lwidth" summary="외국인한도주식수 정보">
<caption>외국인한도주식수</caption>
<tr>
<th scope="row">외국인한도주식수(A)</th>
<td><em>5,969,782,550</em></td>
[...]
~~~
~~~python
# html format -> pandas dataframe
[in]
pd.read_html(str(table))[0]

[out]
	0                    1
0	외국인한도주식수(A)	5969782550
1	외국인보유주식수(B)	3069826224
2	외국인소진율(B/A)	51.42%
~~~
<br><br><br>



## **System OS**
---
### **sys & os**
---
- 모듈 경로 추가  
PycharmProjects  
|-- 현재 작업폴더  
|&#160;&#160;&#160;&#160;&#160;&#160;&#160;|--현재작업파일.py  
|-- 다른 폴더(모듈)  
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;|--다른파일.py  
~~~python
[in]
import sys
parentPath='c:/Users/user/PycharmProjects' # parent 경로
sys.path.append(parentPath) # 경로 추가

from InPracticeEmploy import normalPayroll # from 다른 폴더(모듈) import 다른 파일
~~~

- directory 존재 여부 확인
~~~python
[in]
import os
path = 'c:/Users/user/PycharmProjects/InPracticeEmploy'
os.path.isdir(path)

[out]
True
~~~

- file 존재 여부 확인
~~~python
[in]
import os
path='c:/Users/user/PycharmProjects/InPracticeEmploy/normalPayroll.py'
os.path.isfile(path)

[out]
True
~~~

- directory 또는 file 존재 여부 확인
~~~python
[in]
import os
dirPath = 'c:/Users/user/PycharmProjects/InPracticeEmploy'
filePath='c:/Users/user/PycharmProjects/InPracticeEmploy/normalPayroll.py'
print(os.path.exists(dirPath))
print(os.path.exists(filePath))

[out]
True
True
~~~

- folder 생성하기
~~~python
[in]
import os
dirPath = Path.home().joinpath('Desktop')/'testFolder'
os.makedirs(dirPath)
~~~

### **pathlib**
---
- 사용자 경로 객체 출력
~~~python
[in]
from pathlib import Path

Path.home()

[out]
WindowsPath('C:/Users/user')
~~~

- 현재작업 폴더 객체 출력
~~~python
[in]
Path.cwd()

[out]
WindowsPath('c:/Users/user/PycharmProjects/PythonGuide')
~~~
~~~python
[in]
# 현재경로 출력
Path('.')

[out]
WindowsPath('.')  # Path.cwd()와 동일한 결과임
~~~

- 절대경로로 변환
~~~python
[in]
path = Path('.')
path.absolute()

[out]
WindowsPath('c:/Users/user/PycharmProjects/PythonGuide')
~~~

- 경로 이어 붙이기
~~~python
[in]
# 바탕화면 경로
path1 = Path.home().joinpath('Desktop', 'README.md')
# 위와 동일한 결과
path2 = Path.home() / 'Desktop' / 'README.md'
print(path1, path2, sep='\n')

[out]
C:\Users\user\Desktop
C:\Users\user\Desktop
~~~

- 부모 경로 출력
~~~python
# 상위 부모 경로 출력
[in]
path = Path.home().joinpath('Desktop', 'README.md')
path.parent

[out]
WindowsPath('C:/Users/user/Desktop')
~~~
~~~python
# 모든 부모 경로를 리스트로 반환
[in]
path = Path.home().joinpath('Desktop', 'README.md')
list(path.parents)

[out]
[WindowsPath('C:/Users/user/Desktop'),
 WindowsPath('C:/Users/user'),
 WindowsPath('C:/Users'),
 WindowsPath('C:/')]
~~~

- 파일 이름, 파일 확장자 출력
~~~python
# 상위 부모 경로 출력
[in]
path = Path.home().joinpath('Desktop', 'README.md')
fileName = path.name # 파일 이름
fileSuffix = path.suffix # 파일 확장자
print(fileName, fileSuffix, sep='\n')

[out]
README.md
.md
~~~

<br><br><br>