import React, { useRef } from "react"

// @ts-ignore 
import styles from './AuthInput.module.css'
// @ts-ignore 
import animations from '../../../../Animations.module.css'

import { AuthFormData } from "../../../../store/reducers/auth"

interface AuthInputProps {
    currentInputName: keyof AuthFormData
    inputRef: React.RefObject<HTMLInputElement>
}

// let render = 0


export default function AuthInput(props: AuthInputProps) {
    // console.warn(`render AuthInput is ${++render}`)

    let currentInputText
    const currentInputName = props.currentInputName
    switch (currentInputName) {
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
        <div
            key={Math.random()}
            className={`flex ${styles.auth_wrapper} ${animations.fade} 
            ${currentInputName === "name" && animations.fade_delay}`}
        >
            <label className={`${styles.auth_label}`}>{currentInputText}</label>
            <input
                className={`${styles.auth_input}`}
                type="text"
                ref={props.inputRef}
            />
        </div>
    )
}