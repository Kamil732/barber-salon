import { GET_DATA, UPDATE_OR_CREATE_DATA } from '../actions/types'

const initialState = {
	loading: true,
	data: {},
}

// eslint-disable-next-line
export default function (state = initialState, action) {
	switch (action.type) {
		case GET_DATA:
			return {
				loading: false,
				data: {
					...state.data,
					...action.payload,
				},
			}
		case UPDATE_OR_CREATE_DATA:
			return {
				...state,
				data: {
					...state.data,
					[action.payload.name]: action.payload.value,
				},
			}
		default:
			return state
	}
}
