import React, { useRef } from "react"
// @ts-ignore 
import styles from './AuthInput.module.css'

import { AuthFormData, AuthInputProps } from "../../authTypes"


export default function AuthInput(props: AuthInputProps) {
    let currentInputText
    switch (props.currentInputName) {
        case "surname":
            currentInputText = "Введите вашу фамилия"
            break
        case "email":
            currentInputText = "Введите ваш email"
            break
        // case "phone":
        //     currentInputText = "Введите ваш номер телефона"
        //     break
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
                ref={props.inputRef}
            />
        </div>
    )
}