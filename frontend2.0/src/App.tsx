import React from "react"
import { Route, Routes, BrowserRouter } from "react-router-dom"
import "./App.css"
import HomePage from "pages/HomePage"
import AuthPage from "pages/AuthPage"

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="auth" element={<AuthPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
