import Button from "./button";
import Navbar from "./Navbar"

const Hero = () => {

    return (
        <section className="hero">
            <Navbar isLandingPage = {true}/>
            <div className="hero-text">
                <h1>Your Personal Health <br></br>Companion</h1>
                <i>Your Health, Your Way</i>
            </div>
            <Button fill = 'true'/>
        </section>
    )
  
};
export default Hero;