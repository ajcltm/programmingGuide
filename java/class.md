- 초기화
~~~
초기화 순서
클래스변수의 초기화 순서 : 기본값 - 명시적초기화 - 클래스 초기화 블럭
인스턴스변서의 초기화 순서 : 기본값 - 명시적초기화 - 인스턴스 초기화 블럭 - 생성자
~~~
~~~java
class Product {
    static int count = 0; // 클래스 멤버 변수 선언 및 초기화
    int seialNo; // 인스턴스 멤버 변수 선언
    String Name = "iphone"; // 인스턴스 멤버 변수 초기화(명시적 초기화)

    static {
        count = 1; // 클래스 초기화 블럭
    }

    {
        // 인스턴스 초기화 블럭
        ++count; 
        serialNo = count;
    }

    Product(){
        // 생성자
    }
}
~~~
