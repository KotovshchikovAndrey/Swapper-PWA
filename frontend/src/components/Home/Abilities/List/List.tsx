import React from "react"
import "./List.css"

import AbilityItem from "../Item/Item"
import { AbilitiesListProps } from "../propsTypes"

export default function AbilitiesList(props: AbilitiesListProps) {
	return (
		<div className="container">
			<ul className="flex abilities-list">
				{props.abilities.map((ability) => (
					<AbilityItem
						key={ability.key}
						imageUrl={ability.imageUrl}
						abilityDescription={ability.abilityDescription}
					/>
				))}
			</ul>
		</div>
	)
}
