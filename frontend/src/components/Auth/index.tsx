// @ts-ignore
import styles from "./index.module.css"
// @ts-ignore
import animations from "../../animations/Animations.module.css"

// React inports
import React from "react"
import { Link } from "react-router-dom"

import AuthForm from "./Form"
// import AuthFormData from "./FormData/FormData"
import Footer from "../UI/Footer"

export default function Auth() {
	return (
		<React.Fragment>
			<section className={`${styles.auth_section}`}>
				<Link to="/" className={styles.auth_link}>
					Главная
				</Link>
				<div className="container">
					<h2 className={`${styles.auth_title} ${animations.appearance}`}>
						Добро пожаловать в Swapper!
					</h2>
					<p
						className={`
                        ${styles.auth_text} 
                        ${animations.appearance} 
                        ${animations.appearance_delay}
                    `}
					>
						Чтобы начать пользоваться приложением <br />
						вам необходимо зарегистрироваться
					</p>
					<AuthForm />
					{/* <AuthFormData /> */}
				</div>
			</section>
			<Footer />
		</React.Fragment>
	)
}
