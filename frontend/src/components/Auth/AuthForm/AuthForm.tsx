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
    const currentInput = useRef<HTMLInputElement>(null)

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

    const currentInputName = inputNamesQueue[0]
    const buttonClickHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault()

        if (!currentInput.current || !currentInput.current.value) {
            // errorMessages
            return
        }

        const currentInputValue = currentInput.current.value
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

    const getCurrentInput = () => {
        let currentInputText
        switch (currentInputName) {
            case "surname":
                currentInputText = "Введите вашу фамилия"
                break
            case "email":
                currentInputText = "Введите ваш email"
                break
            default:
                currentInputText = "Введите ваше имя"
        }

        // need refactor key generation
        return (
            <div key={Math.random()} className={`flex ${styles.auth_wrapper} ${styles.fade}`}>
                <label className={`${styles.auth_label}`}>{currentInputText}</label>
                <input
                    className={`${styles.auth_input}`}
                    type="text"
                    ref={currentInput}
                />
            </div>
        )
    }

    return (
        <form className={`flex ${styles.auth_form}`}>
            {getCurrentInput()}
            <AuthButton clickButtonHandler={buttonClickHandler}>Далее</AuthButton>
        </form >
    )
}
