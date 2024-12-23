import Hero from "../Components/Hero";
import LandingCard from "../Components/LandingCard";
import Footer from "../Components/Footer";
import Bottle from "../assets/Drug-Bottle.png";
import  Sick from "../assets/Sick-Boy.png";
import Writing from "../assets/Writing.png";
import Bell from "../assets/Bell.png";
import Inventory from "../assets/Inventory.png";
import FirstAid from "../assets/FirstAid.png";

const LandingPage = () => {
  return (
    <>
    <Hero />
    <p className='ldn-txt'>About us</p>
    <p className='ldn-txt1'>
      Health Aid is a comprehensive personal health management app that aims to enhance health literacy, 
      foster proactive health management and empowers users to have control of their health.
    </p>
    <p className='ldn-txt'>Features</p>
    <LandingCard 
    image={Bottle}
    >
      <strong> Drug Interaction Checker</strong>
      <p>
      This feature when provided with details of a specific drug identifies <br />
      potential interaction with other prescribed drugs, food and more.
      </p>
    </LandingCard>

    <LandingCard 
    image={Sick}
    imgPosition="left"
    >
      <strong> Sypmtoms Checker</strong>
      <p>
      Symptoms Checker provides insights into possible conditions based on <br/>
      user- reported symptoms. This would assist users make informed <br />
      decisions about seeking medical care.
      </p>
    </LandingCard>

    <LandingCard 
    image={Bell}
    imgPosition="right"
    >
      <strong> Pill Reminder with Notifications</strong>
      <p>
      This keeps users on track with their medication schedule, by providing <br />
      timely reminders and tracking their progress, significantly reducing the<br />
      chances of missing doses and improving treatment adherence.
      </p>
    </LandingCard>

    <LandingCard 
    image={Writing}
    imgPosition="left"
    >
      <strong> Health Symptoms Journal</strong>
      <p>
      This feature allows users to document and monitor their symptoms over time,<br /> 
      aiding in personal health tracking and physician consultations.
      </p>
    </LandingCard>

    <LandingCard 
    image={Inventory}
    imgPosition="right"
    >
      <strong> Home Medicine Inventory</strong>
      <p>
      Helps users organize and manage their supplies to avoid shortages or <br />
      expired medications.
      </p>
    </LandingCard>
    
    <LandingCard 
    image={FirstAid}
    imgPosition="left"
    >
      <strong> First Aid Guide</strong>
      <p>
      Offers quick, actionable steps for managing common emergencies until<br />
       professional help is available. 
      </p>
    </LandingCard>
    
    <Footer />
    </>

    
  );
};
export default LandingPage;