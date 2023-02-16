//@ts-ignore
import animations from "./Animations.module.css"
import "animate.css"

export enum FadeType {
  IN_RIGHT = "animate__fadeInRightBig",
  IN_LEFT = "animate__fadeInLeftBig",
}

export function OnScrollFadeInAnimation(
  itemsClassName: string,
  fadeType: FadeType = FadeType.IN_LEFT
) {
  const items = document.querySelectorAll(`.${itemsClassName}`)

  const scrollHandler = (entries: any) => {
    entries.forEach((entry: any) => {
      if (entry.isIntersecting) {
        entry.target.classList.add(
          "animate__animated",
          fadeType,
          "animate__slow",
          animations.visible
        )
      }
    })
  }

  const observer = new IntersectionObserver(scrollHandler)
  for (let i = 0; i < items.length; i++) {
    observer.observe(items[i])
  }

  return () => {
    for (let i = 0; i < items.length; i++) {
      observer.unobserve(items[i])
    }
  }
}
