//@ts-ignore
import animations from "./Animations.module.css"
import "animate.css"

export const FadeInItemsAnimation = (itemsClassName: string) => {
  const manualItems = document.querySelectorAll(`.${itemsClassName}`)
  const scrollHandler = () => {
    manualItems.forEach((element: Element, index: number) => {
      const elementPosition = element.getBoundingClientRect().top + window.scrollY
      if (elementPosition - 800 < window.scrollY) {
        element.classList.add(
          "animate__animated",
          index % 2 === 0 ? "animate__fadeInLeftBig" : "animate__fadeInRightBig",
          "animate__slow",
          animations.visible
        )
      }
    })
  }

  window.onscroll = scrollHandler

  return () => {
    window.onscroll = () => {}
  }
}
