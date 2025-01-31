
### Filter
---
~~~java
import java.io.IOException;  
  
@Log  
@Component  
@WebFilter(urlPatterns = {"/board/main/*"})  
public class LoginFilter implements Filter {  
  
    @Override  
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {  
  
        log.info("......Login filter.....");  
  
        HttpServletRequest req = (HttpServletRequest)request;  
        HttpServletResponse res = (HttpServletResponse)response;  
  
        HttpSession session = req.getSession();  
  
        String requestURI = req.getRequestURI();  
        log.info("요청된 URI: " + requestURI);  
  
        // 🔹 정적 리소스는 필터 제외  
        if (requestURI.startsWith("/css/") || requestURI.startsWith("/js/") || requestURI.startsWith("/images/")) {  
            chain.doFilter(request, response);  
            return;  
        }  
  
        // 🔹 로그인 페이지 요청이면 필터 제외  
        if (requestURI.equals("/board/login")) {  
            chain.doFilter(request, response);  
            return;  
        }  
  
        if(session.getAttribute("loginInfo") == null) {  
            res.sendRedirect("/board/login");  
            return;  
        }  
  
        chain.doFilter(request, response);  
    }  
}
~~~

### Controller
---
~~~java
import org.hgtech.board.DTO.MemberDTO;  
import org.hgtech.board.service.MemberService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestParam;  

@Controller
@RequestMapping("/board")
@Log
public class LoginController {
  
    @Autowired
    MemberService service;
  
    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @PostMapping("/login")  
    public String login(@RequestParam String mbId, String mbPw, ServletRequest request) {
  
        log.info("...........login try.............");
  
        MemberDTO memberDTO = service.getByIdpw(mbId, mbPw);
        if (memberDTO == null) {
            return "loginError";
        }  
        HttpServletRequest req = (HttpServletRequest)request;
        HttpSession session = req.getSession();
//        30초간 세션 유지 (setAttribute 앞에 위치해야함)
        session.setMaxInactiveInterval(180);
        session.setAttribute("loginInfo", memberDTO);
        return "redirect:/board/main/list";
    }

  
	@PostMapping("/logout")
	public String logout(HttpServletRequest req) {
	    log.info("........logout........");
	    HttpSession session = req.getSession();
	    session.removeAttribute("logInfo");
	    session.invalidate();
	    return "login";
}
~~~

### html-javascript
---
- html
~~~html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <link rel="stylesheet" href="/css/style_login.css">  
    <link rel="preconnect" href="https://fonts.googleapis.com">  
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>  
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">  
    <title>Title</title>  
</head>  
<body>  
    <form class="bl_login">  
        <div class="bl_login_section">  
            <label class="bl_login_id" for="bl_login_id">ID</label>  
            <input id="bl_login_id" name="mbId" type="text" class="bl_login_id">  
        </div>        <div class="bl_login_section">  
            <label class="bl_login_pw" for="bl_login_id">PW</label>  
            <input id="bl_login_pw" name="mbPw" type="password" class="bl_login_id">  
        </div>        <div class="bl_login_btn_area">  
            <button id="loginBtn" type="button">Login</button>  
        </div>    </form></body>  
<script src="/js/login.js"></script>  
</html>
~~~

- javascript
~~~javascript
const bl_login = document.querySelector(".bl_login");  // form 태그이어야함
  
bl_login.addEventListener("click", (e) => {  
    e.preventDefault();  
    if (e.target.id === "loginBtn") {  
        const formData = new FormData(bl_login); // FormData 객체 생성  
  
        fetch("http://localhost:8080/board/login", {  
            method: "POST",  
            body: formData  
        })  
        .then(response => {  
            if (response.redirected) {  
                window.location.href = response.url; // 리다이렉트 URL로 이동(반드시 필요)
            }  
        })  
    }  
})
~~~