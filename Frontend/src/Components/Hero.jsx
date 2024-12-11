import Button from "./button";
import Navbar from "./Navbar";
const Hero = () => {
    return (
        <section className="hero">
            <Navbar />
            <div className="hero-text">
                <h1>Your Personal Health Companion</h1>
                <h4>Your Health, Your Way</h4>
                <Button fill = 'true'/>
            </div>
            
        </section>
    )
  
};
export default Hero;