import { createSlice } from "@reduxjs/toolkit"
import { UserState } from "./interfaces"
import IUser from "entities/user"

const initialState: UserState = {
  user: {} as IUser,
}

export const userSlice = createSlice({
  name: "user",
  initialState: {
    data: initialState,
  },
  reducers: {
    setUserData: (state, action: any) => {},
  },
})

export const authActions = userSlice.actions

export default userSlice.reducer
