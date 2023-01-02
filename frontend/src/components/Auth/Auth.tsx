import React from "react"
import { Link } from "react-router-dom"
import { useTypedSelector } from "../../hooks/redux"
// @ts-ignore 
import styles from "./Auth.module.css"

import AuthForm from "./AuthForm/AuthForm"
import Footer from "../UI/Footer/Footer"


export default function Auth() {
    const authFormData = useTypedSelector((state) => state.auth.data)

    return (
        <React.Fragment>
            <section className={`${styles.auth_section}`}>
                <Link to="/" style={{
                    color: "black",
                    display: "block",
                    padding: "10px 0 0 20px",
                    textDecoration: "none",
                    font: "inherit",
                    fontSize: 20
                }}>
                    Главная
                </Link>
                <div className="container">
                    <h2 className={`${styles.auth_title}`}>
                        Добро пожаловать в Swapper!
                    </h2>
                    <p className={`${styles.auth_text}`}>
                        Чтобы начать пользоваться приложением <br />
                        вам необходимо зарегистрироваться
                    </p>
                    <AuthForm />
                </div>
            </section>
            <Footer />
        </React.Fragment>
    )
}