import React from "react"
import './AbilityItem.css'


interface AbilityItemProps {
    imageUrl: string,
    abilityDescription: string
}


export default function AbilityItem(props: AbilityItemProps) {
    return (
        <li className="flex ability">
            <img className="ability-img" src={props.imageUrl} alt="ability" />
            {/* <h3 className="ability-title">
                            ability 1   
                        </h3> */}
            <p className="flex ability-desc">{props.abilityDescription}</p>
        </li>
    )
}