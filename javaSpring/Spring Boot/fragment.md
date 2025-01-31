### **fragment 정의**

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

### **fragment 사용 1**

- controller
~~~java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class FragmentController {

    @GetMapping("/example")
    public String examplePage(Model model) {
        model.addAttribute("message", "Hello from Controller!");
        return "main"; // main.html 반환
    }
}

~~~
- main.html
	- 사용 html 파일에서 사용하고자 하는 fragment 파일의 framgment id를 입력하면 됨
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

### **fragment 사용 2**

- controller
~~~java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class FragmentController {

    @GetMapping("/webinfo/list")
    public String getHeaderFragment(Model model) {
        model.addAttribute("title", "Dynamic Title");
        return "fragmentFileName :: fragmentId"; // fragmentFileName.html 파일의 fragmentId fragment 반환
    }
}
~~~
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
	    <div id=elementId></div>  
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
    loadFragment("/webinfo/list", "elementId");
});
~~~