### **설치하기**
---
#### **Nodejs 설치**
---
- 아래 링크에서 설치
~~~
https://nodejs.org/ko/
~~~

#### **타입스크립트 설치**
---
~~~
npm install typescript
npx tsc
~~~
<br>


#### **create-react-app 설치**
---
- 터미널 창에서 설치
~~~
npm install -g create-react-app
~~~
<br>

#### **타입스크립트로 시작하기**
---
- project folder를 위치시킬 경로로 이동한 상태에서 명령해야함
- app folder를 미리 만들 필요 없음
- app name에 대문자가 들어가면 에러가 발생함
~~~
- project folder
  |- new-react-app
~~~
~~~
npx create-react-app new-react-app --template=typescript
~~~
- app folder로 이동해서 터미널 창에 아래 입력
~~~
npm start
~~~
<br>

컴파일 - ts 파일을 js 로 변환
~~~
npx tsc {타입스크립트 파일이름.ts}
~~~
<br>


#### **프로젝트 구조 간단하게 만들기**
---
- public 폴더에서 index.html 파일만 남기고 모두 삭제
- src 폴더에서는 App.tsx 와 index.tsx 만 남기고 모두 삭제
- public 폴더의 index.html 은 다음과 같은 모습이어야 함
<br>

~~~tsx
// public\index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Test-react-App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
~~~
- src 폴더의 index.tsx 파일은 다음과 같이 수정
~~~tsx
// src\index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
 
ReactDOM.render(<App/>, document.getElementById("root"))
~~~
- src 폴더의 App.tsx 파일은 다음과 같이 수정
~~~tsx
// src\app.tsx
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
~~~tsx
// src\app.tsx
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
~~~
~~~
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

#### **props**
---
~~~tsx
import React from 'react';
import {nanoid} from 'nanoid'

type Content = {
  id: string;
  title: string;
  body: string;
}

type ContentsData = {
  CategoryId: string;
  CategoryTitle: string;
  contents: Content[];
}

function ArchiveApp() {

  const [contentsData, setContentsData] = React.useState<ContentsData[]>([])
  const [currentCategoryId, setCurrentCategoryId] = React.useState(
    (contentsData[0] && contentsData[0].CategoryId) || ""
  )

  function ceateNewCategory() {
    const newContent : ContentsData = {
      CategoryId: nanoid(),
      CategoryTitle: '',
      contents: [{id:nanoid(), title: 'new content title', body:'This is the new content!'}]
    }
    setContentsData(prevContents => [...prevContents, newContent])
    setCurrentCategoryId(newContent.CategoryId)
  }

  function updateCategory(event:React.ChangeEvent<HTMLInputElement>) {
    setContentsData(oldContents => oldContents.map(oldContent => {
      return oldContent.CategoryId === currentCategoryId
        ? {...oldContent, CategoryTitle:event.target.value}
        : oldContent
    }))
  }

  function findCurrentCategory() {
    return contentsData.find(content => {
      return content.CategoryId === currentCategoryId
    }) || contentsData[0]
  }

  return (
    <div>
      <ArchiveNav 
        contentsData={contentsData} 
        currentCategory={findCurrentCategory()} 
        setCurrentCategoryId={setCurrentCategoryId} 
        newCategory={ceateNewCategory}
        changeCategory={updateCategory}
      />
    </div>
  );
}

export default ArchiveApp;
~~~

~~~tsx
import React from 'react';

type Content = {
    id: string;
    title: string;
    body: string;
  }

type ContentsData = {
    CategoryId: string;
    CategoryTitle: string;
    contents: Content[];
}

type ArchiveNavProps = {
    admin : boolean;
    contentsData : Array<ContentsData>
    currentCategory : ContentsData
    setCurrentCategoryId : React.Dispatch<React.SetStateAction<string>>
    newCategory : ()=>void
    changeCategory : (event:React.ChangeEvent<HTMLInputElement>)=>void
};

function ArchiveCategoryAdd(props:ArchiveNavProps) {

    return (
        <div>
            <h4>Category Add</h4>
            <button onClick={props.newCategory}> + </button>
        </div>
    )
};

function AdminArchiveNav(props:ArchiveNavProps) {

    const inputElement = props.contentsData.map(content=>{
        return <input className='archiveNav-input' type='text' placeholder='New Category' value={content.CategoryTitle} onChange={props.changeCategory} onClick={()=>props.setCurrentCategoryId(content.CategoryId)}/>
})
    return (
        props.contentsData.length > 0 ?
        <div className='archive-nav-wraper'>
            {inputElement}
        </div>
        :
        <div className="archive-nav-wraper"></div> 
    )
};

function ArchiveNav(props:ArchiveNavProps) {
    return (
        props.admin ?
            <div className='archive-nav'>  
                <ArchiveCategoryAdd
                admin={props.admin} 
                contentsData={props.contentsData} 
                currentCategory={props.currentCategory} 
                setCurrentCategoryId={props.setCurrentCategoryId} 
                newCategory={props.newCategory}
                changeCategory={props.changeCategory}
                />
                <AdminArchiveNav 
                admin={props.admin} 
                contentsData={props.contentsData} 
                currentCategory={props.currentCategory} 
                setCurrentCategoryId={props.setCurrentCategoryId} 
                newCategory={props.newCategory}
                changeCategory={props.changeCategory}
                />
            </div>
        :
        <a href=""></a>
    );
};

export default ArchiveNav;
~~~

#### **Hook**
---
- useState
~~~jsx
function Counter({initialCount}) {
  const [count, setCount] = useState(initialCount);
  return (
    <>
      Count: {count}
      <button onClick={() => setCount(initialCount)}>Reset</button>
      <button onClick={() => setCount(prevCount => prevCount - 1)}>-</button>
      <button onClick={() => setCount(prevCount => prevCount + 1)}>+</button>
    </>
  );
}
~~~
- useState 사용 시 갱신 객체 합치기
~~~jsx
const [state, setState] = useState({});
setState(prevState => {
  // Object.assign would also work
  return {...prevState, ...updatedValues};
});
~~~

- useEffect
<br> (!) effect를 수행하고 (mount를 하거나 unmount 할 때) 그것을 한 번만 실행하고 싶다면 두 번째 인자로 빈 배열([])을 전달
~~~jsx
useEffect(
  () => {
    const subscription = props.source.subscribe();
    return () => {
      subscription.unsubscribe();
    };
  },
  [props.source],
);
~~~

- useContext
<br> - context 객체(React.createContext에서 반환된 값)을 받아 그 context의 현재 값을 반환
<br> - context의 현재 값은 트리 안에서 이 Hook을 호출하는 컴포넌트에 가장 가까이에 있는 <MyContext.Provider>의 value prop에 의해 결정
~~~jsx
const themes = {
  light: {
    foreground: "#000000",
    background: "#eeeeee"
  },
  dark: {
    foreground: "#ffffff",
    background: "#222222"
  }
};

const ThemeContext = React.createContext(themes.light);

function App() {
  return (
    <ThemeContext.Provider value={themes.dark}>
      <Toolbar />
    </ThemeContext.Provider>
  );
}

function Toolbar(props) {
  return (
    <div>
      <ThemedButton />
    </div>
  );
}

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return (
    <button style={{ background: theme.background, color: theme.foreground }}>
      I am styled by theme context!
    </button>
  );
}
~~~

- useMemo
<br> - “생성(create)” 함수와 그것의 의존성 값의 배열을 전달하여야 함. useMemo는 의존성이 변경되었을 때에만 메모이제이션된 값만 다시 계산. 이 최적화는 모든 렌더링 시의 고비용 계산을 방지
<br> - useMemo로 전달된 함수는 렌더링 중에 실행된다는 것에 주의. 통상적으로 렌더링 중에는 하지 않는 것을 이 함수 내에서 하면 안됨
~~~jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
~~~

- useRef
<br> \<div ref={myRef} />를 사용하여 React로 ref 객체를 전달하면, React는 노드가 변경될 때마다 변경된 DOM 노드에 .current 프로퍼티를 설정
~~~jsx
function TextInputWithFocusButton() {
  const inputEl = useRef(null);
  const onButtonClick = () => {
    // `current` points to the mounted text input element
    inputEl.current.focus();
  };
  return (
    <>
      <input ref={inputEl} type="text" />
      <button onClick={onButtonClick}>Focus the input</button>
    </>
  );
}
~~~

#### **react-router**
---
- 기본적인 router 구조
~~~tsx
// scr\index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import App from './App';
import AboutApp from './components/Child1App';
import AboutApp from './components/Child2App';
import AboutApp from './components/GrandchildApp1';
import AboutApp from './components/GrandchildApp2';

const rootElement = document.getElementById("root");

ReactDOM.render(
    <Router>
        <Routes>
            <Route path="/app" element={<App />}>
                <Route path="/app/child1" element={<Child1App />} />
                <Route path="/app/child2" element={<Child2App />}>
                    <Route path="/app/child2/grandchildapp1" element={<GrandchildApp1 />} />
                    <Route path="/app/child2//grandchildapp2" element={<GrandchildApp2 />} />
                </Route>
            </Route>
        </Routes>
    </Router>,
    rootElement
);
~~~
~~~tsx
// scr\components\LinkApp.tsx   <- App의 어딘가에 사용되는 컴포넌트
import React from 'react';
import {Link} from "react-router-dom"

function LinkApp() {
    return (
        <div>
          <Link className='link-botton' to='child1'> 링크 버튼 </Link>  // 주소 : localhost/app/child1
        </div>
        )
}

export default LinkApp
~~~
~~~tsx
// scr\components\LinkApp2.tsx   <- child2의 어딘가에 사용되는 컴포넌트
import React from 'react';
import {Link} from "react-router-dom"

function LinkApp2() {
    return (
        <div>
          <Link className='link-botton' to='grandchildapp1'> 링크 버튼 </Link>  // 주소 : localhost/app/child2/grandchildapp1
        </div>
        )
}

export default LinkApp2
~~~

- outlet을 이용하는 경우 자식 router는 부모 화면 영역 중 outlet 부분에만 나타남
~~~tsx
// scr\index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import App from './App';
import AboutApp from './components/ChildApp';

const rootElement = document.getElementById("root");

ReactDOM.render(
    <Router>
        <Routes>
            <Route path="/app" element={<App />}>
                <Route path="/app/child" element={<ChildApp />} />
            </Route>
        </Routes>
    </Router>,
    rootElement
);
~~~

~~~tsx
// src\app.tsx
import React from 'react';
import {Outlet} from "react-router-dom"
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div>
      <Header />
      <Outlet />   // ChildApp은 이 영역에만 나타남
      <Footer />
    </div>
  );
}

export default App;
~~~

~~~tsx
// scr\components\Header.tsx   <- App의 어딘가에 사용되는 컴포넌트
import React from 'react';
import {Link} from "react-router-dom"

function Header() {
    return (
        <div>
          <Link className='link-botton' to='child'> 링크 버튼 </Link> 
        </div>
        )
}

export default WebBusinessContentTheme
~~~
- outlet에 props를 사용해야할 경우
~~~tsx
// scr\index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import App from './App';
import AboutApp from './components/ChildApp';

const rootElement = document.getElementById("root");

ReactDOM.render(
    <Router>
        <Routes>
            <Route path="/app" element={<App />}>
                <Route path="/app/child" element={<ChildApp />} />
            </Route>
        </Routes>
    </Router>,
    rootElement
);
~~~

~~~tsx
// src\app.tsx
import React from 'react';
import {Outlet, useOutletContext} from "react-router-dom";
import Header from './components/Header';
import Footer from './components/Footer';

type OutletProps = {
  id: string;
  data : Array<number>
}

const outletProps:OutletProps = {
  id: 'abcd1234',
  data: [1, 2, 3, 4, 5]
}

function App() {
  return (
    <div>
      <Header />
      <Outlet context={outletProps}/>  // outletProps를 context에 담아서 Outlet에 전달함
      <Footer />
    </div>
  );
}

export default App;

// react 내부적으로 useOutletContext를 콜하면 context를 반환하도록 되어 있음(context에는 outletProps가 담겨있는 상태임). 이때, useOutletContext를 콜하는 useOutletProps 함수를 export 시킴
export function useOutletProps() {
  return useOutletContext<OutletProps>();  
~~~

~~~tsx
// scr\components\ChildApp.tsx  < - outlet에 해당하는 컴포넌트
import React from 'react';
import { useOutletProps } from '../App'

function ChildApp() {
    const props = useOutletProps()  // useOutletProps를 콜해서 outletProps를 담고 있는 context를 get함
    return (
      <div> {props.id} </div>
      <div> {props.data.length} </div>
)
}

export default ChildApp
~~~

- RouterProvider & createBrowserRouter
~~~jsx
import {
  createBrowserRouter,
  RouterProvider,
  Outlet
} from "react-router-dom"
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar"
import Footer from "./components/Footer"

const Layout = () =>{
  return (
    <>
      <Navbar />
      <Outlet />
      <Footer />
    </>
  )
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout/>,
    children: [
      {
        path: "/",
        element: <Home/>
      },
      {
        path: "/register",
        element: <Register /> 
      },
      {
        path: "/login",
        element: <Login /> 
      },
    ]
  },

])

function App() {
  return (
    <div className="App">
      <RouterProvider router={router}/>
    </div>
  );
}

export default App;
~~~