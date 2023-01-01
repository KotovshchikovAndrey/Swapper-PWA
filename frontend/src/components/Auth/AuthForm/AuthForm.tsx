import React, { useRef, useState } from "react"
// @ts-ignore 
import styles from './AuthForm.module.css'

import AuthButton from "../AuthButton/AuthButton"
import AuthInput from "./AuthInput/AuthInput"

import { AuthFormData } from "../authTypes"


export default function AuthForm() {
    const currentInputRef = useRef<HTMLInputElement>(null)

    const [errorMessages, setErrorMessages] = useState<string[]>()
    const [authFormData, setAuthFormData] = useState<AuthFormData>({
        name: '',
        surname: '',
        email: '',
        phone: ''
    })
    const [inputNamesQueue, setInputNamesQueue] = useState<Array<keyof AuthFormData>>([
        "name",
        "surname",
        "email",
        // "phone"
    ])

    const currentInputName = inputNamesQueue[0]
    const buttonClickHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault()

        if (!currentInputRef.current || !currentInputRef.current.value) {
            // errorMessages
            return
        }

        const currentInputValue = currentInputRef.current.value
        setAuthFormData((prevAuthData) => {
            return {
                ...prevAuthData,
                [currentInputName]: currentInputValue
            }
        })

        setInputNamesQueue((prevInputQueue) => {
            return prevInputQueue.filter((inputName) => inputName !== currentInputName)
        })
    }

    return (
        <form className={`flex ${styles.auth_form}`}>
            <AuthInput currentInputName={currentInputName} inputRef={currentInputRef} />
            <AuthButton clickButtonHandler={buttonClickHandler}>Далее</AuthButton>
        </form >
    )
}
