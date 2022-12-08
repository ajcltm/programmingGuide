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

- content (zip 파일 다운로드)
  ! zip 파일을 다운로드하여 압출을 풀어놓음(extractall) (아래 예제는 zip파일 안에 파일이 하나인 경우임) 
~~~python
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO

dir = Path.cwd()
z = ZipFile(BytesIO(r.content))
z.extractall(dir)
~~~

