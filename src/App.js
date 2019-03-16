import React, { Component } from 'react';
<<<<<<< HEAD
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

const serverURL = 'http://localhost:3000';
const http = axios.create({
  baseURL: serverURL,
});

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isToggleOn : true
    };
    this.test1 = this.test1.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  test1() {
    // http.post("/")
    // .then(() => console.log("works"))
    // .catch((err) => console.log("error"));
  }

=======
import logo from './logo.svg';
import './App.css';

class App extends Component {
>>>>>>> master
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
<<<<<<< HEAD
            <code>Site under construction!</code>.
          </p>
          <button onClick={this.handleClick}>
            {this.state.isToggleOn ? 'ON' : 'OFF'}
          </button>
          <button onClick={this.test1}>
            button test!
          </button>
=======
            <code>Site under construction</code>.
          </p>
>>>>>>> master
        </header>
      </div>
    );
  }
}

export default App;
