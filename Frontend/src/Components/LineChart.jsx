import { useEffect } from "react";
import {Line} from "react-chartjs-2";
import Chart  from "chart.js/auto";

const LineChart =  ({chartData, title= "PIECHART"}) => {
    // useEffect(() => {
    //     return () => {
    //       // Cleanup all Chart.js instances on unmount
    //       Object.keys(Chart.instances).forEach((key) => {
    //         Chart.instances[key].destroy();
    //       });
    //     };
    //   }, []);

    return <div>
        <Line 
            data={chartData}
            options={{
                plugins:{
                    title: {
                        display: true,
                        text: title 
                    }
                }
            }}
        />
    </div>
}
export default LineChart;