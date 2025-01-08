import Chart from "chart.js/auto";
// import {CategoryScale} from "chart.js";
import {useState, useEffect} from "react";
import {useLoaderData} from "react-router-dom"
import { FaPen, FaPenSquare} from 'react-icons/fa';
import HeartBeat from "../assets/heartBeat.svg?react";
import BloodSugar from "../assets/blood-Sugar.svg?react";
import BloodPressure from "../assets/blood-Pressure.svg?react";
import Temp from "../assets/Temp.svg?react";
import LineChart from "../Components/LineChart";
import PieChart from "../Components/PieChart";
import Card from '../Components/Card'


const Dashboard = () => {
    const [showInput, setShowInput]  = useState(false);
    const [beatValue, setBeatValue] = useState(98);
    const [sugarValue, setSugarValue] = useState(80);
    const [pressureValueTop , setPressureValueTop] = useState(102);
    const [pressureValueBottom , setPressureValueBottom] = useState(72);
    const [tempValue, setTempValue] = useState(99);
    const [name, setName] = useState("afuah");
    const [age, setAge] = useState("53");
    const [weight, setWeight] = useState("");
    const [height, setHeight]= useState("");

    const clickEdit = () => setShowInput(true);

    useEffect(() => {
        const dataloader = async () => {
            const res = await fetch('api/graphData')
            const data = await res.json()
        }
    }, [beatValue, sugarValue,pressureValueBottom,pressureValueTop,tempValue,name,age,weight,height]);

    const saveInput = () => {
        const newInput = {
            "name": "afuah",
            "age": "53",
            "weight": "34",
            "height": "161",
            "gender": "female",
            "bloodSugar": 12,
            "bloodPressure": {
              "systolic": 8,
              "diastolic": 72
            },
            "heartRate": 0,
            "temp": 60,
            "time": "2024-10-20T06:00:00",
        }
    }
    

    return (
      <>
        {
            showInput ?          
        <div className="dashboard">
            <div style={{display: "flex", justifyContent: "flex-end", margin: "0px", marginRight: "85px", }}>
                <form onSubmit={() => {}} >
                        <label htmlFor="heartbeatSubmit"></label>
                        <input type="submit" className= "dashboard-input" id="heartbeatSubmit" value="Save" style={{marginTop: "0"}}/>
                </form>
            </div>
            <Card newStyle={{display: "flex", margin: "0 50px", marginBottom: "30px"}}>
                <div>
                    <div style={{display: "flex", alignItems: "center"}}>
                        <p>Name</p>
                        <input type= "text" className= "dashboard-input" value={name}  onChange={(event) => setName(event.target.value)} placeholder="Full name"/>
                    </div>
                    <div style={{display: "flex", alignItems: "center"}}>
                        <p>Age</p>
                        <input type= "text" className= "dashboard-input" value={age} onChange={(event) => setAge(event.target.value)} placeholder="Age in years"/>
                        <p>yrs</p>
                    </div>
                </div>
                <div>
                    <div style={{display: "flex", alignItems: "center"}}>
                        <p>Weight</p>
                        <input type= "text" className= "dashboard-input" value={weight} onChange={(event) => setWeight(event.target.value)} placeholder="Weight in kgs"/>
                        <p>kgs</p>
                    </div>
                    <div style={{display: "flex", alignItems: "center"}}>
                        <p>Height</p>
                        <input type= "text" className= "dashboard-input" value={height} onChange={(event) => setHeight(event.target.value)} placeholder="Height in cms"/>
                        <p>cm</p>
                    </div>
                </div>
            </Card>
            <div className="dashboard-cards">
                <Card newStyle={{margin: "0px 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header" >
                        <HeartBeat />
                        <p>Heart Rate</p>
                    </div>
                    <form onSubmit={() => {}} >
                        <div style={{display: 'flex', flexDirection: "row", alignItems: 'center'}}>
                            <input type="text" className= "dashboard-input" id="heartbeatInput" value={beatValue} onChange={(event) => setBeatValue(event.target.value)}/>
                            <label htmlFor="heartbeatInput">bpm</label>
                        </div>
                    </form>
                </Card>
                <Card newStyle={{margin: "0px 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header">
                        <BloodSugar />
                        <p>Blood Sugar</p>
                    </div>
                    <form onSubmit={() => {}}>
                        <div style={{display: 'flex', flexDirection: "row", alignItems: 'center'}}>
                            <input type="text" className= "dashboard-input" id="bloodSugarInput" value={sugarValue} onChange={(event) => setSugarValue(event.target.value)}/>
                            <label htmlFor="bloodSugarInput">mg / dl</label>
                        </div>
                    </form>
                </Card>
                <Card newStyle={{margin: "0px 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header">
                        <BloodPressure />
                        <p>Blood Pressure</p>
                    </div>
                    <form onSubmit={() => {}} >
                        <div style={{display: 'flex', flexDirection: "row", alignItems: 'center'}}> 
                            <input type="text" className= "dashboard-input" id="pressureInputTop" value={pressureValueTop} onChange={(event) => setPressureValueTop(event.target.value)}/>
                            /
                            <input type="text" className= "dashboard-input" id="pressureInputBottom" value={pressureValueBottom} onChange={(event) => setPressureValueBottom(event.target.value)}/>
                            <label htmlFor="pressureInputTop">mmhg</label>
                            <label htmlFor="pressureInputBottom"></label>
                        </div>
                    </form>
                </Card>
                <Card newStyle={{margin: "0px 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header" >
                        <Temp />
                        <p>Temperature</p>
                    </div>
                    <form onSubmit={() => {}}>
                        <div style={{display: 'flex', flexDirection: "row", alignItems: 'center'}}>
                            <input type="text" className= "dashboard-input" id="tempInput" value={tempValue} onChange={(event) => setTempValue(event.target.value)}/>
                            <label htmlFor="tempInput"><sup>o</sup>C</label>
                        </div>
                    </form>
                </Card>
            </div>

        </div>
        :
        <div className="dashboard">
            <div style={{display: "flex", justifyContent: "flex-end", }}>
                <FaPenSquare size={40} style={{fill: "#f8c954", marginRight: "85px"}} onClick={clickEdit}/>
            </div>
            <Card newStyle={{margin: "0 50px", marginBottom: "30px",display: "flex", flexDirection: "row", alignItems: "center", justifyContent: "space-evenly",fontSize: "20px"}}>
                <div style={{display: "flex", flexDirection: "column", margin: "0px 60px"}}>
                        <p>Name: {name}</p>
                        <p>Age: {age} yrs</p>
                </div>
                <div style={{display: "flex", flexDirection: "column", margin: "0px 60px"}}>
                        <p>Weight: {weight} kgs</p>
                        <p>Height: {height} cm</p>
                </div>
            </Card>
            <div className="dashboard-cards">
                <Card newStyle={{margin: "0 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header" >
                        <HeartBeat />
                        <p>Heart Rate</p>
                    </div>
                    <div className="card-value">
                        <p> {beatValue} bpm</p>
                        <div style={{backgroundColor: "#56aeff"}}>Normal</div>
                    </div>
                </Card>
                <Card newStyle={{margin: " 0 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header">
                        <BloodSugar />
                        <p>Blood Sugar</p>
                    </div>
                    <div className="card-value">
                        <p>{sugarValue} mg / dl</p>
                        <div style={{backgroundColor: "#6ce5e8"}}>Normal</div>
                    </div>
                </Card>
                <Card newStyle={{margin: " 0 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header">
                        <BloodPressure />
                        <p>Blood Pressure</p>
                    </div>
                    <div className="card-value">
                        <p><span>{pressureValueTop} / {pressureValueBottom} </span> mmhg</p>
                        <div style={{backgroundColor: "#41b8d5"}}>Normal</div>
                    </div>
                </Card>
                <Card newStyle={{margin: "0 20px", borderRadius: "20px", fontSize: "24px", width : "250px", height: "200px"}}>
                    <div className="card-header">
                        <Temp />
                        <p>Temperature</p>
                    </div>
                    <div className="card-value">
                        <p>90 <sup>o</sup> C</p>
                        <div style={{backgroundColor: "#c6e0f9"}}>Normal</div>
                    </div>
                </Card>
            </div>
            <div style={{display: "flex", flexDirection: "row"}}>
                <LineChart />
                <PieChart />
            </div>
            
        </div>
        }
      </>

    )
}


export default Dashboard;
