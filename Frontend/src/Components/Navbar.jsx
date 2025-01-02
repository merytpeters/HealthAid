import { FaBell } from "react-icons/fa";
import { NavLink, Link } from "react-router-dom";

const Navbar = ({ isLandingPage = false }) => {
  if (isLandingPage) {
    return (
      <>
        <p
          style={{
            display: "inline-block",
            margin: "20px 300px 20px 20px",
            color: "#f8c954",
          }}
        >
          <span>HealthAid</span>
          <span style={{ display: "block" }}>
            <a>Personal Health Management</a>
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
      </>
    );
  }

  return (
    <>
      <nav className="navbar">
        <p
          style={{
            display: "inline-block",
            margin: "20px 300px 20px 20px",
            color: "#f8c954",
          }}
        >
          <span>HealthAid</span>
          <span style={{ display: "block" }}>
            <a>Personal Health Management</a>
          </span>
        </p>
        <NavLink
          to="/"
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Home
        </NavLink>
        <NavLink
          to="/"
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Journal
        </NavLink>
        <NavLink
          to="#"
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
          to="#"
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
    </>
  );
};
export default Navbar;
