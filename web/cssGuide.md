### **reset**
---
- 터미널 창에 npm i styled-reset 를 입력하여 모듈 설치
~~~tsx
import { Reset} from 'styled-reset';
~~~

### **units**
---
- px : 픽셀(화소) 단위. 22인치 LCD 모니터의 경우 해상도가 1680*1050인데 이것은 가로 1680개의 픽셀, 세로에 1050개의 픽셀을 가짐
- % : 백분율의 상대 단위. 요소에 지정된 size(상속되었거나 디폴트값)에 상대적인 size를 설정함
- em: 요소 글꼴 크기의 배수
- rem: root 요소 글꼴 크기의 배수
- vw: viewport 너비의 1%
- vh: viewport 높이의 1%

### **box model**
---
- 구성요소 : 모든 box는 안쪽부터 content, padding, border, margin으로 구성됨
- 종류 : 박스의 크기를 측정하는 기준에 따라 content-box와 border-box로 구분하며, 기본값으로 content-box가 적용됨
~~~css
box-item1 {
    box-sizing: content-box;
}
/* content-box는 기본 css box 크기 결정법을 사용. 요소의 너비를 100 픽셀로 설정하면 content영역이 100 픽셀 너비를 가지고, 테두리와 안쪽 여백은 이에 더해짐 */

box-item2 {
    box-sizing: border-box;
}
/* border-box는 테두리와 안쪽 여백의 크기도 요소의 크기로 고려함. 너비를 100 픽셀로 설정하고 테두리와 안쪽 여백을 추가하면, content 영역이 줄어들어 총 너비 100 픽셀을 유지함. 대부분의 경우 이 편이 크기를 조절할 때 쉬움 */


* {
    box-sizing: border-box;
}
/* 보통의 경우 이렇게 모든 box에 적용해두는 편이 좋음 */
~~~ 

### **margin**
---
- 정렬
~~~css
.container {
    margin: 0 auto;
    /* 위 아래는 0이고 좌우는 균등하게 주어 중앙에 정렬 */
}

.container {
    margin-right: auto;
    /* 오른쪽에 가능한 많은 margin이 놓여서 왼쪽 정렬됨. 오른쪽에 item이 있다면 맨 오른쪽으로 밀려나서 그 item은 오른쪽 정렬이 되어 버림 */

~~~

### **gap**
---
- 인접한 요소가 있을 때만 갭(gap)을 만듬. margin의 경우 인접한 요소들의 존재 여부와 상관없이 항상 스타일이 적용됨. 하지만 gap은 인접한 요소가 없다면 불필요한 공간을 만들지 않음
~~~css
.main-head-wraper {
    display: flex;
    height: 100%;
    width: 100%;
    border: 2px solid #61DAFB;
    align-items: baseline;
    padding: .5rem;
    gap: 1rem;
}
~~~

### **display**
---
- block : item 순서대로 아래 방향으로 쌓임
- inline : item 순서대로 오른쪽 방향으로 쌓이며, box size는 content 크기만큼만 적용됨
- inline-block : item 순서대로 오른쪽 방향으로 쌍이며, box size는 기본 box 형태가 됨

~~~css
span {
    width: 100px;
    height: 100px;
    padding: 5px;
}

span.block {
    display: block;
}

span.inline {
    display: inline;
}

span.inline-block {
    display: iblibe-block;
}
~~~

### **position**
- static <br> 요소를 일반적인 문서 흐름에 따라 배치. top, left, right, bottom, z-index 속성이 아무런 영향도 주지 않음
~~~css
/* 기본값임 */
.item {
    position: static;  
}
~~~
- relative <br> 요소를 일반적인 문서 흐름에 따라 배치하고, 자기 자신을 기준으로 top, right, bottom, left의 값에 따라 오프셋을 적용함. 오프셋은 다른 요소에는 영향을 주지 않음. 따라서 페이지 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음. z-index의 값이 auto가 아니라면 새로운 쌓임 맥락을 생성함
~~~css
.item {
    position: relative;  
}
~~~
- absolute <br> 요소를 일반적인 문서 흐름에서 제거하고, 페이지 레이아웃에 공간도 배정하지 않음. 대신 가장 가까운 위치 지정 부모 요소에 대해 상대적으로 배치함. 단, 부모 중 위치 지정 요소가 없다면 초기 컨테이닝 블록을 기준으로 함. 최종 위치는 top, right, bottom, left 값이 지정함. z-index의 값이 auto가 아니라면 새로운 쌓임 맥락을 생성함. 절대 위치 지정 요소의 바깥 여백은 새로 상쇄되지 않음
대부분의 경우, height와 width가 auto로 지정된 absolute 위치 지정 요소는 자신의 컨텐츠에 맞춰 크기가 바뀜. 하지만 top, bottom, left, right를 지정하면 사용 가능한 공간을 가득 채움
~~~css
.item {
    position: absolute;  
}
~~~
- fixed <br> 요소를 일반적인 문서 흐름에서 제거하고, 페이지 레이아웃 공간에도 배정하지 않음. 대신 뷰포트의 초기 컨테이닝 블록을 기준으로 삼아 배치함. 단, 요소의 부모 중 하나가 transfrom, perspective, filter 속성 중 어느 하나라도 none이 아니라면 뷰포트 대신 그 부모를 컨테이닝 블록으로 함. 최종 위치는 top, right, bottom, left 값이 지정함. 새로운 쌓임 맥락을 생성함. 문서를 인쇄할 때는 해당 요소가 모든 페이지의 같은 위치에 출력됨
~~~css
.item {
    position: fixed;  
}
~~~
- sticky <br> 요소를 일반적인 문서 흐름에 따라 배치하고, 테이블 관련 요소를 포함해 가장 가까운, 스크롤 되는 조상과, 표 관련 요소를 포함한 컨테이닝 블록을 기준으로 top, right, bottom, left의 값에 따라 오프셋을 적용함 => 틀고정 기능이라고 생각하면 쉬움
~~~html
<dl>
    <div>
        <dt>A</dt>
        <dd>Andere W.k.</dd>
        <dd>Apparat</dd>
        <dd>Arcade Fire</dd>
    </div>
    <div>
        <dt>C</dt>
        <dd>Chromeo</dd>
        <dd>Common</dd>
        <dd>Converge</dd>
    </div>
    <div>
        <dt>E</dt>
        <dd>Explosions In The Sky</dd>
    </div>
    <div>
        <dt>T</dt>
        <dd>Ted Leo &amp; The Pharmacists</dd>
        <dd>T-Pain</dd>
        <dd>Thrice</dd>
    </div>
</dl>
~~~
~~~css
* {
    box-sizing: border-box;
}

dl > div {
    background: #FFF;
    padding: 24px 0 0 0;
}

dt {
    background: #B8C1C8;
    border-bottom: 1px solid #989EA4;
    border-top: 1px solid #717D85;
    color: #FFF;
    font: bold 18px/21px Helvetica, Arial, sans-serif;
    margin: 0;
    padding: -webkit-sticky;
    position: sticky;
    top: -1px;
}

dd {
    font: bold 20px/45px Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 0 0 0 12px;
    white-space: nowrap;
}

dd + dd {
    border-top: 1px solid #CCC;
}
~~~

### **float**
---
- 기본적인 문서 배치의 흐름에서 벗어나 요서의 모서리가 페이지의 왼쪽이나 오른쪽으로 이동하는 것을 말함
- 중요한 사실은 플로팅된 요소는 그 요소의 종류에 상관없이 block-box가 된다는 점임. inline 요소인 링크를 플로팅 시키는 경우에 이 요소 특성은 블럭 박스로 변경되고 마치 div인 것 처럼 동작함
- 대신 자신의 영역만을 가지고 있는 inline-block처럼 렌더링되는 것이 특이한 점
~~~css
.item {
    float: left;
}
/* 기본값은 none이며, 옵션은 left, right, none */
~~~
- 플로팅한 요소는 문서의 흐름상에서 벗어난 상태이기 때문에 레이아웃을 무너뜨리게 되며(자식요소가 부모요소를 벗어님), 이를 해결하려면 float를 해제시켜야함
- 해제시키는 방법은 부모 요소에 after 가상 엘리먼트 적용
~~~css
ul {
    padding: 15px 20px;
}
ul:after {
    content:'';
    display:block;
    clear:both;
}
ul > li{
    float: left;
}
~~~

### **white-space**
---

- white-space는 스페이스와 탭, 줄바꿈, 자동줄바꿈을 어떻게 처리할지 정하는 속성. 기본값은 normal임

|구분|스페이스와 탭 처리|엔터 처리|자동줄바꿈 유무|
|-|-|-|-|
|nornal|병합|병합|Y|
|nowrap|병합|병합|X|
|pre|보존|보존|X|
|pre-wrap|보존|보존|Y|
|pre-line|병합|보존|Y|

(병합 예를 들어 연속된 두개의 스페이스를 한개의 스페이스로 처리한다는 의미이고, 보존은 2개의 스페이스로 처리한다는 의미)
<br><br><br>
~~~css
.item {
    white-space : nowrap;
}
~~~

### **Grid**
---
- 2 * 6 grid 적용
~~~css
/*css file*/ 
.container {
    display: grid;
    grid-template-columns: 100px auto 100px; /*3 columns, 가운데 크기는 auto*/ 
    grid-template-rows: 50px 50px; /* 2 rows */ 
    grid-gap: 3px;
}
~~~
~~~html
<!--html file--> 
<html>
    <head></head>
    <body>
        <div class='container'>
            <div>item1</div>
            <div>item2</div>
            <div>item3</div>
            <div>item4</div>
            <div>item5</div>
            <div>item6</div>
        </div>
    </body>
</html>
~~~
- fraction unit & repeat
~~~css
/*css file*/ 
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 1fr 1fr 1fr 과 동일*/ 
    grid-template-rows: repeat(2, 50px); /* 50px 50px 와 동일 */ 
    grid-gap: 3px;
}
~~~

- basic layout
~~~css
.container {
    height: 100%;
    display: grid;
    grid-gap: 3px;
    grid-template: 40px auto 40px / repeat(12, 1fr);
}

.header {
    grid-column: 1 / -1; /* grid-column 1 / span 12 와 동일 */
}

.menu {
    grid-row: 2 / 3; /* grid-column 1 / span 12 와 동일 */
}

.content {
    grid-column: 2 / -1; /* grid-column 1 / span 12 와 동일 */
}

.footer {
    grid-column: 1 / -1; /* grid-column 1 / span 12 와 동일 */
}
~~~

~~~html
<!--html file-->
<html>
    <head></head>
    <body>
        <div class='container'>
            <div class='header'>header</div>
            <div class='menu'>menu</div>
            <div class='content'>content</div>
            <div class='footer'>footer</div>
        </div>
    </body>
</html>
~~~
- basic layout + grid-template-areas
~~~css
.container {
    height: 100%;
    display: grid;
    grid-gap: 3px;
    grid-template: 40px auto 40px / repeat(12, 1fr);
    grid-template-areas:
        "h h h h h h h h h h h ."  /*. 은 여백*/
        "m c c c c c c c c c c ."
        "f f f f f f f f f f f ."
}

.header {
    grid-area: h
}

.menu {
    grid-row: m
}

.content {
    grid-column: c
}

.footer {
    grid-column: f
}
~~~

~~~html
<!--html file-->
<html>
    <head></head>
    <body>
        <div class='container'>
            <div class='header'>header</div>
            <div class='menu'>menu</div>
            <div class='content'>content</div>
            <div class='footer'>footer</div>
        </div>
    </body>
</html>
~~~

- auto-fit & minmax() & grid-auto-rows
~~~css
.container {
    display: grid;
    grid-gap: 3px;
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); /*컬럼 갯수 자동으로 창의 크기에 따라 자동 설정, item의 크기가 100px를 넘을때 컬럼으로 추가되고, 크기는 모두 동일하게 유지*/
    grid-auto-rows: 100px; /* 행의 갯수 자동으로 설정, 크기는 항상 100px*/
}
~~~

- 크기가 다양한 사진 앨범 자동 배열
~~~css
.container {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); 
    grid-auto-rows: 75px;
    grid-auto-flow: dense; /*빈공간에 알맞는 크기의 item을 자동으로 위치시켜줌*/
}

.horizontal {
    grid-column: span 2;
}

.vertical {
    grid-row: span 2;
}

.big {
    grid-column: span 2;
    grid-row: span 2;
}
~~~
~~~html
<!--html file-->
<html>
    <head></head>
    <body>
        <div class="container">
            <div><img src="img/normal1.jpg"/></div>
            <div class="horizontal"><img src="img/horizontal1.jpg"/></div>
            <div class="vertical"><img src="img/vertical1.jpg"/></div>
            <div class="big"><img src="img/big1.jpg"/></div>
            <div class="horizontal"><img src="img/horizontal2.jpg"/></div>
            <div><img src="img/normal2.jpg"/></div>
            <div><img src="img/normal3.jpg"/></div>
            <div class="vertical"><img src="img/vertical2.jpg"/></div>
            <div><img src="img/normal4.jpg"/></div>
        </div>
    </body>
</html>
~~~

- 좌우상하 정렬
~~~css
.container {
    display: grid;
    grid-gap: 3px;
    grid-template-columns: repeat(3, 1900px);
    grid-template-rows: repeat(2, 100px);
    justify-content: center; /* 좌우 정렬; start(왼쪽정렬), end(오른쪽 정렬), center(가운데 정렬), space-between(양끝으로 최대한 벌림), space-around(적당히 가운데 간격율 두면서 정렬), space-evenly(똑같은 간격으로 가운데 정렬) */
    align-content: center; /* 상하 가운데 정렬; option은 위와 동일 */
}
~~~

### **flex**
---
#### **flex container**
---
- flex : flex-box 속성을 적용한다.  
~~~css
.flex-container {
    display: flex;
}
~~~
- inline-flex : flex-container가 inline 요소인 경우 inline-flex를 지정한다.  
~~~css
.flex-container {
    display: inline-flex;
}
~~~
- flex-direction : flex-item을 배치하는 방향(주축)을 결정  
row, row-reverse, column, column-reverse
~~~css
.flex-container {
    flex-direction: column;
}
~~~
- flex-wrap : flex-container의 width보다 flex-item들의 width의 합계가 더 큰 경우, 한줄로 표현할 것인지, 여루줄로 표현할 것인지를 지정  
nowrap으로 지정하면, flex-item을 개행하지 않고 1행에 배치하며, 각 flex-item의 폭은 flex-container에 들어갈 수 있는 크기로 축소됨 (기본값임), 하지만 flex-item의 크기가 한계를 넘어 축소되면 item의 배치가 flex-container를 넘어가는 일이 발생하는 데, 이때 overflow를 auto로 지정하면 스크롤이 생기며 container를 넘지 않게 됨
~~~css
.flex-container {
    display: flex;
    flex-wrap: nowrap;
    overflow: auto;
}
~~~
- justify-content : flex-container의 주축을 기준으로 flex-item을 정렬  
center, start, end, flex-start, flex-end, left, right, space-around, space-between, space-evenly
~~~css
.flex-container {
    display: flex;
    justify-content: space-around;
}
~~~
- align-items : flex-container의 교차축을 기준으로 flex-item을 정렬   
normal, stretch, center, start, end, flex-start, flex-end, baseline, first baseline, last baseline, safe center, unsafe center ...
~~~css
.flex-container {
    display: flex;
    align-items: stretch;
}
~~~
- align-content : flex-container의 교착축을 기준으로 주축을 정렬  
center, start, end, flex-start, flex-end, space-between, space-around, space-evenly, strecth, normal, baseline, first baseline, last baseline, safe center, unsafe center ...
~~~css
.flex-container {
    display: flex;
    align-content: space-between;
}
~~~
- flex-grow : 0이면 flex-container의 크기가 켜저도 flex-item의 크기가 커지지 않고 유지됨. 1 이상이면 flex-item의 원래 크기에 상관없이 flex-container를 채우도록 flex-item의 크기가 커짐
- flex-shrink : 0이면 flex-container의 크기가 flex-item의 크기보다 작아져도 flex-item의 크기가 줄어들지 않고 원래 크기로 유지됨. 1 이상이면 flex-container의 크기가 줄어들때 함께 줄어듬
- flex-basis : flex-item으 기본 크기를 결정하는 속성. 기본값은 auto이며, item 안의 content 크기에 따라 자동으로 결정됨. width 처럼 단위값을 입력하면 해당 크기만큼의 크기를 가지지만 content의 크기와 상관없이 강제적으로 크기를 결정하는 width와 달리 유연하게 크기가 조절됨. 0px 로 설정하면 절대 크기가 되어 container에 맞쳐서 크기가 결정됨
- flex 키워드로 설정하면 flex-grow, flex-shrink, flex-basis를 한꺼번에 설정할 수 있음

  |flex|flex-grow|flex-shrink|flex-basis|
  |-|-|-|-|
  |initial(기본값)|0|1|auto|
  |none|0|0|auto|
  |auto|1|1|auto|
  |양의 정수|숫자|1|0|


- 스크롤 없는 100% 레이아웃
~~~css
.flex-container {
    display: flex;
    flex-direction: column;
    height: 100%;
}

.flex-item {
    flex: 1; /* flex: 1 1 0 과 동일*/
    overflow: auto;
}
~~~

- 내비게이션 영역
~~~css
.flex-container {
    display: flex;
}

.flex-item {
    flex: none;  /* flex: 0 0 auto */
}

.flex-item-gnb {
    margin-left: auto; /* 이 아이템만 bar의 오른쪽에 위치*/
}
~~~

- 브라우저 화면 아래에 붙는 footer
~~~css
.flex-container {
    display: flex;
}

.flex-item {
    margin-top: auto;
}
~~~

- 폼 레이블 수직 중앙 정렬
~~~css
.flex-container {
    display: flex;
    align-items: center;
}
~~~

- 유동 너비 박스
~~~css
.flex-container {
    display: flex;
}

.flex-item {
    /* flex: initial or flex: 0 1 auto */
    max-width: 300px;
}
~~~

- 말줄임과 아이콘
~~~css
.flex-container {
    display: inline-flex;
    max-width: 100%;
}

.text {
    /* flex: initial or flex: 0 1 auto */
    text-overflow: ellipsis;
    white-space: nowrap;
}
~~~
- 가로세로 비율을 유지하는 반응형 박스
~~~css
.flex-container {
    display: flex;
    flex-wrap: wrap;
}

.flex-item0-list {
    flex-basis: 33.3%;
    display: flex;
    flex-direction: column;
}

.flex-item-image {()
    flex: auto;
    /* flex: 1 1 auto */
}
~~~
### **background**
---

~~~css
.background-div {
    width: 100%;
    height: 240px;
    background-color: #eee;
    background-image: url(../img/sample.jpg);
    background-position: center; /* 200px 200px 처럼 값을 넣을 수 있음 */
    background-size: 50%; /* contain (세로나 가로 사이즈를 채우고 나머지는 repeat)| cover(무조건 꽉차게함) */
    background-repeat: no-repeat;
}
~~~
~~~css
.background-div {
    background: #004fff url(../img/sample.jpg) no-repeat center/cover;
    /* background-color url background-repeat background-position/background-size */
}
~~~


### **hover / box-shadow / transform**
~~~css
button {
    width: 120px;
    height: 40px;
    background-color: #004fff;
    border: none;
    color: white;
    box-shadow: 0 4px 16px rgba(0, 79, 255, 0.3);  /* x y blur spread color */
    font-size: 16px;
    font-weight: bold;
    border-radius: 20px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); /* x-position y-position 만큼 이동 */
    transition: 0.3s;
}

button: focus {
    ouline: 0%;
}

button:hover {
    background-color: rgba(0,79,255, 0.9)
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0, 79, 255, 0.6); /* x y blur spread color */
}
~~~

### **dropdown memu**
---
~~~html
<!-- html -->
<div className="dropdown">
    <button className="link"> about </button>
    <div className="dropdown-menu">
        Dropdown Content
    </div>
</div>
~~~
~~~css
/* css */
.dropdown {
    position: relative;
    margin-right: auto;
    height: 100%;
}

.link {
    margin: 0px;
    padding: 0px;
    color: white;
    font-size: 1.25rem;
    font-weight: bold;
    height: 100%;
    background-color: inherit;
    cursor: pointer;
}

.link:hover {
    transform: scale(1.05);
    color: #61DAFB;
    transition: .3s;
}

.dropdown-menu {
    position: absolute;
    color: white;
    font-size: 1.1rem;
    left: 0;
    top: calc(100%+.25rem);
    background-color: inherit;
    border-radius: .25rem;
    box-shadow: 5px 5px 5px 0 rgba(0,0,0,.5);
    opacity: 0;
    pointer-events: none;
    transform: translateY(-10px);
    transition: opacity 150ms ease-in-out, transform 150ms ease-in-out;
    z-index: -1;
}

.dropdown > .link:focus + .dropdown-menu {
    opacity: 1;
    transform: translateY(0px);
    pointer-events: auto;
}
~~~
### **login form**
---
~~~html
<!-- html -->
<form className="login-containder">
    <label className="login-label">ID</label>
    <input type='text' placeholder="id" className="login-input" />
    <label className="login-label">Password</label>
    <input type='text' placeholder="password" className="login-input" />
    <input type="submit" value="login" className="login-submit"/>
</form>
~~~
~~~css
.login-containder {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: absolute;
    color: white;
    font-size: 1.1rem;
    left: 0;
    top: calc(100%+.25rem);
    background-color: #2d2d2d;
    border-radius: .25rem;
    box-shadow: 5px 5px 5px 0 rgba(0,0,0,.5);
    opacity: 0;
    pointer-events: none;
    transform: translateY(-10px);
    transition: opacity 150ms ease-in-out, transform 150ms ease-in-out;
    z-index: -1;
}

.login-label {
    align-self: flex-start;
    margin-left: 10px;
    color: white;
    font-weight: bold;
}

.login-input {
    margin: 5px;
    margin-left: 10px;
    margin-right: 10px;
    padding: 5px;
}

.login-submit {
    align-self: stretch;
    background-color: #171a27;
    color: white;
    font-weight: bold;
    margin: 5px;
    padding: 5px;
    height: 2.2rem;
}
~~~