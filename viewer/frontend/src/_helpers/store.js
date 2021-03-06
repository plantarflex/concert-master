import rootReducer from '../_reducers'
//import requestMiddleWare from './requestMiddleware'

import { createStore, applyMiddleware } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { createLogger } from 'redux-logger'


const loggerMiddleware = createLogger()

export const store = createStore(
  rootReducer, applyMiddleware(
  thunkMiddleware,
  loggerMiddleware
  )
)
