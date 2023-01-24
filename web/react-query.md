- install react-query
~~~cmd
npm install react-query
~~~
- setup react-query
~~~jsx
import {
  createBrowserRouter,
  RouterProvider,
  Outlet
} from "react-router-dom"
import {QueryClientProvider, QueryClient} from "react-query"
import "./style.scss"

const queryClient = new QueryClient()

function App() {
  return (
  <QueryClientProvider client={queryClient}>
    <div className="App">
      <div className="container">
        <RouterProvider router={router}/>
      </div>
    </div>
  </QueryClientProvider>
  );
}

export default App;
~~~

- get method
~~~jsx
import axios from 'axios';
import {useQuery} from 'react-query'

const fetchLoginInfo = () => {
    return axios.get('http://127.0.0.1:8000/')
}

export default function Login () {
    const {isloading, data} = useQuery('login-info', fetchLoginInfo)

    if (isloading) {
        return <h2>Loading</h2>
    }

    return (
        <div>
            Login!
            {data?.data.result}
        </div>
    )
}
~~~

- post 
~~~jsx
import axios from 'axios';
import {useQuery} from 'react-query'

const fetchLoginInfo = () => {
    return axios.post('http://127.0.0.1:8000/login',{userId:'ajcltm', userPw:'1111'})
}

export default function Login () {
    const {isloading, data} = useQuery('login-info', fetchLoginInfo)

    if (isloading) {
        return <h2>Loading</h2>
    }

    return (
        <div>
            Login!
            {data?.data.result}
        </div>
    )
}
~~~

- handle error
~~~jsx
import axios from 'axios';
import {useQuery} from 'react-query'

const fetchLoginInfo = () => {
    return axios.post('http://127.0.0.1:8000/login9',{userId:'ajcltm', userPw:'1111'})
}

export default function Login () {
    const {isloading, data, isError, error} = useQuery('login-info', fetchLoginInfo)

    if (isloading) {
        return <h2>Loading</h2>
    }

    if (isError) {
        return <h2>error</h2>
    }


    return (
        <div>
            Login!
            {data?.data.result}
        </div>
    )
}
~~~