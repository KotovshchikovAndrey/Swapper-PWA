import React from "react"
import "./index.css"

import Header from "./Header"
import About from "./About"
import Abilities from "./Abilities"
import Notifications from "./Notifications"
import Footer from "../UI/Footer"

export default function Home() {
	return (
		<React.Fragment>
			<Header />
			<About />
			<Abilities />
			<Notifications />
			<Footer />
		</React.Fragment>
	)
}
