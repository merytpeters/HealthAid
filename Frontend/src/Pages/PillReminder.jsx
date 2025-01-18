import {useState} from "react"
import Card from "../Components/Card";
import {FaTimesCircle, FaPlusCircle,} from "react-icons/fa"
const PillReminder = () => {
    const [addRow, setAddRow] = useState();
    const [showInput, setShowInput] = useState(false)
    const getDate = new Date().toISOString().split('T')[0];
    
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
            <section className="reminder-display">
                    <div className="add-sign">
                        <FaPlusCircle size={50} fill="#f8c954" onClick={() => setShowInput(true)}/>
                    </div>
                    <Card className="pill-card" newStyle={{backgroundColor: "#f8c954", textAlign: "center"}}>
                        <p>{getDate}</p>
                    </Card>
                    <Card className="pill-card">
                        <FaTimesCircle />
                        <input type="checkbox" />
                    </Card> 
            </section>
        }
       </>
        
    )
};

export default PillReminder;