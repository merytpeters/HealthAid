import { useState } from "react";
import { Link } from "react-router-dom";


import "../Styles/signup.css";

export const Signup = () => {
  const [data, setData] = useState({
    fname: "",
    lname: "",
    email: "",
    dob: "",
    weight: "",
    height: "",
    gender: "",
    pass: "",
    cpass: "",
  });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };
  const submitHandler = (e) => {
    e.preventDefault();
    if (data.pass != data.cpass) {
      setError("passwords should match");
      return;
    }
    console.log(data);
  };
  return (
    <div className="main">
      <form className="fields" onSubmit={submitHandler}>
        <h2>Signup</h2>
        <span className="field">
          <div className="field-div">
            <label htmlFor="fname">Firstname:</label>
            <input
              type="text"
              id="fname"
              name="fname"
              required
              value={data.fname}
              onChange={handleChange}
            />
          </div>
          <div className="field-div">
            <label htmlFor="lname">Lastname:</label>
            <input
              type="text"
              id="lname"
              name="lname"
              required
              value={data.lname}
              onChange={handleChange}
            />
          </div>
        </span>
        <span className="field">
          <div className="field-div">
            <label htmlFor="dob">Date of Birth:</label>
            <input
              type="date"
              id="dob"
              name="dob"
              required
              value={data.dob}
              onChange={handleChange}
            />
          </div>
          <div className="field-div">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              required
              value={data.email}
              onChange={handleChange}
            />
          </div>
        </span>
        <span className="field">
          <div className="field-div">
            <label htmlFor="pass">Password:</label>
            <input
              type="password"
              id="pass"
              name="pass"
              required
              value={data.pass}
              onChange={handleChange}
            />
            {error && <p className="error">*{error}</p>}
          </div>
          <div className="field-div">
            <label htmlFor="cpass">Confirm Password:</label>
            <input
              type="password"
              id="cpass"
              name="cpass"
              required
              value={data.cpass}
              onChange={handleChange}
            />
            {error && <p className="error">*{error}</p>}
          </div>
        </span>
        <span className="field">
          <div className="field-div">
            <label htmlFor="gender">Gender:</label>
            <input
              type="gender"
              id="gender"
              name="gender"
              required
              value={data.gender}
              onChange={handleChange}
            />
          </div>
          <div className="field-div">
            <label htmlFor="weight">Weight(in Kg):</label>
            <input
              type="number"
              id="weight"
              name="weight"
              required
              value={data.weight}
              onChange={handleChange}
            />
          </div>
        </span>
        <span className="field">
          <div className="field-div">
            <label htmlFor="height">height(in cm):</label>
            <input
              type="number"
              id="height"
              name="height"
              value={data.height}
              onChange={handleChange}
            />
          </div>
          <div className="field-div">
            {/* <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              //   value={data.email}
              //   onChange={handleChange}
            /> */}
          </div>
        </span>

        <span className="field">
          <div className="field-div">
            <p>
              Already have an account?{" "}
              <i>
                <Link to="/login" style={{ textDecoration: "none" }}>
                  {" "}
                  login
                </Link>
              </i>
            </p>
          </div>
          <div className="field-div">
            <button type="submit">Sign up</button>
          </div>
        </span>
      </form>
    </div>
  );
};
