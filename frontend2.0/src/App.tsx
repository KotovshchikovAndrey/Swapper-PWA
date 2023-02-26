import React from "react"
import { Route, Routes, BrowserRouter, Navigate } from "react-router-dom"
import "./App.css"
import { useTypedDispatch, useTypedSelector } from "hooks/redux"
import { authActions } from "store/reducers/user"
import Home from "pages/Home"
import Registration from "pages/Registration"
import Login from "pages/Login"

const Logout = () => {
  const dispatch = useTypedDispatch()

  localStorage.removeItem("accessToken")
  dispatch(authActions.setIsAuth(false))

  return <Navigate to="/login" replace />
}

function App() {
  const dispatch = useTypedDispatch()

  React.useEffect(() => {
    const authToken = localStorage.getItem("accessToken")
    if (authToken) {
      dispatch(authActions.setIsAuth(true))
    }
  }, [])

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="registration" element={<Registration />} />
          <Route path="login" element={<Login />} />
          <Route path="logout" element={<Logout />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
