import React from "react";
import ReactDOM from "react-dom/client"
import './index.css'
function Login()
{
    function sub()
    {
        
    }
    return(
        <div class="container">
		<h2 class="form-group">Login</h2>
		<form>
			<div class="form-group">
				<label for="username">Username:</label>
				<input type="username" id="username" name="username" required/>
			</div>
			<div class="form-group">
				<label for="password">Password:</label>
				<input type="password" id="password" name="password" required/>
			</div>

			<div class="form-group">
				<button type="submit" class = "login-button" onclick={sub}>Login</button>
			</div>
            <p class="reg"><a href = "3.html">Don't have an account,Register here!</a></p>
		</form>
	    </div>
    )
    
}
ReactDOM.createRoot(document.getElementById("root")).render(<Login/>)