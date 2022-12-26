import React from 'react'
import './Home.css'
import Header from '../../components/Header/Header'
import About from '../../components/About/About'
import Abilities from '../../components/Abilities/Abilities'
import Notifications from '../../components/Notifications/Notifications'

export default function Home() {
    return (
        <>
            <Header />
            <About />
            <Abilities />
            <Notifications />
        </>
    )
}