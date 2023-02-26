import React from "react"
import AuthInput from "components/shared/user/authorization/AuthInput"
import AuthButton from "components/shared/user/authorization/AuthBotton"
import AgreeCheckbox from "components/ui/checkbox/AgreeCheckbox"
import { Alert } from "@mui/material"
import { useTypedDispatch } from "hooks/redux"
import { authActions } from "store/reducers/user"
import { Link, useNavigate } from "react-router-dom"

import AuthService from "services/auth"

export default function RegistrationForm() {
  const navigate = useNavigate()
  const dispatch = useTypedDispatch()

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
      setIsValid(false)
      setErrorMessages(authService.errors)

      return
    }

    dispatch(authActions.setIsAuth(true))
    dispatch(authActions.setUser(user))

    navigate("/")
  }

  return (
    <React.Fragment>
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

        <AgreeCheckbox
          text="Я ознакомлен и согласен с"
          agreementLink="Пользовательским соглашением"
        />
        <AuthButton text="Создать Аккаунт" />
        <Link to="/login">
          <a
            style={{
              display: "block",
              marginTop: "20px",
              textAlign: "right",
            }}
          >
            Уже зарегистрированы?
          </a>
        </Link>
      </form>
    </React.Fragment>
  )
}
