import {
  Route,
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import NavLayouts from "./Layouts/NavLayout";
import { Login } from "./Pages/Login";
import { Signup } from "./Pages/Signup";
import LandingPage from "./Pages/LandingPage";
import Journal from "./Pages/Journal";
import Dashboard from './Pages/Dashboard';
import PillReminder from "./Pages/PillReminder";
import { SymptomsChecker } from "./Pages/SymptomsChecker";
import { Inventory } from "./Pages/Inventory";
import DynamicTables from "./Pages/dynaminx";
import "./App.css";

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route index element={<LandingPage />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />

        <Route path="/" element={<NavLayouts />}>
          <Route path="/journal" element={<Journal />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path="/symptoms" element={<SymptomsChecker />} />
          <Route path="/pillReminder" element={<PillReminder />} />
          <Route path="/test" element={<DynamicTables />} />
          <Route path="/inventory" element={<Inventory />} />
        </Route>
      </>
    )
  );
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
