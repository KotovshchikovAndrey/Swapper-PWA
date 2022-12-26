import React from "react"
import './Notifications.css'

export default function Notifications() {
    return (
        <section className="section">
            <h2 className="section-title notifications-section-title">Email Уведомления</h2>
            <div className="flex notifications-conteiner container">
                <div className="notify-wrapper">
                    <p className="notifications-text">
                        Подключите уведомления, <br /> чтобы не пропустить выгодные сваппы
                    </p>
                    <form className="flex notify-form" action="">
                        <label className="notify-label" htmlFor="notify-input">
                            Введите ваш email
                        </label>
                        <input className="notify-input" type="text" />
                    </form>
                </div>
                <img className="notifications-img" src="http://localhost/images/notifications.jpg" alt="notifications" />
            </div>
        </section>
    )
}