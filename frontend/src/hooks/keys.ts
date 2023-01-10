import React, { useState } from 'react'


export const useKey = (initialKey: number): [number, () => void] => {
    const [key, setKey] = useState(initialKey)
    const incrementKey = () => {
        setKey((prevKey) => {
            return prevKey + 1
        })
    }

    return [key, incrementKey]
}