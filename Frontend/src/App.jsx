import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import NavLayouts from './Layouts/NavLayout';
import { Login } from './Pages/Login';
import {Signup} from "./Pages/Signup";
import LandingPage from './Pages/LandingPage';
import Hero from './Components/Hero';
import './App.css';


function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path='/' element= {<LandingPage />}/>
        <Route path='/' element={<NavLayouts />}>
        
        </Route>
      </>      
    )
  )
  return (
    <>
      <RouterProvider router={router}/>
    </>
  )
}

export default App
