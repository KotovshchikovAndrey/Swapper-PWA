import { createSlice } from '@reduxjs/toolkit'

export const counterSlice = createSlice({
    name: 'test',
    initialState: {
        value: 0,
    },
    reducers: {
        set: (state, action) => {
            state.value = 100
        }
    },
})

export const { set } = counterSlice.actions

export default counterSlice.reducer