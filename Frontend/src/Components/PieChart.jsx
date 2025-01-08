const PieChart = (selected) => {
    const [graphData, setGraphData] = useState({
            labels: [],
            datasets: []})
    
     
    
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
        let high = 0, mid = 0, normal = 0;
        fullGraphData.map(item => {

        })
    }
        
    return <div></div>
};
export default PieChart;