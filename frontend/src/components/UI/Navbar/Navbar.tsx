import React from 'react'
import './Navbar.css'

interface NavbarProps extends React.PropsWithChildren {
    navList: string[]
    className?: string
    itemClassName?: string
}


export default function Navbar(props: NavbarProps) {
    return (
        <nav className="nav">
            <div className="container">
                <ul className={`${props.className ?? "nav-list flex"}`}>
                    {props.children}
                    {props.navList.map((key, index) =>
                        <li key={key} className={`${props.itemClassName ?? "nav-link"}`}>
                            {props.navList[index]}
                        </li>
                    )}
                </ul>
            </div >
        </nav>
    )
}