	#### 네임스페이스 설정
---

~~~html
<!-- src/main/resources/templates/index.html -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Thymeleaf Example</title>
    <link rel="stylesheet" type="text/css" th:href="@{/css/styles.css}">
</head>
<body>
    <h1>Welcome to Thymeleaf</h1>
    <p th:text="${message}">This is a message.</p>
    <script type="text/javascript" th:src="@{/js/scripts.js}"></script>
</body>
</html>
~~~

#### 텍스트 입력
---

~~~html
<p th:text="${message}">This is a sample message.</p>
~~~

#### 속성 입력
---

~~~html
<a th:href="@{/path}">Link</a>
<a th:href="@{/user/{id}(id=${userId})}">User Profile</a>
<img th:src="@{/images/logo.png}" alt="Logo">
~~~

#### 조건부 렌더링
---

~~~html
<p th:if="${user.loggedIn}">Welcome, <span th:text="${user.name}">User</span>!</p>
<p th:unless="${user.loggedIn}">Please log in.</p>
~~~

#### 반복처리
---

~~~html
<ul>
    <li th:each="item : ${items}" th:text="${item}">Item</li>
</ul>
~~~

#### fragment 처리
---

~~~html
<!-- fragment.html -->
<div th:fragment="header">
    <h1>Header Content</h1>
</div>

<!-- main.html -->
<div th:include="fragment :: header"></div>
~~~

