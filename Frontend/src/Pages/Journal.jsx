import { useState , useEffect} from "react";
import SymptomList from "../Components/SymptomList";
import Card from "../Components/Card";
import {FaPlusCircle, FaTimesCircle, FaEdit, FaTimes} from 'react-icons/fa';
const Journal = () => {
    const [showInput, setShowInput] = useState(false);
    const [getData, setGetData] = useState([]);
    const [addsymptom, setAddSymptom] = useState("");
    const [updateSymptom, setUpdateSymptom] = useState(false);
    const [symptomCardId, setSymptomCardId] = useState(null);
    const [symptomValue, setSymptomValue] = useState("")

    useEffect(() => {
        const symptomLoader = async () => {
            try {
                const res = await fetch('/api/symptoms');
                const allSymptoms = await res.json();
                setGetData(allSymptoms)
            } catch (error) {
                console.log('Error fetching data', error)
            }

        }
        symptomLoader();
    }, [showInput]);


    const saveButtonClick = async (event) => {
        const today = new Date();
        const formattedDate = today.toISOString().split('T')[0];

        if (addsymptom === "" || addsymptom === " " || addsymptom === ",")
            return;
        const newSymptom = {
            description : addsymptom,
            date : formattedDate
        }
        const res = await fetch('/api/symptoms', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(newSymptom),
          });
        return;
    }

    const deleteSymptomCard = async (id) => {
        const confirm = window.confirm("Are you sure want to delete?")
        if (!confirm)
            return;
        const res = await fetch(`/api/symptoms/${id}`, {
            method: "DELETE",
        });
        window.location.reload();
    }

    const updateSymptomCard =  async (event, id) => {
        const today = new Date();
        const formattedDate = today.toISOString().split('T')[0];

        if (addsymptom === "" || addsymptom === " " || addsymptom === ",")
            return;

        const updatedSymptom = {
            id: id,
            description : addsymptom,
            date : formattedDate
        }

        const res = await fetch(`/api/symptoms/${id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedSymptom),
          });
        setSymptomValue("");
        setUpdateSymptom(false);
        return;
    }

    return (
        <section>
            {
            showInput  ? 
            <section className="input-flex" id="input-flex">
                <form onSubmit={(event) => updateSymptom ? updateSymptomCard(event, symptomCardId) : saveButtonClick(event)}>
                    <label htmlFor="symtomInput"></label>
                    <input
                    type="text"  
                    placeholder= "Enter your symptoms eg Headche, Fever" 
                    defaultValue={ updateSymptom ? symptomValue : ""}
                    onChange={(event) => setAddSymptom(event.target.value)}
                    style={{   
                        borderRadius: "20px",
                        padding: "20px",
                        textAlign : "center",
                        fontSize: "20px",
                        border: "2px solid #f8c954",
                        width: "100lvh",
                        outline: "none"
                        }}
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
            <section >
                <div style={{display: "flex", justifyContent: "flex-end"}}>
                    <FaPlusCircle size={50} style={{padding: "10px", fill: "#f8c954", marginRight: "85px" }} onClick={() => setShowInput(true)} id="fa-plus-circle"/>
                </div>
                <div className="symptom-list">
                    {getData.map((symptomCard, idx) => 
                    {
                        const symptoms = symptomCard.description.split(",");
                        const date = symptomCard.date;
                        const id = symptomCard.id;
                        return (
                            <Card 
                            key={idx}
                            newStyle={{
                                fontSize: "20px", 
                                borderRadius: "20px", 
                                textAlign: "justify",
                                backgroundColor: "#f8c954",
                                justifyContent: "space-between",
                                display: "flex",
                                flexDirection: "column",
                                alignItems: "center",
                                lineHeight: "1.5",
                                overflow: "hidden",
                                padding: "15px",
                                margin: "15px",
                            }}
                        >
                            <div style={{display: "flex", flexDirection: "row", alignItems: "center"}}>
                                <FaTimesCircle  style={{ margin:"0px 100px 0 0", padding: "0"}} onClick={() => deleteSymptomCard(id)}/>
                                <p style={{margin: "0", padding:"0"}}>{date}</p>
                            </div>
                            <ul>
                                {symptoms.map((symptom, idx) => <li key={idx}>{symptom}</li>)}
                            </ul>
                            <FaEdit onClick={() => {
                                setUpdateSymptom(true);
                                setSymptomCardId(id);
                                setSymptomValue(symptomCard.description);
                                setShowInput(true);
                                return;
                            }}
                            />
                            </Card>
                        )
                    })}
                </div>
            </section>
            }
        </section>
    )
}

// const symptomLoader = async () => {
//     const res = await fetch('/api/symptoms');
//     const allSymptoms = await res.json();
//     return allSymptoms;
// }
// export { Journal as default , symptomLoader};
export default Journal;