import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import NavLayouts from './Layouts/NavLayout';
import { Login } from './Pages/Login';
import {Signup} from "./Pages/Signup";
import LandingPage from './Pages/LandingPage';
import Journal  from './Pages/Journal';
import Dashboard from './Pages/Dashboard';
import Hero from './Components/Hero';
import './App.css';


function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route index element= {<LandingPage />}/>
        <Route path='/' element={<NavLayouts />}>
          <Route path='/journal' element={<Journal />} />
          <Route path='/dashboard' element={<Dashboard />} />
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
