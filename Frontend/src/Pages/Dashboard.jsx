import Chart from "chart.js/auto";
import {CategoryScale} from "chart.js";
import {useState, useEffect} from "react"
import PieChart from "../Components/PieChart";

Chart.register(CategoryScale);
const Dashboard = () => {
    const [chartData, setChartData] = useState({
        labels: [2016, 2017,2018],
        datasets: [
            {
                label: 'Popularity of colours',
                data: [55, 23, 96],
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
        <PieChart chartData={chartData}/>
    </div>)
}
export default Dashboard;