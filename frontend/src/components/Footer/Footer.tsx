import React from 'react'
import './Footer.css'


export default function Footer() {
    return (
        <footer className="footer">
            <div className="flex container footer-container">
                <div className="footer-nav">
                    <h2 className="footer-nav-title">@Swapper</h2>
                    <nav className="nav">
                        <ul className="flex footer-nav-list footer-list">
                            <li className="footer-list-title">Навигация:</li>
                            <li className="footer-list-item">Главная Страница</li>
                            <li className="footer-list-item">Найти Сваппера</li>
                            <li className="footer-list-item">Профиль</li>
                        </ul>
                    </nav>
                </div>
                <div className="footer-contacts">
                    <ul className="flex footer-contacts-list footer-list">
                        <li className="footer-list-title">Контакты:</li>
                        <li className="footer-list-item">Автор: &nbsp; Котовщиков Андрей</li>
                        <li className="footer-list-item">Email: &nbsp; ykt_andrey@mail.ru</li>
                        <li className="footer-list-item">Телефон: &nbsp; +79142230797</li>
                    </ul>
                </div>
            </div>
            <p className="footer-info">
                ООО  тут должно быть что то на капеталистическом
            </p>
        </footer>
    )
}
