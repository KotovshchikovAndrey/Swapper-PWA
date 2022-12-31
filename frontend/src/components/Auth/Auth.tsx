import React from "react"
// @ts-ignore 
import styles from "./Auth.module.css"

import Footer from "../UI/Footer/Footer"


export default function Auth() {
    return (
        <React.Fragment>
            <section className={`${styles.auth_section}`}>
                <div className="container">
                    <h2 className={`${styles.auth_title}`}>
                        Добро пожаловать в Swapper!
                    </h2>
                    <p className={`${styles.auth_text}`}>
                        Чтобы начать пользоваться приложением <br />
                        вам необходимо зарегистрироваться
                    </p>
                    <form className={`flex ${styles.auth_form}`}>
                        <label className={`${styles.auth_label}`}>Введите ваше имя</label>
                        <input
                            className={`${styles.auth_input}`}
                            type="text"
                        />
                    </form>
                </div>
            </section>
            <Footer />
        </React.Fragment>
    )
}