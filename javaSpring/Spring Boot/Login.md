
### Filter
---
~~~java
package org.hgtech.pnpsecure.filter;  
  
import jakarta.servlet.*;  
import jakarta.servlet.annotation.WebFilter;  
import jakarta.servlet.http.Cookie;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import jakarta.servlet.http.HttpSession;  
import lombok.extern.java.Log;  
import org.hgtech.pnpsecure.DTO.MemberDTO;  
import org.hgtech.pnpsecure.service.MemberService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Component;  
  
import java.io.IOException;  
  
@Log  
public class LoginFilter implements Filter {  
  
    private final MemberService service;  
  
    // 생성자 주입 방식 사용 (Autowired 제거)  
    public LoginFilter(MemberService service) {  
        this.service = service;  
    }  
  
    @Override  
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {  
  
        log.info("......Login filter.....");  
  
        HttpServletRequest req = (HttpServletRequest)request;  
        HttpServletResponse res = (HttpServletResponse)response;  
  
        HttpSession session = req.getSession();  
  
        String requestURI = req.getRequestURI();  
        log.info("요청된 URI: " + requestURI);  
  
        // 정적 리소스는 필터 제외  
        if (requestURI.startsWith("/css/") || requestURI.startsWith("/js/") || requestURI.startsWith("/images/")) {  
            chain.doFilter(request, response);  
            return;  
        }  
  
        // 로그인 페이지 요청이면 필터 제외  
        if (requestURI.equals("/pnpsecure/admin/login")) {  
            chain.doFilter(request, response);  
            return;  
        }  
  
        // 로그인에 성공한 session 소유하고 있으면 필터 통과  
        if(session.getAttribute("loginInfo") != null) {  
            chain.doFilter(request, response);  
            return;  
        }  
  
        Cookie[] cookies = req.getCookies();  
        Cookie cookie = findCookie(cookies, "rememberMe");  
  
        // 쿠키를 소유하고 있으면  
        if(cookie!=null) {  
            log.info("쿠키가 존재하는 상황");  
            try {  
                String uuid = cookie.getValue();  
                MemberDTO memberDTO = service.getByUUID(uuid);  
  
                // 유효한 uuid를 소유하고 있으면  
                if(memberDTO!=null) {  
                    session.setMaxInactiveInterval(10);  
                    session.setAttribute("loginInfo", memberDTO);  
                    chain.doFilter(request, response);  
                    return;  
                }  
  
                // 유효하지 못한 uuid 쿠키를 가지고 있으면  
                throw new Exception("Cookie value is not valid");  
            } catch (Exception e) {  
                e.printStackTrace();  
                res.sendRedirect("/pnpsecure/admin/login");  
            }  
        }  
  
        // 세션도 없고 쿠키도 없으면  
        res.sendRedirect("/pnpsecure/admin/login");  
        chain.doFilter(request, response);  
    }  
  
    public Cookie findCookie(Cookie[] cookies, String name) {  
        if (cookies != null) {  
            for (Cookie cookie : cookies) {  
                if (name.equals(cookie.getName())) {  
                    System.out.println("Cookie Found: " + cookie.getValue());  
                    return cookie;  
                }  
            }  
        }  
        return null;  
    }  
}
~~~

### Config
---
- filter는 스프링에 의해 관리되지 않아서 직접 bean 등록을 해야 이상한 에러를 방지할 수 있음

~~~java
package org.hgtech.pnpsecure.config;  
  
import org.hgtech.pnpsecure.filter.LoginFilter;  
import org.hgtech.pnpsecure.service.MemberService;  
import org.springframework.boot.web.servlet.FilterRegistrationBean;  
import org.springframework.context.annotation.Bean;  
import org.springframework.context.annotation.Configuration;  
  
@Configuration  
public class FilterConfig {  
  
    @Bean  
    public FilterRegistrationBean<LoginFilter> loggingFilter(MemberService memberService) {  
        FilterRegistrationBean<LoginFilter> registrationBean = new FilterRegistrationBean<>();  
        registrationBean.setFilter(new LoginFilter(memberService)); // 직접 주입  
        registrationBean.addUrlPatterns("/pnpsecure/admin/*"); // 명시적으로 URL 패턴 설정  
        return registrationBean;  
    }  
}
~~~

### Controller
---
~~~java
package org.hgtech.pnpsecure.controller;  
  
import jakarta.servlet.ServletRequest;  
import jakarta.servlet.ServletResponse;  
import jakarta.servlet.http.Cookie;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import jakarta.servlet.http.HttpSession;  
import lombok.extern.java.Log;  
import org.hgtech.pnpsecure.DTO.MemberDTO;  
import org.hgtech.pnpsecure.domain.MemberVO;  
import org.hgtech.pnpsecure.repository.MemberRepository;  
import org.hgtech.pnpsecure.service.MemberService;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.RequestParam;  
  
import java.util.UUID;  
  
@Log  
@Controller  
@RequestMapping("/pnpsecure/admin")  
public class AdminLogin {  
    @Autowired  
    MemberService service;  
  
    @GetMapping("/login")  
    public String login() {  
        return "login";  
    }  
  
    @PostMapping("/login")  
    public String login(@RequestParam String userId, String password, @RequestParam(required = false, defaultValue = "false") Boolean rememberMe, ServletRequest request, ServletResponse response) {  
  
        log.info("...........login try.............");  
  
        MemberDTO member = service.getByIdPw(userId, password);  
        if (member == null) {  
            return "loginError";  
        }  
        HttpServletRequest req = (HttpServletRequest)request;  
        HttpServletResponse res = (HttpServletResponse)response;  
  
        HttpSession session = req.getSession();  
//       서버측 session 유지 (setAttribute 앞에 위치해야함)  
        session.setMaxInactiveInterval(10);  
        session.setAttribute("loginInfo", member);  
  
        Cookie jsessionidCookie = new Cookie("JSESSIONID", session.getId());  
        jsessionidCookie.setMaxAge(10);  // 브라우저 쿠키 180초 후 만료  
        jsessionidCookie.setPath("/");   // 전체 도메인에서 적용  
        res.addCookie(jsessionidCookie);  
  
        if (rememberMe) {  
            String uuid = UUID.randomUUID().toString();  
            member.setUuid(uuid);  
            service.modify(member);  
            Cookie remember = new Cookie("rememberMe", uuid);  
            remember.setMaxAge(60);  // 브라우저 쿠키 180초 후 만료  
            remember.setPath("/");   // 전체 도메인에서 적용  
            res.addCookie(remember);  
        }  
  
        return "redirect:/pnpsecure/admin/main";  
    }  
  
    @PostMapping("/logout")  
    public String logout(HttpServletRequest req) {  
        log.info("........logout........");  
        HttpSession session = req.getSession();  
        session.removeAttribute("logInfo");  
        session.invalidate();  
        return "login";  
    }  
  
    @GetMapping("/main")  
    public String main() {  
        return "adminMain";  
    }  
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

### Converter
---
~~~java
package org.hgtech.pnpsecure.converter;  
  
import org.springframework.core.convert.converter.Converter;  
import org.springframework.stereotype.Component;  
  
@Component  
public class StringToBooleanConverter implements Converter<String, Boolean> {  
  
    @Override  
    public Boolean convert(String source) {  
        if (source == null) {  
            return false;  
        }  
        return source.equals("on");  
    };  
}
~~~