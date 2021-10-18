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


- datetime에 3개월 더하는 방법 (timedelta는 시간, 일, 주 단위 연산만 가능)
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
