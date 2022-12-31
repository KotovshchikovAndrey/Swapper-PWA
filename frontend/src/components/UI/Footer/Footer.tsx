import React from 'react'
import './Footer.css'

import Navbar from '../Navbar/Navbar'
import { navList, contactsList } from '../../../data/static'


export default function Footer() {
    return (
        <footer className="footer">
            <div className="flex container footer-container">
                <div className="footer-nav">
                    <h2 className="footer-nav-title">@Swapper</h2>
                    <Navbar
                        navList={navList}
                        className="flex footer-nav-list footer-list"
                        itemClassName="footer-list-item"
                    >
                        <li className="footer-list-title">Навигация:</li>
                    </Navbar>
                </div>
                <div className="footer-contacts">
                    <Navbar
                        navList={contactsList}
                        className="flex footer-nav-list footer-list"
                        itemClassName="footer-list-item"
                    >
                        <li className="footer-list-title">Контакты:</li>
                    </Navbar>
                </div>
            </div>
            <p className="footer-info">
                ООО  тут должно быть что то на капеталистическом
            </p>
        </footer>
    )
}
