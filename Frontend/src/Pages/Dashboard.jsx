import Chart from "chart.js/auto";
import {useState, useEffect} from "react";
import { FaPenSquare} from 'react-icons/fa';
import HeartBeat from "../assets/heartBeat.svg?react";
import BloodSugar from "../assets/blood-Sugar.svg?react";
import BloodPressure from "../assets/blood-Pressure.svg?react";
import Temp from "../assets/Temp.svg?react";
import LineChart from "../Components/LineChart";
import PieChart from "../Components/PieChart";
import Card from '../Components/Card'


const Dashboard = () => {
    const [showInput, setShowInput]  = useState(false);
    const [beatValue, setBeatValue] = useState();
    const [sugarValue, setSugarValue] = useState();
    const [systolic , setSystolic] = useState();
    const [diastolic , setDiastolic] = useState();
    const [tempValue, setTempValue] = useState();
    const [name, setName] = useState();
    const [age, setAge] = useState();
    const [weight, setWeight] = useState();
    const [height, setHeight]= useState();
    const [cardSelected, setCardSelected] = useState("bloodSugar")
    const [isActive, setIsActive] = useState();
    const [data, setData] = useState();

    const clickEdit = () => setShowInput(true);

    useEffect(() => {
        const dataloader = async () => {
            const res = await fetch('api/graphData?_sort=-time&_limit=1')
            const data = await res.json();
            defaultData(data);
            console.log("data here is ",data)
            setData(data)
        }
        dataloader();
    }, []);


    const saveInput = async () => {
        const date = new Date();
        const newInput = {
            "name": name,
            "age": age,
            "weight": weight,
            "height": height,
            "gender": "female",
            "bloodSugar": sugarValue,
            "bloodPressure": {
              "systolic": systolic,
              "diastolic": diastolic
            },
            "heartRate": beatValue,
            "temp": tempValue,
            "time": date,
        }

        const res = await fetch('/api/graphData', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newInput)
        });
        return
    }

    const defaultData = (data) => {
        const obj = data[0];

        setName(obj.name);
        setAge(obj.age);
        setWeight(obj.weight);
        setHeight(obj.height);
        setBeatValue(obj.heartRate);
        setSugarValue(obj.bloodSugar);
        setSystolic(obj.bloodPressure.systolic);
        setDiastolic(obj.bloodPressure.diastolic);
        setTempValue(obj.temp);
    }
    

    return (
      <>
        {
            showInput ?          
        <div className="dashboard">
            <div style={{display: "flex", justifyContent: "flex-end", margin: "0px", marginRight: "85px", }}>
                <form onSubmit={saveInput} >
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
                    <form>
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
                    <form>
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
                    <form>
                        <div style={{display: 'flex', flexDirection: "row", alignItems: 'center'}}> 
                            <input type="text" className= "dashboard-input" id="pressureInputTop" value={systolic} onChange={(event) => setSystolic(event.target.value)}/>
                            /
                            <input type="text" className= "dashboard-input" id="pressureInputBottom" value={diastolic} onChange={(event) => setDiastolic(event.target.value)}/>
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
                    <form>
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
            <Card 
            newStyle={{
                margin: "0 50px", 
                marginBottom: "30px",
                display: "flex", 
                flexDirection: "row", 
                alignItems: "center", 
                justifyContent: "space-evenly",
                fontSize: "20px"
            }}
            >
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
                <Card 
                    func={() => {
                        setCardSelected("heartRate");
                        setIsActive(0);
                    }}
                    className={isActive === 0 || cardSelected === "heartRate" ? "data-card-active" : "data-card"}
                >
                    <div className="card-header" >
                        <HeartBeat />
                        <p>Heart Rate</p>
                    </div>
                    <div className="card-value">
                        <p> {beatValue} bpm</p>
                        <div style={{backgroundColor: "#56aeff"}}>{beatValue < 70 ? 'Normal': "High"}</div>
                    </div>
                </Card>
                <Card 
                    func={() => {
                        setCardSelected("bloodSugar");
                        setIsActive(1);
                    }}
                    className={isActive === 1 || cardSelected === "bloodSugar" ? "data-card-active" : "data-card"}
                >
                    <div className="card-header">
                        <BloodSugar />
                        <p>Blood Sugar</p>
                    </div>
                    <div className="card-value">
                        <p>{sugarValue} mg / dl</p>
                        <div style={{backgroundColor: "#6ce5e8"}}>{sugarValue < 70 ? "Normal" : "High"}</div>
                    </div>
                </Card>
                <Card
                    func={() => {
                        setCardSelected("bloodPressure");
                        setIsActive(2);
                    }}
                    className={isActive === 2 || cardSelected ===  "bloodPressure" ? "data-card-active" : "data-card"}
                >
                    <div className="card-header">
                        <BloodPressure />
                        <p>Blood Pressure</p>
                    </div>
                    <div className="card-value">
                        <p><span>{systolic} / {diastolic} </span> mmhg</p>
                        <div style={{backgroundColor: "#41b8d5"}}>{systolic < 70? "Normal": "High"}</div>
                    </div>
                </Card>
                <Card
                    func={() => {
                        setCardSelected("temp");
                        setIsActive(3);
                    }}
                    className={isActive === 3 || cardSelected === "temp" ? "data-card-active" : "data-card"}
                >
                    <div className="card-header">
                        <Temp />
                        <p>Temperature</p>
                    </div>
                    <div className="card-value">
                        <p>{tempValue} <sup>o</sup> C</p>
                        <div style={{backgroundColor: "#c6e0f9"}}>{tempValue <= 70 ? "Normal" : "High"}</div>
                    </div>
                </Card>
            </div>
            <div style={{display: "flex", flexDirection: "row"}}>
                <LineChart />
                <PieChart selected={cardSelected} data={data}/>
            </div>
            
        </div>
        }
      </>

    )
}


export default Dashboard;
