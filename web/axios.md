- install
~~~cmd
npm install axios
~~~

- get method
~~~jsx
import React, { useEffect, useState } from "react";
import axios from 'axios';

export default function Login () {
    const [data, setData] = useState([])
    const [error, setError] = useState([])

    useEffect(()=>{
        axios.get('http://127.0.0.1:8000').then((res)=>{
            setData(res.data)
        }).catch(error=>{
            setError(error)
        })
    },[])

    return (
        <div>
            Login!
            <div>{data.data}</div>
        </div>
    )
}
~~~

- post method
~~~jsx
import React, { useEffect, useState } from "react";
import axios from 'axios';

export default function Login () {
    const [data, setData] = useState([])
    const [error, setError] = useState([])

    useEffect(()=>{
        axios.post('http://127.0.0.1:8000/login',
                    {userId:'ajcltm', userPw:'1111'}).then((res)=>{
            setData(res.data)
        }).catch(error=>{
            setError(error)
        })
    },[])

    console.log(data)

    return (
        <div>
            Login!
            <div>{data.result}</div>
        </div>
    )
}
~~~