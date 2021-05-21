import PropTypes from 'prop-types'
import React from 'react'
import Select, { components } from 'react-select'
import AsyncSelect from 'react-select/async'

function FormControl({ children }) {
	return <div className="form-control">{children}</div>
}

function Label({ inputValue, ...props }) {
	return (
		<label
			className={`form-control__label${inputValue ? ' active' : ''}`}
			{...props}
		/>
	)
}

Label.prototype.propTypes = {
	inputValue: PropTypes.any.isRequired,
}

function CheckBoxLabel(props) {
	return <label className="form-control__checkbox-label" {...props} />
}

function Input(props) {
	return (
		<input
			className="form-control__input"
			title={props.required ? 'Proszę wypełnij to pole' : ''}
			{...props}
		/>
	)
}

function Textarea({ value, ...props }) {
	return (
		<textarea
			className="form-control__textarea"
			title={props.required ? 'Proszę wypełnij to pole' : ''}
			{...props}
		>
			{value}
		</textarea>
	)
}

function CheckBox({ name, checked, onChange, ...props }) {
	return (
		<>
			<input
				type="checkbox"
				className="form-control__checkbox"
				name={name}
				checked={checked}
				onChange={onChange}
				{...props}
			/>
			<span className="form-control__checkbox-checkmark"></span>
		</>
	)
}

CheckBox.prototype.propTypes = {
	name: PropTypes.string.isRequired,
	checked: PropTypes.bool,
	onChange: PropTypes.func.isRequired,
}

function SelectSearchInput({
	children,
	cx,
	isHidden,
	isDisabled,
	innerRef,

	clearValue,
	getStyles,
	getValue,
	hasValue,
	isMulti,
	isRtl,
	options,
	selectOption,
	setValue,
	selectProps,
	theme,
	...props
}) {
	return (
		<input className="form-control__input" {...props}>
			{children}
		</input>
	)
}

function SelectSingleValue({ children, id, ...props }) {
	return (
		<components.SingleValue {...props}>
			{id ? <div id={id}>{children}</div> : <div>{children}</div>}
		</components.SingleValue>
	)
}

function ChoiceField({
	isNotClearable,
	value,
	choices,
	defaultOptions,
	searchAsync,
	onChange,
	labelValue,
	id,
	...props
}) {
	const handleOnChange = (opt) => onChange(opt?.label || '', opt?.value || '')

	const styles = {
		container: () => ({}),
		control: (_, state) => ({
			display: state.hasValue ? 'flex' : 'block',
			justifyContent: 'start-flex',
			alignItems: 'center',
		}),
		indicatorSeparator: () => ({}),
		indicatorsContainer: () => ({
			zIndex: 2,
			flex: 0,
		}),
		valueContainer: (provided, _) => ({
			...provided,
			padding: 0,
		}),
		menu: (provided, _) => ({
			...provided,
			zIndex: 3,
		}),
	}

	const components = {
		IndicatorSeparator: () => <></>,
		DropdownIndicator: () => <></>,
		Input: SelectSearchInput,
		SingleValue: (provided) => <SelectSingleValue {...provided} id={id} />,
	}

	const loadingMessage = () => 'Ładowanie...'

	const noOptionsMessage = () => 'Nic nie znaleziono'

	if (searchAsync)
		return (
			<>
				<AsyncSelect
					defaultOptions={
						defaultOptions?.length > 0 ? defaultOptions : true
					}
					loadOptions={choices}
					loadingMessage={loadingMessage}
					noOptionsMessage={noOptionsMessage}
					components={components}
					styles={styles}
					placeholder=""
					onChange={handleOnChange}
					isClearable={!isNotClearable}
					hideSelectedOptions
					defaultValue={value}
				/>
				{props.required && (
					<input
						tabIndex={-1}
						autoComplete="off"
						style={{ height: 0, width: 0, opacity: 0 }}
						value={labelValue}
						required
					/>
				)}
			</>
		)

	return (
		<>
			<Select
				options={choices}
				noOptionsMessage={noOptionsMessage}
				components={components}
				styles={styles}
				placeholder=""
				onChange={handleOnChange}
				isClearable={!isNotClearable}
				hideSelectedOptions
				value={
					value
						? choices.filter((choice) => choice.value === value)
						: null
				}
				isLoading={choices.length === 0}
			/>
			{props.required && (
				<input
					tabIndex={-1}
					autoComplete="off"
					style={{ height: 0, width: 0, opacity: 0 }}
					value={labelValue}
					required
				/>
			)}
		</>
	)
}

ChoiceField.prototype.propTypes = {
	isNotClearable: PropTypes.bool,
	searchAsync: PropTypes.bool,
	loadOptions: PropTypes.func,
	defaultOptions: PropTypes.oneOfType([PropTypes.bool, PropTypes.array]),
	choices: PropTypes.arrayOf(
		PropTypes.shape({
			label: PropTypes.string.isRequired,
			value: PropTypes.string.isRequired,
		}).isRequired
	).isRequired,
	labelValue: PropTypes.string.isRequired,
	value: PropTypes.any,
	onChange: PropTypes.func.isRequired,
}

FormControl.Label = Label
FormControl.CheckBoxLabel = CheckBoxLabel
FormControl.Input = Input
FormControl.Textarea = Textarea
FormControl.CheckBox = CheckBox
FormControl.ChoiceField = ChoiceField

export default FormControl
