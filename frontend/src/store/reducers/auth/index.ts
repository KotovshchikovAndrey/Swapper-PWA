import { createSlice } from "@reduxjs/toolkit"
import IUser from "../../../models/user"
import { AuthState } from "./types"

const initialState: AuthState = {
	user: {} as IUser,
}

export const authSlice = createSlice({
	name: "auth",
	initialState: {
		data: initialState,
	},
	reducers: {
		setAuthData: (state, action: any) => {
			// const { key, value } = action.payload
			// state.data[key] = value
		},

		resetAuthData: (state) => {
			state.data = initialState
		},
	},
})

export const authActions = authSlice.actions

export default authSlice.reducer
