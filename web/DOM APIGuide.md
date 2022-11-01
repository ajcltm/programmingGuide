#### DOM tree는 네 종류의 노드로 구성
---
- 문서 노드(Document Node)
~~~
트리의 최상위에 존재하며 각각 요소, 어트리뷰트, 텍스트 노드에 접근하려면 문서 노드를 통해야 한다. 즉, DOM tree에 접근하기 위한 시작점(entry point)이다.
~~~
- 요소 노드(Element Node)
~~~
요소 노드는 HTML 요소를 표현한다. HTML 요소는 중첩에 의해 부자 관계를 가지며 이 부자 관계를 통해 정보를 구조화한다. 따라서 요소 노드는 문서의 구조를 서술한다고 말 할 수 있다. 어트리뷰트, 텍스트 노드에 접근하려면 먼저 요소 노드를 찾아 접근해야 한다. 모든 요소 노드는 요소별 특성을 표현하기 위해 HTMLElement 객체를 상속한 객체로 구성된다.
~~~
- 어트리뷰트 노드(Attribute Node)
~~~
어트리뷰트 노드는 HTML 요소의 어트리뷰트를 표현한다. 어트리뷰트 노드는 해당 어트리뷰트가 지정된 요소의 자식이 아니라 해당 요소의 일부로 표현된다. 따라서 해당 요소 노드를 찾아 접근하면 어트리뷰트를 참조, 수정할 수 있다.
~~~
- 텍스트 노드(Text Node)
~~~
텍스트 노드는 HTML 요소의 텍스트를 표현한다. 텍스트 노드는 요소 노드의 자식이며 자신의 자식 노드를 가질 수 없다. 즉, 텍스트 노드는 DOM tree의 최종단이다.
~~~

#### DOM Query / Traversing (요소에의 접근)
---
- document.getElementById(id)
    - id 어트리뷰트 값으로 요소 노드를 한 개 선택한다. 
    - 복수개가 선택된 경우, 첫번째 요소만 반환한다.
    - Return: HTMLElement를 상속받은 객체
    - 모든 브라우저에서 동작
~~~javascript
// CSS 셀렉터를 이용해 요소를 선택한다
const elem = document.querySelector('li.red');
// 클래스 어트리뷰트의 값을 변경한다.
elem.className = 'blue';
~~~
- document.getElementsByClassName(class)
    - class 어트리뷰트 값으로 요소 노드를 모두 선택한다. 공백으로 구분하여 여러 개의 class를 지정할 수 있다.
    - Return: HTMLCollection (live)
    - IE9 이상의 브라우저에서 동작
~~~javascript
// HTMLCollection을 반환한다. HTMLCollection은 live하다.
const elems = document.getElementsByClassName('red');

for (let i = 0; i < elems.length; i++) {
  // 클래스 어트리뷰트의 값을 변경한다.
  elems[i].className = 'blue';
}
~~~
- 위 예제를 실행해 보면 예상대로 동작하지 않는다. (두번째 요소만 클래스 변경이 되지 않는다.)
- getElementsByClassName 메소드의 반환값은 HTMLCollection이다. 이것은 반환값이 복수인 경우, HTMLElement의 리스트를 담아 반환하기 위한 객체로 배열과 비슷한 사용법을 가지고 있지만 배열은 아닌 유사배열(array-like object)이다. 또한 HTMLCollection은 실시간으로 Node의 상태 변경을 반영한다. (live HTMLCollection)
- HTMLCollection을 배열로 변경한다. 아래 방법을 권장한다.
~~~javascript
const elems = document.getElementsByClassName('red');

// 유사 배열 객체인 HTMLCollection을 배열로 변환한다.
// 배열로 변환된 HTMLCollection은 더 이상 live하지 않다.
console.log([...elems]); // [li#one.red, li#two.red, li#three.red]

[...elems].forEach(elem => elem.className = 'blue');
~~~

- document.getElementsByTagName(tagName)
    - 태그명으로 요소 노드를 모두 선택한다.
    - Return: HTMLCollection (live)
    - 모든 브라우저에서 동작
~~~javascript
// HTMLCollection을 반환한다.
const elems = document.getElementsByTagName('li');

[...elems].forEach(elem => elem.className = 'blue');
~~~

- document.querySelectorAll(selector)
    - 지정된 CSS 선택자를 사용하여 요소 노드를 모두 선택한다.
    - Return: NodeList (non-live)
    - IE8 이상의 브라우저에서 동작
~~~javascript
// Nodelist를 반환한다.
const elems = document.querySelectorAll('li.red');

[...elems].forEach(elem => elem.className = 'blue');
~~~

 - parentNode
    - 부모 노드를 탐색한다.
    - Return: HTMLElement를 상속받은 객체
    - 모든 브라우저에서 동작
~~~javascript
const elem = document.querySelector('#two');

elem.parentNode.className = 'blue';
~~~

- firstChild, lastChild
    - 자식 노드를 탐색한다.
    - Return: HTMLElement를 상속받은 객체
    - IE9 이상의 브라우저에서 동작
    - const elem = document.querySelector('ul');
~~~javascript
// first Child
elem.firstChild.className = 'blue';
// last Child
elem.lastChild.className = 'blue';
~~~
- 위 예제를 실행해 보면 예상대로 동작하지 않는다. 그 이유는 IE를 제외한 대부분의 브라우저들은 요소 사이의 공백 또는 줄바꿈 문자를 텍스트 노드로 취급하기 때문이다. 
- firstElementChild, lastElementChild를 사용하면 문제를 회피할 수 있음
~~~javascript
const elem = document.querySelector('ul');

// first Child
elem.firstElementChild.className = 'blue';
// last Child
elem.lastElementChild.className = 'blue';
~~~

- hasChildNodes()
     - 자식 노드가 있는지 확인하고 Boolean 값을 반환한다.
     - Return: Boolean 값
     - 모든 브라우저에서 동작
- childNodes
    - 자식 노드의 컬렉션을 반환한다. 텍스트 요소를 포함한 모든 자식 요소를 반환한다.
    - Return: NodeList (non-live)
    - 모든 브라우저에서 동작
- children
    - 자식 노드의 컬렉션을 반환한다. 자식 요소 중에서 Element type 요소만을 반환한다.
    - Return: HTMLCollection (live)
    - IE9 이상의 브라우저에서 동작
~~~javascript
const elem = document.querySelector('ul');

if (elem.hasChildNodes()) {
  console.log(elem.childNodes);
  // 텍스트 요소를 포함한 모든 자식 요소를 반환한다.
  // NodeList(9) [text, li#one.red, text, li#two.red, text, li#three.red, text, li#four, text]

  console.log(elem.children);
  // 자식 요소 중에서 Element type 요소만을 반환한다.
  // HTMLCollection(4) [li#one.red, li#two.red, li#three.red, li#four, one: li#one.red, two: li#two.red, three: li#three.red, four: li#four]
  [...elem.children].forEach(el => console.log(el.nodeType)); // 1 (=> Element node)
}
~~~

- previousSibling, nextSibling
    - 형제 노드를 탐색한다. text node를 포함한 모든 형제 노드를 탐색한다.
    - Return: HTMLElement를 상속받은 객체
    - 모든 브라우저에서 동작
- previousElementSibling, nextElementSibling
    - 형제 노드를 탐색한다. 형제 노드 중에서 Element type 요소만을 탐색한다.
    - Return: HTMLElement를 상속받은 객체
    - IE9 이상의 브라우저에서 동작
~~~javascript
const elem = document.querySelector('ul');

elem.firstElementChild.nextElementSibling.className = 'blue';
elem.firstElementChild.nextElementSibling.previousElementSibling.className = 'blue';
~~~

#### DOM Manipulation (조작)
---
- 요소의 텍스트는 텍스트 노드에 저장되어 있다. 텍스트 노드에 접근하려면 아래와 같은 수순이 필요하다.

    - 해당 텍스트 노드의 부모 노드를 선택한다. 텍스트 노드는 요소 노드의 자식이다.
    - firstChild 프로퍼티를 사용하여 텍스트 노드를 탐색한다.
    - 텍스트 노드의 유일한 프로퍼티(nodeValue)를 이용하여 텍스트를 취득한다.
    - nodeValue를 이용하여 텍스트를 수정한다.

- nodeValue
    - 노드의 값을 반환한다.
    - Return: 텍스트 노드의 경우는 문자열, 요소 노드의 경우 null 반환
    - IE6 이상의 브라우저에서 동작한다.
    - nodeName, nodeType을 통해 노드의 정보를 취득할 수 있다.
~~~javascript
// 해당 텍스트 노드의 부모 요소 노드를 선택한다.
const one = document.getElementById('one');
console.dir(one); // HTMLLIElement: li#one.red

// nodeName, nodeType을 통해 노드의 정보를 취득할 수 있다.
console.log(one.nodeName); // LI
console.log(one.nodeType); // 1: Element node

// firstChild 프로퍼티를 사용하여 텍스트 노드를 탐색한다.
const textNode = one.firstChild;

// nodeName, nodeType을 통해 노드의 정보를 취득할 수 있다.
console.log(textNode.nodeName); // #text
console.log(textNode.nodeType); // 3: Text node

// nodeValue 프로퍼티를 사용하여 노드의 값을 취득한다.
console.log(textNode.nodeValue); // Seoul

// nodeValue 프로퍼티를 이용하여 텍스트를 수정한다.
textNode.nodeValue = 'Pusan';
~~~

- className
    - class 어트리뷰트의 값을 취득 또는 변경한다. className 프로퍼티에 값을 할당하는 경우, class 어트리뷰트가 존재하지 않으면 class 어트리뷰트를 생성하고 지정된 값을 설정한다. class 어트리뷰트의 값이 여러 개일 경우, 공백으로 구분된 문자열이 반환되므로 String 메소드 split(' ')를 사용하여 배열로 변경하여 사용한다.
    - 모든 브라우저에서 동작한다.
- classList
    - add, remove, item, toggle, contains, replace 메소드를 제공한다.
     - IE10 이상의 브라우저에서 동작한다.
~~~javascript
const elems = document.querySelectorAll('li');

// className
[...elems].forEach(elem => {
  // class 어트리뷰트 값을 취득하여 확인
  if (elem.className === 'red') {
    // class 어트리뷰트 값을 변경한다.
    elem.className = 'blue';
  }
});

// classList
[...elems].forEach(elem => {
  // class 어트리뷰트 값 확인
  if (elem.classList.contains('blue')) {
    // class 어트리뷰트 값 변경한다.
    elem.classList.replace('blue', 'red');
  }
});
~~~

- id
    - id 어트리뷰트의 값을 취득 또는 변경한다. id 프로퍼티에 값을 할당하는 경우, id 어트리뷰트가 존재하지 않으면 id 어트리뷰트를 생성하고 지정된 값을 설정한다.
    - 모든 브라우저에서 동작한다.
~~~javascript
// h1 태그 요소 중 첫번째 요소를 취득
const heading = document.querySelector('h1');

console.dir(heading); // HTMLHeadingElement: h1
console.log(heading.firstChild.nodeValue); // Cities

// id 어트리뷰트의 값을 변경.
// id 어트리뷰트가 존재하지 않으면 id 어트리뷰트를 생성하고 지정된 값을 설정
heading.id = 'heading';
console.log(heading.id); // heading
~~~

- hasAttribute(attribute)
    - 지정한 어트리뷰트를 가지고 있는지 검사한다.
    - Return : Boolean
    - IE8 이상의 브라우저에서 동작한다.
- getAttribute(attribute)
    - 어트리뷰트의 값을 취득한다.
    - Return : 문자열
    - 모든 브라우저에서 동작한다.
- setAttribute(attribute, value)
    - 어트리뷰트와 어트리뷰트 값을 설정한다.
    - Return : undefined
    - 모든 브라우저에서 동작한다.
- removeAttribute(attribute)
    - 지정한 어트리뷰트를 제거한다.
    - Return : undefined
    - 모든 브라우저에서 동작한다.
~~~javascript
<!DOCTYPE html>
<html>
  <body>
  <input type="text">
  <script>
  const input = document.querySelector('input[type=text]');
  console.log(input);

  // value 어트리뷰트가 존재하지 않으면
  if (!input.hasAttribute('value')) {
    // value 어트리뷰트를 추가하고 값으로 'hello!'를 설정
    input.setAttribute('value', 'hello!');
  }

  // value 어트리뷰트 값을 취득
  console.log(input.getAttribute('value')); // hello!

  // value 어트리뷰트를 제거
  input.removeAttribute('value');

  // value 어트리뷰트의 존재를 확인
  console.log(input.hasAttribute('value')); // false
  </script>
  </body>
</html>
~~~
~~~javascript
<!DOCTYPE html>
<html>
<body>
  <input class="password" type="password" value="123">
  <button class="show">show</button>
  <script>
    const $password = document.querySelector('.password');
    const $show = document.querySelector('.show');

    function makeClickHandler() {
      let isShow = false;
      return function () {
        $password.setAttribute('type', isShow ? 'password' : 'text');
        isShow = !isShow;
        $show.innerHTML = isShow ? 'hide' : 'show';
      };
    }

    $show.onclick = makeClickHandler();
  </script>
</body>
</html>
~~~

#### HTML 콘텐츠 조작(Manipulation)
---
- textContent
    - 요소의 텍스트 콘텐츠를 취득 또는 변경한다. 이때 마크업은 무시된다. textContent를 통해 요소에 새로운 텍스트를 할당하면 텍스트를 변경할 수 있다. 이때 순수한 텍스트만 지정해야 하며 마크업을 포함시키면 문자열로 인식되어 그대로 출력된다.
    - IE9 이상의 브라우저에서 동작한다.
~~~javascript
<!DOCTYPE html>
<html>
  <head>
    <style>
      .red  { color: #ff0000; }
      .blue { color: #0000ff; }
    </style>
  </head>
  <body>
    <div>
      <h1>Cities</h1>
      <ul>
        <li id="one" class="red">Seoul</li>
        <li id="two" class="red">London</li>
        <li id="three" class="red">Newyork</li>
        <li id="four">Tokyo</li>
      </ul>
    </div>
    <script>
    const ul = document.querySelector('ul');

    // 요소의 텍스트 취득
    console.log(ul.textContent);
    /*
            Seoul
            London
            Newyork
            Tokyo
    */

    const one = document.getElementById('one');

    // 요소의 텍스트 취득
    console.log(one.textContent); // Seoul

    // 요소의 텍스트 변경
    one.textContent += ', Korea';

    console.log(one.textContent); // Seoul, Korea

    // 요소의 마크업이 포함된 콘텐츠 변경.
    one.textContent = '<h1>Heading</h1>';

    // 마크업이 문자열로 표시된다.
    console.log(one.textContent); // <h1>Heading</h1>
    </script>
  </body>
</html>
~~~
- innerText
    - innerText 프로퍼티를 사용하여도 요소의 텍스트 콘텐츠에만 접근할 수 있다. 하지만 아래의 이유로 사용하지 않는 것이 좋다.
비표준이다.
    - CSS에 순종적이다. 예를 들어 CSS에 의해 비표시(visibility: hidden;)로 지정되어 있다면 텍스트가 반환되지 않는다.
    - CSS를 고려해야 하므로 textContent 프로퍼티보다 느리다
- innerHTML
    - 해당 요소의 모든 자식 요소를 포함하는 모든 콘텐츠를 하나의 문자열로 취득할 수 있다. 이 문자열은 마크업을 포함한다.
~~~javascript
const ul = document.querySelector('ul');

// innerHTML 프로퍼티는 모든 자식 요소를 포함하는 모든 콘텐츠를 하나의 문자열로 취득할 수 있다. 이 문자열은 마크업을 포함한다.
console.log(ul.innerHTML);
// IE를 제외한 대부분의 브라우저들은 요소 사이의 공백 또는 줄바꿈 문자를 텍스트 노드로 취급한다
/*
        <li id="one" class="red">Seoul</li>
        <li id="two" class="red">London</li>
        <li id="three" class="red">Newyork</li>
        <li id="four">Tokyo</li>
*/
~~~
- innerHTML 프로퍼티를 사용하여 마크업이 포함된 새로운 콘텐츠를 지정하면 새로운 요소를 DOM에 추가할 수 있다.
~~~javascript
const one = document.getElementById('one');

// 마크업이 포함된 콘텐츠 취득
console.log(one.innerHTML); // Seoul

// 마크업이 포함된 콘텐츠 변경
one.innerHTML += '<em class="blue">, Korea</em>';

// 마크업이 포함된 콘텐츠 취득
console.log(one.innerHTML); // Seoul <em class="blue">, Korea</em>
~~~
- 위와 같이 마크업이 포함된 콘텐츠를 추가하는 것은 크로스 스크립팅 공격(XSS: Cross-Site Scripting Attacks)에 취약하다.
~~~javascript
// 크로스 스크립팅 공격 사례

// 스크립트 태그를 추가하여 자바스크립트가 실행되도록 한다.
// HTML5에서 innerHTML로 삽입된 <script> 코드는 실행되지 않는다.
// 크롬, 파이어폭스 등의 브라우저나 최신 브라우저 환경에서는 작동하지 않을 수도 있다.
elem.innerHTML = '<script>alert("XSS!")</script>';

// 에러 이벤트를 발생시켜 스크립트가 실행되도록 한다.
// 크롬에서도 실행된다!
elem.innerHTML = '<img src="#" onerror="alert(\'XSS\')">';
~~~

#### DOM 조작 방식
---
- innerHTML 프로퍼티를 사용하지 않고 새로운 콘텐츠를 추가할 수 있는 방법은 DOM을 직접 조작하는 것이다. 한 개의 요소를 추가하는 경우 사용한다. 이 방법은 다음의 수순에 따라 진행한다.

- 요소 노드 생성 createElement() 메소드를 사용하여 새로운 요소 노드를 생성한다. createElement() 메소드의 인자로 태그 이름을 전달한다.

- 텍스트 노드 생성 createTextNode() 메소드를 사용하여 새로운 텍스트 노드를 생성한다. 경우에 따라 생략될 수 있지만 생략하는 경우, 콘텐츠가 비어 있는 요소가 된다.

- 생성된 요소를 DOM에 추가 appendChild() 메소드를 사용하여 생성된 노드를 DOM tree에 추가한다. 또는 removeChild() 메소드를 사용하여 DOM tree에서 노드를 삭제할 수도 있다.

- createElement(tagName)
    - 태그이름을 인자로 전달하여 요소를 생성한다.
    - Return: HTMLElement를 상속받은 객체
    - 모든 브라우저에서 동작한다.
- createTextNode(text)
    - 텍스트를 인자로 전달하여 텍스트 노드를 생성한다.
    - Return: Text 객체
    - 모든 브라우저에서 동작한다.
- appendChild(Node)
    - 인자로 전달한 노드를 마지막 자식 요소로 DOM 트리에 추가한다.
    - Return: 추가한 노드
    - 모든 브라우저에서 동작한다.
- removeChild(Node)
    - 인자로 전달한 노드를 DOM 트리에 제거한다.
    - Return: 추가한 노드
    - 모든 브라우저에서 동작한다.
~~~javascript
// 태그이름을 인자로 전달하여 요소를 생성
const newElem = document.createElement('li');
// const newElem = document.createElement('<li>test</li>');
// Uncaught DOMException: Failed to execute 'createElement' on 'Document': The tag name provided ('<li>test</li>') is not a valid name.

// 텍스트 노드를 생성
const newText = document.createTextNode('Beijing');

// 텍스트 노드를 newElem 자식으로 DOM 트리에 추가
newElem.appendChild(newText);

const container = document.querySelector('ul');

// newElem을 container의 자식으로 DOM 트리에 추가. 마지막 요소로 추가된다.
container.appendChild(newElem);

const removeElem = document.getElementById('one');

// container의 자식인 removeElem 요소를 DOM 트리에 제거한다.
container.removeChild(removeElem);
~~~


#### insertAdjacentHTML()
- insertAdjacentHTML(position, string)
인자로 전달한 텍스트를 HTML로 파싱하고 그 결과로 생성된 노드를 DOM 트리의 지정된 위치에 삽입한다. 첫번째 인자는 삽입 위치, 두번째 인자는 삽입할 요소를 표현한 문자열이다. 첫번째 인자로 올 수 있는 값은 아래와 같다.
    - ‘beforebegin’
    - ‘afterbegin’
    - ‘beforeend’
    - ‘afterend’
- 모든 브라우저에서 동작한다.
~~~javascript
const one = document.getElementById('one');

// 마크업이 포함된 요소 추가
one.insertAdjacentHTML('beforeend', '<em class="blue">, Korea</em>');
~~~

### style
---
- style 프로퍼티를 사용하면 inline 스타일 선언을 생성한다. 특정 요소에 inline 스타일을 지정하는 경우 사용한다.
~~~javascript
const four = document.getElementById('four');

// inline 스타일 선언을 생성
four.style.color = 'blue';

// font-size와 같이 '-'으로 구분되는 프로퍼티는 카멜케이스로 변환하여 사용한다.
four.style.fontSize = '2em';
~~~
- style 프로퍼티의 값을 취득하려면 window.getComputedStyle을 사용한다. window.getComputedStyle 메소드는 인자로 주어진 요소의 모든 CSS 프로퍼티 값을 반환한다.

~~~html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>style 프로퍼티 값 취득</title>
  <style>
    .box {
      width: 100px;
      height: 50px;
      background-color: red;
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <div class="box"></div>
  <script>
    const box = document.querySelector('.box');

    const width = getStyle(box, 'width');
    const height = getStyle(box, 'height');
    const backgroundColor = getStyle(box, 'background-color');
    const border = getStyle(box, 'border');

    console.log('width: ' + width);
    console.log('height: ' + height);
    console.log('backgroundColor: ' + backgroundColor);
    console.log('border: ' + border);

    /**
     * 요소에 적용된 CSS 프로퍼티를 반환한다.
     * @param {HTTPElement} elem - 대상 요소 노드.
     * @param {string} prop - 대상 CSS 프로퍼티.
     * @returns {string} CSS 프로퍼티의 값.
     */
    function getStyle(elem, prop) {
      return window.getComputedStyle(elem, null).getPropertyValue(prop);
    }
  </script>
</body>
</html>
~~~

#### The Element Object
---

Property / Method	| Description 
---|---
accessKey|	Sets or returns the accesskey attribute of an element|
addEventListener()|	Attaches an event handler to an element|
appendChild()|	Adds (appends) a new child node to an element
attributes|	Returns a NamedNodeMap of an element's attributes
blur()|	Removes focus from an element
childElementCount|	Returns an elements's number of child elements
childNodes|	Returns a NodeList of an element's child nodes
children|	Returns an HTMLCollection of an element's child elements
classList|	Returns the class name(s) of an element
className|	Sets or returns the value of the class attribute of an element
click()|	Simulates a mouse-click on an element
clientHeight|	Returns the height of an element, including padding
clientLeft|	Returns the width of the left border of an element
clientTop|	Returns the width of the top border of an element
clientWidth|	Returns the width of an element, including padding
cloneNode()|	Clones an element
closest()|	Searches the DOM tree for the closest element that matches a CSS selector
compareDocumentPosition()|	Compares the document position of two elements
contains()|	Returns true if a node is a descendant of a node
contentEditable|	Sets or returns whether the content of an element is editable or not
dir|	Sets or returns the value of the dir attribute of an element
firstChild|	Returns the first child node of an element
firstElementChild|	Returns the first child element of an element
focus()|	Gives focus to an element
getAttribute()|	Returns the value of an element's attribute
getAttributeNode()|	Returns an attribute node
getBoundingClientRect()|	Returns the size of an element and its position relative to the viewport
getElementsByClassName()|	Returns a collection of child elements with a given class name
getElementsByTagName()|	Returns a collection of child elements with a given tag name
hasAttribute()|	Returns true if an element has a given attribute
hasAttributes()|	Returns true if an element has any attributes
hasChildNodes()| Returns true if an element has any child nodes
id|	Sets or returns the value of the id attribute of an element
innerHTML|	Sets or returns the content of an element
innerText|	Sets or returns the text content of a node and its descendants
insertAdjacentElement()|	Inserts a new HTML element at a position relative to an element
insertAdjacentHTML()|	Inserts an HTML formatted text at a position relative to an element
insertAdjacentText()|	Inserts text into a position relative to an element
insertBefore()|	Inserts a new child node before an existing child node
isContentEditable|	Returns true if an element's content is editable
isDefaultNamespace()|	Returns true if a given namespaceURI is the default
isEqualNode()|	Checks if two elements are equal
isSameNode()|	Checks if two elements are the same node
isSupported()|	Deprecated
lang|	Sets or returns the value of the lang attribute of an element
lastChild|	Returns the last child node of an element
lastElementChild|	Returns the last child element of an element
matches()|	Returns true if an element is matched by a given CSS selector
namespaceURI|	Returns the namespace URI of an element
nextSibling|	Returns the next node at the same node tree level
nextElementSibling|	Returns the next element at the same node tree level
nodeName|	Returns the name of a node
nodeType|	Returns the node type of a node
nodeValue|	Sets or returns the value of a node
normalize()|	Joins adjacent text nodes and removes empty text nodes in an element
offsetHeight|	Returns the height of an element, including padding, border and scrollbar
offsetWidth|	Returns the width of an element, including padding, border and scrollbar
offsetLeft|	Returns the horizontal offset position of an element
offsetParent|	Returns the offset container of an element
offsetTop|	Returns the vertical offset position of an element
outerHTML|	Sets or returns the content of an element (including the start tag and the end tag)
outerText|	Sets or returns the outer text content of a node and its descendants
ownerDocument|	Returns the root element (document object) for an element
parentNode|	Returns the parent node of an element
parentElement|	Returns the parent element node of an element
previousSibling|	Returns the previous node at the same node tree level
previousElementSibling|	Returns the previous element at the same node tree level
querySelector()|	Returns the first child element that matches a CSS selector(s)
querySelectorAll()|	Returns all child elements that matches a CSS selector(s)
remove()|	Removes an element from the DOM
removeAttribute()|	Removes an attribute from an element
removeAttributeNode()|	Removes an attribute node, and returns the removed node
removeChild()|	Removes a child node from an element
removeEventListener()|	Removes an event handler that has been attached with the addEventListener(|) method
replaceChild()|	Replaces a child node in an element
scrollHeight|	Returns the entire height of an element, including padding
scrollIntoView()|	Scrolls the an element into the visible area of the browser window
scrollLeft|	Sets or returns the number of pixels an element's content is scrolled horizontally
scrollTop|	Sets or returns the number of pixels an element's content is scrolled vertically
scrollWidth|	Returns the entire width of an element, including padding
setAttribute()|	Sets or changes an attribute's value
setAttributeNode()|	Sets or changes an attribute node
style|	Sets or returns the value of the style attribute of an element
tabIndex|	Sets or returns the value of the tabindex attribute of an element
tagName|	Returns the tag name of an element
textContent|	Sets or returns the textual content of a node and its descendants
title|	Sets or returns the value of the title attribute of an element
toString()|	Converts an element to a string