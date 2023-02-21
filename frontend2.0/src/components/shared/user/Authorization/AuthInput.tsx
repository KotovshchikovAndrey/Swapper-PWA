import { AlertTitle } from "@mui/material"
import React from "react"

interface AuthInputProps {
  label: string
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void
  value: any
}

export default function AuthInput(props: AuthInputProps) {
  return (
    <React.Fragment>
      <div className="form-outline mb-4">
        <input
          type="text"
          className="form-control form-control-lg"
          value={props.value}
          onChange={props.onChange}
        />
        <label className="form-label">{props.label}</label>
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
      </div>
    </React.Fragment>
  )
}
