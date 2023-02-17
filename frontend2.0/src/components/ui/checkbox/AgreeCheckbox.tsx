import React from "react"

interface AgreeCheckboxProps {
  text: string
  agreementLink: string
}

export default function AgreeCheckbox(props: AgreeCheckboxProps) {
  return (
    <React.Fragment>
      <div className="form-check d-flex justify-content-center mb-5">
        <input className="form-check-input me-2" type="checkbox" />
        <label className="form-check-label">
          {props.text}{" "}
          <a href="#!" className="text-body">
            <u>{props.agreementLink}</u>
          </a>
        </label>
      </div>
    </React.Fragment>
  )
}
