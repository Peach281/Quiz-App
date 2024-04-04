import React from "react"
import ReactDOM  from "react-dom/client" 
import './Sports.css'
export default function Sports()
{
    const [ques,setQues] = React.useState([])
    const [currentIndex,setCurrentIndex]= React.useState(0)
    const [ans,setAns]=React.useState("")
    const [result,setResult] = React.useState(false)
    const [message,setMessage] = React.useState("")
    const [total,setTotal] = React.useState(0)
    const [count,setCount]= React.useState(0)
    React.useEffect(()=>{
        fetch("http://localhost:5000/SportsData")
        .then(res=>res.json())
        .then(d=>setQues(d))
    },[])
   const handleSubmit = ()=>{
        const currentQues = ques[currentIndex]
        if(ans.toLowerCase()==currentQues.answer.toLowerCase())
        {
            setMessage("Kudos! Correct answer")
            setTotal(prev=>prev+10)
            setCount(p=>p+1)
        }
            
        else
        {
            setMessage("Oh! Wrong answer")
            setCount(p=>p+1)
        }
            
        setResult(true)
        
   }
   const nextQues=()=>
   {
        setResult(false)
        setResult(true)
        setCurrentIndex(prev=>prev+1)
        setAns('')
        setMessage('')
        setCount(0)
   }
    return(
        <div>
            {ques.length>0 && currentIndex<ques.length &&(
                <div>
                    <h1>{ques[currentIndex].name}</h1>
                    <div className="list">
                    <ul style={{ listStyleType: 'none', padding: 0 }}>
                        {ques[currentIndex].options.map((option,index)=>(
                            <li key={index} >
                                <input type="radio"
                                name="answer"
                                value={option}
                                onChange={(e)=>setAns(e.target.value)}
                                checked = {ans===option}
                                className="custom-radio"
                                />
                                <label className="option-label">{option}</label>
                            </li>
                        ))}
                    </ul>
                    </div>

                    {count<1 && <button onClick={handleSubmit} className="btn">Submit Answer</button>}
                    <button onClick={nextQues} className="btn1">Next Question</button>
                    {result&&<p className="m">{message}</p>}
                </div>
            )}
            {currentIndex===ques.length &&<h1>You scored {total} points out of 50</h1>}
        </div>
        
    )
}
ReactDOM.createRoot(document.getElementById("root")).render(<Sports/>)