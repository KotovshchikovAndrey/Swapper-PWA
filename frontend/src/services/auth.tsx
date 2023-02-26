import ky, { HTTPError } from "ky"
import { UserLoginDTO, UserRegisterDTO, UserPayloadDTO } from "dto/user"
import { UserResponseDTO } from "dto/response"
import jwt_decode from "jwt-decode"

export default class AuthService {
  private apiUrl: string
  private apiErrors: string[]

  constructor(apiUrl: string) {
    this.apiUrl = apiUrl
    this.apiErrors = []
  }

  async register(userData: UserRegisterDTO) {
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
        await this.setHttpErrorMessages(exc)
      }

      return null
    }
  }

  async login(userData: UserLoginDTO) {
    try {
      const response = await ky.post(`${this.apiUrl}/login`, {
        json: userData,
        mode: "cors",
      })

      const { user, tokens } = await response.json<UserResponseDTO>()
      this.setToken(tokens.access_token)

      return user
    } catch (exc) {
      if (exc instanceof HTTPError) {
        await this.setHttpErrorMessages(exc)
      }

      return null
    }
  }

  private setToken(token: string) {
    localStorage.setItem("accessToken", token)
  }

  private async setHttpErrorMessages(exc: HTTPError) {
    const errorResponse = await exc.response.json()
    const errorMessage: string = errorResponse.message
    this.apiErrors.push(errorMessage)
  }

  static getCurrectUser() {
    const authToken = localStorage.getItem("accessToken")
    if (!authToken) {
      return null
    }

    const currentUser = jwt_decode<UserPayloadDTO>(authToken)

    return currentUser
  }

  get errors() {
    return this.apiErrors
  }
}
