import { useState , useEffect} from "react";
import { useLoaderData } from "react-router-dom";
import Card from "../Components/Card";
import SymptomList from "../Components/SymptomList";
import { Input } from "../Components/Input";
import Button from "../Components/Button";
import {FaPlusCircle} from 'react-icons/fa'
const Journal = () => {
    const [showInput, setShowInput] = useState(false);
    const [getData, setGetData] = useState([])
    // const allSymptoms = useLoaderData();

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
    }, [showInput])
    const addButtonClick = () => {
        setShowInput(true);
    }
    const saveButtonClick = ( ) => {
        
    }

    const cancelButtonClick = () => {
        setShowInput(false);
    }

    return (
        <section className="grid">
            {
            showInput ? 
            <section className="input-flex" id="input-flex">
                <Input 
                  type="text"  
                  placeholder= "Enter your symptoms eg Headche, Fever" 
                  newStyle={{   
                    borderRadius: "20px",
                    padding: "20px",
                    textAlign : "center",
                    fontSize: "20px",
                    border: "2px solid #f8c954",
                    width: "100lvh",
                    }}
                />
                <div >
                    <Button 
                        text="Save" 
                        newStyle= 
                            {{ 
                                backgroundColor: "#f8c954", 
                                color: "white",
                                margin: "15px 15px"
                            }}
                    >
                        
                    </Button>

                    <Button 
                        text="Cancel" 
                        newStyle= 
                            {{ 
                                backgroundColor: "#f8c954", 
                                color: "white",
                            }}
                        clickFunc={cancelButtonClick}
                    >
                        
                    </Button>
                </div>
            </section>
            : 
            <section >
                <div style={{display: "flex", justifyContent: "flex-end"}}>
                    <FaPlusCircle size={50} style={{padding: "10px", fill: "#f8c954", marginRight: "85px" }} onClick={addButtonClick} id="fa-plus-circle"/>
                </div>
                <div className="symptom-list">
                    {getData.map((symptomCard, idx) => <SymptomList symptomCard={symptomCard} key={idx}/>)}
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