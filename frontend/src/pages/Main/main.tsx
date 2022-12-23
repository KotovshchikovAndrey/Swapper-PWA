import React from 'react'
import './main.css'
import Header from '../../components/Header/header'
import About from '../../components/About/about'
import AbilitiesList from '../../components/Abilities-List/abilities-list'
import Notifications from '../../components/Notifications/notifications'

export default function MainPage() {
    return (
        <>
            <Header />
            <About />
            <AbilitiesList />
            <Notifications />
        </>
    )
}