import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CollegeList from './ReactComps/collegeList'
import HeaderComponent from './ReactComps/navigation'
import StudentList from './ReactComps/studentList'
import Login from './ReactComps/login'

import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class App extends Component {
    state = {
        token : null
    }
    
    componentWillMount(){
        const username = "pranadeep";
        const password = "chandrareddy";
        const hash = Buffer.from(`${username}:${password}`).toString('base64');
        this.setState(prev => ({token: hash}));
    }
    render() {
        return (
          <div className="App">
            <HeaderComponent title = "My App" isLoggedIn = {true}/>
            <React.Fragment>
                <Router>
                    <div>
                        <Route exact path="/" component = {Login}/>
                        <Route exact path="/college" render={props => <CollegeList token={this.state.token} />} />
                        <Route exact path="/college/:id/" render={props => <StudentList token={this.state.token}/>} />
                    </div>
                </Router>
            </React.Fragment>  
          </div>
        );
      }
}

export default App;
