import Chart from "chart.js/auto";
// import {CategoryScale} from "chart.js";
import {useState, useEffect} from "react"
import LineChart from "../Components/LineChart";
import Card from '../Components/Card'

// Chart.register(CategoryScale);
const Dashboard = () => {
    const [chartData, setChartData] = useState({
        labels: [2016, 2017,2018],
        datasets: [
            {
                label: 'Popularity of colours',
                data: [56, 23, 96],
                backgroundColor: [
                    'red',
                    'green',
                    'yellow'
                ],
                borderColor: "black",
                borderWidth: 2
            }
        ],
    })

    return (
    <div>
        <Card>

        </Card>
        <Card>

        </Card>
        <Card>

        </Card>
        <Card>

        </Card>
        <Card>
            
        </Card>
        <LineChart chartData={chartData}/>
    </div>)
}
export default Dashboard;