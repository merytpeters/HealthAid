import { useState, useEffect } from "react";
import {Chart as ChartJs}  from "chart.js/auto";
import "chartjs-adapter-date-fns";
import {Line} from "react-chartjs-2";


const LineChart =  () => {
    const [graphData, setGraphData] = useState({
        labels: [],
        datasets: []
    })

 

    useEffect(()=> {

        const dashboardDataLoader = async () => {
            try{
                const res = await fetch('http://localhost:8000/graphData');
                const allGraphData = await res.json();
                filterGraphData(allGraphData);
            } catch(error) {
                console.log("Error fetching data", error)
            }
            
        }
        dashboardDataLoader();

        return () => {
            // Cleanup all Chart.js instances on unmount
            Object.keys(ChartJs.instances).forEach((key) => {
              ChartJs.instances[key].destroy();
            });
          };
    }, []);

    const filterGraphData = (fullGraphData) => {
        const time = [];
        const heartRate = [];
        const systolic = [];
        const diastolic = [];
        const bloodSugar = [];
        const temp = [];

        fullGraphData.forEach((item) => {
            heartRate.push({ x: item.time, y: item.heartRate});
            bloodSugar.push({x: item.time, y: item.bloodSugar});
            temp.push({x: item.time, y: item.temp});
            systolic.push({x: item.time, y: item.bloodPressure.systolic});
            diastolic.push({x: item.time, y: item.bloodPressure.diastolic});
        });

        setGraphData(
            {
                datasets: [
                    {
                        label: "Heart Rate",
                        data: heartRate,
                        borderColor: "#f8c954",
                        borderWidtth: 1,
                        backgroundColor: "#f8c954"
                    },
                    {
                        label: "Blood Sugar",
                        data: bloodSugar,
                        borderColor: "#ed155d",
                        borderWidtth: 1,
                        backgroundColor: "#ed155d"
                    },
                    {
                        label: "Blood Pressure",
                        data: systolic,
                        borderColor: "#f05a39",
                        borderWidtth: 1,
                        backgroundColor: "#f05a39"
                    },
                    // {
                    //     label: "Diastolic Blood Pressure",
                    //     data: diastolic,
                    //     borderColor: "#f05a39",
                    //     borderWidtth: 1
                    // },
                    // {
                    //     label: "Temperature",
                    //     data: temp,
                    //     borderColor: "#f05a39",
                    //     borderWidtth: 1
                    // }
                ]
            }
        );
    };



    const options = {
        responsive: false,
        plugins: {
            title: {
                display: true,
                text: "Rate per Hour"
            }
        },
        scales: {
            x: {
                type: "time",
                time: {
                    tooltipFormat: "hh:mm",
                    unit: "hour"
                },
                title: {
                    display: true,
                    text: "Time"
                },
                grid: {
                    drawOnChartArea: false,
                }
            },
            y : {
                title: {
                    display: true,
                    text: "Rate"
                }
            }
        }
    };
    
    return (
    <div style={{border: "3px solid #f8c954", borderRadius: "15px", width: "600px", height: "400px", padding: "15px", margin: "50px", marginTop: "10px"}}>
        <Line data={graphData} options={options} width={600} height={400}/>
    </div>
    )

}
export default LineChart;