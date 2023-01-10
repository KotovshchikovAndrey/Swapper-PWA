import { createSlice } from '@reduxjs/toolkit'

export interface AuthFormData {
    name: string
    surname: string
    email: string
    phone: string
}

interface Action {
    payload: {
        key: keyof AuthFormData,
        value: string
    }
    type: string
}

const initialAuthData: AuthFormData = {
    name: '',
    surname: '',
    email: '',
    phone: ''
}

export const authSlice = createSlice({
    name: 'auth',
    initialState: {
        data: initialAuthData
    },
    reducers: {
        setAuthData: (state, action: Action) => {
            const { key, value } = action.payload
            state.data[key] = value
        },

        resetAuthData: (state) => {
            state.data = initialAuthData
        }
    },
})

export const { setAuthData, resetAuthData } = authSlice.actions

export default authSlice.reducer