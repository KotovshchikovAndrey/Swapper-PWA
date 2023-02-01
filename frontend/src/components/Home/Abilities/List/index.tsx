import React from "react"
import "./index.css"

import AbilityItem from "../Item"
import { AbilitiesListProps } from "../types"

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
