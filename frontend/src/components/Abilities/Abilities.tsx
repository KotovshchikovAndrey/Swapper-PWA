import React from "react"
import './Abilities.css'

import AbilitiesList from "./AbilitiesList/AbilitiesList"
import { abilities } from "../../data/static"


export default function Abilities() {
    return (
        <section className="section">
            <h2 className="section-title">Почему Swapper?</h2>
            <AbilitiesList abilities={abilities} />
        </section>
    )
}