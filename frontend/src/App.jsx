import React from "react";
import Register from "./pages/Register"
import ProtectedRoute from "./components/ProtectedRoute"
import Login from "./pages/Login"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import { Navigate, BrowserRouter, Routes, Route } from "react-router"
import api from "./api"
import { REFRESH_TOKEN } from "./constants";

function Logout () {
    const data = api.post("authentication/logout", {
        "refresh": localStorage.getItem(REFRESH_TOKEN)
    })
    if (data.status_code === 204)
    {
        // create a pop up on the down right corner to show message of successfully logout
        localStorage.clear()
        return <Navigate to="/login" />
    }
    //create a pop up to show a error message
}

function RegisterAndLogout () {
    localStorage.clear()
    return <Register />
}

function App () {
    return <BrowserRouter>
            <Routes>
                <Route
                    path='/'
                    element={
                        <ProtectedRoute>
                            <Home />
                        </ProtectedRoute>
                    }
                />
                <Route 
                    path='/register'
                    element={<RegisterAndLogout />}
                />
                <Route
                    path='/login'
                    element={<Login />}
                />
                <Route
                    path="/logout"
                    element={<Logout />}
                />
                <Route
                    path='*'
                    element={<NotFound />}
                />
            </Routes>
        </BrowserRouter>
}

export default App