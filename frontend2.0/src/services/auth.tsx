import ky, { HTTPError } from "ky"
import IUser from "entities/user"

export default class AuthService {
  private apiUrl: string
  private apiErrors: string[]

  constructor(apiUrl: string) {
    this.apiUrl = apiUrl
    this.apiErrors = []
  }

  async register(user: IUser) {
    try {
      const response = await ky.post(`${this.apiUrl}/registration`, { json: user, mode: "cors" })
      const data = await response.json()
    } catch (err) {
      if (err instanceof HTTPError) {
        const errorResponse = await err.response.json()
        const errorMessages: string[] = errorResponse.details
        this.apiErrors.push(...errorMessages)
      }
    }

    return null
  }

  get errors() {
    return this.apiErrors
  }
}
