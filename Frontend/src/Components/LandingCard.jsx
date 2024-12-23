import Card from "./Card";

const LandingCard = ({children , image, size, round, imgPosition = "right"}) => {
    const imgStyle = {
        width: "150px", 
        borderColor: "white",
        margin: imgPosition === "right" ? '5px 150px 5px 5px' : '5px 5px 5px 150px'


    }
    const justifyContent = imgPosition === "right" ? "right" : "left"
    if (imgPosition === "left")
        return (
            <section style={{display: "flex", justifyContent}}> 
            <Card size= {size} round={round} marginDirection= {imgPosition}>
                {children}
            </Card>
            <img  src= {image} style={imgStyle}/>
            
            </section>
        )
    return (
        <section style={{display: "flex", justifyContent}}> 
        <img  src= {image} style={imgStyle}/>
        <Card size= {size} round={round} marginDirection= {imgPosition}>
            {children}
        </Card>
        
        
        </section>
    )
}
export default LandingCard;