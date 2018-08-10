import React, { Component } from 'react';

import './styles.css'



class HeaderComponent extends Component{
    constructor(props){
        super(props)
        this.state = {
            isLoggedIn : this.props.isLoggedIn,
            title : this.props.title,
        };

    }
    toggleIsLoggedIn = () =>{
        this.setState(prev => ({isLoggedIn: !prev.isLoggedIn}))
    }
    render(){
        const {title} = this.props
        const {isLoggedIn} = this.state
        return (

            <React.Fragment>
                <div>
                    <div className="App-header">
                          <span className="navHeader"> {title} </span>
                            <span className = "logout">
                                <div className="menu" onClick={this.toggleIsLoggedIn}>
                                {
                                    isLoggedIn ? <span class="btn btn-primary btn-lg">Logout</span>
                                    : <span class="btn btn-primary btn-lg"> Log In </span>
                                }
                                </div>
                         </span>
                    </div>

                </div>


            </React.Fragment>
        )

    }
}

export default HeaderComponent;