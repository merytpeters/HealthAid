
const Card = ({children ,newStyle = {} ,}) => {
    return (
        <div className="card" style={{...newStyle}} id="card">
            {children}
        </div>
        
    )
}
export default Card;