//@ts-ignore
import styles from "./index.module.css"
import React from "react"

interface AuthButtonProps {
  text: string
}

export default function AuthButton(props: AuthButtonProps) {
  return (
    <React.Fragment>
      <div className="d-flex justify-content-center">
        <button
          type="button"
          className={`btn btn-success btn-block btn-lg gradient-custom-4 text-body ${styles.auth_button}`}
        >
          {props.text}
        </button>
      </div>
    </React.Fragment>
  )
}
