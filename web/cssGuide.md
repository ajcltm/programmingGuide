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