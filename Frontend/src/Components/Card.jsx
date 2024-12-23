const Card = ({children, size = '20px', round = '36px', marginDirection = "right"}) => {
    const styles = {
        fontSize: size, 
        borderRadius: round,
        border: '2px solid #f8c954',
        color: '#000000',
        textAlign: 'center',
        padding: '15px',
        width:'fit-content',
        height: 'fit-content',
        margin: marginDirection === "right" ? '0 100px 0 0' : '0 0 0 100px'
     
    }
    return (
        <section className="card" style={styles}>
            {children}
        </section>
    )
}
export default Card;