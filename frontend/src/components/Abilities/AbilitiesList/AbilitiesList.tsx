import React from "react"
import './AbilitiesList.css'
import AbilityItem from "../AbilityItem/AbilityItem"


export default function AbilitiesList() {
    return (
        <div className="container">
            <ul className="flex abilities-list">
                <AbilityItem
                    imageUrl="http://localhost/images/security_and_abilities.png"
                    abilityDescription="Swapper предоставляет удобную и безопасную площадку
                        для поиска и предоставления услуг"
                />
                <AbilityItem
                    imageUrl="http://localhost/images/functionality.png"
                    abilityDescription="Обширный, простой и интуитивно понятный функционал,
                        который поможет вам легко и удобно совершать обмены"
                />
                <AbilityItem
                    imageUrl="http://localhost/images/support.png"
                    abilityDescription="Круглосуточная техподдержка, готовая помочь вам с любым
                    вопросом в любое время"
                />
            </ul>
        </div>
    )
}