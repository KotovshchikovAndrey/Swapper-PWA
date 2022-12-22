import React from 'react'
import './navbar.css'


export default function NavBar() {
    return (
        <div className="container">
            <nav className='nav flex'>
                <li className='nav-link'>Найти Сваппера</li>
                <li className='nav-link'>Рейтинг Свапперов</li>
                <li className='nav-link'>Сваппы Дня</li>
            </nav>
        </div>
    )
}