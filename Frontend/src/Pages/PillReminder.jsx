import {useState, useEffect} from "react"
import Card from "../Components/Card";
import {FaTimesCircle, FaPlusCircle, FaPills, FaPrescriptionBottle, FaCapsules} from "react-icons/fa"
const PillReminder = () => {
    const [addRow, setAddRow] = useState();
    const [showInput, setShowInput] = useState(false)
    const [data, setData] = useState([])
    const getDate = new Date().toISOString().split('T')[0];


    const deleteReminder = async (id) => {
        const confirm = window.confirm("Are you sure want to delete?")
        if (!confirm)
            return;
        const res = await fetch(`http://localhost:8000/reminder/${id}`, {
            method: "DELETE",
        });
        window.location.reload();
    }

    useEffect(() => {
        const fetchdata = async () => {
            try {
                const res = await fetch('http://localhost:8000/reminder')
                const data = await res.json();
                // console.log(data)
                setData(data)
            } catch (e) {
                console.log("Error fetching data", e)
            }
        }
        fetchdata();
    }, [showInput]);

    const missedReminder = (time) => {

    }
    
    return (
       <>
        {
            showInput ?
            <section>
                <form onSubmit={{}}>
                    <label htmlFor=""></label>
                    <input
                    type="text"  
                    placeholder= "" 
                    defaultValue={{}}
                    onChange={{}}
      
                    />
                    
                    <div>
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
                        <p>{getDate}</p>
                    </Card>
                    {
                        data.map((item) => {
                            return (
                            <Card className="pill-card" key={item.id}>
                                <FaTimesCircle style={{margin: "15px"}} onClick={() => deleteReminder(item.id)}/>
                                <div className="reminder-text">
                                    <p>{item.pill_time}</p>
                                    <p>{item.drug_name}</p>
                                    <p>Dose: {item.dosage}</p>
                                </div>
                                <label htmlFor="pill-input"></label>
                                <input type="checkbox"  onClick={(event) => event} id="pill-input" />
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