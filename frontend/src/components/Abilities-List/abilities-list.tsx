import React from "react"
import './abilities-list.css'

export default function AbilitiesList() {
    return (
        <section className="abilities-section">
            <h2 className="section-title">Почему Swapper?</h2>
            <div className="container">
                <ul className="flex abilities-list">
                    <li className="flex ability">
                        <img className="ability-img" src="http://localhost/images/security_and_abilities.png" alt="ability" />
                        {/* <h3 className="ability-title">
                            ability 1   
                        </h3> */}
                        <p className="flex ability-desc">
                            Swapper предоставляет удобную и безопасную площадку
                            для поиска и предоставления услуг
                        </p>
                    </li>
                    <li className="flex ability">
                        <img className="ability-img" src="http://localhost/images/functionality.png" alt="ability" />
                        {/* <h3 className="ability-title">
                            ability 2   
                        </h3> */}
                        <p className="ability-desc">
                            Обширный, простой и интуитивно понятный функционал,
                            который поможет вам легко и удобно совершать обмены
                        </p>
                    </li>
                    <li className="flex ability">
                        <img className="ability-img" src="http://localhost/images/support.png" alt="ability" />
                        {/* <h3 className="ability-title">
                            ability 3  
                        </h3> */}
                        <p className="ability-desc">
                            Круглосуточная техподдержка, готовая помочь вам с любым 
                            вопросом в любое время
                        </p>
                    </li>
                </ul>
            </div>
        </section>
    )
}