import React from "react"
import ReactDOM  from "react-dom/client" 
import './Sports.css'
function Politics()
{
    const [ques,setQues]=React.useState([])
    const [index,setIndex] = React.useState(0)
    const [shown,setShown] = React.useState(false)
    const [ans,setAns] = React.useState("")
    const [message,setMessage] = React.useState("")
    const [total,setTotal] = React.useState(0)
    const [count,setCount] = React.useState(0)
    React.useEffect(()=>{
        fetch('http://localhost:5000/PoliticsData')
        .then(res=>res.json())
        .then(d=>setQues(d))
    },[])
    const handleSub=()=>{
        const current = ques[index]
        if(ans.toLowerCase()===current.answer.toLowerCase())
        {
            setMessage("Kudos! right answer")
            setTotal(prev=>prev+10)
        }
        else
        {
            setMessage("Oh! Wrong answer")
        }
        setCount(p=>p+1)
        setShown(true)
    }
    const next = ()=>{
        setIndex(prev=>prev+1)
        setShown(false)
        setAns('')
        setMessage('')
        setCount(0)
    }
    const back=()=>{
        window.location.href="4.html"
    }
    const again = ()=>{
        window.location.href="Politics.html"
    }
    return(
        <div>
            {ques.length>0 && index<ques.length&&(
                <div>
                    <h1>{ques[index].name}</h1>
                    <div className="list">
                        <ul style={{ listStyleType: 'none', padding: 0 }}>
                        {ques[index].options.map((option,id)=>(
                            <li key={id}>
                                <input
                                type="radio"
                                name="answer"
                                value={option}
                                onChange={(e)=>setAns(e.target.value)}
                                checked={ans==option}
                                className="custom-radio"
                                />
                                <label className="option-label">{option}</label>
                            </li>
                        ))}
                        </ul>
                    </div>
                    {count<1 && <button className="btn" onClick={handleSub}>Submit answer</button>}
                    <button className="btn1" onClick={next}>Next Question</button>
                    {shown && <p className="m">{message}</p>}
                    </div>
                    )}
                    
                    {index==ques.length && (
                    <div>
                    <h1>You have scored {total} points out of 80!</h1>
                    <button className="btn" onClick={back}>Main Menu</button>
                    <button  className="btn1" onClick={again}>Play again</button> 
                    </div>)
                    }
                    
                
            
        </div>
    )
}
ReactDOM.createRoot(document.getElementById("root")).render(<Politics/>)