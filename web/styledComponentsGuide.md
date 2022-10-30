### 기본 예시
---
~~~tsx
// src/components/styles/Conatainer.styled.tsx
import styled from 'styled-components';

export const Container = styled.div`
    width: 1000px;
    max-width: 100%;
    padding: 0 20px;
    margin: 0 auto;
~~~
~~~tsx
// src/components/styles/Header.styled.tsx
import styled from 'styled-components';

export const StyledHeader = styled.header`
    background-color: #fff};
    padding : 40px 0;
    }
`
~~~

~~~tsx
// src/components/Header.tsx
import React from 'react';
import { Container } from './styles/Container.styled';
import { Header } from './styles/Header.styled';

export default function Header() {
    return (
        <StyledHeader>
            <Container>
                <div>   
                    <h1> Helow World </h1>
                </div>
            </Container>
        </StyledHeader>
    )
}
~~~
~~~tsx
// scr/App.tsx
import React from 'react';
import Header from './components/Header';

export default function app() {
    return (
        <>
            <Header />
        </>
    )
}
~~~

### props 사용하기
---
~~~tsx
// src/components/styles/Card.styled.tsx
import styled from "styled-components";

interface StyledCardProps {
    readonly layout?: string;
}

export const StyledCard = styled.div<StyledCardProps>`
    display: flex;
    align-items: space-between;
    justify-content: space-between;
    background-color: #fff;
    border-radius: 15px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
    margin : 40px 0;
    padding: 40px;
    flex-direction: ${(props) => props.layout || 'row'};

    img {
        width: 80%;
        // padding-left: 50px;
    }

    & > div {   
        flex: 1;
        padding: 10px;
    }
`
~~~
~~~tsx
// src/components/Card.tsx
import React from 'react';
import { StyledCard } from './styles/Card.styled';


interface Item {
    id: number;
    title: string;
    body: string;
    image: string;
}

interface CardProps {
    item: Item
}

export default function Card(props:CardProps) {
    return (
        <StyledCard layout={props.item.id % 2 === 0 ? 'row-reverse' : undefined}>
            <div>
                <h2>{props.item.title}</h2>
                <p>{props.item.body}</p>
            </div>

            <div>
                <img src={`${props.item.image}`} alt="" />
            </div>
        </StyledCard>
    )
}
~~~
~~~tsx
const content = [
    {
        id: 1,
        title : 'Grow Together',
        body: 'Generate meanigful discussions with your audience and bulid a strong, loyal community.',
        image: 'https://img.freepik.com/free-vector/1,
    },
    {
        id: 2,
        title : 'Flowing Conversations',
        body: `You wouldn't paginate a conversation in real life.`,
        image: 'https://img.freepik.com/free-vector/2,
    },
    {
        id: 3,
        title : 'Your Users',
        body: `It takes no time at all to inergrate Huddle with your app's authentication solution.`,
        image: 'https://img.freepik.com/free-vector/3',
    },
    {
        id: 4,
        title : 'Grow Together',
        body: 'Generate meanigful discussions with your audience and bulid a strong, loyal community.',
        image: 'https://img.freepik.com/free-vector/4',
    }
]

export default content
~~~

~~~tsx
// src/App.tsx
import React from 'react';
import Header from './components/Header';
import Card from './components/Card';
import {Container} from './components/styles/Container.styled'
import content from './content';

export default function app() {
    return (
        <>
            <Header />
            <Container>
                {content.map((item, index)=>(
                    <Card key={index} item={item} />
                ))}
            </Container>
        </>
    )
}
~~~

### Theme
---
- ThemeProvider tag의 theme props를 통해서 다른 style파일에서 별도 props 설정이나 import 없이도 theme 속성에 접근이 가능함
~~~tsx
// src/App.tsx
import React from 'react';
import {ThemeProvider} from 'styled-components'
import Header from './components/Header';
import { DefaultTheme } from 'styled-components';

const colors = {
    header: '#ebfbff',
    body: '#fff',
    footer: '#003333'
};

const mediaQuery = {
    mobile : '768px'
}

const theme:DefaultTheme = {
    colors,
    mediaQuery
}

export default function app() {
    return (
        <ThemeProvider theme = {theme}>
            <>
                <Header />
            </>
        </ThemeProvider>
    )
}
~~~
~~~tsx
// src/components/styles/Header.styled.tsx
import styled from 'styled-components';

export const StyledHeader = styled.header`
    background-color: ${({ theme })=> theme.colors.header};
    padding : 40px 0;
    }
    
    @media (max-width: ${( {theme} ) => theme.mediaQuery.mobile}) {
    margin-bottom: 40px;
`
~~~
~~~tsx
// src/components/Header.tsx
import React from 'react';
import { Container } from './styles/Container.styled';
import { Header } from './styles/Header.styled';

export default function Header() {
    return (
        <StyledHeader>
            <Container>
                <div>   
                    <h1> Helow World </h1>
                </div>
            </Container>
        </StyledHeader>
    )
}
~~~

### createGlobalStyle
---
- createGlobalStyle : 모든 components에 적용할 style을 정의
- 가장 윗단의 component로 두면, 다른 components에 자동으로 적용됨
- GlobalStyle 컴포넌트에 theme props를 넘기려면, DefaultTheme에 커스텀된 theme object를 type정의를 추가하고, generic 타입 설정해야함
~~~tsx
// src/App.tsx
import React from 'react';
import GlobalStyles from './components/styles/Global';
import {ThemeProvider} from 'styled-components'
import Header from './components/Header';
import { DefaultTheme } from 'styled-components';

const colors = {
    header: '#ebfbff',
    body: '#fff',
    footer: '#003333'
};

const mediaQuery = {
    mobile : '768px'
}

type ColorsTypes = typeof colors

type MobileTypes = typeof mediaQuery

declare module 'styled-components' {
    export interface DefaultTheme {
        colors : ColorsTypes
        mediaQuery : MobileTypes
    }
}

const theme:DefaultTheme = {
    colors,
    mediaQuery
}

export default function app() {
    return (
        <ThemeProvider theme = {theme}>
            <>
                <GlobalStyles /> 
                <Header />
            </>
        </ThemeProvider>
    )
}
~~~
~~~tsx
import { createGlobalStyle } from "styled-components";
import { DefaultTheme } from 'styled-components';

const GlobalStyles = createGlobalStyle<{theme:DefaultTheme}>`
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    * {
        box-sizing: border--box;
    }
    body {
        background: ${({ theme })=> theme.colors.body};
        color: hsl(192, 100%, 9%);
        font-family: 'Poppins', sans-serif;
        font-size: 1.15em;
        margin: 0;
    }
    p {
        opacity: 0.6;
        line-height: 100%;
    }
    img {
        max-width: 100%;
    }
`

export default GlobalStyles
~~~

### 상속 및 확장 재사용
~~~tsx
import React from "react";
import styled from "styled-components";

const App = () => (
  <Container>
    <Button>버튼</Button>
    <GreenButton>초록버튼</GreenButton>
    <BlueButton>파란버튼</BlueButton>
  </Container>
);

const Container = styled.div`
  display: flex;
`;

const Button = styled.button`
  outline: none;
  border: none;
  border-radius: 50%;
`;

const GreenButton = styled(Button)`
  background-color: green;
`;

const BlueButton = styled(Button)`
  background-color: blue;
`;

export default App;
~~~
