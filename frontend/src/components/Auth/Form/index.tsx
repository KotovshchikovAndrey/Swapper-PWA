// @ts-ignore
import styles from "./index.module.css"
// @ts-ignore
import animations from "../../../animations/Animations.module.css"

import React from "react"
import { useTypedDispatch, useTypedSelector } from "../../../hooks/redux"

import AuthButton from "../Button"
import AuthInput from "./Input"

export default function AuthForm() {
	const dispatch = useTypedDispatch()
	const [name, setName] = React.useState("")
	const [surname, setSurname] = React.useState("")
	const [age, setAge] = React.useState(NaN)
	const [email, setEmail] = React.useState("")
	const [patronymic, setPatronymic] = React.useState<string | undefined>("")
	const [password, setPassword] = React.useState("")

	const [currentInputIndex, setCurrentInputIndex] = React.useState(0)

	const AuthInputs = [
		<AuthInput
			key={0}
			labelText="Введите ваше имя"
			onChange={(e) => setName(e.target.value)}
			className={`${animations.fade_delay}`}
		/>,
		<AuthInput
			key={1}
			labelText="Введите вашу фамилия"
			onChange={(e) => setSurname(e.target.value)}
		/>,
		<AuthInput
			key={2}
			labelText="Введите ваш email"
			onChange={(e) => setEmail(e.target.value)}
		/>,
		<AuthInput
			key={3}
			labelText="Введите ваш возраст"
			onChange={(e) => setAge(Number(e.target.value))}
		/>,
		<AuthInput
			key={4}
			labelText="Введите ваше отчество (не обязательно)"
			onChange={(e) => setPatronymic(e.target.value)}
		/>,
		<AuthInput
			key={5}
			labelText="Придумайте пароль"
			onChange={(e) => setPassword(e.target.value)}
		/>,
	]

	const swapInput = () => {
		if (currentInputIndex < AuthInputs.length - 1) {
			setCurrentInputIndex((prevInputIndex: number) => {
				return prevInputIndex + 1
			})
		}
	}

	const buttonClickHandler = (e: React.MouseEvent<HTMLButtonElement>) => {
		e.preventDefault()
		swapInput()
	}

	return (
		<form className={`flex ${styles.auth_form}`}>
			{AuthInputs[currentInputIndex]}
			<AuthButton onClickHandler={buttonClickHandler}>Далее</AuthButton>
		</form>
	)
}
