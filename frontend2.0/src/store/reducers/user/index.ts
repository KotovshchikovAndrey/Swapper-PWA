import { createSlice, PayloadAction } from "@reduxjs/toolkit"
import { UserState } from "./interfaces"
import IUser from "entities/user"

const initialState: UserState = {
  user: {} as IUser,
  isAuth: false,
}

export const userSlice = createSlice({
  name: "user",
  initialState: {
    value: initialState,
  },
  reducers: {
    setUser: (state, action: PayloadAction<IUser>) => {
      state.value.user = action.payload
    },

    setIsAuth: (state, action: PayloadAction<boolean>) => {
      state.value.isAuth = action.payload
    },
  },
})

export const authActions = userSlice.actions

export default userSlice.reducer
