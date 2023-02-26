import React from "react"
import Navbar from "components/ui/navigation/Navbar"
import AuthSection from "../../components/shared/user/authorization/AuthSection"
import RegistrationForm from "./components/RegistrationForm"
import { Stack } from "@mui/system"

export default function Registration() {
  return (
    <React.Fragment>
      <Stack
        className="vh-100"
        sx={{
          backgroundImage:
            "url('https://kartinkin.net/pics/uploads/posts/2022-08/1661270295_1-kartinkin-net-p-fon-bez-risunka-odnotonnii-krasivo-1.jpg')",
        }}
      >
        <Navbar />
        <AuthSection>
          <RegistrationForm />
        </AuthSection>
      </Stack>
    </React.Fragment>
  )
}
