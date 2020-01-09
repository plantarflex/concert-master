import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import React from 'react'
import styles from './Calendar.module.scss'
import classNames from 'classnames/bind'
import { connect } from 'react-redux'
import './Calendar.scss'
const cx = classNames.bind(styles)

class Calendar extends React.Component {
  constructor(props) {
  super(props)
  }

  render() {
    return (
      <div className={cx('wrapper')}>
        <FullCalendar
          defaultView="dayGridMonth"
          plugins={[ dayGridPlugin ]}
          />
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
