import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

import CardContainer from '../../layout/cards/CardContainer'
import Card from '../../layout/cards/Card'

class Pricing extends Component {
	static propTypes = {
		hair_price: PropTypes.string.isRequired,
		beard_price: PropTypes.string.isRequired,
	}

	render() {
		const { hair_price, beard_price } = this.props

		return (
			<CardContainer>
				<Card>
					<Card.Title>Cena za włosy</Card.Title>
					<Card.Body>
						<h1>
							{hair_price}
							<sub>zł</sub>
						</h1>
					</Card.Body>
				</Card>
				<Card>
					<Card.Title>Cena za brodę</Card.Title>
					<Card.Body>
						<h1>
							{beard_price}
							<sub>zł</sub>
						</h1>
					</Card.Body>
				</Card>
			</CardContainer>
		)
	}
}

const mapStateToProps = (state) => ({
	hair_price: state.data.data.hair_price,
	beard_price: state.data.data.beard_price,
})

export default connect(mapStateToProps, null)(Pricing)