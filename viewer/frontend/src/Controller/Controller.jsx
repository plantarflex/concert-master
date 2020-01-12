import React from 'react'
import styles from './Controller.module.scss';
import classNames from 'classnames/bind'
import { connect } from 'react-redux'

const cx = classNames.bind(styles)

class Controller extends React.Component {
  constructor(props) {
  super(props)
  }

  render() {
    return (
      <div className={cx('wrapper')}>
        Controller
      </div>
    )
  }
}

function mapStateToProps(state){
  return {
  }
}

const connectedComponent = connect(mapStateToProps, {

})(Controller)

export { connectedComponent as Controller }
