import Button from "./Button";
import Navbar from "./Navbar"

const Hero = () => {

    return (
        <section className="hero">
            <Navbar isLandingPage = {true}/>
            <div className="hero-text">
                <h1>Your Personal Health <br/>Companion</h1>
                <i>Your Health, Your Way</i>
            </div>
            <Button newStyle={{ backgroundColor: "#f8c954", color: "white" ,  margin: "20px 50px"}}/>
        </section>
    )
  
};
export default Hero;