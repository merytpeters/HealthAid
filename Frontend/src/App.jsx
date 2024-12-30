// import {
//   Route,
//   RouterProvider,
//   createBrowserRouter,
//   createRoutesFromElements,
// } from "react-router-dom";
import { BrowserRouter as Router, Routes,Route } from "react-router-dom";
import NavLayouts from "./Layouts/NavLayout";
import { Login } from "./Pages/Login";
import { Signup } from "./Pages/Signup";
import { Layout } from "./Layout/Layout";
import LandingPage from "./Pages/LandingPage";
import Journal from "./Pages/Journal";
import "./App.css";

function App() {
  // const router = createBrowserRouter(
  //   createRoutesFromElements(
  //     <>
  //       <Route index element={<LandingPage />} />
  //       <Route path="/" element={<NavLayouts />}>
  //         <Route path="/journal" element={<Journal />} />
  //       </Route>
  //     </>
  //   )
  // );
  return (
    <>
      {/* <RouterProvider router={router} /> */}
      <Router>
        <Routes>
          <Route index element={<LandingPage />} />
          <Route path="login" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route path="/auth" element={<Layout />}>
            <Route path="login" element={<Login />} />
            <Route path="signup" element={<Signup />} />
            <Route path="journal" element={<Journal />} />
          </Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
