import Card from "./Card";
import {FaTimesCircle, FaEdit} from "react-icons/fa";
import {useNavigate} from "react-router-dom";

const SymptomList = ({symptomCard = [], func, editFunc, updateUi}) => {
    const symptoms = symptomCard.description.split(",");
    const date = symptomCard.date;
    const id = symptomCard.id;
    const navigate = useNavigate()
    console.log(id , " is the id")

    const deleteSymptomCard = async (id) => {
        console.log("id is ", id)
        const res = await fetch(`/api/symptoms/${id}`, {
            method: "DELETE",
        });
        func(false);
        return true;
    }

    const editSymtomCard = async (id) => {

    }

    
    if (symptoms.length >= 4) {

    }
    return (
        <Card 
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
            <div style={{display: "inline-block"}}>
                <FaTimesCircle style={{margin:"15px 50px 0 0"}} onClick={() => deleteSymptomCard(id)}/>
                <span>{date}</span>
            </div>
            <ul>
                {symptoms.map((symptom, idx) => <li key={idx}>{symptom}</li>)}
            </ul>
            <FaEdit onClick={() => editFunc(id)}/>
        </Card>
    )
}
export default SymptomList;