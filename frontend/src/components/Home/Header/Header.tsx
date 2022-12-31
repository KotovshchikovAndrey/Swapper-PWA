import React from "react"
import { Link } from "react-router-dom"
import "./Header.css"

import Navbar from "../../UI/Navbar/Navbar"
import { navList, headerDescription } from "../../../data/static"


export default function Header() {
    return (
        <section className="section header-section">
            <header className="header flex">
                <h2>Swapper-Logo</h2>
                <Navbar navList={navList} />
                <Link to="/auth" className="header-auth-link">Регистрация / Авторизация</Link>
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