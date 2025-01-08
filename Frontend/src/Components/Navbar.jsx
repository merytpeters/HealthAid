import { CiVault } from "react-icons/ci";
import { FaBell } from "react-icons/fa";
import { NavLink, Link } from "react-router-dom";

const Navbar = ({ isLandingPage = false }) => {
  if (isLandingPage) {
    return (
      <>
        <div style={{ width: "100%", boxSizing: "border-box" }}>
          <p
            style={{
              display: "inline-block",
              margin: "20px 300px 20px 20px",
              color: "#f8c954",
            }}
          >
            <span style={{ display: "block" }}>
              <Link to="/" style={{ textDecoration: "none", color: "#f8c954" }}>
                HealthAid <br />
                Personal Health Management
              </Link>
            </span>
          </p>
          <NavLink
            style={{ float: "right", marginTop: "20px" }}
            className={({ isActive }) => (isActive ? "nav" : "nav-active")}
          >
            <Link
              to="signup"
              style={{ textDecoration: "none", color: "#f8c954" }}
            >
              Signup
            </Link>
          </NavLink>
        </div>
      </>
    );
  }

  return (
    <>
    <div>
{/* fixing the nav bar issue */}
      <nav className="navbar" style={{width: "100%"}}>
        <p
          style={{
            display: "inline-block",
            margin: "20px 100px 20px 20px",
            color: "#f8c954",
          }}
        >
          <span style={{ display: "block" }}>
            <Link to="/" style={{ textDecoration: "none", color: "#f8c954" }}>
              HealthAid <br />
              Personal Health Management
            </Link>
          </span>
        </p>
        <NavLink
          to="/"
          style={{ textDecoration: "none", color: "#f8c954" }}
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Home
        </NavLink>
        <NavLink
          to="journal"
          style={{ textDecoration: "none", color: "#f8c954" }}
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Journal
        </NavLink>
        <NavLink
          to="inventory"
          style={{ textDecoration: "none", color: "#f8c954" }}
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Inventory
        </NavLink>
        <NavLink
          to="#"
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          FirstAid
        </NavLink>
        <NavLink
          to="symptoms"
          style={{ textDecoration: "none", color: "#f8c954" }}
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Symptom Checker
        </NavLink>
        <NavLink
          to="#"
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Drug Interaction Checker
        </NavLink>
        <NavLink
          to="#"
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Pill Reminder
        </NavLink>
        <FaBell className="nav" />
      </nav>
    </div>
    </>
  );
};
export default Navbar;
