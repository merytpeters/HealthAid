const Card = ({children, size = '20px', round = '36px'}) => {
    return (
        <section className="card" style={{fontSize: size, borderRadius: round}}>
            {children}
        </section>
    )
}
export default Card;