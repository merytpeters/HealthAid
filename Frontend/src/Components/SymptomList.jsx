import Card from "./Card";
const SymptomList = ({symptomCard = []}) => {
    const symptoms = symptomCard.description.split(",");
    console.log(symptoms.length);
    if (symptoms.length >= 4) {

    }
    return (
        <Card 
            newStyle={{
                fontSize: "20px", 
                // margin: "0", 
                // width: "150px", 
                // height: "150px", 
                borderRadius: "20px", 
                textAlign: "justify",
                backgroundColor: "#f8c954",
                justifyContent: "space-between",
                display: "flex",
                alignItems: "center",
                lineHeight: "1.5",
                overflow: "hidden",
                padding: "15px",
                margin: "15px"
            }}
        >
            <ul>
                {symptoms.map((symptom, idx) => <li key={idx}>{symptom}</li>)}
            </ul>
        </Card>
    )
}
export default SymptomList;