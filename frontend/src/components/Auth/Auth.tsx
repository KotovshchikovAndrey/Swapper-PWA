import React from "react"
import { Link } from "react-router-dom"
import { useTypedSelector } from "../../hooks/redux"

// @ts-ignore 
import styles from "./Auth.module.css"
// @ts-ignore 
import animations from "../../Animations.module.css"

import AuthForm from "./AuthForm/AuthForm"
import Footer from "../UI/Footer/Footer"

// let render = 0


export default function Auth() {
    // console.warn(`render Auth is ${++render}`)
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
                    <h2 className={`${styles.auth_title} ${animations.appearance}`}>
                        Добро пожаловать в Swapper!
                    </h2>
                    <p className={`
                        ${styles.auth_text} 
                        ${animations.appearance} 
                        ${animations.appearance_delay}
                    `}>
                        Чтобы начать пользоваться приложением <br />
                        вам необходимо зарегистрироваться
                    </p>
                    <AuthForm />
                    <div className={`flex ${styles.auth_data_wrapper}`}>
                        <ul className={`flex ${styles.auth_data_list} ${styles.auth_text}`}>
                            {authFormData.name &&
                                <li className={`${animations.appearance} ${styles.auth_data_item}`}>
                                    Ваше имя: {authFormData.name}
                                </li>
                            }
                            {authFormData.surname &&
                                <li className={`${animations.appearance} ${styles.auth_data_item}`}>
                                    Ваша фамилия: {authFormData.surname}
                                </li>
                            }
                            {authFormData.email &&
                                <li className={`${animations.appearance} ${styles.auth_data_item}`}>
                                    Ваш email: {authFormData.email}
                                </li>
                            }
                        </ul>
                    </div>
                </div>
            </section>
            <Footer />
        </React.Fragment>
    )
}