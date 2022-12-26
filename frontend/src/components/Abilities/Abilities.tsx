import React from "react"
import './Abilities.css'
import AbilitiesList from "./AbilitiesList/AbilitiesList"


export default function Abilities() {
    return (
        <section className="section">
            <h2 className="section-title">Почему Swapper?</h2>
            <AbilitiesList />
        </section>
    )
}