import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import AppPage from './pages/AppPage';
import AboutPage from './pages/AboutPage';
import reportWebVitals from './reportWebVitals';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from 'react-router-dom';

import { Provider } from 'react-redux'
import store from './store';

const Routing = () => {
  return(
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="about">About</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" index element = {<AppPage />} />
          <Route path="/about" element = {<AboutPage />} />
        </Routes>
      </div>
    </Router>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <Routing />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
