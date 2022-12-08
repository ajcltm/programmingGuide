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

