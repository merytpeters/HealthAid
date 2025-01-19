
const Card = ({children ,newStyle = {} ,func, className = "card"}) => {
    return (
        <div  style={{...newStyle}} id="card" onClick={func} className={className}>
            {children}
        </div>
        
    )
}
export default Card;