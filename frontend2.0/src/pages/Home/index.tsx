import React from "react"
import Header from "./components/Header"
import Manual from "./components/Manual"
import Abilities from "./components/Abilities"
import Notification from "./components/Notification"
import Footer from "components/layout/Footer"

export default function Home() {
  return (
    <React.Fragment>
      <Header />
      <Manual />
      <Abilities />
      <Notification />
      <Footer />
    </React.Fragment>
  )
}
