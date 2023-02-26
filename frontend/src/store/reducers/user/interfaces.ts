import IUser from "entities/user"

export interface UserState {
  user: IUser
  isAuth: boolean
}
