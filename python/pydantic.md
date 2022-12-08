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
### **Serializtion**
---
- from dictionary
~~~python
class Person(BaseModel):
    first_name: str = None
    last_name: str
    age: Optional[int]

data = {
    "first_name" : "isaac",
    "last_name" : "Newton",
    "dob" : "1643-01-04"
}

p = Person.parse_obj(data)
~~~

- from json
~~~python
class Person(BaseModel):
    first_name: str = None
    last_name: str
    age: Optional[int]

json = '''{
    "first_name" : "isaac",
    "last_name" : "Newton",
    "dob" : "1643-01-04"
}'''

p = Person.parse_raw(json)
~~~
### **Deserialization**
---
- to dictionary
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
- to json
~~~python
class Person(BaseModel):
    first_name: str = None
    last_name: str
    age: Optional[int]

p = Person(first_name='Isaac', last_name='Newton', age=84)
print(p.json(include={'last_name', 'age'}, indent=4))
~~~

### **alias**
---
~~~python
from pydantic import BaseModel, Field
from datetime import date

class Person(BaseModel):
    first_name: str = Field(alias='firstName', default=None)
    last_name: str = Field(alias='lastName')
    dob: date = None 

   class Config:
    allow_population_by_field_name = True  ## config 설정안하면, 객체 생성시 alias를 사용해야하고, represent는 model 송성명으로 출력됨

Person(first_name='Isaac', last_name='Newton')
data = {'first_name'='Isaac', 'last_name':'Newton'}
p = Person.parse_obj(data) ## Person(first_name='Isaac', last_name:'Newton', dob:None)

data2 = {'firstName'='Isaac', 'lastName':'Newton'}
p = Person.parse_raw(data2) ## Person(first_name='Isaac', last_name:'Newton', dob:None)

p.dict() ## {'first_name'='Isaac', 'last_name':'Newton', 'dob':None}
p.json() ## '{'first_name'='Isaac', 'last_name':'Newton', 'dob':Null}'
p.dict(by_alias=True) ## {'firstName'='Isaac', 'lastName':'Newton', 'dob':None}
p.json(by_alias=True) ## '{'firstName'='Isaac', 'lastName':'Newton', 'dob':Null}'
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

