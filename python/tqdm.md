## **TQDM**
---
- parameter
~~~
- desc: 진행바 앞에 텍스트 출력
- tota: 전체 작업량
- leave: bool, default는 True (진행상태 잔상이 남음)
- ncols: 진행바 컬럼길이
- mininterval, maxinterval: 업데이트 주기, 기본은 mininterval: 0.1sec, maxinterval: 10sec
- ascii: True이면 '#'로 진행바가 표시됨
- initial: 진행 시작 값. 기본값은 0
~~~
- progress bar size
~~~python
lst = range(0,100000)

num = 0
for i in tqdm(lst, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
    num = i
~~~

