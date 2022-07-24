### **Instance Method**

- Instance methods takes self as the first argument.
- Decorator is not required for instance methods.
~~~python
class RECTANGLE:

    def number_of_sides(self):
        print(“I have 2 sides”)
~~~

### **Static Method**

- Use static method when there is a method inside a class that is logically related to the class, but does not necessarily interact with any specific instance.
- Static methods are created using the @staticmethod decorator.
~~~python
class RECTANGLE:

     def number_of_sides(self):
          print(“I have 2 sides”)
     @staticmethod
     def info():
         print("inside the Square class")
~~~

### **Class method**

- Class methods are created using the @classmethod decorator.
- The class method has access to the class’s state as it takes a class parameter that points to the class and not the object instance.
~~~python
class RECTANGLE:
    name = "RECTANGLE"
    def number_of_sides(self):
        print(“I have 2 sides”)
    
    @classmethod
    def info_class_name(cls):
        print(cls.name)
~~~

### **Abstract Method**

- Abstract methods are created using the @abstractmethod decorator.
- They override the properties of base class.
~~~python
from abc import ABC, abstractmethod
class POLYGON(ABC):
    @abstractmethod
    def number_of_sides(self):
        pass
class RECTANGLE(POLYGON):

    def number_of_sides(self):
        print(“I have 2 sides”)
~~~