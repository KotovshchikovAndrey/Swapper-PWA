import React from 'react'
import './header.css'
import NavBar from '../NavBar/navbar'


export default function Header() {
    return (
        <section className='header-section'>
            <header className='header'>
                <NavBar />
            </header>
            <section className='header-description'>
                <div className="container">
                    <div className='about flex'>
                        <h2 className='about-title'>Что такое Swapper?</h2>
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