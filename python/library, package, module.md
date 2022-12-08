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

