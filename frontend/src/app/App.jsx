import React, { Component } from 'react'
import '../assets/css/main.css'

import { BrowserRouter as Router } from 'react-router-dom'

import Header from '../containers/Header'
import Footer from '../containers/Footer'
import Routes from './Routes'
import { Provider } from 'react-redux'

import store from '../redux/store'
import { loadUser } from '../redux/actions/auth'

class App extends Component {
	componentDidMount() {
		store.dispatch(loadUser())
	}

	render() {
		return (
			<Provider store={store}>
				<Router>
					<Header />

					<div className="content-wrap">
						<Routes />
					</div>

					<Footer />
				</Router>
			</Provider>
		)
	}
}

export default App