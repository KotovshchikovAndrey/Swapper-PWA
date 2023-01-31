import React from "react"
import "./Item.css"
import { AbilityItemProps } from "../propsTypes"

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
