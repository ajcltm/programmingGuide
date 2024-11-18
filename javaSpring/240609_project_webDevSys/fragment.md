- fragment 정의
~~~html
<!DOCTYPE html>  
<html xmlns:th="http://www.thymeleaf.org">  
<head>  
    <meta charset="UTF-8">
    <title>Title</title>  
</head>  
<body>  
    <div class="webinfolist-container" th:fragment="fragmentId">
</div>
</body>  
</html>
~~~

- fragment 사용 1 (공통 컨트롤러 사용)
~~~html
<!DOCTYPE html>  
<html xmlns:th="http://www.thymeleaf.org">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
    <header>       
    </header>    
    <main>        
	    <div th:replace="fragmentFileName :: fragmentId"></div>  
    </main>    
    <footer>
    </footer>    
</body>  
</html>
~~~

- fragment 사용 2 (다른 컨트롤러 사용)
~~~html
<!DOCTYPE html>  
<html xmlns:th="http://www.thymeleaf.org">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
    <header>       
    </header>    
    <main>        
	    <div id=fragmentId></div>  
    </main>    
    <footer>
    </footer>    
</body>  
</html>
~~~
~~~javascript
document.addEventListener("DOMContentLoaded", function() {  
    function loadFragment(url, elementId) {  
        fetch(url)  
            .then(response => {  
                if (!response.ok) {  
                    throw new Error('Network response was not ok');  
                }  
                return response.text();  
            })  
            .then(data => {  
                document.getElementById(elementId).innerHTML = data;  
            })  
            .catch(error => {  
                console.error('There was a problem with the fetch operation:', error);  
            });  
    }
    loadFragment("/webinfo/list", "fragmentId");
});
~~~