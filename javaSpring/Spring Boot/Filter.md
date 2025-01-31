~~~java
import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.FilterConfig;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.annotation.WebFilter;
import java.io.IOException;
import java.time.LocalDateTime;

@WebFilter(urlPatterns = "/*") // 모든 요청을 가로챔
public class LoggingFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("📌 LoggingFilter 초기화됨");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("📌 요청이 필터를 통과함: " + LocalDateTime.now());
        
        // 다음 필터 또는 컨트롤러로 요청을 전달
        chain.doFilter(request, response);
        
        System.out.println("📌 응답이 필터를 통과함: " + LocalDateTime.now());
    }

    @Override
    public void destroy() {
        System.out.println("📌 LoggingFilter 종료됨");
    }
}

~~~
