import { Link } from "react-router-dom";

import "../Styles/sidenav.css";
export const SideNav = () => {
  return (
    <div className="nav-items">
      <div className="menus">
        <Link to="/">
          <h2>Health Aid</h2>
        </Link>

        <div className="menu">
          <Link to="/auth/journal">Symptom Journal</Link>
        </div>
        <div className="menu">
          <Link to="/auth/signup">Symptom Checker</Link>
        </div>
        <div className="menu">
          <Link to="/auth/signup">Symptom Checker</Link>
        </div>
        <div className="menu">
          <Link to="/auth/signup">Symptom Checker</Link>
        </div>
        <div className="menu">
          <Link to="/auth/signup">Symptom Checker</Link>
        </div>
      </div>
    </div>
  );
};
