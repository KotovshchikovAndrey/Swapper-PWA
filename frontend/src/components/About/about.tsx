import React from 'react'
import './about.css'


export default function About() {
    return (
        <section className='about-section'>
            <div className="container flex about-wrapper">
                <h2 className='about-title'>
                    Как пользоваться Swapper?
                </h2>
                <div className='flex about-description-wrapper'>
                    <img src='http://localhost/images/doc.jpg' alt="1111" className='about-description-img' />
                    <p className='about-description-text'>
                        Lorem ipsum dolor sit amet consectetur
                        adipisicing elit. Hic, similique unde
                        perferendis nostrum maxime sit eveniet
                        tenetur molestiae accusantium neque
                        dolorem autem cum quia error.
                        Ipsum nesciunt earum non consequuntur.
                    </p>
                </div>
            </div>
        </section>
    )
}