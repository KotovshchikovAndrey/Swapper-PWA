import React from "react"
import "./index.css"

import { aboutDescription } from "../../../data/static"

export default function About() {
	return (
		<section className="section">
			<h2 className="section-title">Как пользоваться Swapper?</h2>
			<div className="container flex about-wrapper">
				<div className="flex about-description-wrapper">
					<img
						src="http://localhost/images/doc.png"
						alt="doc"
						className="about-description-img"
					/>
					<p className="about-description-text">{aboutDescription}</p>
				</div>
			</div>
		</section>
	)
}
