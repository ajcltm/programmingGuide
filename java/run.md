- JDK(Java Development Kit) 설치
    - http://java.sun.com에서 JDK8.0 설치
- path 환경설정
    - bin 디렉토리(예: c:\jdk1.8\bin)를 path에 추가
- 실행파일
    - javac.exe : 자바 컴파일러, 자바소스코드를 바이트코드로 컴파일한다.
    ~~~cmd
    c:\jdk1.8\work > javac Hello.java
    ~~~
    - java.exe : 자바 인터프리터, 컴파일러가 생성한 바이트코드를 해석ㅎ하고 실행한다.
    ~~~cmd
    c:\jdk1.8\work > java Hello
    ~~~
    - jar.exe 압축프로그램, 클래스파일과 프로그램의 실행에 관련된 파일ㅇ르 하나의 jar파일(.jar)로 압축하거나 압축해제한다.
    ~~~cmd
    # 압축할때
    c:\jdk1.8\work > jar cvf Hello.jar Hello1.class Hello2.class

    # 압축풀때
    c:\jdk1.8\work > jar xvf Hello.jar
    ~~~

- Hello.java
    -  하나의 Java 어플리케이션에는 main메서드를 포함한 클래스가 반드시 하나는 있어야 한다.
~~~java
public class Hello {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}
~~~