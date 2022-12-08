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
