import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Hero from "./Components/Hero";
// import { SideNav } from "./Components/SideNav";
import { Login } from "./Pages/Login";
import { Signup } from "./Pages/Signup";
import { Layout } from "./Layout/Layout";
import "./App.css";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route index element={<Hero />} />
          <Route path="/auth" element={<Layout />}>
            <Route path="login" element={<Login />} />
            <Route path="signup" element={<Signup />} />
          </Route>
        </Routes>
      </Router>
      {/* <Hero /> */}
      {/* <Login /> */}
      {/* <Signup /> */}
      {/* <SideNav /> */}
    </>
  );
}

export default App;
