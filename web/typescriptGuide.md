### 기본 타입
---
- number, boolean, string , array
~~~typescript
let age: number = 30;
let isAdult:boolean = True;
let a:number[] = [1,2,3];
let a2:Array<number>  = [1,2,3];
let wee1:string[] = ['mon', 'tue', 'wed']
~~~

- tuple
~~~typescript
// 튜플
let b:[string, number];
b = ['z',1];
~~~

- void
~~~typescript
//void, never

function sayHello():void {
    console.log('Hello')    
}
~~~

- never : 항상 error를 반환하거나, 영원히 끝나지 않는 함수 정의
~~~typescript
function showError():never{
    throw new Error();
}

fuction infLoop():never{
    while (true) {
        // do
    }
}
~~~
- eum
~~~typescript
enum Os {
    Window, 
    Ios, 
    Android
}

enum Os {
    Window = 3, 
    Ios, // = 4
    Android // = 5


enum Os {
    Window = 3, 
    Ios = 10, 
    Android // = 11

console.log(Os[10])  // "Ios"
console.log(Os['Ios'])  // "10"


let myOs : Os;
myOs = Os.Window
~~~

- null, undefined
~~~typescript
let a:null = null;
let b:undefined = undefined;
~~~


### Interface
---
~~~typescript
type Score = 'A'|'B'|'C'|'D'|'F' ;

interface User {
    name : string;
    age : number;
    gender? : stirng; // 정의하지 않아도 됨
    readonly birthYear: number ; // 수정할 수 없음
    [grade:number] : Score; // key가 number인 grade가 되고 value가 type이 Scroe로 입력 정의 (정의할 key, value 의 숫자가 확정적이지 않을때 사용)
}

let use : User = {
    name: 'xx',
    age: 30
    1 : 'A',
    2 : 'B' // 계속 추가 할 수 있음
}
~~~

- 함수 정의
~~~typescript
interface Add {
    (num1:number, num2:number) : number;
}

const add : Add = function(x, y) {
    return x+y;
}

add(10, 20); // 30 리턴

interface IsAdult {
    (age:number) : boolean;
}

const a:IsAdult = (age) => {
    return age>19;
}

a(30) // true 리턴
~~~

- 클래스 정의
~~~typescript
interface Car {
    color: string;
    wheels: number;
    start(): void;
}

class Bmw implements Car {
    color;
    wheels = 4;
    constructor(c:string){
        this.color = c;
    }
    start(){
        console.log('go...');
    }
}

const b = new Bmw('green');
console.log(b)
// Bmw: {
//     "wheels":4,
//     "color": grren
// }

~~~

- 확장
~~~typescript
interface Benz extends Car {
    door: number;
    stop(): void;
}

const benz : Benz = {
    door:5,
    stop(){
        console.log('stop');
    },
    color: 'black',
    wheels: 4,
    start(){
    }
}
~~~
~~~typescript
// 두 인터페이스를 동시에 확장

interface Car {
    color: string;
    wheels: number;
    start(): void;
}


interface Toy {
    name: string;
}

interface ToyCar extends Car, Toy {
    price : number;
}
~~~

### 함수
---
~~~typescript
function hello(name?:string) {
    return `Hello, ${name||"world"}`;
}

const result = hello(); // "Hello World"
const result2 = hello("Sam") // Hello Sam"

// 위와 동일한 함수
function hello(name='world') {
    return `Hello, ${name}`;
}

// 아래는 잘못된 정의 -> optional한 매개변수는 뒤에 정의해야함
function hello(age?:number, name:string):string {
    if (age !== undefined) {
        return `Hello, ${name}. You are ${age}.`;
    } else {
        return `Hello, ${name}`;
    }
}

// 아래는 가능
function hello(age:number|undefined, name:string):string {
    if (age !== undefined) {
        return `Hello, ${name}. You are ${age}.`;
    } else {
        return `Hello, ${name}`;
    }
}

console.log(hello(undefined, "Sam"));
~~~

- 나머지 매개변수 : 파이썬의 *arg 와 동일
~~~typescript
function add(...nums: number[]) {
    return nums.reduce((result, num)=> result+num, 0);
}

add(1, 2, 3); // 6
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10); // 55

// [참고] reduce 함수
// const array1 = [1,2,3,4];
// const initialValue = 0;
// const sumWithInitial = array1.reduce(
//     (previousValue, currentValue) => previousValue + currentValue, initialValue
// );
// console.log(sumWithInitial) // expected output: 10
~~~

~~~typescript
interface User {
    name: string;
}

const Sam: User = {name:'Sam'}

function showName(this:User, age:number, gender:'m'|'f'){
    console.log(this.name);
}

a(30, 'm') // this 다음의 매개변수부터 입력해야함 (python의 self와 비슷)
~~~

- 오버로드 : 매개변수의 타입에 따라서 다른 타입을 반환할때 함수 위에 해당 경우에 해당하는 함수를 오버로드하여 정의
~~~typescript
interface User {
    name:string;
    age: number;
}

function join(name: string, age: string): string; // age가 string이면 string을 반환
function join(name: string, age: number): User; // ager가 number이면 User를 반환
function join(name: string, age: number |string): User | string {
    if (typeof age ==="number") {
        return {
            name,
            age
        };
    } else {
        return "나이는 숫자로 입력해주세요.";
    }
}

const sam: User = join("Sam", 30);
const jane: string = join("Jane", "30");
~~~

### Literal Types
~~~typescript
const userName1 = "Bob";
let userName2 = string | number = "Tom"
useName2 = 3;

type Job = "police" | "developer" | "teacher";

interface User {
    name: string;
    job: Job;
}

const user: User {
    name: "Bob",
    job: "developer"
}
~~~

### 클래스
---
~~~typescript
class Car {
    color: string; 
    constructor(color:string) {
        this.color = color;
    }
    start() {
        console.log('start')
    }
}

// 멤버 변수를 적지 않고 사용하려면 아래와 같이함
// constructor의 매개 변수를 public 또는 readonly 로 선언해주면됨

class Car {
    constructor(public color:string) {
        this.color = color;
    }
    start() {
        console.log('start')
    }
}

const bnw = new Car("red")
~~~

- public : 아무것도 선언하지 않으면 public으로 간주됨
~~~typescript
class Car {
    public name : string = "car";
    color: string;
    constructor(color: string) {
        this.color = color;
    }
    start() {
        console.log("start");
    }
}

class Bmw extends Car {
    constructor(color: string) {
        super(color);
    }
    showName() {
        console.log(super.name);  // 자식 클래스에서 사용 가능
    }
}

const z4 = new Bmw("black");
~~~

- private : 외부와 자식 클래스에서 사용이 불가능함. 앞에 # 을 붙여도 됨
~~~typescript
class Car {
    #name : string = "car"; // private name : string  과 같이 표기 가능
    color: string;
    constructor(color: string) {
        this.color = color;
    }
    start() {
        console.log("start");
        console.log(this.#name); // 사용은 가능
    }
}

class Bmw extends Car {
    constructor(color: string) {
        super(color);
    }
    showName() {
        console.log(super.#name); // 자식 클래스에서는 사용 불가능  
    }
}

const z4 = new Bmw("black");
~~~

- protected : 자식 클래스에서 사용가능하지만, 클래스 인스턴스로는 사용 불가
~~~typescript
class Car {
    protected name : string = "car"; 
    color: string;
    constructor(color: string) {
        this.color = color;
    }
    start() {
        console.log("start");
        console.log(this.name); // 사용 가능
    }
}

class Bmw extends Car {
    constructor(color: string) {
        super(color);
    }
    showName() {
        console.log(super.name); // 자식 클래스에서도 사용 가능  
    }
}

const z4 = new Bmw("black");
console.log(z4.name); // 클래스 인스턴스로는 사용 불가
~~~

- static : 정적 변수로 클래스 그 자체의 상태변수임
~~~typescript
class Car {
    protected name : string = "car"; 
    color: string;
    static wheels = 4;
    constructor(color: string) {
        this.color = color;
    }
    start() {
        console.log("start");
        console.log(this.name);
        console.log(Car.wheels); // 클래스 이름으로 접근해야함
    }
}

class Bmw extends Car {
    constructor(color: string) {
        super(color);
    }
    showName() {
        console.log(super.name); 
    }
}

const z4 = new Bmw("black");
console.log(Car.wheels);  // 클래스 이름으로 접근해야함
~~~


- readonly일때 변수 내용을 변경하는 방법
~~~typescript
class Car {
    readonly name : string = "car"; 
    color: string;
    constructor(color: string, name:string) {
        this.color = color;
        this.name = name;
    }
    start() {
        console.log("start");
        console.log(this.name); 
    }
}

class Bmw extends Car {
    constructor(color: string, name: string) {
        super(color, name);
    }
    showName() {
        console.log(super.name);   
    }
}

const z4 = new Bmw("black", "zzzz4"); // name이 "car" 에서 "zzzz4"로 변경
console.log(z4.name); 
~~~

- 추상 클래스
~~~typescript
abstract class Car {
    color: string;
    constructor(color:string) {
        this.color = color;
    }
    start() {
        console.log("start");
    }
    abstract doSomething(): void;
}

const car = new Car("red") // 에러가 발생함. 추상클래스는 new를 선언할 수 없음

class Bmw extends Car {
    constructor(color: string) {
        super(color);
    }
    doSomething(){
        alert(3);
    }
}
~~~

### 제네릭 타입 정의
---
~~~typescript
function getSize<T>(arr:T[]) :number {
    return arr.length;
}

const arr1 = [1,2,3];
getSize<number>(arr1)
const arr2 = ['a','b','c'];
getSize<string>(arr2)
const arr3 = [false, true, true];
getSize<boolean>(arr3)
~~~

~~~typescript
interface Mobile<T> {
    name: string;
    price: number;
    option: T;
}

const n1:Mobile<{color:string;, coupon: boolean}> = {
    name: "s21",
    price: 1000,
    option: {
        color: "red",
        coupon: false
    }
}

const n2:Mobile<{string}> = {
    name: "s21",
    price: 1000,
    option: "good",
}
~~~

- extends를 활용한 generic 표현 
~~~typescript
interface User {
    name: string;
    age: number;
}

interface Car {
    name: string;
    color: string;
}

interface Book {
    price: number;
}

const user: User = { name: 'a', age: 10};
const car: Car = { name:'bmw', color: 'red'};
const book: Book = { price: 3000 };

function showName<T extends { name: string }>(data: T) : string {
    return data.name
}

showName(user);
showName(car);
showName(book); // error 가 남 -> name 속성이 없음
~~~

### 유틸리티 타입
---
- keyof
~~~typescript
interface User {
    id: number;
    name: string;
    age: number;
    gender: "m"|"f";
}

type UserKey = keyof User; // 'id' | 'name' | 'age' |'gender'

const uk:UserKey = "name";
~~~

- Partial<T>
~~~typescript
interface User {
    id: name;
    name: string;
    age: number;
    gender: 'm'|'f';
}

let admin: Partial<User> {
    id: 1,
    name: 'Bob',
};

// 위는 아래의 인터페이스를 사용한것과 동일함
interface User {
    id?: name;
    name?: string;
    age?: number;
    gender?: 'm'|'f';
}
~~~

- Required<T> : 선택 변수를 반드시 입력해야하는 변수 타입으로 변경함
~~~typescript
interface User {
    id: number;
    name: string;
    age?: number;
}

let admin: Required<User> = {
    id: 1,
    name: "Bob",
    age: 30, // 입력해줘야 함
};
~~~

- Readonly<T> : 모든 변수를 읽기 전용 변수로 변경함
~~~typescript
interface User {
    id: number;
    name: string;
    age?: number;
}

let admin: Readonly<User> = {
    id: 1,
    name: "Bob",
};

admin.id = 4; // error 발생
~~~

- Record<K, T>
~~~typescript
type Grade = "1" | "2" | "3" | "4";
type Scroe = "A" | "B" | "C" | "D" | "F";

const score: Record<Grade, Score> = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
}
~~~
~~~typescript
interface User {
    id: number;
    name: string;
    age: number;
}

function isValid(user: User) {
    const result: Record<keyof User, boolean> = {
        id: user.id >0,
        name: user.name !== "",
        age: user.age >0,
    };
    return result;
}
~~~

- Pick<T, K> : T 타입 중에서 K 키만 선택
~~~typescript
interface User {
    id?: name;
    name?: string;
    age?: number;
    gender?: 'm'|'f';
}

const admin: Pick<User, "id" | "name"> = {
    id: 0,
    name: "Bob"
};
~~~

- Omit<T, K> : T 타입 중에서 K 키만 생략
~~~typescript
interface User {
    id?: name;
    name?: string;
    age?: number;
    gender?: 'm'|'f';
}

const admin: Omit<User, "age" | "gender"> = {
    id: 0,
    name: "Bob"
};
~~~

- Exclude<T1, T2> : T1 타입에서 T2타입들을 제거

~~~typescript
type T1 = string | number | boolean;
type T2 = Exclude<T1, number | boolean> // T3 = string ; 과 동일
~~~

- NonNullable<Type> : Type 중에서 null 과 undefined를 제거
~~~typescript
type T1 = string | null | undefined | void;
type T2 = NonNullable<T1> // type T3 = string | void; 와 동일
~~~