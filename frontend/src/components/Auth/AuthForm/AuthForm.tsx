import React, { useRef, useState } from "react"
// @ts-ignore 
import styles from './AuthForm.module.css'

import AuthButton from "../AuthButton/AuthButton"

interface AuthFormData {
    name: string
    surname: string
    email: string
    phone: string
}


export default function AuthForm() {
    const nameInput = useRef<HTMLInputElement>(null)
    const surnameInput = useRef<HTMLInputElement>(null)
    const emailInput = useRef<HTMLInputElement>(null)
    const phoneInput = useRef<HTMLInputElement>(null)

    const [errorMessages, setErrorMessages] = useState<string[]>()
    const [inputNamesQueue, setInputNamesQueue] = useState<Array<keyof AuthFormData>>([
        "name",
        "surname",
        "email"
    ])
    const [authData, setAuthData] = useState<AuthFormData>({
        name: '',
        surname: '',
        email: '',
        phone: ''
    })

    const buttonClickHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault()

        let currentInputRef: React.RefObject<HTMLInputElement>
        const currentInputName = inputNamesQueue[0]
        switch (currentInputName) {
            case "surname":
                currentInputRef = surnameInput
                break
            case "email":
                currentInputRef = emailInput
                break
            default:
                currentInputRef = nameInput
        }

        if (!currentInputRef.current || !currentInputRef.current.value) {
            // errorMessages
            return
        }

        const currentInputValue = currentInputRef.current.value
        setAuthData((prevAuthData) => {
            return {
                ...prevAuthData,
                [currentInputName]: currentInputValue
            }
        })

        setInputNamesQueue((prevInputQueue) => {
            return prevInputQueue.filter((inputName) => inputName !== currentInputName)
        })
    }

    console.log(authData, inputNamesQueue)
    return (
        <form className={`flex ${styles.auth_form}`}>
            <div className={`flex ${styles.auth_wrapper}`}>
                <label className={`${styles.auth_label}`}>Введите ваше имя</label>
                <input
                    className={`${styles.auth_input}`}
                    type="text"
                    ref={nameInput}
                // onChange={inputChangeHandler}
                />
            </div>
            <div className={`flex ${styles.auth_wrapper} ${styles.hidden}`}>
                <label className={`${styles.auth_label}`}>Введите вашу фамилия</label>
                <input
                    className={`${styles.auth_input}`}
                    type="text"
                    ref={surnameInput}
                />
            </div>
            <div className={`flex ${styles.auth_wrapper} ${styles.hidden}`}>
                <label className={`${styles.auth_label}`}>Введите ваше отчество</label>
                <input
                    className={`${styles.auth_input}`}
                    type="email"
                    ref={emailInput}
                />
            </div>
            <div className={`flex ${styles.auth_wrapper} ${styles.hidden}`}>
                <label className={`${styles.auth_label}`}>Введите ваше отчество</label>
                <input
                    className={`${styles.auth_input}`}
                    type="tel"
                    ref={phoneInput}
                />
            </div>
            <AuthButton clickButtonHandler={buttonClickHandler}>Далее</AuthButton>
        </form>
    )
}
