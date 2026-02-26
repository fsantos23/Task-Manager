import "../styles/Login.css"
import { useState } from "react"
import api from "../api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import { toast } from "sonner"


function Login () {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmition = async (e) => {
        e.preventDefault()

        console.log(api.baseURL)

        await api.post('authentication/login', {
            "username": username,
            "password": password,
        })
        .then(function (response){
            if (response.status === 201) {
                const data = response.data
                localStorage.setItem(ACCESS_TOKEN, data.access)
                localStorage.setItem(REFRESH_TOKEN, data.refresh)
                toast(`Succesfully logged in`, {
                    style: {
                        background: 'green',
                    },
                })
            } else {
                toast(`Error: ${response.data}`, {
                    style: {
                        background: 'red',
                    },
                })
            }
        })
        .catch(function (error){
            toast(`Error: ${error.response.data}`, {
                    style: {
                        background: 'red',
                    },
                })
        })
    }

    return <div>
        <div className="container">
            <div className="login-container">
                <h1 className="login-title">Login</h1>
                <form className="login-form" onSubmit={handleSubmition}>
                    <div className="form-group">
                        <label htmlFor='username' className="form-label">
                            Username
                        </label>
                        <input 
                            type="text"
                            id="username"
                            className="login-input"
                            placeholder="Enter your username"
                            value={username}
                            onChange={(e) => {setUsername(e.target.value)}}
                        ></input>
                    </div>
                    <div className="form-group">
                        <label htmlFor="password" className="form-label">
                            Password
                        </label>
                        <input
                            type="password"
                            id="password"
                            className="login-input"
                            placeholder="Enter your password"
                            value={password}
                            onChange={(e) => {setPassword(e.target.value)}}
                        ></input>
                    </div>
                    <button className="login-button">Login</button>
                </form>
            </div>
        </div>
    </div>
}

export default Login