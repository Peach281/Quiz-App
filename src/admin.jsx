import React from "react"
import ReactDOM from "react-dom/client"
import './Admin.css'
function Admin()
{
    const cret=()=>{
        window.location.href="AddQues.html"
    }
    const dret=()=>{
        window.location.href="Delete.html"
    }
    return(
        <div className="gen">
            <h1>Admin Privileges</h1>
            <div className="button-container">
                <button className="btn" onClick={cret}>Create Questions</button>
                <button className="btn" onClick={dret}>Delete Questions</button>
                <button className="btn" >Change Answers</button>
            </div>
        </div>
    )
}
ReactDOM.createRoot(document.getElementById("root")).render(<Admin/>)