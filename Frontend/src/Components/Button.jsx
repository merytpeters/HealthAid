const Button = ({ text = "Learn More", fill = false }) => {
  return (
    <>
      {fill ? (
        <button
          className="button"
          type="button"
          style={{ backgroundColor: "#f8c954", color: "white" }}
        >
          {text}
        </button>
      ) : (
        <button
          className="button"
          type="button"
          style={{ backgroundColor: "transparent", color: "black" }}
        >
          {text}
        </button>
      )}
    </>
  );
};
export default Button;
