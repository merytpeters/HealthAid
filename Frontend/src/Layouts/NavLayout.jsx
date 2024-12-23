import Navbar from "../Components/Navbar";
import { Outlet } from "react-router-dom";

const NavLayouts = () => {
    return (
        <>
            <Navbar />
            <Outlet />
        </>
    )
}
export default NavLayouts;