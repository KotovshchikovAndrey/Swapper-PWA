import React from "react"
import AuthInput from "./AuthInput"
import AuthButton from "components/shared/user/Authorization/AuthBotton"
import AgreeCheckbox from "components/ui/checkbox/AgreeCheckbox"

export default function AuthForm() {
  return (
    <React.Fragment>
      <form>
        <AuthInput label="Ваше Имя" />
        <AuthInput label="Ваша Фамилия" />
        <AuthInput label="Ваше Отчество" />
        <AuthInput label="Ваш Вазраст" />

        <AgreeCheckbox text="I agree all statements in" agreementLink="Terms of service" />
        <AuthButton text="Создать Аккаунт" />

        <p className="text-center text-muted mt-5 mb-0">
          Have already an account?{" "}
          <a href="#!" className="fw-bold text-body">
            <u>Login here</u>
          </a>
        </p>
      </form>
    </React.Fragment>
  )
}
