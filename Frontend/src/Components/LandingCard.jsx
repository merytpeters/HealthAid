import Card from "./Card";

const LandingCard = ({children , image, newStyle = {}, imgPosition = "right"}) => {
    const imgStyle = {
        width: "150px", 
        borderColor: "white",
        margin: imgPosition === "right" ? '5px 150px 5px 5px' : '5px 5px 5px 150px'


    }
    const justifyContent = imgPosition === "right" ? "right" : "left"
    if (imgPosition === "left")
        return (
            <section style={{display: "flex", justifyContent}}> 
            <Card  newStyle={{...newStyle, margin: "0 0 0 100px"}}>
                {children}
            </Card>
            <img  src= {image} style={imgStyle}/>
            
            </section>
        )
    return (
        <section style={{display: "flex", justifyContent}}> 
        <img  src= {image} style={imgStyle}/>
        <Card   newStyle={{...newStyle, margin: "0 100px 0 0"}} >
            {children}
        </Card>
        
        
        </section>
    )
}
export default LandingCard;