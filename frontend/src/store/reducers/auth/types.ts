import IUser from "../../../models/user"

export interface AuthState {
	user: IUser
}

export interface setUserAction {
	payload: IUser
}
// // Auth Actions
// export interface SetNameAction {
// 	payload: string
// }

// export interface SetSurnameAction {
// 	payload: string
// }

// export interface SetEmailAction {
// 	payload: string
// }

// export interface SetAgeAction {
// 	payload: number
// }

// export interface SetPasswordAction {
// 	payload: string
// }

// export interface SetPatronymicAction {
// 	payload?: string
// }

// export interface SetPhoneAction {
// 	payload?: string
// }

// export type AuthAction =
// 	| SetNameAction
// 	| SetSurnameAction
// 	| SetEmailAction
// 	| SetAgeAction
// 	| SetPasswordAction
// 	| SetPatronymicAction
// 	| SetPhoneAction

// export enum AuthAction {
// 	SET_NAME = "SET_NAME",
// 	SET_SURNAME = "SET_SURNAME",
// 	SET_EMAIL = "SET_EMAIL",
// 	SET_AGE = "SET_AGE",
// 	SET_PASSWORD = "SET_PASSWORD",
// 	SET_PATRONYMIC = "SET_PATRONYMIC",
// 	SET_PHONE = "SET_PHONE",
// }
