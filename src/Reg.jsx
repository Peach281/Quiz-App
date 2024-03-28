import React from "react";
import ReactDOM from "react-dom/client";
import './Reg.css'
function Register()
{
    return(
        <div class="container">
        <h2>Registration Form</h2>
        <form>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required/>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required/>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required/>
            </div>
            <div class="form-group">
                <button type="submit" onclick="return register()">Register</button>
            </div>
        </form>
    </div>
    )
}
ReactDOM.createRoot(document.getElementById("root")).render(<Register/>)