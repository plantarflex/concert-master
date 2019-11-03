import React from 'react'
import logo from './logo.svg';
import styles from './App.module.scss';
import classNames from 'classnames/bind'
import { connect } from 'react-redux'
import { Calendar } from './Calendar'
import { Controller } from './Controller'
import { Nav } from './Nav'

const cx = classNames.bind(styles)

class App extends React.Component {
  constructor(props) {
  super(props)
  }

  render() {
    return (
      <div className={cx('wrapper')}>
        <Nav />
        <Controller />
        <Calendar />
      </div>
    )
  }
}


export default App;
