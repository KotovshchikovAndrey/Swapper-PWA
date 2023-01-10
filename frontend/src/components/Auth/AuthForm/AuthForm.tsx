import React, { useRef, useState } from "react"

// @ts-ignore 
import styles from './AuthForm.module.css'

import { useTypedDispatch, useTypedSelector } from "../../../hooks/redux"
import { useKey } from "../../../hooks/keys"
import { setAuthData } from "../../../store/reducers/auth"

import AuthButton from "../AuthButton/AuthButton"
import AuthInput from "./AuthInput/AuthInput"

import { AuthFormData } from "../../../store/reducers/auth"

// let render = 0


export default function AuthForm() {
    // console.warn(`render AuthForm is ${++render}`)
    const dispatch = useTypedDispatch()
    const [key, incrementKey] = useKey(0)

    const currentInputRef = useRef<HTMLInputElement>(null)

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

        incrementKey()
    }

    return (
        <form className={`flex ${styles.auth_form}`}>
            <AuthInput key={key} currentInputName={currentInputName} inputRef={currentInputRef} />
            <AuthButton onClickHandler={buttonClickHandler}>Далее</AuthButton>
        </form >
    )
}
