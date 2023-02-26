import React from "react"
import AuthInput from "./AuthInput"
import AuthButton from "components/shared/user/authorization/AuthBotton"
import AgreeCheckbox from "components/ui/checkbox/AgreeCheckbox"
import { Alert } from "@mui/material"
import { useTypedDispatch, useTypedSelector } from "hooks/redux"
import { authActions } from "store/reducers/user"

import AuthService from "services/auth"

export default function AuthForm() {
  const dispatch = useTypedDispatch()

  const [isSuccess, setIsSuccess] = React.useState<boolean>(false)
  const [isValid, setIsValid] = React.useState<boolean>(true)
  const [errorMessages, setErrorMessages] = React.useState<string[]>([])
  const [name, setName] = React.useState<string>("")
  const [email, setEmail] = React.useState<string>("")
  const [password, setPassword] = React.useState<string>("")

  const submitFormHandler = async (event: React.FormEvent) => {
    event.preventDefault()

    const authService = new AuthService(`${process.env.REACT_APP_API_URL}`)
    const user = await authService.register({
      name,
      email,
      password,
    })

    if (!user) {
      console.log(authService.errors)
      setIsValid(false)
      setErrorMessages(authService.errors)

      return
    }

    setIsValid(true)
    setIsSuccess(true)
    dispatch(authActions.setIsAuth(true))
    dispatch(authActions.setUser(user))
  }

  return (
    <React.Fragment>
      <Alert
        severity="success"
        hidden={!isSuccess}
        sx={{
          marginBottom: 3,
        }}
      >
        Вы успешно зарегистрировались!
      </Alert>
      <Alert
        severity="error"
        hidden={isValid}
        sx={{
          marginBottom: 3,
        }}
      >
        {errorMessages.map((error: string) => {
          return <li>{error}</li>
        })}
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
          type="email"
          onChange={(event) => setEmail(event.target.value)}
        />
        <AuthInput
          label="Пароль"
          value={password}
          type="password"
          onChange={(event) => setPassword(event.target.value)}
        />

        <AgreeCheckbox text="I agree all statements in" agreementLink="Terms of service" />
        <AuthButton text="Создать Аккаунт" />
      </form>
    </React.Fragment>
  )
}
