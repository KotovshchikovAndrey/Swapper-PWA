import React from 'react'
import './Home.css'

import Header from '../../components/Header/Header'
import About from '../../components/About/About'
import Abilities from '../../components/Abilities/Abilities'
import Notifications from '../../components/Notifications/Notifications'
import Footer from '../../components/Footer/Footer'


export default function Home() {
    return (
        <React.Fragment>
            <Header />
            <About />
            <Abilities />
            <Notifications />
            <Footer />
        </React.Fragment>
    )
}