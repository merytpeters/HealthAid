import Hero from "../Components/Hero";
import Card from "../Components/Card";

const LandingPage = () => {
  return (
    <>
    <Hero />
    <p className='ldn-txt'>About us</p>
    <p className='ldn-txt1'>
      Health Aid is a comprehensive personal health management app that aims to enhance health literacy, foster proactive<br/> health management and empowers users to have control of their health.
    </p>
    <p className='ldn-txt'>Features</p>
    <img src={Bottle}/>
    <Card>
      <p>
      Health Symptoms Journal<br />
      This feature allows users to document and monitor their symptoms over time,<br /> aiding in personal health tracking and physician consultations
      </p>
    </Card>
    </>
  );
};
export default LandingPage;