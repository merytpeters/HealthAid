const Footer = () => {
    const styles = {
        fontSize : "14px",
        textAlign: "center",
        borderTop: "1px solid #f8c954",
        margin: "10px",
        width: "100%",
    }
    return (
        <footer>
            <div>
                <p style={styles}>
                    The information provided on this website is for general informational purposes only and is not intended as professional medical advice. Please consult with a qualified medical professional for any specific advice or concerns.
                </p>
            </div>
            {/* <p>Copyright &copy;</p> */}
        </footer>
    )
}
export default Footer;