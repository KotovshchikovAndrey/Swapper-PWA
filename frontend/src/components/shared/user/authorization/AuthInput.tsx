import { AlertTitle, Input, Stack } from "@mui/material"
import React from "react"

interface AuthInputProps {
  label: string
  value: string
  type?: "text" | "password" | "email"
  required?: boolean
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void
}

export default function AuthInput(props: AuthInputProps) {
  return (
    <React.Fragment>
      <Stack marginBottom="30px">
        <Input
          placeholder={props.label}
          value={props.value}
          type={props.type ?? "text"}
          required={props.required ?? true}
          onChange={props.onChange}
          sx={{
            fontSize: "17px",
          }}
        />
        <AlertTitle
          hidden={true}
          color="red"
          sx={{
            margin: 0,
            paddingLeft: "12px",
            fontSize: "14px",
          }}
        >
          Неверное email или пароль!
        </AlertTitle>
      </Stack>
    </React.Fragment>
  )
}
