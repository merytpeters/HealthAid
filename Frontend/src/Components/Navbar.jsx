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
          to="/dashboard"
          end
          className={({ isActive }) => (isActive ? "nav-active" : "nav")}
        >
          Home
        </NavLink>
        <NavLink
          to="/journal"
          end
          className={({ isActive }) => (isActive ? "nav-active" : "nav")}
        >
          Journal
        </NavLink>
        <NavLink
          to="/inventory"
          end
          className={({ isActive }) => (isActive ? "nav-active" : "nav")}
        >
          Inventory
        </NavLink>
        <NavLink
          to="#"
          end
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          FirstAid
        </NavLink>
        <NavLink
          to="/symptoms"
          end
          className={({ isActive }) => (isActive ? "nav-active" : "nav")}
        >
          Symptom Checker
        </NavLink>
        <NavLink
          to="#"
          end
          className={({ isActive }) => (isActive ? "nav" : "nav-active")}
        >
          Drug Interaction Checker
        </NavLink>
        <NavLink
          to="/pillReminder"
          end
          className={({ isActive }) => (isActive ? "nav-active" : "nav")}
        >
          Pill Reminder
        </NavLink>
        <FaBell className="nav" />
      </nav>
    </>
  );
};
export default Navbar;
