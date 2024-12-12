import {FaBell} from 'react-icons/fa'
const Navbar = () => {
    return (
        <>
          <nav>
            <p style={{display: "inline-block", margin: '20px 300px 20px 20px', color: '#f8c954'}} >
                <span><a>HealthAid</a></span>
                <span style={{display: 'block'}}><a>Personal Health Management</a></span>
            </p>
            <span className="nav"><a href='#'>Home</a></span>
            <span className="nav"><a href='#'>Journal</a></span>
            <span className="nav"><a href='#'>Inventory</a></span>
            <span className="nav"><a href='#'>FirstAid</a></span>
            <span className="nav"><a href='#'>Symptom Checker</a></span>
            <span className="nav"><a href='#'>Drug Interaction Checker</a></span>
            <span className="nav"><a href='#'>Pill Reminder</a></span>
            <span className='nav'><FaBell /></span>
            
          </nav>
        </>
      )
};
export default Navbar;