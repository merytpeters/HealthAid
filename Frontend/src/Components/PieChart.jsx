import {Pie} from "react-chartjs-2";

const PieChart =  ({chartData}) => {
    return <div>
        <Pie 
            data={chartData}
            options={{
                plugins:{
                    title: {
                        display: true,
                        text: "Heart Rate 30-12-2024" 
                    }
                }
            }}
        />
    </div>
}
export default PieChart;