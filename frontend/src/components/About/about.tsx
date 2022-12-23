import React from 'react'
import './about.css'


export default function About() {
    return (
        <section className='about-section'>
            <h2 className='section-title'>
                Как пользоваться Swapper?
            </h2>
            <div className="container flex about-wrapper">
                <div className='flex about-description-wrapper'>
                    <img src='http://localhost/images/doc.png' alt="doc" className='about-description-img' />
                    <p className='about-description-text'>
                        Если вы ищите людей для выгодных барторных отношений,
                        то Swapper - ваш выбор. Чтобы найти свапера - нажмите 
                        "Найти свапера". Для просмотра самых выгодных предложений 
                        за сегодняшний день - перейдите в "Свапы дня". Хотите получить
                        наилучший опыт сотрудничество с людьми с наивысшим рейтингом - нажмите
                        "Рейтинг сваперов".
                    </p>
                </div>
            </div>
        </section>
    )
}