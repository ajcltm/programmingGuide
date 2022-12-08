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

- xml 노드 만들기
~~~python
from xml.etree.ElementTree import Element, dump

node1 = Element("first")
node1.text = "안녕"
dump(node1)
#결과
<first>안녕</first>
~~~

- 노드에 노드 추가하기
~~~python
from xml.etree.ElementTree import Element, dump

root = Element("xml")
node1 = Element("first")
node1.text = "안녕"
root.append(node1)

node2 = Element("second")
node2.text = "Hello"
root.append(node2)

dump(root)
#결과
<xml><first>안녕</first><second>Hello</second></xml>
~~~

- 속성 추가하기 
~~~python
from xml.etree.ElementTree import Element, dump
root = Element("xml", kind="language")
node1 = Element("first")
node1.text = "안녕"
root.append(node1)

node2 = Element("second")
node2.text = "Hello"
root.append(node2)
dump(root)
#결과
<xml kind="language"><first>안녕</first><second>Hello
</second></xml>
~~~

- 보기 좋게 xml만들기
~~~python
from xml.etree.ElementTree import Element, dump

root = Element("xml", kind="language")

node1 = Element("first")
node1.text = "안녕"
root.append(node1)

node2 = Element("second")
node2.text = "Hello"
root.append(node2)

def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
indent(root)
dump(root)
#결과
<xml kind="language">
    <first>안녕</first>
    <second>Hello</second>
</xml>
~~~

- xml파일로 쓰기
~~~python
from xml.etree.ElementTree import ElementTree

ElementTree(note).write("note.xml")
~~~

