import React from 'react'
import PropTypes from 'prop-types'

function Modal({ children, isOpen, closeModal, ...props }) {
	return (
		<>
			{isOpen && <div className="dark-bg" onClick={closeModal}></div>}
			<div className={`modal${isOpen ? ' show' : ''}`} {...props}>
				<span
					className="btn-close rt-corner"
					onClick={closeModal}
				></span>
				{children}
			</div>
		</>
	)
}

function Header(props) {
	return <div className="modal__header" {...props} />
}

function Body(props) {
	return <div className="modal__body" {...props} />
}

Modal.prototype.propTypes = {
	isOpen: PropTypes.bool,
	closeModal: PropTypes.func.isRequired,
}

Modal.Header = Header
Modal.Body = Body

export default Modal