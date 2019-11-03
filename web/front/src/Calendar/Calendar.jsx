import React from 'react'
import styles from './Calendar.module.scss';
import classNames from 'classnames/bind'
import { connect } from 'react-redux'

const cx = classNames.bind(styles)

class Calendar extends React.Component {
  constructor(props) {
  super(props)
  }

  render() {
    return (
      <div className={cx('wrapper')}>
        Calendar
      </div>
    )
  }
}

function mapStateToProps(state) {
 return {
 } 
}

const connectedComponent = connect(mapStateToProps, {})(Calendar)

export { connectedComponent as Calendar }
