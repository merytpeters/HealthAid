import { Outlet } from "react-router-dom";
import { SideNav } from "../Components/SideNav";
import "../Styles/layout.css";

export const Layout = () => {
  return (
    <div className="layout">
      <div className="side-nav">
        <SideNav />
      </div>
      <main style={{ flex: 1 }}>
        <Outlet />
      </main>
    </div>
  );
};
