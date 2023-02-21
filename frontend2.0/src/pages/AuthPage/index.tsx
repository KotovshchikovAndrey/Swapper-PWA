import React from "react"
import Navbar from "components/ui/navigation/Navbar"
import AuthSection from "./components/AuthSection"
import AuthForm from "components/shared/user/Authorization/AuthForm"
import { Stack } from "@mui/system"

export default function AuthPage() {
  return (
    <React.Fragment>
      <Stack
        className="vh-100"
        sx={{
          backgroundImage:
            "url('https://images.wallpaperscraft.ru/image/single/gradient_raznotsvetnyj_abstraktsiia_204077_3840x2400.jpg')",
        }}
      >
        <Navbar />
        <AuthSection>
          <AuthForm />
        </AuthSection>
      </Stack>
    </React.Fragment>
  )
}
