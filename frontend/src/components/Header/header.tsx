import React from "react"
import "./Header.css"

import NavBar from "./NavBar/Navbar"
import { headerDescription } from "../../data/static"


export default function Header() {
    return (
        <section className="section header-section">
            <header className="header flex">
                <h2>Swapper-Logo</h2>
                <NavBar />
                <p className="header-auth-link">Регистрация / Авторизация</p>
            </header>
            <section className="header-description">
                <div className="container">
                    <div className="header-about flex">
                        <h2 className="header-about-title">Что такое Swapper?</h2>
                        <p className="about-description">{headerDescription}</p>
                    </div>
                </div>
            </section>
        </section>
    )
}