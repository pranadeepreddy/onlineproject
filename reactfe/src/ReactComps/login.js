import React,{Component} from 'react'

class Login extends Component{

    state = { 
        name : '',
        pass : ''
    };

    saveName=(event)=>{

        const {target :{value}} = event;
        this.setState({
            name:value
        });

    }

    savePass = (event)=>{

        const {target :{value}} = event;
        this.setState({
            pass:value
        });
    }

    submit = (e) =>{

        const{name,pass} = this.state;
        const hash = Buffer.from(`${name}:${pass}`).toString('base64');
//        fetch("http://localhost:8080/api-auth/",{
//
//            method:'post',
//            headers:{
//                "Content-type":"application/x-www-form-urlencoded; charset=UTF-8"
//            },
//
//            body:'username = ${name}&password=${pass}'
//            })
//            .then(res=>res.json())
//            .then(response=>{
//
//                console.log('response',response);
//            })
//            .catch(e => {console.log (e);});
        }

        render(){

            return(<div>

                <input onChange = {this.saveName} name = "name"/>
                <br/>
                <input onChange = {this.savePass} name = "pass"/>
                <br/>

                <button onClick={this.submit}>Submit</button>
                </div>)

        }

}

                   
export default Login;                   