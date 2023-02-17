import React from "react"

interface AuthInputProps {
  label: string
}

export default function AuthInput(props: AuthInputProps) {
  return (
    <React.Fragment>
      <div className="form-outline mb-4">
        <input type="text" className="form-control form-control-lg" />
        <label className="form-label">{props.label}</label>
      </div>
    </React.Fragment>
  )
}
