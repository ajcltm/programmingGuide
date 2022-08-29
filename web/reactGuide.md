### **설치하기**
---
#### **Nodejs 설치**
---
- 정말 기본적인 설치만 한다. 리눅스 설치는 다시 알아봐야겠지만 윈도우는 그냥 설치파일 받아서 next, next 진행하면 된다.
<br><br>

#### **타입스크립트 설치**
---
~~~
npm install typescript
npx tsc
~~~
<br>


#### **create-react-app 설치**
---
- npm 으로 설치하면 됨
<br><br>

#### **타입스크립트로 시작하기**
---
- project name에 대문자가 들어가면 에러가 발생함
- project folder를 위치시킬 결로로 이동한 상태에서 명령해야함
~~~
npx create-react-app tictactoe-app --template=typescript
npm start
~~~
<br>


컴파일 - ts 파일을 js 로 변환
~~~
npx tsc {타입스크립트 파일이름.ts}
~~~
<br>

### **시작하기**
---
- 다음 명령으로 프로젝트를 생성한다.
~~~
npx create-react-app tictactoe-app --template typescript
~~~
<br>

#### **프로젝트 구조 간단하게 만들기**
---
- 처음 해야할 일은 기본적인 파일들만 남기고 모두 지우는 것이다. public 폴더에서 index.html 파일만 남기고 모두 지우자. src 폴더에서는 App.tsx 와 index.tsx 만 남기고 모두 지우자. public 폴더의 index.html 은 다음과 같은 모습이어야 한다.
<br>

~~~
File: public\index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>TicTacToe App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
~~~
- src 폴더의 index.tsx 파일은 다음과 같이 수정하자.
~~~
File: src\index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
 
const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
~~~
- src 폴더의 App.tsx 파일은 다음과 같이 수정하자.
~~~
File: src\App.tsx
import React from 'react';
 
function App() {
  return (
    <div className="App">
    </div>
  );
}
 
export default App;
~~~

#### **react element**
---
~~~typescript
[in]
import React from 'react';

function App() {
  const element = <h1 className="header">This is JSX</h1>
  console.log(element)
  return (
    <div className="App">
      
    </div>
  );
}

export default App;

[out]
$$typeof: Symbol(react.element)
key: null
props: {className: 'header', children: 'This is JSX'}
ref: null
type: "h1"
_owner: FiberNode {tag: 0, key: null, stateNode: null, elementType: ƒ, type: ƒ, …}
_store: {validated: false}
_self: undefined
_source: {fileName: 'C:\\Users\\ajcltm\\PycharmProjects\\ajcltmblog\\src\\App.tsx', lineNumber: 4, columnNumber: 19}
[[Prototype]]: Object
~~~