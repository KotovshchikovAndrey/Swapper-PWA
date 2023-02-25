import ky, { HTTPError } from "ky"
import IUser from "entities/user"
import { UserResponseDTO } from "dto/response"

export default class AuthService {
  private apiUrl: string
  private apiErrors: string[]

  constructor(apiUrl: string) {
    this.apiUrl = apiUrl
    this.apiErrors = []
  }

  async register(userData: IUser) {
    try {
      const response = await ky.post(`${this.apiUrl}/registration`, {
        json: userData,
        mode: "cors",
      })

      const { user, tokens } = await response.json<UserResponseDTO>()
      this.setToken(tokens.access_token)

      return user
    } catch (exc) {
      if (exc instanceof HTTPError) {
        const errorResponse = await exc.response.json()
        const errorMessage: string = errorResponse.message
        this.apiErrors.push(errorMessage)
      }

      return null
    }
  }

  setToken(token: string) {
    localStorage.setItem("accessToken", token)
  }

  get errors() {
    return this.apiErrors
  }
}
