import React, { useRef, useState } from "react"
import { useTypedDispatch, useTypedSelector } from "../../../hooks/redux"
import { setAuthData } from "../../../store/reducers/auth"
// @ts-ignore 
import styles from './AuthForm.module.css'

import AuthButton from "../AuthButton/AuthButton"
import AuthInput from "./AuthInput/AuthInput"

import { AuthFormData } from "../../../store/reducers/auth"


export default function AuthForm() {
    const currentInputRef = useRef<HTMLInputElement>(null)

    const authFormData = useTypedSelector((state) => state.auth.data)
    const dispatch = useTypedDispatch()

    const [errorMessages, setErrorMessages] = useState<string[]>()
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
        dispatch(setAuthData({
            key: currentInputName,
            value: currentInputValue
        }))

        setInputNamesQueue((prevInputQueue) => {
            return prevInputQueue.filter((inputName) => inputName !== currentInputName)
        })
    }

    return (
        <form className={`flex ${styles.auth_form}`}>
            <AuthInput currentInputName={currentInputName} inputRef={currentInputRef} />
            <AuthButton onClickHandler={buttonClickHandler}>Далее</AuthButton>
        </form >
    )
}
