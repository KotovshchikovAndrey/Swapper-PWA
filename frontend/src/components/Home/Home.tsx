import React from 'react'
import './Home.css'

import Header from './Header/Header'
import About from './About/About'
import Abilities from './Abilities/Abilities'
import Notifications from './Notifications/Notifications'
import Footer from '../UI/Footer/Footer'


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