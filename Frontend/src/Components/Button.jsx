const Button = ({ text = "Learn More", newStyle = {}, clickFunc}) => {
  return (
    <>
    <button
      className="button"
      type="button"
      style={{...newStyle}}
      onClick={clickFunc}
      
    >
      {text}
    </button>
    </>
  );
};
export default Button;
