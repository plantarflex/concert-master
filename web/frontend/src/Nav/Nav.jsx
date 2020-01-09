import styles from './Nav.module.scss'

import { connect } from 'react-redux'
import React from 'react'
import classNames from 'classnames/bind'


const cx = classNames.bind(styles)

class Nav extends React.Component {
  constructor(props){
    super(props)
  }

  render(){
    return (
      <div className={cx('wrapper')}>
        Nav
      </div>
    )
  }
}

function mapStateToProps(state) {
  return {
  }

}

const connectedComponent = connect(
  mapStateToProps, {}
)(Nav)

export { connectedComponent as Nav }
