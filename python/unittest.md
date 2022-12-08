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
