import React, { Component } from 'react';

class StudentList extends Component {

    state ={
        studentList : [],
        token : this.props.token,

    }
    componentDidMount(){
        fetch('http://127.0.0.1:8000/onlineapp/colleges_/' + this.props.match.params.id + '/', { 
           method: 'get', 
           headers: new Headers({
             'Authorization': `Basic ${this.state.token}`,
             'Content-Type': 'application/x-www-form-urlencoded',
           }), 
         })
         .then(response => response.json())
        .then(responseJson => {
        this.setState({ studentList : responseJson});
        })
        .catch(e => {console.log (e);});
        
        
//        fetch('http://127.0.0.1:8000/onlineapp/colleges_/' + this.props.match.params.id + '/')
//        .then(response => response.json())
//        .then(responseJson => {
//        this.setState({ studentList : responseJson});
//        })
//        .catch(e => {console.log (e);});
    }


    render(){
    return(
        <React.Fragment>
            <div>
                <table>
                    <thead>
                        <th>Name</th>
                        <th>Db Name</th>
                        <th>Email</th>
                        <th>Action</th>
                    </thead>
                    <tbody>
                    {this.state.studentList.map(item => (
                        <tr key={item.id}>
                            <td>{item.name}</td>
                            <td>{item.db_folder}</td>
                            <td>{item.email}</td>
                        </tr>

                    ))}
                    </tbody>

                </table>
            </div>
        </React.Fragment>
        );
    }
}

export default StudentList
