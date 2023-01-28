import React from "react"

// @ts-ignore
import styles from "./AuthInput.module.css"
// @ts-ignore
import animations from "../../../../Animations.module.css"

import { AuthFormData } from "../../../../store/reducers/auth"
import { authInputsText } from "../../../../data/static"

interface AuthInputProps {
	currentInputName: keyof AuthFormData
	inputRef: React.RefObject<HTMLInputElement>
}

// let render = 0

export default function AuthInput(props: AuthInputProps) {
	// console.warn(`render AuthInput is ${++render}`)
	const currentInputName = props.currentInputName
	const currentInputText = authInputsText[currentInputName]

	return (
		<div
			className={`flex ${styles.auth_wrapper} ${animations.fade} 
            ${currentInputName === "name" && animations.fade_delay}`}
		>
			<label className={`${styles.auth_label}`}>{currentInputText}</label>
			<input className={`${styles.auth_input}`} type="text" ref={props.inputRef} />
		</div>
	)
}
