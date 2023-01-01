import React from "react"
import './AbilitiesList.css'

import AbilityItem from "../AbilityItem/AbilityItem"
import { AbilitiesListProps } from "../propsTypes"


export default function AbilitiesList(props: AbilitiesListProps) {
    return (
        <div className="container">
            <ul className="flex abilities-list">
                {props.abilities.map((ability) => <AbilityItem
                    key={ability.key}
                    imageUrl={ability.imageUrl}
                    abilityDescription={ability.abilityDescription}
                />)}
            </ul>
        </div>
    )
}