import React from "react"
import AuthInput from "./AuthInput"
import AuthButton from "components/shared/user/Authorization/AuthBotton"
import AgreeCheckbox from "components/ui/checkbox/AgreeCheckbox"
import { Alert } from "@mui/material"

import AuthService from "services/auth"

export default function AuthForm() {
  const [errorMessages, setErrorMessages] = React.useState<string[]>([])
  const [name, setName] = React.useState<string>("")
  const [email, setEmail] = React.useState<string>("")
  const [password, setPassword] = React.useState<string>("")

  const submitFormHandler = async (event: React.FormEvent) => {
    event.preventDefault()

    const authService = new AuthService(`${process.env.REACT_APP_API_URL}`)
    await authService.register({
      name,
      email,
      password,
    })
  }

  return (
    <React.Fragment>
      <Alert
        severity="error"
        hidden={true}
        sx={{
          marginBottom: 3,
        }}
      >
        This is an error alert — check it out!
      </Alert>
      <form id="auth-form" onSubmit={submitFormHandler}>
        <AuthInput
          label="Ваше Имя"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
        <AuthInput
          label="Ваш Email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
        />
        <AuthInput
          label="Пароль"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />

        <AgreeCheckbox text="I agree all statements in" agreementLink="Terms of service" />
        <AuthButton text="Создать Аккаунт" />
      </form>
    </React.Fragment>
  )
}
