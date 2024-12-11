const Button = ({text = 'Learn More', fill = false}) => {
    return(
        <>
            {fill ? <button className="button" type="button" style={{backgroundColor: '#f8c954'}}>{text}</button> : <button className="button" type="button" style={{backgroundColor: 'transparent'}}>{text}</button> } 
        </>
    )
};
export default Button;