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