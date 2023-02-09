// //@ts-ignore
// import "./index.module.css"
import React from "react"
import Header from "./components/Header"
import Manual from "./components/Manual"
import Abilities from "./components/Abilities"
import Notification from "./components/Notification"

export default function HomePage() {
  return (
    <React.Fragment>
      <Header />
      <Manual />
      <Abilities />
      <Notification />
    </React.Fragment>
  )
}
