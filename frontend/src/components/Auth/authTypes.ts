import React from "react"

export interface AuthFormData {
    name: string
    surname: string
    email: string
    phone: string
}

export interface AuthInputProps {
    currentInputName: keyof AuthFormData
    inputRef: React.RefObject<HTMLInputElement>
}