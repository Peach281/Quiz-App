import React from 'react'
import './App.css'
export default function App() {
  function next()
  {
    setTimeout(()=>{
      window.location.href="3.html"
    },1000)
  }
  return(
    <div >
      <h1  className='t'>Welcome to Quizzyverse</h1>
      <p className='p'>where you can play a variety of quizzes of different genres</p>
      <button className='b' onClick={next}>Explore more</button>
    </div>
    
  )
  
}


