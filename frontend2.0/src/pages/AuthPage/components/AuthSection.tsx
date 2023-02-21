import React from "react"

interface AuthSectionProps extends React.PropsWithChildren {}

export default function AuthSection(props: AuthSectionProps) {
  return (
    <section className="vh-100 bg-image">
      <div
        className="mask d-flex align-items-center h-100 gradient-custom-3"
        style={{
          marginTop: "35px",
        }}
      >
        <div className="container h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-9 col-lg-7 col-xl-6">
              <div className="card">
                <div className="card-body p-5">
                  <h2 className="text-uppercase text-center mb-5">Регистрация</h2>
                  {props.children}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
