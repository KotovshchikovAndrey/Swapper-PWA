import IUser from "entities/user"
import ITokenPair from "entities/token"

export interface UserResponseDTO {
  user: IUser
  tokens: ITokenPair
}
