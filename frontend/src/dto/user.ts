export interface UserRegisterDTO {
  name: string
  email: string
  password: string
}

export interface UserLoginDTO {
  email: string
  password: string
}

export interface UserPayloadDTO {
  id: number
  name: string
  email: string
}
