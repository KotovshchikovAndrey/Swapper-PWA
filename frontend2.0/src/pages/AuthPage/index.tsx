import React from "react"
import AuthSection from "./components/AuthSection"
import AuthForm from "components/shared/user/Authorization/AuthForm"

export default function AuthPage() {
  return (
    <React.Fragment>
      <AuthSection>
        <AuthForm />
      </AuthSection>
    </React.Fragment>
  )
}
