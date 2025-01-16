import { useState, useEffect } from "react";
import {Chart as ChartJs}  from "chart.js/auto";
import {Pie} from "react-chartjs-2";

const PieChart = ({selected = "bloodSugar"}) => {
    const [graphData, setGraphData] = useState({
            labels: [],
            datasets: []
        });
    


    useEffect(()=> {
            const dashboardDataLoader = async () => {
                try{
                    const res = await fetch('http://localhost:8000/graphData');
                    const allGraphData = await res.json();
                    filterGraphData(allGraphData);
                    console.log("fetching data here")
                } catch(error) {
                    console.log("Error fetching data", error)
                }
                
            }
            dashboardDataLoader();
    
            // return () => {
            //     // Cleanup all Chart.js instances on unmount
            //     Object.keys(ChartJs.instances).forEach((key) => {
            //       ChartJs.instances[key].destroy();
            //     });
            //   };
    }, [selected]);

    const filterGraphData = (fullGraphData) => {
        let high = 0, mid = 0, normal = 0;
        fullGraphData.map(item => {
            console.log(item)
            if (selected === "bloodPressure") {
                if (item[selected].systolic > 70) 
                    high++;
                else if(item[selected].systolic > 50 && item.selected.systolic < 70) 
                    mid++;
                else 
                    normal++;
            }else {
                if (item[selected] > 70) 
                    high++;
                else if(item[selected] > 50 && item[selected] < 70) 
                    mid++;
                else 
                    normal++;
            }  
        });

        console.log([normal, mid,high])
        setGraphData(
            {
                labels: ["normal", "medium","high"],
                datasets: [
                    {
                        label: "",
                        data: [normal, mid, high],
                        borderWidtth: 1,
                        backgroundColor: ["#ffec4e", "#eeba2b","#f05a39"],
                        hoverOffset: 4
                    }
                ]
            }
        )
    }
    const options = {
        responsive: false,
        plugins: {
            title: {
                display: true,
                text: selected
            },
            tooltip: {
                enabled: false 
            }
        }
    } 
    return (
    <div style={{margin: "50px", marginTop: "30px"}}>
        <Pie data={graphData} width={600} height={400} options={options}></Pie>
    </div>)
};
export default PieChart;