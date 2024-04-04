export default function Sports()
{
    const [data,setData]=React.useState("")
    React.useEffect(()=>{
        fetch("http://localhost:5000/SportsData")
        .then(res=>res.json())
        .then(d=>setData(d))
    },[0])
   

    return(
        <div>
            <h1>{JSON.stringify(data)}</h1>
        </div>
        
    )
}