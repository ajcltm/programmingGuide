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

## **Functool**
---
### **Ruduce**
---
- reduce(집계 함수, 순회 가능한 데이터[, 초기값])
~~~python
# Example 1
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
{'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
{'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
{'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
{'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]
~~~
~~~python
[in]
from functools import reduce
reduce(lambda acc, cur: acc + cur["age"], users, 0)

[out]
227
---------------------------------------------------
[in]
reduce(lambda acc, cur: acc + [cur["mail"]], users, [])

[out]
['gregorythomas@gmail.com', 'hintoncynthia@hotmail.com', 'wwagner@gmail.com', 'daniel79@gmail.com', 'ujackson@gmail.com']

---------------------------------------------------
[in]
def names_by_sex(acc, cur):
     sex = cur["sex"]
     if sex not in acc:
         acc[sex] = []
     acc[sex].append(cur["name"])
     return acc

reduce(names_by_sex, users, {})

[out]
{'M': ['Brett Holland', 'Michael Jenkins'], 'F': ['Madison Martinez', 'Karen Rodriguez', 'Amber Rhodes']}
~~~

~~~python
# Example 2
array = ["F", "D", "A", "C", "F", "B", "C", "E", "D", "C", "F", "A", "B", "E"]

[in]
result = reduce(lambda acc, cur: acc if cur in acc else acc+[cur], array, [])

[out]
['F', 'D', 'A', 'C', 'B', 'E']
~~~

### **Partial**
---
- partial
~~~python
def power(base, exponent):
    return base ** exponent

[in]
from functools import partial

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

def test_partials():
    assert square(2) == 4
    assert cube(2) == 8
~~~

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



## **Pandas**
---
### **Object creation**
---
- pd.Series()
~~~python
[in]
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

[out]
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
~~~
- pd.DataFrame()
~~~python
[in]
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

[out]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

df2

[out]
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
~~~

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

- df.dtypes
~~~python
# df2

     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
---------------------------------------------------------------
[in]
df2.dtypes

[out]
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
~~~

- df.describe()
~~~python 
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
---------------------------------------------------------------
[in]
df.describe()

[out]

              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
~~~

### **Viewing data**
---
- Viewing the top and bottom rows of the frame
~~~python
[in]
df.head()

[Out] 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
~~~
~~~python
[in]
df.tail(3)

[Out]
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~

- Display the index, columns
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
df.index

[Out] 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
~~~
~~~python
[in]
df.columns

[Out]
Index(['A', 'B', 'C', 'D'], dtype='object')
~~~

- Transposing data
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
---------------------------------------------------------------
[in]
df.T

[Out]
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
~~~

- Sorting data
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Sorting by an axis
[in]
df.sort_index(axis=1, ascending=False)

[Out]
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
~~~
~~~python
# Sorting by values
[in]
df.sort_values(by="B")

[Out]
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
~~~

### **Data Selection**
---
- Getting
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Selecting a single column, which yields a Series, equivalent to df.A
[in]
df["A"]

[out]
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.67369
~~~

~~~python
# Selecting via [], which slices the rows:
[in]
df[0:3]

[out]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
~~~

~~~python
[in]
df["20130102":"20130104"]

[out]
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
~~~

- Selection by label
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# For getting a cross section using a label
[in]
df.loc[dates[0]]

[out]
A    0.469112
B   -0.282863
C   -1.509059
D   -1.135632
Name: 2013-01-01 00:00:00, dtype: float64
~~~
~~~python
# Selecting on a multi-axis by label
[in]
df.loc[:, ["A", "B"]]

[out] 
                   A         B
2013-01-01  0.469112 -0.282863
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
2013-01-06 -0.673690  0.113648
~~~

~~~python
# Showing label slicing, both endpoints are included
[in]
df.loc["20130102":"20130104", ["A", "B"]]

[out] 
                   A         B
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
~~~

~~~python
# Reduction in the dimensions of the returned object
[in]
df.loc["20130102", ["A", "B"]

[out] 
A    1.212112
B   -0.173215
Name: 2013-01-02 00:00:00, dtype: float64
~~~

~~~python
# For getting a scalar value
[in]
df.loc[dates[0], "A"]

[out] 
0.4691122999071863
~~~

~~~python
# For getting fast access to a scalar (equivalent to the prior method)
[in]
df.at[dates[0], "A"]

[out] 
0.4691122999071863
~~~

- Selection by position
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# By integer slices, acting similar to NumPy/Python
[in]
df.iloc[3:5, 0:2]

[out] 
                   A         B
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
~~~
~~~python
# By lists of integer position locations, similar to the NumPy/Python style
[in]
df.iloc[[1, 2, 4], [0, 2]]

[out] 
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
~~~

~~~python
# For getting a value explicitly
[in]
df.iloc[1, 1]

[out] 
-0.17321464905330858
~~~

~~~python
# For getting fast access to a scalar (equivalent to the prior method)
[in]
df.iat[1, 1]

[out] 
-0.17321464905330858
~~~

- loc와 iloc의 차이
~~~python
# df
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

- Boolean indexing
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Using a single column’s values to select data
[in]
df[df["A"] > 0]

[out]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
~~~
~~~python
# Selecting values from a DataFrame where a boolean condition is met
[in]
df[df > 0]

[out]
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
~~~
~~~python
# Using the isin() method for filtering
[in]
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2

[out]
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three
---------------------------------------------------------------
[in]
df2[df2["E"].isin(["two", "four"])]

[out]
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
~~~

- Setting
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1

[out]
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
~~~
~~~python
[in]
df["F"] = s1  # Setting a new column automatically aligns the data by the indexes
df.at[dates[0], "A"] = 0  # Setting values by label
df.iat[0, 1] = 0  # Setting values by position
df.loc[:, "D"] = np.array([5] * len(df))  # Setting by assigning with a NumPy array
df

[out]
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059  5  NaN
2013-01-02  1.212112 -0.173215  0.119209  5  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0
2013-01-05 -0.424972  0.567020  0.276232  5  4.0
2013-01-06 -0.673690  0.113648 -1.478427  5  5.0
~~~
~~~python
# A where operation with setting
[in]
df2 = df.copy()
df2[df2 > 0] = -df2
df2

[out]
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059 -5  NaN
2013-01-02 -1.212112 -0.173215 -0.119209 -5 -1.0
2013-01-03 -0.861849 -2.104569 -0.494929 -5 -2.0
2013-01-04 -0.721555 -0.706771 -1.039575 -5 -3.0
2013-01-05 -0.424972 -0.567020 -0.276232 -5 -4.0
2013-01-06 -0.673690 -0.113648 -1.478427 -5 -5.0
~~~

### **MultiIndex**
---
~~~python
                     A         B         C
first second                              
bar   one     0.895717  0.410835 -1.413681
      two     0.805244  0.813850  1.607920
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
      two    -0.226169 -1.436737 -2.006747
~~~
~~~python
[in]
df.loc[("bar", "two")]

[out] 
A    0.805244
B    0.813850
C    1.607920
Name: (bar, two), dtype: float64
~~~
~~~python
[in]
df.loc[("bar", "two"), "A"]

[out] 
0.8052440253863785
~~~
~~~python
[in]
df.loc["bar"]

[out]
               A         B         C
second                              
one     0.895717  0.410835 -1.413681
two     0.805244  0.813850  1.607920
~~~
~~~python
[in]
df.loc["baz":"foo"]

[out]
                     A         B         C
first second                              
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
~~~
~~~python
[in]
df.loc[("baz", "two"):("qux", "one")] 

[out]
                     A         B         C
first second                              
baz   two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
~~~
~~~python
[in]
df.loc[("baz", "two"):"foo"]

[out]
                     A         B         C
first second                              
baz   two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
~~~
~~~python
[in]
df.loc[[("bar", "two"), ("qux", "one")]]

[out]
                     A         B         C
first second                              
bar   two     0.805244  0.813850  1.607920
qux   one    -1.170299  1.130127  0.974466
~~~

~~~python
# another example : there is a seies...
A  c    1   
   d    2   
   e    3   
B  c    4   
   d    5   
   e    6  

[in]
s.loc[[("A", "c"), ("B", "d")]]  # list of tuples

[out]
A  c    1
B  d    5
dtype: int64

[in]
s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists

[out]
A  c    1
   d    2
B  c    4
   d    5
dtype: int64
~~~

~~~python
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C0 D0    1    0    3    2
         D1    5    4    7    6
      C1 D0    9    8   11   10
         D1   13   12   15   14
      C2 D0   17   16   19   18
...          ...  ...  ...  ...
A3 B1 C1 D1  237  236  239  238
      C2 D0  241  240  243  242
         D1  245  244  247  246
      C3 D0  249  248  251  250
         D1  253  252  255  254
~~~
~~~python

[in]
dfmi.loc[(slice("A1", "A3"), slice(None), ["C1", "C3"]), :]

[out]
lvl0           a         b     
lvl1         bar  foo  bah  foo
A1 B0 C1 D0   73   72   75   74
         D1   77   76   79   78
      C3 D0   89   88   91   90
         D1   93   92   95   94
   B1 C1 D0  105  104  107  106
...          ...  ...  ...  ...
A3 B0 C3 D1  221  220  223  222
   B1 C1 D0  233  232  235  234
         D1  237  236  239  238
      C3 D0  249  248  251  250
         D1  253  252  255  254

[24 rows x 4 columns]

[in]
idx = pd.IndexSlice

dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]

[out]
lvl0           a    b
lvl1         foo  foo
A0 B0 C1 D0    8   10
         D1   12   14
      C3 D0   24   26
         D1   28   30
   B1 C1 D0   40   42
...          ...  ...
A3 B0 C3 D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

[in]
dfmi.loc["A1", (slice(None), "foo")]

[out]
lvl0        a    b
lvl1      foo  foo
B0 C0 D0   64   66
      D1   68   70
   C1 D0   72   74
      D1   76   78
   C2 D0   80   82
...       ...  ...
B1 C1 D1  108  110
   C2 D0  112  114
      D1  116  118
   C3 D0  120  122
      D1  124  126

[16 rows x 2 columns]

[in]
dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]

[out]
lvl0           a    b
lvl1         foo  foo
A0 B0 C1 D0    8   10
         D1   12   14
      C3 D0   24   26
         D1   28   30
   B1 C1 D0   40   42
...          ...  ...
A3 B0 C3 D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

[in]
mask = dfmi[("a", "foo")] > 200
dfmi.loc[idx[mask, :, ["C1", "C3"]], idx[:, "foo"]]

[out]
lvl0           a    b
lvl1         foo  foo
A3 B0 C1 D1  204  206
      C3 D0  216  218
         D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

[in]
dfmi.loc(axis=0)[:, :, ["C1", "C3"]]

[out]
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C1 D0    9    8   11   10
         D1   13   12   15   14
      C3 D0   25   24   27   26
         D1   29   28   31   30
   B1 C1 D0   41   40   43   42
...          ...  ...  ...  ...
A3 B0 C3 D1  221  220  223  222
   B1 C1 D0  233  232  235  234
         D1  237  236  239  238
      C3 D0  249  248  251  250
         D1  253  252  255  254
~~~


### **타입 변경**
---
- df.to_numpy()
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
df.to_numpy()

[out]
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
~~~

- to dictionary
~~~python
# df
   col1  col2
0     1     1
1     5     2
2     7     3
3     6     6
4     3     9
~~~
~~~python
[in]
df.to_dict()

[out]
{'col1': {0: 1, 1: 5, 2: 7, 3: 6, 4: 3}, 'col2': {0: 1, 1: 2, 2: 3, 3: 6, 4: 9}}
~~~
~~~python
[in]
df.to_dict(orient="list")

[out]
{'col1': [1, 5, 7, 6, 3], 'col2': [1, 2, 3, 6, 9]}
~~~

~~~python
[in]
df.to_dict(orient='series')

[out]
{'col1': 0    1
1    5
2    7
3    6
4    3
Name: col1, dtype: int64, 'col2': 0    1
1    2
2    3
3    6
4    9
Name: col2, dtype: int64}
~~~

~~~python
[in]
df.to_dict(orient="split")

[out]
{'index': [0, 1, 2, 3, 4], 'columns': ['col1', 'col2'], 'data': [[1, 1], [5, 2], [7, 3], [6, 6], [3, 9]]}
~~~

~~~python
[in]
df.to_dict(orient="index")

[out]
{0: {'col1': 1, 'col2': 1}, 1: {'col1': 5, 'col2': 2}, 2: {'col1': 7, 'col2': 3}, 3: {'col1': 6, 'col2': 6}, 4: {'col1': 3, 'col2': 9}}
~~~

~~~python
[in]
df.to_dict(orient="records")

[out]
[{'col1': 1, 'col2': 1}, {'col1': 5, 'col2': 2}, {'col1': 7, 'col2': 3}, {'col1': 6, 'col2': 6}, {'col1': 3, 'col2': 9}]
~~~

### **column, row, index 변경, 추가, 삭제**
---
- df.set_index()
~~~python
# df
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
---------------------------------
[in]
df = df.set_index('A')
print(df)

[out]
   B  C
A      
1  2  3
4  5  6
7  8  9
~~~
- df.columns or df.rename
~~~python

[in]
# 전체 열 이름 입력하기
df.columns = ['name1', 'name2', 'name3']

# 선택하여 열 이름 변경하기
df.rename(columns={'Beforename':'Aftername'}, inplace=True)
~~~
- df.append()
~~~python
# df
    48  49  50
0   1   2   3
1   4   5   6
2   7   8   9

# a 
   48  49  50
0   1   2   3
---------------------------
[in]
df = df.append(a)
df = df.reset_index(drop=True)

[out]
   48  49  50
0   1   2   3
1   4   5   6
2   7   8   9
3   1   2   3
~~~
- df.drop()
~~~python
# df
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9

[in]
df.drop('A', axis=1, inplace=True)
print(df)

[out]
   B  C
0  2  3
1  5  6
2  8  9
---------------------------
[in]
print(df.drop(df.index[1]))

[out]
   A  B  C
0  1  2  3
2  7  8  9
---------------------------
[in]
print(df.drop(0))

[out]
   A  B  C
1  4  5  6
2  7  8  9
~~~

### **데이터 수정하기**
---
- selecting 후 수정
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
-------------------------
# df가 원본이면 아래와 같이 작동함
[in]
df.loc[0, 'col1'] = 100

[out]
   col1  col2 col3
0   100     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
-------------------------
# df를 selectig하면 얕은 복사가된 사본이 되어 원본데이터는 바뀌어 있지 않음
[in]
con = df.loc[:, 'col1']==1
df.loc[con][0] = 100

print(df)

[out]
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
-------------------------
# df를 index로 직접 selectig하면 원본데이터가 변경됨
[in]
con = df.loc[:, 'col1']==1
df.loc[df.loc[con].index, 'col1'] = 100

print(df)

[out]
   col1  col2 col3
0   100     1    a
1   100     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
- df.replace or series.replace로 데이터 수정
~~~python
# df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e

[in]
df.replace(0, 5)

[out]
    A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
--------------------------
# List-like `to_replace`
[in]
df.replace([0, 1, 2, 3], 4)

[out]
    A  B  C
0  4  5  a
1  4  6  b
2  4  7  c
3  4  8  d
4  4  9  e
--------------------------
# List-like `to_replace`
[in]
df.replace([0, 1, 2, 3], [4, 3, 2, 1])

[out]
    A  B  C
0  4  5  a
1  3  6  b
2  2  7  c
3  1  8  d
4  4  9  e
--------------------------
# dict-like `to_replace`
[in]
df.replace({0: 10, 1: 100})

[out]
    A  B  C
0   10  5  a
1  100  6  b
2    2  7  c
3    3  8  d
4    4  9  e
--------------------------
# dict-like `to_replace`
[in]
df.replace({'A': 0, 'B': 5}, 100)

[out]
    A    B  C
0  100  100  a
1    1    6  b
2    2    7  c
3    3    8  d
4    4    9  e
--------------------------
# dict-like `to_replace`
[in]
df.replace({'A': {0: 100, 4: 400}})

[out]
    A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e
~~~
~~~python
# df
      A    B
0   bat  abc
1   foo  bar
2  bait  xyz
--------------------------
# Regular expression `to_replace`
[in]
df.replace(to_replace=r'^ba.$', value='new', regex=True)

[out]
        A    B
0   new  abc
1   foo  new
2  bait  xyz
--------------------------
[in]
df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)

[out]
        A    B
0   new  abc
1   foo  bar
2  bait  xyz
~~~

- where 또는 mask함수로 수정
~~~python
s = pd.Series(range(5))
--------------------------
[in]
s.where(s > 0)

[out]
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64
--------------------------
[in]
s.mask(s > 0)

[out]
0    0.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64
--------------------------
[in]
s.where(s > 1, 10)

[out]
0    10
1    10
2    2
3    3
4    4
dtype: int64
--------------------------
[in]
s.mask(s > 1, 10)

[out]
0     0
1     1
2    10
3    10
4    10
dtype: int64
~~~

~~~python
   A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9
--------------------------
[in]
m = df % 3 == 0
df.where(m, -df)

[out]
   A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9
~~~

### **Missing data 처리**
---
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data
[in]
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
df1
[out]
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN
~~~
~~~python
# To drop any rows that have missing data
[in]
df1.dropna(how="any")
[out]
                   A         B         C  D    F    E
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
~~~
~~~python
# Filling missing data
[in]
df1.fillna(value=5)
[out]
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  5.0  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  5.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  5.0
~~~
~~~python
# To get the boolean mask where values are nan
[in]
pd.isna(df1)
[out]
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
~~~

### **중복값 또는 고유값 처리**
---
- series.unique()
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
[in]
unique = df.col1.unique()
print(unique)
print(type(unique))

[out]
[1 2 3]
<class 'numpy.ndarray'>
~~~

- df.duplicated() ; row 기준으로 중복 검사하여 bool 값이 있는 series로 반환함
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
# row 전체가 같을 경우 뒤에 나오는 row를 중복된 row로 인식
[in]
print(df.duplicated())

[out]
0    False
1     True
2    False
3    False
4    False
dtype: bool
~~~

~~~python
# subset을 인자로 넣을 경우 해당 컬럼들만을 기준으로 중복 검사함
[in]
print(df.duplicated(['col1']))

[out]
0    False
1     True
2    False
3     True
4    False
dtype: bool
~~~

~~~python
# keep='last'로 하면 중복된 마지막 row을 살리고, 앞에 있는 row들을 중복으로 인식
[in]
print(df.duplicated(['col1'], keep='last'))

[out]
0     True
1    False
2     True
3    False
4    False
dtype: bool
~~~

- df.drop_duplicates() ; 중복된 row를 제거
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
# row 전체가 동일한 값을 갖는 뒤에 나오는 row들을 제거
[in]
print(df.drop_duplicates())

[out]
   col1  col2 col3
0     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
# subset을 인자로 넣을 경우 해당 컬럼들만을 기준으로 중복 제거함
[in]
print(df.drop_duplicates(['col1']))

[out]
   col1  col2 col3
0     1     1    a
2     2     2    b
4     3     7    d
~~~
~~~python
# keep='last'로 하면 중복된 마지막 row을 살리고, 앞에 있는 row들을 중복 제거
[in]
print(df.drop_duplicates(['col1'], keep='last'))

[out]
   col1  col2 col3
1     1     1    a
3     2     4    c
4     3     7    d
~~~


### **데이터 타입 변경** 
---
- to_numeric()  
 : DataFrame 이나 Series 내 문자열 칼럼을 숫자형으로 변환  
 ! 수치형으로 변환이 불가능한 값이 있을 경우, 인자 옵션은 errors = 'raise'(에러메시지 띄움), 'coerce'(nan 반환), 'ignore'(무시하고 원래값 반환)
 ~~~python
# df
   col_1  col_2
0      1    4.0
1      2    bbb
2      3    6.0
~~~
~~~python
[in]
df = df.apply(pd.to_numeric, errors = 'coerce')
print(df)

[out]
   col_1  col_2
0      1    4.0
1      2    NaN
2      3    6.0
~~~

- nan 값을 None 값으로 변환   
 ! Pandas DataFrame에 None 데이터를 넣으면 NaN 객체로 자동 변환이 된다. None은 다른 프로그래밍 언어에서의 NULL이다. NaN은 Not a Number의 약자로 정의되거나, 표현되지 않는 부동소수점 값으로 Python에서는 float 타입이 된다.  math 모듈에서는 isnan(), pandas 모듈에서는 isnull() 함수로 nan인지 확인하는 함수를 제공한다.
~~~python
df = df.where(pd.notnull(df), None)
~~~

### **Operations**
---
- Stats
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Performing a descriptive statistic
[in]
df.mean()

[out]
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
~~~
~~~python
# Same operation on the other axis
[in]
df.mean(1)

[out]
2013-01-01    0.872735
2013-01-02    1.431621
2013-01-03    0.707731
2013-01-04    1.395042
2013-01-05    1.883656
2013-01-06    1.592306
Freq: D, dtype: float64
~~~
- df.sub()
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Same operation on the other axis
[in]
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
[out]
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64
~~~
~~~python
# Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension
[in]
df.sub(s, axis="index")

[out]
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN
~~~

- Histogramming
~~~python
[in]
s = pd.Series(np.random.randint(0, 7, size=10))
s

[out]
0    4
1    2
2    1
3    2
4    6
5    4
6    4
7    6
8    4
9    4
dtype: int64
~~~
~~~python
[in]
s.value_counts()

[out]
4    5
2    2
6    2
1    1
dtype: int64
~~~

### **Merge**
---
- concat
~~~python
[in]
df = pd.DataFrame(np.random.randn(10, 4))
df

[out]
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
~~~
~~~python
[in]
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

[out]
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
~~~

- join  
pd.merge(
    left,
    right,
    how="inner",
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=True,
    suffixes=("_x", "_y"),
    copy=True,
    indicator=False,
    validate=None,
)

|Merge method| SQL Join Name| Description|
|---|---|---|
|left|LEFT OUTER JOIN|Use keys from left frame only|
|right|RIGHT OUTER JOIN|Use keys from right frame only|
|outer|FULL OUTER JOIN|Use union of keys from both frames|
|inner|INNER JOIN|Use intersection of keys from both frames|
|cross|CROSS JOIN|Create the cartesian product of rows of both frames|


~~~python
# left
   key  lval
0  foo     1
1  foo     2

# right
   key  rval
0  foo     4
1  foo     5
---------------------------------------------------------------
[in]
pd.merge(left, right, on="key")

[out]
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
~~~

~~~python
[in]
# left
   key  lval
0  foo     1
1  bar     2

# right
   key  rval
0  foo     4
1  bar     5
---------------------------------------------------------------
[in]
pd.merge(left, right, on="key")

[out]
   key  lval  rval
0  foo     1     4
1  bar     2     5
~~~

~~~python
# left
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3

# right
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, on="key")

[out]
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, on=["key1", "key2"])

[out]
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="left", on=["key1", "key2"])

[out]
  key1 key2   A   B    C    D
0   K0   K0  A0  B0   C0   D0
1   K0   K1  A1  B1  NaN  NaN
2   K1   K0  A2  B2   C1   D1
3   K1   K0  A2  B2   C2   D2
4   K2   K1  A3  B3  NaN  NaN
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="right", on=["key1", "key2"])

[out]
  key1 key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K1   K0   A2   B2  C1  D1
2   K1   K0   A2   B2  C2  D2
3   K2   K0  NaN  NaN  C3  D3
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="outer", on=["key1", "key2"])

[out]
  key1 key2    A    B    C    D
0   K0   K0   A0   B0   C0   D0
1   K0   K1   A1   B1  NaN  NaN
2   K1   K0   A2   B2   C1   D1
3   K1   K0   A2   B2   C2   D2
4   K2   K1   A3   B3  NaN  NaN
5   K2   K0  NaN  NaN   C3   D3
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="inner", on=["key1", "key2"])

[out]
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="cross")

[out]
   key1_x key2_x   A   B key1_y key2_y   C   D
0      K0     K0  A0  B0     K0     K0  C0  D0
1      K0     K0  A0  B0     K1     K0  C1  D1
2      K0     K0  A0  B0     K1     K0  C2  D2
3      K0     K0  A0  B0     K2     K0  C3  D3
4      K0     K1  A1  B1     K0     K0  C0  D0
5      K0     K1  A1  B1     K1     K0  C1  D1
6      K0     K1  A1  B1     K1     K0  C2  D2
7      K0     K1  A1  B1     K2     K0  C3  D3
8      K1     K0  A2  B2     K0     K0  C0  D0
9      K1     K0  A2  B2     K1     K0  C1  D1
10     K1     K0  A2  B2     K1     K0  C2  D2
11     K1     K0  A2  B2     K2     K0  C3  D3
12     K2     K1  A3  B3     K0     K0  C0  D0
13     K2     K1  A3  B3     K1     K0  C1  D1
14     K2     K1  A3  B3     K1     K0  C2  D2
15     K2     K1  A3  B3     K2     K0  C3  D3
~~~
### **apply**
---
~~~python
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df
   A  B
0  4  9
1  4  9
2  4  9
~~~
~~~python
[in]
df.apply(np.sqrt)

[out]
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0
~~~
~~~python
[in]
df.apply(np.sum, axis=0)

[out]
A    12
B    27
dtype: int64
~~~
~~~python
[in]
df.apply(np.sum, axis=1)

[out]
0    13
1    13
2    13
dtype: int64
~~~
~~~python
[in]
df.apply(lambda x: [1, 2], axis=1)

[out]
0    [1, 2]
1    [1, 2]
2    [1, 2]
dtype: object
~~~
~~~python
[in]
df.apply(lambda x: [1, 2], axis=1, result_type='expand')

[out]
   0  1
0  1  2
1  1  2
2  1  2
~~~
~~~python
[in]
df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)

[out]
   foo  bar
0    1    2
1    1    2
2    1    2
~~~
~~~python
[in]
df.apply(lambda x: [1, 2], axis=1, result_type='broadcast')

[out]
   A  B
0  1  2
1  1  2
2  1  2
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
### **Reshaping**
- Melt
~~~python
# cheese
  first last  height  weight
0  John  Doe     5.5     130
1  Mary   Bo     6.0     15
~~~
~~~python
[in]
cheese.melt(id_vars=["first", "last"])

[out]
  first last variable  value
0  John  Doe   height    5.5
1  Mary   Bo   height    6.0
2  John  Doe   weight  130.0
3  Mary   Bo   weight  150.0
-------------------------------------------
[in]
cheese.melt(id_vars=["first", "last"], var_name="quantity")

[out]
  first last quantity  value
0  John  Doe   height    5.5
1  Mary   Bo   height    6.0
2  John  Doe   weight  130.0
3  Mary   Bo   weight  150.0
~~~

- Stack
~~~python
[in]
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2

[out]
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
~~~
~~~python
[in]
stacked = df2.stack()
stacked

[out]
first  second   
bar    one     A   -0.727965
               B   -0.589346
       two     A    0.339969
               B   -0.693205
baz    one     A   -0.339355
               B    0.593616
       two     A    0.884345
               B    1.591431
dtype: float64
~~~
- unstack
~~~python
[in]
stacked.unstack()

[out]
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
~~~
~~~python
[in]
stacked.unstack(1)

[out]
second        one       two
first                      
bar   A -0.727965  0.339969
      B -0.589346 -0.693205
baz   A -0.339355  0.884345
      B  0.593616  1.591431
~~~
~~~python
[in]
stacked.unstack(0)

[out]
first          bar       baz
second                      
one    A -0.727965 -0.339355
       B -0.589346  0.593616
two    A  0.339969  0.884345
       B -0.693205  1.591431
~~~

### **Pivot Tables**
---

- df.pivot()
~~~python
# df
         date variable     value
0  2000-01-03        A  0.469112
1  2000-01-04        A -0.282863
2  2000-01-05        A -1.509059
3  2000-01-03        B -1.135632
4  2000-01-04        B  1.212112
5  2000-01-05        B -0.173215
6  2000-01-03        C  0.119209
7  2000-01-04        C -1.044236
8  2000-01-05        C -0.861849
9  2000-01-03        D -2.104569
10 2000-01-04        D -0.494929
11 2000-01-05        D  1.071804
----------------------------------------------
[in]
filtered = df[df["variable"] == "A"]
filtered

[out]
        date variable     value
0 2000-01-03        A  0.469112
1 2000-01-04        A -0.282863
2 2000-01-05        A -1.509059
----------------------------------------------
# much better way to represent the column "value"
[in]
pivoted = df.pivot(index="date", columns="variable", values="value")
pivoted

[out]
variable           A         B         C         D
date                                              
2000-01-03  0.469112 -1.135632  0.119209 -2.104569
2000-01-04 -0.282863  1.212112 -1.044236 -0.494929
2000-01-05 -1.509059 -0.173215 -0.861849  1.071804
----------------------------------------------
[in]
df["value2"] = df["value"] * 2
pivoted = df.pivot(index="date", columns="variable")
pivoted

[out]
               value                                  value2                              
variable           A         B         C         D         A         B         C         D
date                                                                                      
2000-01-03  0.469112 -1.135632  0.119209 -2.104569  0.938225 -2.271265  0.238417 -4.209138
2000-01-04 -0.282863  1.212112 -1.044236 -0.494929 -0.565727  2.424224 -2.088472 -0.989859
2000-01-05 -1.509059 -0.173215 -0.861849  1.071804 -3.018117 -0.346429 -1.723698  2.143608
----------------------------------------------
[in]
pivoted["value2"]

[out]
variable           A         B         C         D
date                                              
2000-01-03  0.938225 -2.271265  0.238417 -4.209138
2000-01-04 -0.565727  2.424224 -2.088472 -0.989859
2000-01-05 -3.018117 -0.346429 -1.723698  2.143608
~~~


- pd.pivot_table()  
; While pivot() provides general purpose pivoting with various data types (strings, numerics, etc.), pandas also provides pivot_table() for pivoting with aggregation of numeric data.

~~~
- data: a DataFrame object.

- values: a column or a list of columns to aggregate.

- index: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the pivot table index. If an array is passed, it is being used as the same manner as column values.

- columns: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the pivot table column. If an array is passed, it is being used as the same manner as column values.

- aggfunc: function to use for aggregation, defaulting to numpy.mean.
~~~

~~~python
[in]
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 6,
        "B": ["A", "B", "C"] * 8,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": np.random.randn(24),
        "E": np.random.randn(24),
        "F": [datetime.datetime(2013, i, 1) for i in range(1, 13)]
        + [datetime.datetime(2013, i, 15) for i in range(1, 13)],
    }
)

[out]
        A  B    C         D         E          F
0     one  A  foo  0.341734 -0.317441 2013-01-01
1     one  B  foo  0.959726 -1.236269 2013-02-01
2     two  C  foo -1.110336  0.896171 2013-03-01
3   three  A  bar -0.619976 -0.487602 2013-04-01
4     one  B  bar  0.149748 -0.082240 2013-05-01
..    ... ..  ...       ...       ...        ...
19  three  B  foo  0.690579 -2.213588 2013-08-15
20    one  C  foo  0.995761  1.063327 2013-09-15
21    one  A  bar  2.396780  1.266143 2013-10-15
22    two  B  bar  0.014871  0.299368 2013-11-15
23  three  C  bar  3.357427 -0.863838 2013-12-15
----------------------------------------------
[in]
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])

[out]
C             bar       foo
A     B                    
one   A  1.120915 -0.514058
      B -0.338421  0.002759
      C -0.538846  0.699535
three A -1.181568       NaN
      B       NaN  0.433512
      C  0.588783       NaN
two   A       NaN  1.000985
      B  0.158248       NaN
      C       NaN  0.176180
----------------------------------------------
[in]
pd.pivot_table(df, values="D", index=["B"], columns=["A", "C"], aggfunc=np.sum)

[out]
A       one               three                 two          
C       bar       foo       bar       foo       bar       foo
B                                                            
A  2.241830 -1.028115 -2.363137       NaN       NaN  2.001971
B -0.676843  0.005518       NaN  0.867024  0.316495       NaN
C -1.077692  1.399070  1.177566       NaN       NaN  0.352360
----------------------------------------------
[in]
pd.pivot_table(
    df, values=["D", "E"],
    index=["B"],
    columns=["A", "C"],
    aggfunc=np.sum,
)

[out]
          D                                                           E                                                  
A       one               three                 two                 one               three                 two          
C       bar       foo       bar       foo       bar       foo       bar       foo       bar       foo       bar       foo
B                                                                                                                        
A  2.241830 -1.028115 -2.363137       NaN       NaN  2.001971  2.786113 -0.043211  1.922577       NaN       NaN  0.128491
B -0.676843  0.005518       NaN  0.867024  0.316495       NaN  1.368280 -1.103384       NaN -2.128743 -0.194294       NaN
C -1.077692  1.399070  1.177566       NaN       NaN  0.352360 -1.976883  1.495717 -0.263660       NaN       NaN  0.872482
~~~

### **Pandas Options**
---
- 출력포맷 변경하기
~~~python

import pandas as pd
pd.options.display.float_format = '{:.02f}'.format

#            date  funding  openCashValue
# 0    1995-05-02     0.00           0.00
# 1    1995-05-03     0.00           0.00
~~~
<br><br><br>


## **Dataclass**
---
### **Dataclass**
---
- 정의 및 비교
  
~~~python
[in]
from dataclasses import dataclass

@dataclass
class Car:
    name: str
    brand: str
    price: int


car1 = Car('Model X', 'Tesla', 120_000)
car2 = Car('Model X', 'Tesla', 120_000)

print(car1 == car2)
print(car2.name)

[out]
True
Model X
~~~

- 비교 제외, 프린트 제외, default값 입력
  
~~~python
[in]
from dataclasses import dataclass, field

@dataclass
class Car:
    name: str = field(compare=False)  # 비교 대상에서 제외
    brand: str = field(repr=False)  # 프린트할때 감추기
    price: int = 120_000
    condition: str = field(default='New') # default값 정의


car1 = Car('Model X', 'Tesla', 120_000)
car2 = Car('Model Y', 'Tesla', 120_000)

print(car1 == car2)
print(car2)

[out]
True
Car(name='Model Y', price=120000, condition='New')
~~~

- 대소 비교 가능하도록 설정
~~~python
[in]
from dataclasses import dataclass

@dataclass(order=True)
class Book:
    name: str
    weight: float
    shelf_id: int

b1 = Book('I need Python',1.5,1267)		
b2 = Book('You need Python',0.5,6453)

print(b1>b2)

[out]
False		# 'I' < 'Y'
~~~

- 불변객체로 설정 (변경 시도하면 에러 발생시킴)
~~~python
[in]
from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    name: str
    weight: float
    shelf_id: int = 0

test = Book('I need Python',1.5,1267)
test.weight = 2.43
print(test)

[out]
Traceback (most recent call last):
  File line 11, in <module>
    test.weight = 2.43
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'weight'
~~~

- 중복된 dataclass 제거
~~~python
[in]
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Book:
    name: str
    weight: float
    shelf_id: int

b1 = Book('I need Python',1.5,1267)
b2 = Book('You need Python',0.5,6453)
b3 = Book('I need Python',1.5,1267)
b4 = Book('You need Python',0.5,6453)

print(set([b1,b2,b3,b4]))

[out]
{Book(name='I need Python', weight=1.5, shelf_id=1267), Book(name='You need Python', weight=0.5, shelf_id=6453)}
~~~

- Overriding
~~~python
[in]
from dataclasses import dataclass, field

@dataclass
class Car:
    name: str = field(compare=False)
    brand: str = field(repr=False)
    price: int = 120_000
    condition: str = field(default='New')

    def __post_init__(self):
        if self.condition == "Old":
            self.price -= 30_000

old_car = Car('Model X', 'Tesla', 130_000, 'Old')

print(old_car)

[out]
Car(name='Model X', price=90000, condition='Old')
~~~

- dataclass List
  
~~~python
[in]
ffrom dataclasses import dataclass
from typing import List

@dataclass
class Car:
    name: str # Supports tying out of the box!
    brand: str
    price: int

@dataclass
class CarDealer:
    cars: List[Car]


car3 = Car('Model S', 'Tesla', 89_000)
car4 = Car('Model Y', 'Tesla', 54_000)
car_dealer = CarDealer(cars=[car3, car4])

print(car_dealer)

[out]
CarDealer(cars=[Car(name='Model S', brand='Tesla', price=89000), Car(name='Model Y', brand='Tesla', price=54000)])
~~~

- dataclass dict
  
~~~python
[in]
from dataclasses import dataclass, field

@dataclass
class Car:
    name: str 
    brand: str
    price: int

@dataclass
class CarDealer:
    date : str
    name : str
    car: dict = field(default_factory=dict)

    def __post_init__(self):
        self.car['car'] = Car(self.name, 'tesla', '120000')

car = CarDealer(date='20100101', name='tesla')
print(car)

[out]
CarDealer(date='20100101', name='tesla', car={'car': Car(name='tesla', brand='tesla', price='120000')})
~~~

- dataclass to dict or tupele
  
~~~python
[in]
from dataclasses import dataclass, field, asdict, astuple

from typing import List

@dataclass
class User:
    number: int
    name: str = 'Anonymous'
    test: List[int] = field(default_factory=list)

user = User(number=122, name='Kim')

print(asdict(user))
print(astuple(user))


[out]
{'number': 122, 'name': 'Kim', 'test': []}
(122, 'Kim', [])
~~~

- dynamic dataclass
~~~python
# dataclasses.make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
# bases는 상속클래스이며, 상속 클래스가 하나이면 (class, ) 이렇게 표현해야함

C = make_dataclass('C',
                   [('x', int),
                     'y',
                    ('z', int, field(default=5))],
                   namespace={'add_one': lambda self: self.x + 1})

# is equal to

@dataclass
class C:
    x: int
    y: 'typing.Any'
    z: int = 5

    def add_one(self):
        return self.x + 1
~~~
<br><br><br>

## **Pydantic**
---
### **overview**
---
- id is of type int; the annotation-only declaration tells pydantic that this field is required. Strings, bytes or floats will be coerced to ints if possible; otherwise an exception will be raised.
- name is inferred as a string from the provided default; because it has a default, it is not required.
- signup_ts is a datetime field which is not required (and takes the value None if it's not supplied). pydantic will process either a unix timestamp int (e.g. 1496498400) or a string representing the date & time.
- friends uses python's typing system, and requires a list of integers. As with id, integer-like objects will be converted to integers.
~~~Python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.id)
#> 123
print(repr(user.signup_ts))
#> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
#> [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
~~~
- If validation fails pydantic will raise an error with a breakdown of what was wrong:
~~~python
from pydantic import ValidationError

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())

[output]
[
  {
    "loc": [
      "id"
    ],
    "msg": "field required",
    "type": "value_error.missing"
  },
  {
    "loc": [
      "signup_ts"
    ],
    "msg": "invalid datetime format",
    "type": "value_error.datetime"
  },
  {
    "loc": [
      "friends",
      2
    ],
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
  }
]
~~~
### **Validator**
---
- Custom validation and complex relationships between objects can be achieved using the validator decorator.
- validators are "class methods", so the first argument value they receive is the UserModel class, not an instance of UserModel.
- the second argument is always the field value to validate; it can be named as you please
- you can also add any subset of the following arguments to the signature (the names must match):
  - values: a dict containing the name-to-value mapping of any previously-validated fields
  - config: the model config
  - field: the field being validated. Type of object is pydantic.fields.ModelField.
  - **kwargs: if provided, this will include the arguments above not explicitly listed in the signature
- validators should either return the parsed value or raise a ValueError, TypeError, or AssertionError (assert statements may be used).
- where validators rely on other values, you should be aware that:
  - Validation is done in the order fields are defined. E.g. in the example above, password2 has access to password1 (and name), but password1 does not have access to password2. See Field Ordering for more information on how fields are ordered
  - If validation fails on another field (or that field is missing) it will not be included in values, hence if 'password1' in values and ... in this example.
~~~python
from pydantic import BaseModel, ValidationError, validator


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


user = UserModel(
    name='samuel colvin',
    username='scolvin',
    password1='zxcvbn',
    password2='zxcvbn',
)
print(user)
#> name='Samuel Colvin' username='scolvin' password1='zxcvbn' password2='zxcvbn'

try:
    UserModel(
        name='samuel',
        username='scolvin',
        password1='zxcvbn',
        password2='zxcvbn2',
    )
except ValidationError as e:
    print(e)
    """
    2 validation errors for UserModel
    name
      must contain a space (type=value_error)
    password2
      passwords do not match (type=value_error)
    """
~~~
- A few more things to note:
  - a single validator can be applied to multiple fields by passing it multiple field names
  - a single validator can also be called on all fields by passing the special value '*'
  - the keyword argument pre will cause the validator to be called prior to other validation
  - passing each_item=True will result in the validator being applied to individual values (e.g. of List, Dict, Set, etc.), rather than the whole object

~~~python
from typing import List
from pydantic import BaseModel, ValidationError, validator


class DemoModel(BaseModel):
    square_numbers: List[int] = []
    cube_numbers: List[int] = []

    # '*' is the same as 'cube_numbers', 'square_numbers' here:
    @validator('*', pre=True)
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split('|')
        return v

    @validator('cube_numbers', 'square_numbers')
    def check_sum(cls, v):
        if sum(v) > 42:
            raise ValueError('sum of numbers greater than 42')
        return v

    @validator('square_numbers', each_item=True)
    def check_squares(cls, v):
        assert v ** 0.5 % 1 == 0, f'{v} is not a square number'
        return v

    @validator('cube_numbers', each_item=True)
    def check_cubes(cls, v):
        # 64 ** (1 / 3) == 3.9999999999999996 (!)
        # this is not a good way of checking cubes
        assert v ** (1 / 3) % 1 == 0, f'{v} is not a cubed number'
        return v


print(DemoModel(square_numbers=[1, 4, 9]))
#> square_numbers=[1, 4, 9] cube_numbers=[]
print(DemoModel(square_numbers='1|4|16'))
#> square_numbers=[1, 4, 16] cube_numbers=[]
print(DemoModel(square_numbers=[16], cube_numbers=[8, 27]))
#> square_numbers=[16] cube_numbers=[8, 27]
try:
    DemoModel(square_numbers=[1, 4, 2])
except ValidationError as e:
    print(e)
    """
    1 validation error for DemoModel
    square_numbers -> 2
      2 is not a square number (type=assertion_error)
    """

try:
    DemoModel(cube_numbers=[27, 27])
except ValidationError as e:
    print(e)
    """
    1 validation error for DemoModel
    cube_numbers
      sum of numbers greater than 42 (type=value_error)
    """
~~~
- For performance reasons, by default validators are not called for fields when a value is not supplied. However there are situations where it may be useful or required to always call the validator, e.g. to set a dynamic default value.
- You'll often want to use this together with pre, since otherwise with always=True pydantic would try to validate the default None which would cause an error.
~~~python
from datetime import datetime

from pydantic import BaseModel, validator


class DemoModel(BaseModel):
    ts: datetime = None

    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()


print(DemoModel())
#> ts=datetime.datetime(2022, 7, 10, 23, 6, 7, 47620)
print(DemoModel(ts='2017-11-08T14:00'))
#> ts=datetime.datetime(2017, 11, 8, 14, 0)
~~~

~~~python
from pydantic import BaseModel

class BarModel(BaseModel):
    whatever: int

class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel

m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

# returns a dictionary:
print(m.dict())
"""
{
    'banana': 3.14,
    'foo': 'hello',
    'bar': {'whatever': 123},
}
"""
print(m.dict(include={'foo', 'bar'}))
#> {'foo': 'hello', 'bar': {'whatever': 123}}
print(m.dict(exclude={'foo', 'bar'}))
#> {'banana': 3.14}
~~~
- None 처리
~~~python 
class ComplexModel(BaseModel):
    complexNo:str
    complexName:str
    dongNo:str
    realEstateTypeCode:str
    cortarAddress:str
    detailAddress:str
    totalHouseholdCount:int
    totalBuildingCount:int
    highFloor:int
    lowFloor:int
    useApproveYmd:Optional[datetime]

    @validator('useApproveYmd', always=True)
    def deal_with_none(cls, v, values):
        if not v:
            return None
        return v
~~~


<br><br><br>


## **openpyxl**
---
### **create a workbook**
---
~~~python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
# This is set to 0 by default. Unless you modify its value, you will always get the first worksheet by using this method.
~~~
~~~python
wb = Workbook()
ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position
~~~
~~~python
ws.title = "New Title"
ws.sheet_properties.tabColor = "1072BA" # RRGGBB color code for the background color of the tab holding this title
~~~
~~~python
# Once you gave a worksheet a name, you can get it as a key of the workbook
ws3 = wb["New Title"]
# You can review the names of all worksheets of the workbook with the Workbook.sheetname attribute
print(wb.sheetnames)
# >>> ['Sheet2', 'New Title', 'Sheet1']
~~~
### **Playing with data**
~~~python
# Now we know how to get a worksheet, we can start modifying cells content. Cells can be accessed directly as keys of the worksheet:
c = ws['A4']
# This will return the cell at A4, or create one if it does not exist yet. Values can be directly assigned:
ws['A4'] = 4
# There is also the Worksheet.cell() method. This provides access to cells using row and column notation:
d = ws.cell(row=4, column=2, value=10)
~~~
~~~python
# Ranges of cells can be accessed using slicing:
cell_range = ws['A1':'C2']
# Ranges of rows or columns can be obtained similarly:
colC = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]
~~~
~~~python
# You can also use the Worksheet.iter_rows() method:
[in]
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
  for cell in row:
      print(cell)
[out]
<Cell Sheet1.A1>
<Cell Sheet1.B1>
<Cell Sheet1.C1>
<Cell Sheet1.A2>
<Cell Sheet1.B2>
<Cell Sheet1.C2>
~~~
~~~python
# Likewise the Worksheet.iter_cols() method will return columns:
[in]
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
  for cell in col:
      print(cell)
[out]
<Cell Sheet1.A1>
<Cell Sheet1.A2>
<Cell Sheet1.B1>
<Cell Sheet1.B2>
<Cell Sheet1.C1>
<Cell Sheet1.C2>
~~~
~~~python
# If you need to iterate through all the rows or columns of a file, you can instead use the Worksheet.rows property:
[in]
ws = wb.active
ws['C9'] = 'hello world'
tuple(ws.rows)
[out]
((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
(<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
(<Cell Sheet.A3>, <Cell Sheet.B3>, <Cell Sheet.C3>),
(<Cell Sheet.A4>, <Cell Sheet.B4>, <Cell Sheet.C4>),
(<Cell Sheet.A5>, <Cell Sheet.B5>, <Cell Sheet.C5>),
(<Cell Sheet.A6>, <Cell Sheet.B6>, <Cell Sheet.C6>),
(<Cell Sheet.A7>, <Cell Sheet.B7>, <Cell Sheet.C7>),
(<Cell Sheet.A8>, <Cell Sheet.B8>, <Cell Sheet.C8>),
(<Cell Sheet.A9>, <Cell Sheet.B9>, <Cell Sheet.C9>))
~~~
~~~python
# or the Worksheet.columns property:
[in]
tuple(ws.columns)
[out]
((<Cell Sheet.A1>,
<Cell Sheet.A2>,
<Cell Sheet.A3>,
<Cell Sheet.A4>,
<Cell Sheet.A5>,
<Cell Sheet.A6>,
...
~~~
~~~python
# Both Worksheet.iter_rows() and Worksheet.iter_cols() can take the values_only parameter to return just the cell’s value:
[in]
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
  print(row)
[out]
(None, None, None)
(None, None, None)
~~~
### **Data storage**
~~~python
# Once we have a Cell, we can assign it a value:
[in]
c = ws['A4']
c.value = 'hello, world'
print(c.value)

[out]
'hello, world'
-------------------------------------------------
[in]
d = ws.cell(row=4, column=2, value=10)
d.value = 3.14
print(d.value)

[out]
3.14
-------------------------------------------------
#(note) Because of this feature, scrolling through cells instead of accessing them directly will create them all in memory, even if you don’t assign them a value
for x in range(1,101):
      for y in range(1,101):
          ws.cell(row=x, column=y)
#  -> This code dosen't create any cell value
-------------------------------------------------
# simple usage
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()
dest_filename = 'empty_book.xlsx'
ws1 = wb.active
ws1.title = "range names"
for row in range(1, 40):
     ws1.append(range(600))
ws2 = wb.create_sheet(title="Pi")
ws2['F5'] = 3.14
ws3 = wb.create_sheet(title="Data")
for row in range(10, 20):
    for col in range(27, 54):
        _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
wb.save(filename = dest_filename)
~~~


### **Saving to a file**
~~~python
# The simplest and safest way to save a workbook is by using the Workbook.save() method of the Workbook object:
wb = Workbook()
wb.save('balances.xlsx')
~~~

### **Loading from a file**
---
~~~python
[in]
from openpyxl import load_workbook
wb2 = load_workbook('test.xlsx')
print(wb2.sheetnames)

[out]
['Sheet2', 'New Title', 'Sheet1']
~~~

## **pymysql**
---
### create schema
---
~~~python
### MySQL Workbench query 창에서 입력 후 ctrl+enter 키실행
CREATE SCHEMA krxData DEFAULT CHARACTER SET utf8;
~~~

### **create DB file & table**
---
- data type

|데이터형식| 바이트 수|숫자 범위| 설명|
|---|---|---|---|
|BIT(N)|	N/8|	 	|1~64Bit 표현, b'0000'형식으로 표현
|TINYINT|	1|	-128 ~ 127	|정수
|SMALLINT|	2|	-32,768 ~ 32,767	|정수
|MEDIUMINT|	3|	-8,388,608 ~ 8,388,607	|정수
|INT, INTEGER|	4|	약-21억 ~ +21억	|정수
|BIGINT|	8|	약 -900경 ~ +900경	|정수
|FLOAT|	4|	-3.40E+38 ~ -1.17E-38	|소수점 아래 7자리까지 표현
|DOUBLE, REAL|	8|	-1.22E-308 ~ 1.79E+308	|소수점 아래 15자리까지 표현
|DECIMAL(m,[d]), NUMBER(m,[d])|	5~17|	-10^38+1 ~ 10^38-1	|전체 자릿수(m)와 소수점 이하 자릿수(d)를 가진 숫자형 예) decimal(5,2)는 전체 자릿수를 5자리로 하되, 그 중 소수점 이하를 2자리로 함

---

|데이터 형식	|바이트 수	|설명|
|---|---|---
CHAR(n)	|1 ~ 255	|고정길이 문자형 n을 1부터 255까지 지정 그냥 CHAR만 쓰면 CHAR(1)과 동일
VARCHAR(n)	|1 ~ 65535	|가변길이 문자형 n을 사용하면 1부터 65535까지 지정
BINARY(n)	|1 ~ 255	|고정길이의 이진 데이터 값
VARBINARY(n)	|1 ~ 255	|가변길이의 이진 데이터 값
TINYTEXT	|1 ~ 255	|255 크기의 TEXT 데이터 값
TEXT	|1 ~ 65535	|N 크기의 TEXT 데이터 값
MEDIUMTEXT	|1 ~ 16777215	|16777215 크기의 TEXT 데이터 값
LONGTEXT	|1 ~ 4294967295	|최대 4GB 크기의 TEXT 데이터 값
TINYBLOB	|1 ~ 255	|255 크기의 BLOB 데이터 값
BLOB	|1 ~ 65535	|N 크기의 BLOB 데이터 값
MEDIUMBLOB	|1 ~ 16777215	|16777215 크기의 BLOB 데이터 값
LONGBLOB	|1 ~ 4294967295	|최대 4GB 크기의 BLOB 데이터 값
ENUM(값들...)	|1 또는 2	|최대 65535개의 열거형 데이터 값
SET(값들...)	|1, 2, 3, 4, 8	|최대 64개의 서로 다른 데이터 값

---

~~~python
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8')
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
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db='fundamentalData', charset='utf8')
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

## **sqlite**
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

### **BeautifulSoup**
---

~~~
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
~~~
- Making the Soup
~~~python
from bs4 import BeautifulSoup

with open("index.html") as fp:          # file case : method1
    soup = BeautifulSoup(fp, 'html.parser')
~~~
~~~python
soup = BeautifulSoup("<html>a web page</html>", 'html.parser')  # methond 2
~~~

- prettify() 
~~~python
[in]
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

[out]

<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
    ...     # (skip)
~~~

- get_text() 
~~~python
[in]
print(soup.get_text())

[out]
The Dormouse's story

The Dormouse's story

Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
...
~~~

- find_all() 
~~~python
[in]
soup.find_all('a')

[out]
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
~~~

~~~python
[in]
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

[out]
body
b
~~~

~~~python
# This code finds all the tags whose names contain the letter ‘t’
[in]
for tag in soup.find_all(re.compile("t")):
    print(tag.name)

[out]
html
title
~~~

~~~python
# This code finds only strings(contents).
soup.find_all(string=re.compile(parser))
~~~

~~~python
[in]
soup.find_all(["a", "b"])

[out]
[<b>The Dormouse's story</b>,
 <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
~~~

- find_all_next(name, attrs, string, limit, **kwargs)
~~~python
[in]
first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_all_next(string=True)

[out]
['Elsie', ',\n', 'Lacie', ' and\n', 'Tillie',
 ';\nand they lived at the bottom of a well.', '\n', '...', '\n']
~~~
~~~python
[in]
first_link.find_next("p")

[out]
<p class="story">...</p>
~~~


- .contents : list형태임
~~~python
[in]
head_tag = soup.head
head_tag

#<head><title>The Dormouse's story</title></head>

head_tag.contents

[out]
[<title>The Dormouse's story</title>]
~~~
~~~python
[in]
title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents

[out]
['The Dormouse's story']
~~~
~~~python
# A string does not have .contents, because it can’t contain anything.
[in]
text = title_tag.contents[0]
text.contents

[out]
AttributeError: 'NavigableString' object has no attribute 'contents' 
~~~

- .children : generator 형태임 (iteratable)
~~~python
[in]
for child in title_tag.children:
    print(child)

[out]
The Dormouse's story
~~~

- .descendants : generator 형태임. 해당 soup 아래의 모든 soup 객체를 generate함. 반면, .contents와 .children은 직속 바로 아래의 soup 객체 하나만 반환함. 
~~~python
[in]
head_tag.contents

[out]
[<title>The Dormouse's story</title>]
~~~

~~~python
[in]
for child in head_tag.descendants:
    print(child)

[out]
<title>The Dormouse's story</title>
The Dormouse's story
~~~

~~~python
[in]
len(list(soup.children))
len(list(soup.descendants))

[out]
1
26
~~~

- .string / .strings / .stripped_strings
~~~python 
[in]
title_tag.string

[out]
'The Dormouse's story'
~~~
~~~python
[in]
print(head_tag.contents)
print(head_tag.string)

[out]
[<title>The Dormouse's story</title>]
'The Dormouse's story'
~~~
~~~python
# If a tag contains more than one thing, then it’s not clear what .string should refer to, so .string is defined to be None
[in]
print(soup.html.string)

[out]
None  
~~~

~~~python
# If there’s more than one thing inside a tag, you can still look at just the strings. Use the .strings generator
[in]
for string in soup.strings:
    print(repr(string))

[out]
"The Dormouse's story"
'\n'
'\n'
"The Dormouse's story"
'\n'
'Once upon a time there were three little sisters; and their names were\n'
'Elsie'
... # skip
~~~

~~~python
# These strings tend to have a lot of extra whitespace, which you can remove by using the .stripped_strings generator instead:
[in]
for string in soup.stripped_strings:
    print(repr(string))

[out]
"The Dormouse's story"
"The Dormouse's story"
'Once upon a time there were three little sisters; and their names were'
'Elsie'
','
'Lacie'
'and'
'Tillie'
';\n and they lived at the bottom of a well.'
... # skip
~~~

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

### **XML 파일 다루기**
---
- xml 파일 프린트하기
~~~python
[in]
dir = Path.cwd()

with open(dir/'CORPCODE.xml','r',  encoding='UTF8') as f:
    xmlString = f.read()
print(xmlString)

[out]
<?xml version="1.0" encoding="UTF-8"?>
<result>
    <list>
        <corp_code>00434003</corp_code>
        <corp_name>다코</corp_name>
        <stock_code> </stock_code>
        <modify_date>20170630</modify_date>
    </list>
    <list>
        <corp_code>00434456</corp_code>
        <corp_name>일산약품</corp_name>
        <stock_code> </stock_code>
        <modify_date>20170630</modify_date>
    </list>
~~~

- xml 파일을 python dictionary로 변환
~~~python
from xml.etree.ElementTree import parse

dir = Path.cwd()

tree = parse(dir/'CORPCODE.xml')
root = tree.getroot()

list = root.findall("list")

dic = [{'corp_code' : x.findtext("corp_code"), 'corp_name' : x.findtext("corp_name"), 'stock_code' : x.findtext("stock_code"), 'modify_date' : x.findtext("modify_date")} for x in list]
~~~

## **TQDM**
---
- progress bar size
~~~python
lst = range(0,100000)

num = 0
for i in tqdm(lst, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
    num = i
~~~

## **Blinker**
---
- Subscribing to Signals & Emitting Signals
~~~python
[in]
from blinker import signal

def subscriber(sender):
    print("Got a signal sent by %r" % sender)

class Processor:
  def __init__(self, name):
    self.name = name

  def go(self):
    ready = signal('ready')
    ready.send(self)
    print("Processing.")
    complete = signal('complete')
    complete.send(self)

  def __repr__(self):
    return '<Processor %s>' % self.name


ready = signal('ready')
ready.connect(subscriber)
processor_a = Processor('a')
processor_a.go()

[out]
Got a signal sent by <Processor a>
Processing.
~~~

- Subscribing to Specific Senders
~~~python
[in]
def b_subscriber(sender):
  print("Caught signal from processor_b.")
  assert sender.name == 'b'
processor_b = Processor('b')
ready.connect(b_subscriber, sender=processor_b)
processor_a.go()
processor_b.go()

[out]
Got a signal sent by <Processor b>
Caught signal from processor_b.
Processing.
~~~
- Sending and Receiving Data Through Signals
~~~python
[in]
send_data = signal('send-data')
@send_data.connect
def receive_data(sender, **kw):
  print("Caught signal from %r, data %r" % (sender, kw))
  return 'received!'

result = send_data.send('anonymous', abc=123)
print(result)
# The return value of send() collects the return values of each connected function as a list of (receiver function, return value) pairs:

[out]
Caught signal from 'anonymous', data {'abc': 123}
[(<function receive_data at 0x...>, 'received!')]
~~~

- Practicle Example
~~~python
[in]
from blinker import signal
frobnicated = signal('frobnicated')

class Receiver(object):

  def __init__(self):
    def handle_frobnicated(sender, **kwargs):
      self.on_frobnicated(sender, **kwargs)
    self.handle_frobnicated = handle_frobnicated
    frobnicated.connect(handle_frobnicated)

  def on_frobnicated(self, sender, **kwargs):
    print sender, kwargs['message']

if __name__ == '__main__':
  receiver = Receiver()
  for i in range(10):
      frobnicated.send('Sender %s' % i, message='hello')

[out]
Sender 0 hello
Sender 1 hello
Sender 2 hello
Sender 3 hello
Sender 4 hello
Sender 5 hello
Sender 6 hello
Sender 7 hello
Sender 8 hello
Sender 9 hello
~~~
## **Library, Package, Module**
---
- **Project 기본 구조**
~~~
-ProjectName(folder)
 |-package(folder)
 |  |-__init__.py
 |  |-module1.py
 |  |-module2.py
 |-test(folder)
 |  |-__init__.py 
 |  |-test_module1.py
 |  |-test_module2.py
 |-setup.py
 |-main.py
~~~
- package 또는 test에서 run 방법  
(!) run은 해당 프로젝트에서 실행되어야 함
~~~
# TERMINAL 창에서

python -m package.moudule1

python -m test.test_moudule1
~~~

- setup.py 구성 방법
~~~python
from setuptools import setup, find_packages

setup(name='naverLand_v2',
      version='0.1',
      url='https://github.com/ajcltm/naverLand_v2',
      license='jnu',
      author='ajcltm',
      author_email='ajcltm@gmail.com',
      description='',
      packages=find_packages(exclude=['test']),
      zip_safe=False,
      setup_requires=['requests>=1.0'],
      test_suite='test.test_guScraper')
~~~
- setup.py 실행방법
~~~
# TERMINAL 창에서 실행
pip install -e projectName
~~~

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
from pathlib import Path
sys.path.append(str(Path.cwd())) # 경로 추가
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

- 파일리스트 확인
~~~python
[in]
import os
path = "./"
os.listdir(path)
~~~

- folder 생성하기
~~~python
[in]
import os
dirPath = Path.home().joinpath('Desktop')/'testFolder'
os.makedirs(dirPath)
~~~

- 확장자 알아내기
~~~python
[in]
import os
file_path = 'C:/Users/Sim/Desktop/test/c1.txt'
print(os.path.splitext(file_path))
print("확장자: ", os.path.splitext(file_path)[1])

[out]
('C:/Users/Sim/Desktop/test/c1', '.txt')
확장자 : .txt
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

## unittest
---
- 기본 프레임
~~~python
import unittest

# TestCase를 작성
class CustomTests(unittest.TestCase):
  def test_runs(self):
    custom_function()

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()
~~~

- setUp / tearDown
~~~python
import unittest
import os

def custom_function(file_name):
  with open(file_name, 'rt') as f:
    return sum(1 for _ in f)

# TestCase를 작성
class CustomTests(unittest.TestCase):

#테스트 시작되기 전 파일 작성
  def setUp(self):

    self.file_name = 'test_file.txt'
    with open(self.file_name, 'wt') as f:
      f.write("
      멋지군요! 단위테스트
      ".strip())

#테스트 종료 후 파일 삭제 
  def tearDown(self):
    try:
        os.remove(self.file_name)
    except:
        pass

#단순 실행여부 판별하는 테스트 메소드
  def test_runs(self):
    custom_function(self.file_name)

  def test_line_count(self):
    self.assertEqual(custom_function(self.file_name), 3)

#unittest를 실행
if __name__ == '__main__':
    unittest.main()
~~~

- mock
~~~python
import unittest
from mock import Mock
class TestMocking(unittest.TestCase):
  def test_mock_method_returns(self):
    my_mock = Mock()
    my_mock.my_method.return_value = "hello mock"
    self.assertEqual("hello mock", my_mock.my_method())
~~~
- mock : side_effect
~~~python
import unittest
from unittest.mock import Mock

class TestSampleClass(unittest.TestCase):
  
  def test_side_effect_function(self):
    sample_function = Mock(side_effect=lambda x: x+1)
    self.assertEqual(sample_function(1),2)

  def test_side_effect_iterable(self):
    sample_function = Mock(side_effect=[1,2,3])
    self.assertEqual(sample_function(), 1)
    self.assertEqual(sample_function(), 2)
    self.assertEqual(sample_function(), 3)

  def test_side_effect_exception(self):
    sample_function = Mock(side_effect=ValueError())
    with self.assertRaises(ValueError):
      sample_function()
~~~


- unittest의 assert메소드 리스트

Method|	Checks that|
---|---|
assertEqual(a, b)|	a == b	 
assertNotEqual(a, b)|	a != b	 
assertTrue(x)|	bool(x) is True	 
assertFalse(x)|	bool(x) is False	 
assertIs(a, b)|	a is b
assertIsNot(a, b)|	a is not b
assertIsNone(x)|	x is None
assertIsNotNone(x)|	x is not None
assertIn(a, b)|	a in b
assertNotIn(a, b)|	a not in b
assertIsInstance(a, b)|	isinstance(a, b)
assertNotIsInstance(a, b)|	not isinstance(a, b)
assertRaises(exc, fun, *args, **kwds)|	fun(*args, **kwds) raises exc	 
assertRaisesRegex(exc, r, fun, *args, **kwds)|	fun(*args, **kwds) raises exc and the message matches regex r
assertWarns(warn, fun, *args, **kwds)|	fun(*args, **kwds) raises warn
assertWarnsRegex(warn, r, fun, *args, **kwds)|	fun(*args, **kwds) raises warn and the message matches regex r
assertLogs(logger, level)|	The with block logs on logger with minimum level
assertAlmostEqual(a, b)|	round(a-b, 7) == 0
assertNotAlmostEqual(a, b)|	round(a-b, 7) != 0	 
assertGreater(a, b)|	a > b
assertGreaterEqual(a, b)|	a >= b
assertLess(a, b)|	a < b
assertLessEqual(a, b)|	a <= b
assertRegex(s, r)|	r.search(s)
assertNotRegex(s, r)|	not r.search(s)
assertCountEqual(a, b)|	a and b have the same elements in the same number, regardless of their order
assertMultiLineEqual(a, b)|	strings
assertSequenceEqual(a, b)|	sequences
assertListEqual(a, b)|	lists
assertTupleEqual(a, b)|	tuples
assertSetEqual(a, b)|	sets or frozensets
assertDictEqual(a, b)|	dicts