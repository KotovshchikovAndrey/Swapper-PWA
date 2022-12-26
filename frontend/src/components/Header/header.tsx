import React from 'react'
import './Header.css'
import NavBar from './NavBar/Navbar'


export default function Header() {
    return (
        <section className='section header-section'>
            <header className='header'>
                <div className="contauner">
                    <NavBar />
                </div>
            </header>
            <section className='header-description'>
                <div className="container">
                    <div className='about flex'>
                        <h2 className='header-about-title'>Что такое Swapper?</h2>
                        <p className='about-description'>
                            Swapper - это сервис для поиска и осуществления взаимовыгодных отношений
                            между людьми. Мы предоставляем
                            удобную площадку для обмена, поиска и предоставления улуг.
                        </p>
                    </div>
                </div>
            </section>
        </section>
    )
}