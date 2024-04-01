import React from "react";
import ReactDOM from "react-dom/client"
import './index.css'
function Login()
{
	const[logData,setLogData]=React.useState({
		username:"",
		password:""
	})
	
    function sub(event)
    {
		
       	setLogData(prev=>{
		return{
			...prev,
			[event.target.name]:event.target.value
			
		}
		
	   })
	  
    }
	function sub1(event)
	{
		event.preventDefault()
		fetch('http://localhost:5000/login',{
			method:'POST',
			headers:
			{
				'Content-Type':'application/json'
			},
			body:JSON.stringify(logData)
		})
		
		.then(response=>response.json())
		.then(data=>{
			console.log('Success',data)
		})
		.catch(error=>{
			console.error('Error',error)
		})
		
	}
    return(
        <div className="container">
		<h2 className="form-group">Login</h2>
		<form onSubmit={sub1}>
			<div className="form-group">
				<label htmlFor="username">Username:</label>
				<input 
				type="text" 
				id="username" 
				name="username" 
				onChange={sub}
				value={logData.username}
				required/>
			</div>
			<div className="form-group">
				<label htmlFor="password">Password:</label>
				<input 
				type="password" 
				id="password" 
				name="password" 
				onChange={sub}
				value={logData.password}
				required/>
			</div>

			<div className="form-group">
				<button type="submit" className = "login-button">Login</button>
			</div>
           
		</form>
	    </div>
    )
    
}
ReactDOM.createRoot(document.getElementById("root")).render(<Login/>)