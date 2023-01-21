## **문자열**
---
### **따옴표 처리**
---
- 문자열에 문자열 ' 를 넣을 땐 문자열 " 으로 감싼다
~~~python
[in]
food = "Python's favorite food is perl"
print(food)

[out]
"Python's favorite food is perl"
~~~

- 문자열에 문자열 " 를 넣을 땐 문자열 ' 으로 감싼다
~~~python
[in]
say = '"Python is very easy." he says.'
print(say)

[out]
"Python is very easy." he says.
~~~

- 백슬러시 \ 를 사용해서 기호를 인식 시킨다.
~~~python
[in]
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

[out]
"Python's favorite food is perl"
"Python is very easy." he says.
~~~

<br><br><br>


### **줄바꾸기**
---
~~~python
[in]
multiline = "Life is too short\nYou need python"
print(multiline)

[out]
Life is too short
You need python
~~~

~~~python
[in]
multiline_1= '''
            Life is too short
            You need python
            '''
multiline_2= """
            Life is too short
            You need python
            """
print(multiline_1)
print(multiline_2)

[out]
Life is too short
You need python

Life is too short
You need python
~~~

- 이스케이프 코드 : 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용


|코드| 설명|
|---|---|
|\n|문자열 안에서 줄을 바꿀 때 사용|
|\t|문자열 사이에 탭 간격을 줄 때 사용|
| \ \ |문자 \를 그대로 표현할 때 사용|
|\'|작은따옴표(')를 그대로 표현할 때 사용|
|\"|큰따옴표(")를 그대로 표현할 때 사용|
|\r|캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)|
|\f|폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)|
|\a|벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)|
|\b|백 스페이스|
|\000| 널 문자|

<br><br><br>

### **문자열 연산**
---
- 문자열 더하기
~~~python
[in]
head = "Python"
tail = " is fun!"
print(head + tail)


[out]
'Python is fun!'
~~~

- 문자열 곱하기
~~~python
[in]
a = "python"
a * 2

print(a * 2)

[out]
'pythonpython'
~~~

- 문자열 길이 구하기
~~~python
[in]
a = "Life is too short"
print(len(a))

[out]
17
~~~

<br><br><br>

### **문자열 인덱싱**
---
~~~python
[in]
a = "Life is too short, You need Python"
a[3]
a[0]
a[12]
a[-1]
a[-5]
a[0:4]
a[0:3]
a[19:-7]


[out]
'e'  #  a[3]
'L'  #  a[0]
's'  #  a[12]
'n'  #  a[-1]
'y'  #  a[-5]
'Life'  # a[0:4]
'Lif'  # a[0:3]     0 <= a < 3
'You need'  # a[19:-7]
~~~

~~~python
[in]
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
[out]
'20010331'
'Rainy'
~~~

### **문자열 포맷팅**
---
- 숫자 바로 대입
~~~python
[in]
"I eat %d apples." % 3

[out]
'I eat 3 apples.'
~~~

- 문자열 바로 대입
~~~python
[in]
"I eat %s apples." % "five"
[out]
'I eat five apples.'
~~~

- 숫자 값을 나타내는 변수로 대입
~~~python
[in]
number = 3
"I eat %d apples." % number
[out]
'I eat 3 apples.'
~~~

- 2개 이상의 값 넣기
~~~python
[in]
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

[out]
'I ate 10 apples. so I was sick for three days.'
~~~

- %s 포맷 코드
~~~python
[in]
"I have %s apples" % 3
[out]
'I have 3 apples'
~~~
~~~python
[in]
"rate is %s" % 3.234

[out]
'rate is 3.234'
~~~

- 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
~~~python
[in]
"Error is %d%." % 98
[out]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: incomplete format
~~~
~~~python
[in]
"Error is %d%%." % 98

[out]
'Error is 98%.'
~~~


- 정렬과 공백
~~~python
[in]
"%10s" % "hi"
[out]
'        hi'
~~~
~~~python
[in]
"%-10sjane." % 'hi'
[out]
'hi        jane.'
~~~

- 소수점 표현하기
~~~python
[in]
 "%0.4f" % 3.42134234
[out]
'3.4213'
~~~
~~~python
[in]
"%10.4f" % 3.42134234

[out]
'    3.4213'
~~~

- 문자열 포맷 코드

|코드| 설명|
|---|---|
|%s	|문자열(String)|
|%c	|문자 1개(character)|
|%d	|정수(Integer)|
|%f	|부동소수(floating-point)|
|%o	|8진수|
|%x	|16진수|
|%%	|Literal % (문자 % 자체)|


<br><br><br>


### **format 함수를 사용한 포매팅**
---
- 숫자 바로 대입하기
~~~python
[in]
 "I eat {0} apples".format(3)

[out]
'I eat 3 apples'
~~~

- 문자열 바로 대입하기
~~~python
[in]
"I eat {0} apples".format("five")

[out]
'I eat five apples'

- 숫자 값을 가진 변수로 대입하기
~~~

~~~python
[in]
number = 3
"I eat {0} apples".format(number)

[out]
'I eat 3 apples'
~~~

- 2개 이상의 값 넣기
~~~python
[in]
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

[out]
'I ate 10 apples. so I was sick for three days.'
~~~

- 이름으로 넣기
~~~python
[in]
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)


[out]
'I ate 10 apples. so I was sick for 3 days.'
~~~

- 인덱스와 이름을 혼용해서 넣기
~~~python
[in]
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

[out]
'I ate 10 apples. so I was sick for 3 days.'
~~~

- 왼쪽 정렬
~~~python
[in]
"{0:<10}".format("hi")

[out]
'hi        '
~~~

- 오른쪽 정렬
~~~python
[in]
"{0:>10}".format("hi")

[out]
'        hi'
~~~

- 가운데 정렬
~~~python
[in]
"{0:^10}".format("hi")

[out]
'    hi    '
~~~

- 공백 채우기
~~~python
[in]
"{0:=^10}".format("hi")


[out]
'====hi===='
~~~
~~~python
[in]
"{0:!<10}".format("hi")


[out]
'hi!!!!!!!!'
~~~

-소수점 표현하기
~~~python
[in]
y = 3.42134234
"{0:0.4f}".format(y)

[out]
'3.4213'
~~~
~~~python
[in]
"{0:10.4f}".format(y)
[out]
'    3.4213'
~~~

- { 또는 } 문자 표현하기
~~~python
[in]
"{{ and }}".format()
[out]
'{ and }'
~~~

<br><br><br>

### **f 문자열 포매팅**
---
~~~python
[in]
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

[out]
'나의 이름은 홍길동입니다. 나이는 30입니다.
~~~


~~~python
[in]
age = 30
f'나는 내년이면 {age+1}살이 된다.'

[out]
'나는 내년이면 31살이 된다.'
~~~

~~~python
[in]
d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

[out]
'나의 이름은 홍길동입니다. 나이는 30입니다.'
~~~

~~~python
[in]
f'{"hi":<10}'  # 왼쪽 정렬
f'{"hi":>10}'  # 오른쪽 정렬
f'{"hi":^10}'  # 가운데 정렬

[out]
'hi        '
'        hi'
'    hi    '
~~~

~~~python
[in]
f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기

[out]
'====hi===='
'hi!!!!!!!!'
~~~

~~~python
[in]
y = 3.42134234
f'{y:0.4f}'  # 소수점 4자리까지만 표현
f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

[out]
'3.4213'
'    3.4213'
~~~

~~~python
[in]
f'{{ and }}'

[out]
'{ and }'
~~~

### **0으로 시작하는 문자열 만들기**
---
~~~python
[in]
print ("%05d"% 5)
print (format(5000,'05')) 
print ('{0:05d}'.format(273))

[out]
00005
05000
00273
~~~

~~~python
[in]
num = 37
num_str = str(num)

print(num_str.zfill(3))
print(num_str.zfill(5))

num = 12345
num_str = str(num)

print(num_str.zfill(3))
[out]
037
00037
12345
~~~

<br><br><br>


### **문자열 관련 함수들**
---
- 문자 개수 세기(count)
~~~python
[in]
a = "hobby"
a.count('b')

[out]
2
~~~
- 위치 알려주기1(find)
~~~python
[in]
a = "Python is the best choice"
a.find('b')
a.find('k')

[out]
14  # 문자열 중 문자 b가 처음으로 나온 위치를 반환
-1  # 문자나 문자열이 존재하지 않으면 -1을 반환
~~~

- 위치 알려주기2(index)
~~~python
[in]
a = "Life is too short"
a.index('t')

[out]
8   # 맨 처음으로 나온 위치를 반환
~~~

~~~python
[in]
a = "Life is too short"
a.index('k')

[out]
#  존재하지 않는 문자를 찾으면 오류가 발생

File "<stdin>", line 1, in <module>
ValueError: substring not found
~~~

- 문자열 삽입(join)
~~~python
[in]
",".join('abcd')

[out]
'a,b,c,d'
~~~

- 리스트를 하나의 문자열로 반환
~~~python
[in]
str_list = ['This', 'is', 'a', 'python tutorial']
result = ' '.join(s for s in str_list)
print(result)

[out]
This is a python tutorial
~~~


- 소문자를 대문자로 바꾸기(upper)
~~~python
[in]
a = "hi"
a.upper()

[out]
'HI'
~~~

- 대문자를 소문자로 바꾸기(lower)
~~~python
[in]
a = "HI"
a.lower()

[out]
'hi'
~~~

- 왼쪽 공백 지우기(lstrip)
~~~python
[in]
a = " hi "
a.lstrip()

[out]
'hi '
~~~

- 오른쪽 공백 지우기(rstrip)
~~~python
[in]
a= " hi "
a.rstrip()

[out]
' hi'
~~~

- 양쪽 공백 지우기(strip)
~~~python
[in]
a = " hi "
a.strip()

[out]
'hi'
~~~

~~~python
[in]
text = '"okNoProblem"'
print(text)
print(text.strip(' " '))

[out]
"okNoProblem"       # text
okNoProblem         # text.strip(' " ')
~~~

- 문자열 바꾸기(replace)
~~~python
[in]
a = "Life is too short"
a.replace("Life", "Your leg")


[out]
'Your leg is too short'
~~~

- 문자열 나누기(split)
~~~python
[in]
a = "Life is too short"
a.split()

[out]
['Life', 'is', 'too', 'short']
~~~
~~~python
[in]
b = "a:b:c:d"
b.split(':')

[out]
['a', 'b', 'c', 'd']
~~~

<br><br><br>


## **List**
---
### **List slicing**
---
~~~python
lst = ['show', 'how', 'to', 'index', 'into', 'sequences']
~~~

~~~python
[in]
s[1:4]

[out]
['how', 'to', 'index']
~~~
~~~python
# step example 1
[in]
s[1:4:2]

[out]
['how', 'index']
~~~
~~~python
# step example 2
[in]
s[::2]

[out]
['show', 'to', 'into']
~~~
~~~python
# step을 이용한 reverse 1
[in]
s[::-1]

[out]
['sequences', 'into', 'index', 'to', 'how', 'show']
~~~
~~~python
# step을 이용한 reverse 2
[in]
lst[::-2]

[out]
['sequences', 'index', 'how']
~~~
~~~python
[in]
s[1:-1]

[out]
['how', 'to', 'index', 'into']
~~~
~~~python
[in]
s[3:]


[out]
['index', 'into', 'sequences']
~~~
~~~python
[in]
s[:3]

[out]
['show', 'how', 'to']
~~~
~~~python
[in]
s[:3] + s[3:] == s

[out]
True
~~~
~~~python
[in]
full_slice = s[:]
full_slice
[out]
['show', 'how', 'to', 'index', 'into', 'sequences']
~~~
~~~python
# 슬라이스를 통해 새롭게 만든 변수와 값은 같지만, 같은 변수는 아님
[in]
full_slice == s
full_slice is s
 
[out]
True
False
~~~

### **List 연산**
---
~~~python
# List 더하기
[in]
a = [1, 2, 3]
b = [4, 5, 6]
a + b

[out]
[1, 2, 3, 4, 5, 6]
~~~
~~~python
# List 곱하기
[in]
a = [1, 2, 3]
a * 3

[out]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
~~~

### **List 수정과 삭제**
---
- List 수정하기
~~~python
# 수정
[in]
a = [1, 2, 3]
a[2] = 4
a

[out]
[1, 2, 4]
~~~
- List 삭제하기
~~~python
# 인덱스로 삭제하기
[in]
a = [1, 2, 3]
del a[1]
a

[out]
[1, 3]
~~~
~~~python
# 슬라이싱 기법을 사용하여 리스트의 요소 여러 개를 한꺼번에 삭제
[in]
a = [1, 2, 3, 4, 5]
del a[2:]
a

[out]
[1, 2]
~~~
~~~python
# remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수임
[in]
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a

[out]
[1, 2, 1, 2, 3]
~~~
~~~python
# remove(3)을 한 번 더 실행하면 다시 3이 삭제됨
[in]
a = [1, 2, 1, 2, 3]
a.remove(3)
a

[out]
[1, 2, 1, 2]
~~~
~~~python
# remove하는 값이 존재하지 않으면 ValueError 발생함
[in]
a = [1, 2, 1, 2]
a.remove(3)

[out]
Exception has occurred: ValueError
list.remove(x): x not in list
~~~
~~~python
# pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제함
[in]
a = [1,2,3]
a.pop()

[out]
3

[in]
a

[out]
[1, 2]
~~~
~~~python
# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제함
[in]
a = [1,2,3]
a.pop(1)

[out]
2

[in]
a

[out]
[1, 3]
~~~

### **List 관련 함수들**
---
- list.append()
~~~python
[in]
a = [1, 2, 3]
a.append(4)
a

[out]
[1, 2, 3, 4]
~~~
~~~python
# 리스트 안에 리스트를 append하면 nested되니 주의
[in]
a.append([5,6])
a

[out]
[1, 2, 3, 4, [5, 6]]
~~~

- list.extend()
~~~python
[in]
a = [1,2,3]
a.extend([4,5])
a

[out]
[1, 2, 3, 4, 5]  # a.extend([4, 5])는 a += [4, 5]와 동일
~~~

- list.sort()
~~~python
[in]
a = [1, 4, 3, 2]
a.sort()
a

[out]
[1, 2, 3, 4]
~~~
~~~python
[in]
a = ['a', 'c', 'b']
a.sort()
a

[out]
['a', 'b', 'c']
~~~

- list.reverse()
~~~python
[in]
a = ['a', 'c', 'b']
a.reverse()
a

[out]
['b', 'c', 'a']
~~~

- list.index()
~~~python
[in]
a = [1,2,3]
a.index(3)
a.index(1)

[out]
2
0
~~~

- list.insert()
~~~python
[in]
a = [1, 2, 3]
a.insert(0, 4)
a

[out]
[4, 1, 2, 3]
~~~

- list.count()
~~~python
[in]
a = [1,2,3,1]
a.count(1)

[out]
2
~~~

### **List 랜덤 추출**
---
- random.choice(lst)   
  ! 한가지 요소만 랜덤 추출
  
~~~python
[in]
import random 
lst = [1, 2, 3]
choiceLst = random.choice(lst)

[out]
1
~~~

- random.sample(lst, n)   
  ! n개의 요소를 리스트로 랜덤 추출(중복 허용하지 않음)
  
~~~python
[in]
import random 
lst = [1, 2, 3]
sampleLst = random.sample(lst, 2)

[out]
[2, 3]
~~~

- 중복 허용하면서 랜덤 추출 하는 방법
~~~python
[in]
li = [1, 2, 3]
choiceLst = [random.choice(li) for i in range(5)]

[out]
[1, 3, 2, 3, 3]
~~~
<br><br><br>



## **Dictionary**
---
### **dictionary 기본**
---
- dictionary 생성
~~~python
[in] 
dic = dict(a=1, b=2, c=3)
print(dic)

[out]
{'a'=1, 'b'=2, c='3'}
~~~
~~~python
[in]
dic = {f'key_{i}' : i for i in range(0,4)}
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
~~~python
# 위의 예제와 동일한 결과
[in]
symbols = ['AAPL', 'NVDA', 'AMZN']
values = {'unitPrice': 0, 'amounts': 0}

dic = dict.fromkeys(symbols, values)
print(dic)

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

~~~python
# key값이 string인 경우만 작동함
[in]
dic1 = {'1':10, '2':20}
dic2 = {'1':100, '3':300}

dict(dic1, **dic2)

[out]
{'1': 100, '2': 20, '3': 300}
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

## **pickle**
---
- save pickle
---
~~~python
import pickle
my_list = ['a','b','c']

with open("data.pickle","wb") as fw:
    pickle.dump(my_list, fw)
~~~
- load pickle
~~~python
with open("data.pickle","rb") as fr:
    data = pickle.load(fr)
print(data)
~~~
<br><br><br>

## **Json**
---
- json to python object
~~~python
import json

json_string = '''{
    "id": 1,
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874"
    },
    "admin": false,
    "hobbies": null
}'''

json_object = json.loads(json_string)
~~~

- python object to json
~~~python
import json

json_object = {
    "id": 1,
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874"
    },
    "admin": False,
    "hobbies": None
}

json_string = json.dumps(json_object, indent=2)
~~~

- json file load
~~~python
import json

with open('input.json') as f:
    json_object = json.load(f)
~~~

- json file save
~~~python
import json

json_object = {
    "id": 1,
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874"
    },
    "admin": False,
    "hobbies": None
}

with open('output.json', 'w') as f:
    json.dump(json_object, f, indent=2)
~~~
<br><br>

## **&#42;args & 	&#42;&#42;kwargs**
---
- &#42;args
~~~python
[in]
def test_var_args(f_arg, *argv):
    print ("첫 번째 인자:", f_arg)
    for arg in argv:
        print ("*argv의 다른 인자", arg)

tast_var_args('야숩', 'python', '달걀', 'test')

[out]
첫번째 인자: 야숩
*argv의 다른 인자: python
*argv의 다른 인자: 달걀
*argv의 다른 인자: test
~~~

- &#42;&#42;kwargs
~~~python
[in]
def greet_me(**kwargs):
  if kwargs is not None:
    for key, value in kwargs.items(): 
      print("%s == %s" % (key, value)) 

greet_me(name="yasoob")


[out]
name == yasoob
~~~

## **Built-in Fuctions**
---

- zip
~~~python
[in]
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

[out]
(1, 'A')
(2, 'B')
(3, 'C')
~~~

- map 
~~~python
# map(변환 함수, 순회 가능한 데이터)
[in]
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

[out]
[1, 2, 3, 4]
~~~
