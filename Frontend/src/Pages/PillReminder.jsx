import {useState, useEffect} from "react";
import {FaTimesCircle, FaPlusCircle, FaTimes} from "react-icons/fa";
import Card from "../Components/Card";


const PillReminder = () => {
    const [showInput, setShowInput] = useState(false)
    const [data, setData] = useState([]);
    const [drugName, setDrugName] = useState("");
    const [pillTime, setPillTime] = useState("");
    const [dosage, setDosage] = useState("")
    const getDate = new Date().toISOString().split('T')[0];


    const deleteReminder = async (id) => {
        const confirm = window.confirm("Are you sure want to delete?")
        if (!confirm)
            return;
        const res = await fetch(`/api/reminder/${id}`, {
            method: "DELETE",
        });
        window.location.reload();
    }

    useEffect(() => {
        const fetchdata = async () => {
            try {
                const res = await fetch('http://localhost:8000/reminder')
                const data = await res.json();
                setData(data)
            } catch (e) {
                console.log("Error fetching data", e)
            }
        }
        fetchdata();
    }, [showInput]);

    const missedReminder = (time) => {
        const timeNow = new Date().getHours();
        const remindTime = new Date(`${time}`).getHours();
        if (timeNow > remindTime)
            return true
        return false
    }

    const updateReminder = async (remind) => {
        const updatedReminder = {
            "id" : remind.id,
            "drug_name": remind.drug_name,
            "pill_time": remind.pill_time,
            "dosage": remind.dosage,
            "email_notification": false
        }
        const res = await fetch(`/api/reminder/${remind.id}` , {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedReminder)
        })
    }

    const saveButtonClick = async () => {
        if ((drugName == ""  || drugName == " " ) || (pillTime == "" || pillTime == " ") || (dosage == "" || dosage == " ")) {
            alert("Please fill all form inputs with valid values");
            return;
        }

        const newReminder = {
            "drug_name": drugName,
            "pill_time": pillTime,
            "dosage": dosage,
            "email_notification": true
        }
        try {
            const res = await fetch("/api/reminder/" , {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newReminder)
            })
        } catch (error) {
            console.log("Error Saving data", error)
        }
    }
    
    const formatTime = (olddate) => {
        const date = new Date(olddate)
        let hours = date.getHours();
        let minutes = date.getMinutes();
        let ampm = hours >= 12 ? 'pm' : 'am';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        minutes = minutes < 10 ? '0' + minutes : minutes;
        let strTime = hours + ':' + minutes + " " + ampm;
        return strTime;
    }

    function formatDate() {
        const date = new Date();
        const day = date.getDate();
        const month = date.toLocaleString('default', { month: 'short' }); // Get short month name
        const year = date.getFullYear();
        
        // Determine ordinal suffix
        const ordinalSuffix = (n) => {
            const suffixes = ["th", "st", "nd", "rd"];
            const value = n % 100;
            return suffixes[(value - 20) % 10] || suffixes[value] || suffixes[0];
        };
    
        return `${day}${ordinalSuffix(day)} ${month} ${year}`;
    }
    return (
       <>
        {
            showInput ?
            <section>
                <form onSubmit={saveButtonClick} className="reminder-form">
                    <label htmlFor="drug_name"></label>
                    <input
                    type="text"  
                    placeholder= "Drug Name" 
                    onChange={(event) => setDrugName(event.target.value)}
                    id="drug_name"
                    className="reminder-input"
                    />

                    <label htmlFor="remind-time"></label>
                    <input
                    type="datetime-local"  
                    placeholder= "Remind time" 
                    onChange={(event) => setPillTime(event.target.value)}
                    id="remind-time"
                    className="reminder-input"
                    />
                    <label htmlFor="dosage"></label>
                    <input
                    type="text"  
                    placeholder= "Dosage" 
                    onChange={(event) => setDosage(event.target.value)}
                    id="dosage"
                    className="reminder-input"
                    />
                    
                    <div className="reminder-button">
                        <label htmlFor="saveInput"></label>
                        <input 
                        type="submit" 
                        value="Save"
                        style= {{
                        backgroundColor: "#f8c954", 
                        color: "white",
                        border: "1px solid #f8c954", 
                        marginTop: "20px", 
                        marginRight: "30%",
                        borderRadius: "36px", 
                        padding: "10px 50px", 
                        textAlign: "center",
                        fontSize: "20px"}}
                        />
                        <label htmlFor="cancelInput"></label>
                        <input 
                        type="button" 
                        value="Cancel" 
                        onClick={() => setShowInput(false)}
                        style= {{
                        backgroundColor: "#f8c954", 
                        color: "white",
                        border: "1px solid #f8c954",  
                        marginTop: "20px", 
                        marginLeft: "30%",
                        borderRadius: "36px", 
                        padding: "10px 50px", 
                        textAlign: "center",
                        fontSize: "20px"}}
                        />
                    </div>
                </form>
                    
            </section>
            :
            <>
                <div className="add-sign">
                    <FaPlusCircle size={50} fill="#f8c954" onClick={() => setShowInput(true)}/>
                </div>
                <section className="reminder-display">
                    <Card className="pill-card" newStyle={{backgroundColor: "#f8c954", textAlign: "center", justifyContent: "center"}}>
                        <p>{formatDate()}</p>
                    </Card>
                    {
                        data.map((item) => {
                            const todayOnly = new Date(item.pill_time).toISOString().split('T')[0]
                            if (todayOnly != getDate)
                                return null
                            return (
                            <Card className="pill-card" key={item.id}>
                                <FaTimesCircle style={{margin: "15px"}} onClick={() => deleteReminder(item.id)}/>
                                <div className="reminder-text">
                                    <p>{formatTime(item.pill_time)}</p>
                                    <p>{item.drug_name}</p>
                                    <p>Dose: {item.dosage}</p>
                                </div>
                                <div>
                                    <label htmlFor="pill-input"></label>
                                    {
                                        item.email_notification == false ? 
                                        <input type="checkbox"  onClick={(event) => event.target.checked ? updateReminder(item) : ""} id="pill-input" checked readOnly/> 
                                        : 
                                        <>
                                            {missedReminder(item.pill_time) ?  <FaTimes size={30} style={{margin: "20px", fill: "red", marginTop: "40px"}}/> : <input type="checkbox"  onClick={(event) => event.target.checked ? updateReminder(item) : ""} id="pill-input" />}
                                        </>
                                    }
                                </div>
                            </Card>
                            )
                        })
                    }
                </section>
            </>
        }
       </>
        
    )
};

export default PillReminder;