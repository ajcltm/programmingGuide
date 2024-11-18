- ArrayList
~~~
import java.util.List;

public List<String> list = new ArrayList<String>();

list.add(1)
list.add(2) # 요소 추가
list.get(list.size() -1); # 마지막 요소 반환
~~~

- 역순
~~~java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections; 
public class ReverseArrayList {public static void main(String[] args{         
    // 원본 배열        
    ArrayList<String> list = new ArrayList<>(Arrays.asList("H", "e", "l", "l", "o"));        
    System.out.println(list);  // [H, e, l, l, o]         
    // reverse        
    Collections.reverse(list);        
    System.out.println(list);  // [o, l, l, e, H]    }    
}
~~~

- clone
~~~java
import java.util.ArrayList; 

public class CloneArrayList {    
    public static void main(String[] args) {         
        // 1. ArrayList 준비        
        ArrayList<Fruit> fruitList = new ArrayList<Fruit>();
        fruitList.add(new Fruit("Apple", 1000));        
        fruitList.add(new Fruit("Banana", 2000));         
        // 2. ArrayList 복사 - clone()        
        ArrayList<Fruit> copyOfFruitList = (ArrayList<Fruit>) fruitList.clone();
~~~

~~~java
public static void main(String[] args) {
    // ... 중략 ...
    List<Card> copiedCardList = new ArrayList<>(cardList);    // cardList 복사
 
    System.out.println("cardList: " + getCardListStr(cardList));    // cardList 출력
    System.out.println("copiedCardList: " + getCardListStr(cardList));    // copiedCardList 출력
}
 
// 카드 리스트를 String으로 변환하여 반환
public static String getCardListStr(List<Card> cardList) {
    String str = "";
    for(Card card : cardList) {
        str += card.getCard() + " ";
    }
    return str;
}

~~~

- hashmap
~~~java
HashMap<Integer,String> map = new HashMap<>();//new에서 타입 파라미터 생략가능
map.put(1,"사과"); //값 추가
map.put(2,"바나나");
map.put(3,"포도");

HashMap<Integer,String> map = new HashMap<Integer,String>(){{//초기값 지정
    put(1,"사과");
    put(2,"바나나");
    put(3,"포도");
}};
map.remove(1); //key값 1 제거
map.clear(); //모든 값 제거
~~~