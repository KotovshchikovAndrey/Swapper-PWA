// @ts-ignore
import styles from "./Button.module.css"

import React, { ButtonHTMLAttributes } from "react"

interface AuthButtonInterface extends React.PropsWithChildren {
	onClickHandler: (event: React.MouseEvent<HTMLButtonElement>) => void
}

export default function AuthButton(props: AuthButtonInterface) {
	return (
		<div className={`flex ${styles.auth_button_wrapper}`}>
			<button className={styles.auth_button} onClick={props.onClickHandler}>
				{props.children}
			</button>
		</div>
	)
}
