//@ts-ignore
import telegram from "assets/telegram.png"
//@ts-ignore
import vk from "assets/vk.png"
//@ts-ignore
import whatsapp from "assets/whatsapp.png"
import React from "react"

export default function Footer() {
  return (
    <React.Fragment>
      <footer className="text-center text-white" style={{ backgroundColor: "DodgerBlue" }}>
        <div className="container">
          <section>
            <div className="row text-center d-flex justify-content-center">
              <hr style={{ marginBottom: "54px" }} />
              <div className="col-md-2">
                <h6 className="text-uppercase font-weight-bold">
                  <a href="#!" className="text-white">
                    О Нас
                  </a>
                </h6>
              </div>
              <div className="col-md-2">
                <h6 className="text-uppercase font-weight-bold">
                  <a href="#!" className="text-white">
                    Блог
                  </a>
                </h6>
              </div>
              <div className="col-md-2">
                <h6 className="text-uppercase font-weight-bold">
                  <a href="#!" className="text-white">
                    История создания
                  </a>
                </h6>
              </div>
              <div className="col-md-2">
                <h6 className="text-uppercase font-weight-bold">
                  <a href="#!" className="text-white">
                    Контакты
                  </a>
                </h6>
              </div>
              <div className="col-md-2">
                <h6 className="text-uppercase font-weight-bold">
                  <a href="#!" className="text-white">
                    Техподдержка
                  </a>
                </h6>
              </div>
            </div>
          </section>
          <hr className="my-5" />
          <section className="mb-5">
            <div className="row d-flex justify-content-center">
              <div className="col-lg-8">
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt distinctio earum
                  repellat quaerat voluptatibus placeat nam, commodi optio pariatur est quia magnam
                  eum harum corrupti dicta, aliquam sequi voluptate quas.
                </p>
              </div>
            </div>
          </section>
          <section className="text-center mb-5">
            <a href="" className="text-white me-4">
              <i className="fab fa-facebook-f"></i>
            </a>
            <a href="" className="text-white me-4">
              <i className="fab fa-twitter"></i>
            </a>
            <a href="" className="text-white me-4">
              <i className="fab fa-google"></i>
            </a>
            <a href="" className="text-white me-4">
              <i className="fab fa-instagram"></i>
            </a>
            <a href="" className="text-white me-4">
              <i className="fab fa-linkedin"></i>
            </a>
            <a href="" className="text-white me-4">
              <i className="fab fa-github"></i>
            </a>
          </section>
        </div>
        <div className="text-center p-3" style={{ backgroundColor: "#000000" }}>
          © 2023
          <a className="text-white" href="https://mdbootstrap.com/">
            @Swapper.com
          </a>
        </div>
      </footer>
    </React.Fragment>
  )
}
