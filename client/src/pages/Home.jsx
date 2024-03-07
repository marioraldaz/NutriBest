
import React, { useState, useEffect, useContext } from 'react'
import {AuthContext} from '../context/AuthContext';

export function Home() {
  const { authTokens, logoutUser } = useContext(AuthContext);
  let [profile, setProfile] = useState([])

  useEffect(() => {
    if(authTokens!=null) {
      getProfile()
    }
  },[])

  const getProfile = async() => {
      let response = await fetch('http://localhost:8000/api/profile', {
      method: 'GET',
      headers:{
          'Content-Type': 'application/json',
          'Authorization':'Bearer ' + String(authTokens.access)
      }
      })
      let data = await response.json()
      console.log(data)
      if(response.status === 200){
          setProfile(data)
      } else if(response.statusText === 'Unauthorized'){
          logoutUser()
      }
  }
  
  return (
    <div className="flex items-center justify-center w-full text-green-600 text-4xl h-32">
      <h1 className="gradient-text">Living Fast Needs Keeping Track</h1>
    </div>
  );
}
