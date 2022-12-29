import React from 'react'
import './Navbar.css'


export default function NavBar() {
    return (
        <nav className="nav">
            <div className="container">
                <ul className="nav-list flex">
                    <li className="nav-link">Найти Сваппера</li>
                    <li className="nav-link">Рейтинг Свапперов</li>
                    <li className="nav-link">Сваппы Дня</li>
                </ul>
            </div >
        </nav>
    )
}