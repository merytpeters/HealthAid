import {FaBell} from 'react-icons/fa';

const Navbar = () => {
    return (
        <>
          <nav>
            <p style={{display: "inline-block", margin: '20px 300px 20px 20px', color: '#f8c954'}} >
                <span><NavLink></NavLink></span>
                <span style={{display: 'block'}}><a>Personal Health Management</a></span>
            </p>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>Home</NavLink></span>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>Journal</NavLink></span>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>Inventory</NavLink></span>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>FirstAid</NavLink></span>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>Symptom Checker</NavLink></span>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>Drug Interaction Checker</NavLink></span>
            <span className="nav"><NavLink to='#' className={({isActive}) => isActive ? 'nav-active' : ''}>Pill Reminder</NavLink></span>
            <span className='nav'><FaBell /></span>
            
          </nav>
        </>
      )
};
export default Navbar;