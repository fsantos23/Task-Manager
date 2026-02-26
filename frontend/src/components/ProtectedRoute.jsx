import api from "../api"
import { jwtDecode } from "jwt-decode"
import { Navigate } from "react-router"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import { useState, useEffect } from "react"


function ProtectedRoute({ children }) {
    const [isAuth, setIsAuth] = useState(null)

    useEffect(() => {
        auth().catch()(() => setIsAuth(false))
    }, [])

    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)

        try {
            const response = await api.post("authorization/token/refresh", { "refresh": refreshToken })

            if (response.status == 200) {
                localStorage.setItem(ACCESS_TOKEN, response.data.access)
                setIsAuth(true)
            }
            else {
                setIsAuth(false)
            }
        }
        catch (error) {
            console.log(error)
            setIsAuth(false)
        }
    }

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN)

        if (!token) {
            setIsAuth(false)
            return
        }

        const decode = jwtDecode(token)
        const tokenExpiration = decode.exp
        const now = Date.now() / 1000

        if (tokenExpiration < now) {
            refreshToken()
        }
        else {
            setIsAuth(true)
        }
    }

    if (isAuth === null)
        <div>Loading...</div>

    return isAuth ? children : <Navigate to="/login" />
}

export default ProtectedRoute