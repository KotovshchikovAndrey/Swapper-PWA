import React from "react"
import { BrowserRouter as Router, Route } from "react-router-dom"
import "./App.css"

import HomePage from "./pages/HomePage"

function App() {
	return (
		<HomePage />
		// <div className="App">
		// 	<Router>
		// 		<Routes>
		// 			<Route path="/" element={<Home />} />
		// 			<Route path="/auth" element={<Auth />} />
		// 		</Routes>
		// 	</Router>
		// </div>
	)
}

export default App
