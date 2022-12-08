## **Time**
---
### **time**
---
- localtime
~~~python
[in]
from time import localtime

tm = localtime(1649637016.7605205)

print("year:", tm.tm_year)
print("month:", tm.tm_mon)
print("day:", tm.tm_mday)
print("hour:", tm.tm_hour)
print("minute:", tm.tm_min)
print("second:", tm.tm_sec)

[out]
year: 2019
month: 11
day: 30
hour: 14
minute: 35
second: 26
~~~

- 실행 속도 계산
~~~python
[in]
start = time.time()
time.sleep(5)
end = time.time()

print(f'duration : {end - start} seconds')

[out]
duration : 5.004604816436768 seconds
~~~
- random sleep
~~~python
class RandomSleep:

    def sleep(self):
        range_option = {'quicker': [0, .5], 'slower': [.5, 2], 'stop': [10, 15]}
        sleepLevel = random.choices(['quicker', 'slower', 'stop'], weights=[.6, .39, .01])
        range = range_option.get(sleepLevel[0])
        if sleepLevel[0] == 'stop' : print('Now taking a rest in a seconds')
        time.sleep(random.uniform(range[0], range[1]))
~~~

### **schedule**
---
~~~python
import schedule
import time

def job():
    print("If you can, do it. if you can't, teach it.")

schedule.every(3).seconds.do(job) # 3초마다 job 실행
schedule.every(3).minutes.do(job) # 3분마다 job 실행
schedule.every(3).hours.do(job) # 3시간마다 job 실행
schedule.every(3).days.do(job)  # 3일마다 job 실행
schedule.every(3).weeks.do(job) # 3주마다 job 실행

schedule.every().minute.at(":23").do(job) # 매분 23초에 job 실행
schedule.every().hour.at(":42").do(job) # 매시간 42분에 작업 실행

# 5시간 20분 30초마다 작업 실행
schedule.every(5).hours.at("20:30").do(job)

# 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
schedule.every().day.at("10:30").do(job)
schedule.every().day.at("10:30:42").do(job)

# 주중 특정일에 작업 실행
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
~~~
~~~python
import schedule
import time

def work():
    print("If you can, do it. if you can't, teach it.")

def start_work():
    schedule.every(5).seconds.do(work)

# 매일 9시에 5초 마다 실행
schedule.every().days.at("09:00").do(start_work)

while True:
    schedule.run_pending()
    time.sleep(1)
~~~

### **threding**
---

~~~python
[in]
import time
import threading

def printing():
    print('now threading!')
    threading.Timer(2, printing).start()

printing()

while True:
    time.sleep(1)
    print('another threding...')

[out]
now threading!
another threding...
now threading!
another threding...
another threding...
now threading!
another threding...
another threding...
~~~


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

- 시간 표기법

|코드| 설명| 출력
|---|---|---
|%a|요일 줄임말|Sun, Mon, ... Sat
%A | 요일 | Sunday, Monday, ..., Saturday
%w | 요일을 숫자로 표시, 월요일~일요일, 0~6 | 0, 1, ..., 6
%d | 일 | 01, 02, ..., 31
%b | 월 줄임말 | Jan, Feb, ..., Dec
%B | 월 | January, February, …, December
%m | 숫자 월 | 01, 02, ..., 12
%y | 두 자릿수 연도 | 01, 02, ..., 99
%Y | 네 자릿수 연도 | 0001, 0002, ..., 2017, 2018, 9999
%H | 시간(24시간) | 00, 01, ..., 23
%I | 시간(12시간) | 01, 02, ..., 12
%p | AM, PM | AM, PM
%M | 분 | 00, 01, ..., 59
%S | 초 | 00, 01, ..., 59
%Z | 시간대 | 대한민국 표준시
%j | 1월 1일부터 경과한 일수 | 001, 002, ..., 366
%U | 1년중 주차, 월요일이 한 주의 시작으로 | 00, 01, ..., 53
%W | 1년중 주차, 월요일이 한 주의 시작으로 | 00, 01, ..., 53
%c | 날짜, 요일, 시간을 출력, 현재 시간대 기준 | Sat May 19 11:14:27 2018
%x | 날짜를 출력, 현재 시간대 기준 | 05/19/18
%X | 시간을 출력, 현재 시간대 기준 | '11:44:22'
---
- strptime vs strftime  
(!) strptime is short for "parse time" where strftime is for "formatting time"
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
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)+1]

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
