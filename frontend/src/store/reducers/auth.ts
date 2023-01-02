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

export const authSlice = createSlice({
    name: 'auth',
    initialState: {
        data: {
            name: '',
            surname: '',
            email: '',
            phone: ''
        },
    },
    reducers: {
        setAuthData: (state, action: Action) => {
            const { key, value } = action.payload
            state.data[key] = value
        }
    },
})

export const { setAuthData } = authSlice.actions

export default authSlice.reducer