#### 기본 설정
---
- HTML 문서 기본구성
~~~html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>여기에는 문서의 제목을 입력해주세요</title>
  </head>
  <body>
    여기에 웹페이지에 표시할 콘텐츠(태그)를 입력해주세요
  </body>
</html>
~~~

- css link
~~~html
<head>
    <link rel="stylesheet" href="css.css">
</head>
~~~

- font link
~~~html
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
</head>
~~~

- Font-Awesome link
~~~html
<head>
	<link
	    rel="stylesheet"
	    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
	/>
</head>
~~~

~~~css
p::after { 
content:'\f002'; /*유니코드 붙여넣기*/
font-family:"Font Awesome 5 Free"; /*폰트어썸 fas, far 글꼴 연결*/ 
font-weight:600; /*폰트어썸 굵기 Solid → 900, Regular, Brands → 400, Light → 300*/ 
}
~~~

- css 초기셋팅

~~~css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Noto Sans KR', sans-serif;
    border-collapse : collapse;
}
~~~

### layout
---
#### header
~~~html
<header class="ly_header">
	<div class="ly_header_inner">
	</div>
</header>
~~~

~~~css
.ly_header {
	padding-top: 20px;
	border-bottom: 1px solid #ddd;
}

.ly_header_inner {
	max-width: 1230px;
	padding-right: 15px;
	padding-left: 15px;
	margin-right: auto;
	margin-left: auto;
}
~~~

#### footer
~~~html
<footer>
	<div class="ly_footer">
		<div class="ly_footer_inner">
		</div>
	</div>
	<div class="ly_footer hp_btGray">
		<div class="ly_footer_inner">
			<small class="el_footerCopyright">2019 Triad Inc.</small>
		</div>
	</div>
</footer>
~~~

~~~css
.ly_footer {
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: #445069;
}

.ly_footer_inner {
    max-width: 1230;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
    text-align: center;
    color: #ddd;
}

.hp_btGray {
    border-top: 1px solid #777 !important;
}

.el_footerCopyright {
    color:#ddd;
}
~~~

#### main
~~~html
<div class="ly_cont ly_cont_col hp_ly_marginRight_pct_col1">
	<main class="ly_cont_main">
	</main>
	<aside class="ly_cont_side">
	</aside>
</div>
~~~

~~~css
.ly_cont{
	max-width: 1230px
	padding: 60px 15px;
	margin-right: auto;
	margin-left: auto;
}

.ly_cont.ly_cont_col {
	display: flex;
	justify-content: space-between;
}

.ly_cont_main {
	/* flex-grow : 1 */
	flex:1 ;
}

.hp_ly_marginRight_pct_col1 > * {
	margin-right: 3%;
}

.hp_ly_marginRight_pct_col1 > *:last-child {
	margin-right: 0;
}

.ly_cont_side {
	flex: 0 0 260px;
}

@media screen and (max-width: 768px) {
	.ly_cont.ly_cont_col{
		flex-direction: column;
	}
	.ly_cont_main {
		margin-right: 0;
		margin-bottom: 60px;
	}
}
~~~

- margin helper : px base
~~~css
.hp_ly_bottomMargin_px_s {
    margin-bottom: -10px;
}

.hp_ly_bottomMargin_px_s > * {
    margin-bottom: 10px;
}
~~~

- margin helper : percentage base
~~~css
.hp_ly_marginRight_pct_s > * {
    margin-right: 3.333%;
}

.hp_ly_marginRight_pct_s > *:last-child {
    margin-right: 0;
}
~~~

~~~css
.hp_ly_marginLeft_pct_s > * {
    margin-left: 3.333%;
}

.hp_ly_marginLeft_pct_s > *:last-child {
    margin-left: 0;
}
~~~

~~~css
.hp_ly_marginRight_pct_s_col3 > * {
    margin-right: 3.3333%;
}

.hp_ly_marginRight_pct_s_col3 > nth-of-type(3n) {
    margin-right: 0;
}
~~~

- margin helper : rem base
~~~css
.hp_ly_marginRight_rem_s > * {
    margin-right: .5rem;
}

.hp_ly_marginRight > *:last-child {
    margin-right: 0;
}
~~~

~~~css
.hp_ly_marginBottom_rem_s > * {
    margin-bottom: .5rem;
}

.hp_ly_marginBottom_rem_s > *:last-child {
    margin-bottom: 0;
}
~~~

### elements
---
#### section
~~~html
<section class="el_section hp_ly_marginBottom_rem_s">
	<p>
	Lorem ipsum dolor sit amet consectetur, adipisicing elit. Vero excepturi earum laborum voluptatum nobis harum omnis tenetur id porro sunt nemo, debitis quasi dolor soluta corrupti tempora, molestiae suscipit commodi? Lorem ipsum dolor sit amet, consectetur adipisicing elit. A voluptatibus sapiente laborum quae magnam tenetur eligendi aperiam, possimus reiciendis veniam quidem aliquam alias, beatae ex facere iure libero, est atque. Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime voluptas sunt aut? Cumque, mollitia accusamus. Veritatis unde recusandae minus
	</p>
	<p>
	Lorem ipsum dolor sit amet consectetur, adipisicing elit. Vero excepturi earum laborum voluptatum nobis harum omnis tenetur id porro sunt nemo, debitis quasi dolor soluta corrupti tempora, molestiae suscipit commodi? Lorem ipsum dolor sit amet, consectetur adipisicing elit. A voluptatibus sapiente laborum quae magnam tenetur eligendi aperiam, possimus reiciendis veniam quidem aliquam alias, beatae ex facere iure libero, est atque. Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime voluptas sunt aut? Cumque, mollitia accusamus. Veritatis unde recusandae minus
	</p>
</section>
~~~

~~~css
.el_section {
    padding: 15px;
}

.hp_ly_marginBottom_rem_s > * {
    margin-right: .5rem;
}

.hp_ly_marginBottom_rem_s > *:last-child {
    margin-right: 0;
}
~~~

#### basic button
~~~html
<a class="el_btn" href="#">버튼</a>
~~~

~~~css
.el_btn {
    display: inline-block;
    width: 300px;
    max-width: 100%;
    padding: 20px 10px;
    background-color: #252B48;
    border: 2px solid transparent;
    box-shadow: 0 3px 6px rgba(0, 0, 0, .16);
    color: #fff;
    font-size: 1.125rem;
    text-align: center;
    text-decoration: none;
    transition: .25s;
}

.el_btn:focus,
.el_btn:hover {
    background-color: #fff;
    border-color: currentColor;
    color: #252B48;
}
~~~

#### basic buttom + size
~~~html
<a class="el_btn hp_el_btn_small" href="#">버튼</a>
~~~

~~~css
.hp_el_btn_small {
    width: 150px;
    padding-top: 10px;
    padding-bottom: 10px;
    font-size: .9rem;
}
~~~

#### basic button + color
~~~html
<a class="el_btn hp_el_btn_bright" href="#">클릭</a>
~~~

~~~css
.hp_el_btn_bright {
    background-color: #5B9A8B;
    color: #fff;
}
.el_btn.hp_el_btn_bright:focus,
.el_btn.hp_el_btn_bright:hover {
    background-color: #fff;
    color: #5B9A8B;
}
~~~

#### basic button + rounded
~~~html
<a class="el_btn hp_el_btn_rounded" href="#">클릭</a>
~~~

~~~css
.hp_el_btn_rounded {
    border-radius: 10px;
}
~~~

#### arrow button
~~~html
<a class="el_btn el_btn_arrowRight" href="#">다음</a>
~~~

~~~css
.el_btn.el_btn_arrowRight {
    position: relative;
    padding-right: 2rem;
    padding-left: 1.38rem;
}

.el_btn.el_btn_arrowRight::after {
    content: '\f061';
    position :absolute;
    top: 50%;
    right: .83em;
    font-family: 'Font Awesome 5 Free';
    font-weight: 900;
    transform: translateY(-50%);
}
~~~

#### icon button
~~~html
<a class="el_beforeIconBtn el_beforeIconBtn_download" href="#">다운로드</a>
~~~

~~~css
.el_beforeIconBtn {
    position: relative;
    display: inline-block;
    padding: .2em .3em;
    border: 1px solid currentColor;
    color: #445069;
    text-decoration: none;
    transition: .25s;
}

.el_beforeIconBtn:focus,
.el_beforeIconBtn:hover{
    background-color: #445069;
    color: #fff;
}

.el_beforeIconBtn::before{
    display: inline-block;
    margin-right: .5em;
    font-family: 'Font Awesome 5 Free';
    font-weight: 900;
}

.el_beforeIconBtn_download::before {
    content: '\f019';
}
~~~

#### link button
~~~html
<a class="el_beforeIconLink el_beforeIconLink_pdf" href="#">파일이름.pdf</a>
~~~

~~~css
.el_beforeIconLink::before {
    display: inline-block;
    margin-right: .3em;
    color: #252B48;
    font-family: 'Font Awesome 5 Free';
    font-weight: 400;
}

.el_beforeIconLink_pdf::before {
    content: '\f1c1';
}
~~~

~~~html
<a class="el_beforeIconLink el_beforeIconLink_chevLeft" href="#">되돌아가기</a>
~~~

~~~css
.el_beforeIconLink::before {
    display: inline-block;
    margin-right: .3em;
    color: #252B48;
    font-family: 'Font Awesome 5 Free';
    font-weight: 400;
}

.el_beforeIconLink_chevLeft::before {
    content: '';
    width: .375em;
    height: .375em;
    border-bottom: .125em solid #445069;
    border-left: .125em solid #445069;
    transform: rotate(45deg) translateY(-30%);
}
~~~

#### label
~~~html
<span class="el_label hp_el_label_lv2Color hp_el_label_rounded">업데이트 예정</span>
~~~

~~~css
.el_label {
    display: inline-block;
    padding: .2em .3em;
    background-color: #F7E987;
    color: #252B48;
    font-size: .75rem;
    font-weight: bold;
}

.hp_el_label_bright {
    background-color: #5B9A8B;
    color: #fff;
}

.hp_el_label_rounded {
    padding: .3em .9em;
    border-radius: 1em;
}
~~~

#### heading level 1
~~~html
<h1 class="el_lv1Heading">
	<span>최신 글 목록</span>
</h1>
~~~

~~~css
.el_lv1Heading {
    padding: 30px 10px;
    background-color: #252B48;
    color: #fff;
    font-size: 1.75rem;
    text-align: center;
}

.el_lv1Heading > span {
    position: relative;
    display: inline-block;
    transform: translateY(-20%);
}

.el_lv1Heading > span::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    width: 80px;
    height: 1px;
    background-color: currentColor;
    transform: translateX(-50%);
}
~~~

#### heading level 2
~~~html
<h2 class="el_lv2Heading">첫번째 글 제목</h2>
~~~

~~~css
.el_lv2Heading {
    padding-bottom: 10px;
    border-bottom: 2px solid #445069;
    font-size: 1.25rem;
    font-weight: bold;
}
~~~

#### heading level 3
~~~html
<h2 class="el_lv3Heading">최신기사</h2>
~~~

~~~css
.el_lv3Heading {
    padding-left: 6px;
    border-left: 2px solid #5B9A8B;
    font-size: 1.25rem;
    font-weight: bold;
}
~~~

#### heading level 4
~~~html
<h4 class="el_lv4Heading">소제목 2</h4>
~~~

~~~css
.el_lv4Heading {
    padding-left: 6px;
    border-left: 2px solid #5B9A8B;
    font-size: 1.1rem;
    font-weight: bold;
}
~~~

#### caution (주석)
~~~html
<p class="el_caution">※ 이 부분은 아주 중요한 주석입니다.</p>
~~~

~~~css
.el_caution {
    color: #445069;
    font-size: .95rem;
    font-weight: bold;
}
~~~

### block
---
#### media
~~~html
<div class="bl_media hp_ly_marginRight_pct_s">
	<figure class="bl_media_imgWrapper">
		<img src="assets/img/images1.jpg" alt="#">
	</figure>
	<div class="bl_media_body hp_ly_bottomMargin">
		<h3 class="bl_media_ttl">미디어 타이미디어 타이틀</h3>
		<div class="bl_media_txt">
			Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit magni ratione vero et dolorem nisi, rem voluptatibus quod! Commodi beatae maxime aliquid tempora vel explicabo perspiciatis iure, consectetur aliquam id?
		</div>
	</div>
</div>
~~~

~~~css
.bl_media {
    display: flex;
    align-items: flex-start;
}

.bl_media_imgWrapper {
    flex: 0 1 27%;
}

.bl_media_imgWrapper > img {
    width: 100%;
}

.bl_media_body {
    flex: 1;
}

.bl_media_ttl {
    font-size: 1.125rem;
    font-weight: bold;
}

.hp_ly_marginRight_pct_s > * {
    margin-right: 3.333%;
}

.hp_ly_marginRight_pct_s > *:last-child {
    margin-right: 0;
}

@media screen and (max-width: 760px) {
    .bl_media {
        display: block;
    }

    .bl_media > * {
        margin-right: 0;
        text-align: left;
    }

    .bl_media_imgWrapper {
        margin-bottom: 10px;
    }
}
~~~

#### media reversed
~~~html
<div class="bl_media hp_ly_row_reverse hp_ly_marginLeft_pct_s">
	<figure class="bl_media_imgWrapper">
		<img src="assets/img/images1.jpg" alt="#">
	</figure>
	<div class="bl_media_body hp_ly_bottomMargin">
		<h3 class="bl_media_ttl">미디어 타이미디어 타이틀</h3>
		<div class="bl_media_txt">
			Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit magni ratione vero et dolorem nisi, rem voluptatibus quod! Commodi beatae maxime aliquid tempora vel explicabo perspiciatis iure, consectetur aliquam id?
		</div>
	</div>
</div>
~~~

~~~css
.bl_media {
    display: flex;
    align-items: flex-start;
}

.hp_ly_row_reverse {
    flex-direction: row-reverse;
}

.hp_ly_marginLeft_pct_s > * {
    margin-left: 3.333%;
}

.hp_ly_marginLeft_pct_s > *:last-child {
    margin-left: 0;
}

.bl_media_imgWrapper {
    flex: 0 1 27%;
}

.bl_media_imgWrapper > img {
    width: 100%;
}

.bl_media_body {
    flex: 1;
}

.hp_ly_row_reverse .bl_media_body{
    text-align: right;
}

.bl_media_ttl {
    font-size: 1.125rem;
    font-weight: bold;
}

@media screen and (max-width: 760px) {
    .bl_media {
        display: block;
    }

    .bl_media > * {
        margin-left: 0;
        text-align: left;
    }

    .bl_media_imgWrapper {
        margin-bottom: 10px;
    }
}
~~~

#### card
~~~html
<a class="bl_card hp_ly_bottomMargin">
	<figure class="bl_card_imgWrapper">
		<img src="assets/img/images4.jpg" alt="#">
	</figure>
	<div class="bl_card_body hp_ly_bottomMargin">
		<h3 class="bl_card_ttl">웹사이트 구축</h3>
		<p class="bl_card_txt">사용자에게 최고의 체험을 제공하는 크리에이티브와 테크놀로지를 만들어 드립니다.</p>
	</div>
</a>
~~~

~~~css
.bl_card {
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16);
}

.bl_card_imgWrapper {
    position: relative;
    padding-top: 56.25%;
    overflow: hidden;
}

.bl_card_imgWrapper > img {
    position: absolute;
    top: 50%;
    width: 100%;
    transform: translateY(-50%);
}

.bl_card_body {
    padding: 15px;
}

.bl_card_ttl {
    font-size: 1.125rem;
    font-weight: bold;
}

.bl_card_txt {
    color: #445069;
}

a.bl_card {
    display: block;
    color: currentColor;
    text-decoration: none;
    transition: .25s;
}

a.bl_card .bl_card_ttl,
a.bl_card .bl_card_txt {
    transition: .25s;
}

a.bl_card:focus,
a.bl_card:hover {
    opacity: .75;
}

a.bl_card:focus .bl_card_ttl,
a.bl_card:focus .bl_card_txt,
a.bl_card:hover .bl_card_ttl,
a.bl_card:hover .bl_card_txt {
    color: #252B48;
    text-decoration: underline;
}
~~~

#### card badge
~~~html
<a class="bl_card hp_ly_bottomMargin">
	<b class="bl_card_badge">
		<span class="bl_card_badge_txt">New</span>
	</b>
	<figure class="bl_card_imgWrapper">
		<img src="assets/img/images4.jpg" alt="#">
	</figure>
	<div class="bl_card_body hp_ly_bottomMargin">
		<h3 class="bl_card_ttl">웹사이트 구축</h3>
		<p class="bl_card_txt">사용자에게 최고의 체험을 제공하는 크리에이티브와 테크놀로지를 만들어 드립니다.</p>
	</div>
</a>
~~~

~~~css

/* basic card 생략 */

.bl_card_badge {
    position: relative;
}

.bl_card_badge::after {
    content: "";
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    border-width: 3.75rem 3.75rem 0 0;
    border-style: solid;
    border-color: #F7E987 transparent transparent transparent;
}

.bl_card_badge_txt {
    position: absolute;
    z-index: 2;
    top: .5rem;
    left: .3125rem;
    color: #252B48;
    font-size: .875rem;
    font-weight: bold;
    transform: rotate(-45deg);
}
~~~

#### card unit
~~~html
                <div class="bl_cardUnit bl_cardUnit_col hp_ly_marginRight_pct_s_col3 hp_ly_marginBottom_px_s">
                    <a class="bl_card hp_ly_bottomMargin">
                        <b class="bl_card_badge">
                            <span class="bl_card_badge_txt">New</span>
                        </b>
                        <figure class="bl_card_imgWrapper">
                            <img src="assets/img/images4.jpg" alt="#">
                        </figure>
                        <div class="bl_card_body hp_ly_bottomMargin">
                            <h3 class="bl_card_ttl">웹사이트 구축</h3>
                            <p class="bl_card_txt">사용자에게 최고의 체험을 제공하는 크리에이티브와 테크놀로지를 만들어 드립니다.</p>
                        </div>
                    </a>
                    /* bl_card 반복 생략 */
                </div>
~~~

~~~css
.bl_cardUnit {
    display: flex;
    flex-wrap: wrap;
}

.hp_ly_marginRight_pct_s_col3 > * {
    margin-right: 3.333%;
}

.hp_ly_marginRight_pct_s_col3 > *:nth-of-type(3n) {
    margin-right: 0;
}

.hp_ly_bottomMargin_px_s {
    margin-bottom: -10px;
}

.hp_ly_bottomMargin_px_s > * {
    margin-bottom: 10px;
}

.bl_cardUnit_col > .bl_card {
    width: 30.7%;
}

@media screen and (max-width: 768px) {
    .bl_cardUnit > .bl_card {
        width: 100%;
    }
    .bl_cardUnit.hp_ly_marginRight_pct_s_col3 > * {
        margin-right: 0;
    }
}
~~~

#### horizontal table
~~~html
<div class="bl_horizTable bl_horizTable_mdScroll">
	<table>
		<tbody>
			<tr>
				<th>이름</th>
				<td>김동이</td>
			</tr>
			<tr>
				<th>생년월일</th>
				<td>2011-9-29</td>
			</tr>
			<tr>
				<th>취미</th>
				<td>산책, 맛있는거 먹기</td>
			</tr>
			<tr>
				<th>성격</th>
				<td>착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고 착하고</td>
			</tr>
		</tbody>
	</table>
</div>
~~~

~~~css
.bl_horizTable {
    border: 1px solid #445069;
}

.bl_horizTable table {
    width: 100%;
    font-size: .8rem;
    border-collapse: collapse;
}

.bl_horizTable th {
    width: 20%;
    padding: 10px;
    background-color: #445069;
    border-bottom: 1px solid #252B48;
    font-weight: bold;
    vertical-align: middle;
    color: #ddd;
}

.bl_horizTable td {
    padding: 10px;
    border-bottom: 1px solid #252B48;
}

.bl_horizTable tr:last-child th,
.bl_horizTable tr:last-child td {
    border-bottom-width: 0;
}

@media screen and (max-width: 768px) {
    .bl_horizTable_mdScroll {
        border-right-width: 0;
        overflow-x: auto;
    }

    .bl_horizTable_mdScroll th,
    .bl_horizTable_mdScroll td {
        white-space: nowrap;
    }

    .bl_horizTable_mdScroll td {
        border-right: 1px solid #252B48;
    }
}
~~~

#### vertical table
~~~html
<div class="bl_vertTable">
	<table>
		<thead>
			<tr>
				<th>이름</th>
				<th>소속</th>
				<th>직종</th>
				<th>특기 분야</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>김동이</td>
				<td>동호회</td>
				<td>개콤</td>
				<td>사람 행동 분석(일명 눈치코치) 외출과 집지키는 시간을 정확히 구분한다</td>
			</tr>
		</tbody>
	</table>
</div>
~~~

~~~css
.bl_vertTable {
    border: 1px solid #252B48;
}

.bl_vertTable table {
    width: 100%;
    text-align: center;
    table-layout: fixed;
    font-size: .8rem;
    border-collapse: collapse;
}

.bl_vertTable thead tr {
    background-color: #445069;
}

.bl_vertTable th {
    padding: 10px;
    border-right: 1px solid #252B48;
    border-bottom: 1px solid #252B48;
    font-weight: bold;
    vertical-align: middle;
    color: #ddd;
}

.bl_vertTable td {
    padding: 10px;
    border-right: 1px solid #252B48;
    border-bottom: 1px solid #252B48;
    vertical-align: middle;
}

.bl_vertTable th:last-child,
.bl_vertTable td:last-child {
    border-right-width: 0;
}

.bl_vertTable tr:last-child td{
    border-bottom-width: 0;
}

@media screen and (max-width: 768px){
    .bl_vertTable {
        border-right: 0;
        overflow-x: auto;
    }
    .bl_vertTable table {
        width: auto;
        min-width: 100%;
    }
    .bl_vertTable th,
    .bl_vertTable td {
        white-space: nowrap;
    }
    .bl_vertTable th:last-child,
    .bl_vertTable td:last-child {
        border-right-width: 1px;
    }
 }
~~~

#### cross table
~~~html
<div class="bl_crossTable">
	<table>
		<thead>
			<tr>
				<th class="bl_crossTable_mdSticky">이름</th>
				<th>소속</th>
				<th>직종</th>
				<th>특기분야</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<th class="bl_crossTable_mdSticky">홍길동</th>
				<td class="crossTable_text">주식회사 제이펍 / 주식회사 효광</td>
				<td class="crossTable_text">테크니컬 디렉터</td>
				<td class="crossTable_text">설계</td>
			</tr>
			<tr>
				<th class="bl_crossTable_mdSticky">홍길동</th>
				<td class="crossTable_text">주식회서 제이펍</td>
				<td class="crossTable_text">테크니컬 디렉터</td>
				<td class="crossTable_text">설계</td>
			</tr>
			<tr>
				<th class="bl_crossTable_mdSticky">홍길동</th>
				<td class="crossTable_text">주식회서 제이펍</td>
				<td class="crossTable_text">테크니컬 디렉터</td>
				<td class="crossTable_text">설계</td>
			</tr>
		</tbody>
	</table>
</div>
~~~

~~~css
 .bl_crossTable {
    border: 1px solid #445069;
 }

 .bl_crossTable table{
    width: 100%;
    text-align: center;
    table-layout: fixed;
 }

 .bl_crossTable th{
    padding: 10px;
    background-color: #445069;
    border-right: 1px solid #252B48;
    border-bottom: 1px solid #252B48;
    font-weight: bold;
    vertical-align: middle;
    color: #ddd;
 }

 .bl_crossTable td {
    padding: 15px;
    border-right: 1px solid #252B48;
    border-bottom: 1px solid #252B48;
    vertical-align: middle;
 }

 .bl_crossTable th:last-child,
 .bl_crossTable td:last-child{
    border-right-width: 0;
 }

 .bl_crossTable tbody tr:last-child th,
 .bl_crossTable tbody tr:last-child td{
    border-bottom-width: 0;
 }

 @media screen and (max-width: 768px) {
    .bl_crossTable {
        border-right-width: 0;
        overflow-x:auto;
    }
    .bl_crossTable table{
        width: auto;
        min-width: 100%;
    }
    .bl_crossTable th,
    .bl_crossTable td {
        white-space: nowrap;
    }
    .bl_crossTable th:last-child,
    .bl_crossTable td:last-child {
        border-right-width: 1px;
    }
    .bl_crossTable_mdSticky{
        position: -webkit-sticky;
        position: sticky;
        left: 0;
    }
 }
~~~

#### navtab
~~~html
<nav clas="bl_tabNav">
	<ul class="bl_tabNav_inner">
		<li>
			<a class="bl_tabNav_link is_active">계약 및 절차 소개</a>
		</li>
		<li>
			<a class="bl_tabNav_link" href="#">제품 소개</a>
		</li>
		<li>
			<a class="bl_tabNav_link" href="#">캠페인 소개</a>
		</li>
		<li>
			<a class="bl_tabNav_link" href="#">회원 기능 소개</a>
		</li>
		<li>
			<a class="bl_tabNav_link" href="#">각종 절차 소개</a>
		</li>
	</ul>
</nav>
~~~

~~~css
.bl_tabNav_inner {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: -10px;
    list-style-type: none;
}

.bl_tabNav_link {
    display: inline-block;
    padding-right: 30px;
    padding-bottom: 10px;
    padding-left: 30px;
    margin-bottom: 10px;
    border-bottom: 4px solid #efefef;
    color:#777;
    text-decoration: none;
    transition: .25s;
}

.bl_tabNav_link:focus,
.bl_tabNav_link:hover {
    border-bottom-color: currentColor;
    color: #252B48;
    opacity: .75;
}

.bl_tabNav_link.is_active {
    border-bottom-color: currentColor;
    color: #252B48;
    pointer-events: none;
}

@media screen and (max-width: 750px) {
    .bl_tabNav {
        overflow-x: auto;
    }
    .bl_tabNav_inner {
        flex-wrap: nowrap;
        justify-content: flex-start;
        margin-bottom: 0;
        white-space: nowrap;
    }
}
~~~


### dropdown memu
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
### login form
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

### background image

~~~html
<div class="background">  
    <div class="content">  
        <h1>Hello! WebDev System</h1>  
        <button><a href="/webinfo/main">Start</a></button>  
    </div>
</div>
~~~

~~~css
.background {  
    position: relative;  
    width: 100%;  
    height: 100vh;  
    background-image: url('/images/nature.jpg');  
    background-repeat: no-repeat;  
    background-position: center;  
    background-size: cover;  
    z-index: 1;  
}  
  
.background::before {  
    content: "";  
    position: absolute;  
    width: 100%;  
    height: 100vh;  
    background: rgba(0,0,0,.6);  
    z-index: 2;  
}
~~~

### Modal
---
~~~html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Modal Example</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Trigger Button -->
  <button id="openModalBtn">Open Modal</button>

  <!-- The Modal -->
  <div id="myModal" class="modal">
    <!-- Modal Content -->
    <div class="modal-content">
      <span class="close">&times;</span>
      <h2>Modal Header</h2>
      <p>This is a simple modal example.</p>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>

~~~

~~~css
/* styles.css */
body {
  font-family: Arial, sans-serif;
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: 15% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

/* Close Button */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

~~~

~~~javascript
// script.js
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("openModalBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
~~~

### Slider
---
- html
~~~html
<div class="bl_slider">
	<div class="bl_slider_mvleft"><</div>
	<div class="bl_slider_track">
		<div class="bl_slider_item">a</div>
		<div class="bl_slider_item">b</div>
		<div class="bl_slider_item">c</div>
	</div>
	<div class="bl_slider_mvright">></div>
</div>
~~~

- css
~~~css
.bl_slider {
    position: relative;
    width: 300px;
    height: 300px;
}

.bl_slider_mvleft {
    position: absolute;
    top: 50%;
    left: 5%;
    width: 20px;
    height: 20px;
    transform: translateY(-50%);
    z-index: 2;
}

.bl_slider_mvright {
    position: absolute;
    top: 50%;
    width: 20px;
    height: 20px;
    right: 5%;
    transform: translateY(-50%);
    z-index: 2;
}

.bl_slider_track {
    height: 100%;
    display: flex;
}

.bl_slider_track > * {
    flex: 0 0 300px;
}
~~~

- javascript
~~~javascript
const track = document.querySelector('.bl_slider_track');
const slides = document.querySelectorAll('.bl_slider_item');
const prevButton = document.querySelector('.bl_slider_mvleft');
console.log(prevButton);
const nextButton = document.querySelector('.bl_slider_mvright');
console.log(nextButton);

const slideCount = slides.length;
let currentIndex = 0;

// 클론 슬라이드 추가
const firstClone = slides[0].cloneNode(true);
const lastClone = slides[slideCount - 1].cloneNode(true);
track.appendChild(firstClone); // 맨 뒤에 첫 슬라이드 복사
track.insertBefore(lastClone, slides[0]); // 맨 앞에 마지막 슬라이드 복사

// 초기 위치 설정
const slideWidth = slides[0].offsetWidth;
track.style.transform = `translateX(-${slideWidth}px)`;

function moveToSlide(index) {
    track.style.transition = 'transform 0.5s ease';
    track.style.transform = `translateX(-${(index + 1) * slideWidth}px)`;
    currentIndex = index;

    // 무한 루프 처리
    track.addEventListener('transitionend', () => {
    if (currentIndex === slideCount) {
        track.style.transition = 'none';
        track.style.transform = `translateX(-${slideWidth}px)`;
        currentIndex = 0;
    }
    if (currentIndex === -1) {
        track.style.transition = 'none';
        track.style.transform = `translateX(-${slideCount * slideWidth}px)`;
        currentIndex = slideCount - 1;
    }
    });
}

function addEventListner_mvbtn() {
    prevButton.addEventListener('click', () => {
        console.log("click mvleft")
        if (currentIndex > -1) {
        moveToSlide(currentIndex - 1);
        }
    });

    // 버튼 이벤트 핸들러
    nextButton.addEventListener('click', () => {
        if (currentIndex < slideCount) {
        moveToSlide(currentIndex + 1);
        }
    });
}

addEventListner_mvbtn();
~~~
