import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'

import Home from './components/Home/Home'
import Auth from './components/Auth/Auth'


function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/auth" element={<Auth />} />
        </ Routes>
      </Router>
    </div >
  )
}

export default App
