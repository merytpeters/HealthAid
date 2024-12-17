import Card from './Components/Card'
import Hero from './Components/Hero'
import { Login } from './Pages/Login'
import {Signup} from "./Pages/Signup"
import Bottle from './assets/Drug-Bottle.png'
import './App.css'

function App() {
  
  return (
    <>
      {/* <Hero /> */}
      <Login />
      {/* <Signup /> */}
      <Hero />
      <p className='ldn-txt'>About us</p>
      <p className='ldn-txt1'>
        Health Aid is a comprehensive personal health management app that aims to enhance health literacy, foster proactive<br/> health management and empowers users to have control of their health.
      </p>
      <p className='ldn-txt'>Features</p>
      <img src={Bottle}/>
      <Card>
        <p>
        Health Symptoms Journal<br />
        This feature allows users to document and monitor their symptoms over time,<br /> aiding in personal health tracking and physician consultations
        </p>
      </Card>
    </>
  )
}

export default App
