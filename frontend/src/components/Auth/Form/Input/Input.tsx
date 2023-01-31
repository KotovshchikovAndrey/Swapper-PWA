// @ts-ignore
import styles from "./Input.module.css"
// @ts-ignore
import animations from "../../../../animations/Animations.module.css"

import React from "react"

export interface AuthInputProps {
	labelText: string
	onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
	className?: string
}

const AuthInput: React.FC<AuthInputProps> = (props: AuthInputProps) => {
	return (
		<div
			className={`flex ${styles.auth_wrapper} ${animations.fade} 
			${props.className ?? ""}`}
		>
			<label className={`${styles.auth_label}`}>{props.labelText}</label>
			<input className={`${styles.auth_input}`} type="text" onChange={props.onChange} />
		</div>
	)
}

export default AuthInput
