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
import Dashboard from "./Pages/Dashboard";
import { SymptomsChecker } from "./Pages/SymptomsChecker";
import { Inventory } from "./Pages/Inventory";
import { DrugInteraction } from "./Pages/DrugInteraction";
import { DrugIntResponse } from "./Pages/DrugIntResponse";
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
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/symptoms" element={<SymptomsChecker />} />
          <Route path="/test" element={<DynamicTables />} />
          <Route path="/inventory" element={<Inventory />} />
          <Route path="/drug-int" element={<DrugInteraction />} />
          <Route path="/drug-int-res" element={<DrugIntResponse />} />
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
