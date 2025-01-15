import { useState } from "react";
import { Link } from "react-router-dom";

import { postRequest } from "../services/apis";

import "../Styles/signup.css";

export const Signup = () => {
  const [data, setData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    // dob: "",
    weight: "",
    height: "",
    gender: "",
    password: "",
    // cpass: "",
    username: "",
  });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };
  const submitHandler = async (e) => {
    e.preventDefault();
    if (
      data.password == "" ||
      data.username == "" ||
      data.email == "" ||
      data.first_name == "" ||
      data.last_name == "" ||
      data.weight == "" ||
      data.height == "" ||
      data.gender == ""
    ) {
      setError("field is required");
      return;
    }

    //the
    const result = await postRequest(data, "signup");
    console.log(result.data);

    console.log(data);
  };
  return (
    <div className="main">
      <form className="fields" onSubmit={submitHandler}>
        <h2>Signup</h2>
        <span className="field">
          <div className="field-div">
            <label htmlFor="first_name">Firstname:</label>
            <input
              type="text"
              id="first_name"
              name="first_name"
              required
              value={data.first_name}
              onChange={handleChange}
            />
          </div>
          <div className="field-div">
            <label htmlFor="last_name">Lastname:</label>
            <input
              type="text"
              id="last_name"
              name="last_name"
              required
              value={data.last_name}
              onChange={handleChange}
            />
          </div>
        </span>
        <span className="field">
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
          <div className="field-div">
            <label htmlFor="gender">Username:</label>
            <input
              type="text"
              id="username"
              name="username"
              required
              value={data.username}
              onChange={handleChange}
            />
          </div>
        </span>
        <span className="field">
          <div className="field-div">
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              required
              value={data.password}
              onChange={handleChange}
            />
            {error && <p className="error">*{error}</p>}
          </div>
          <div className="field-div">
            <label htmlFor="cpass">Gender:</label>
            <input
              type="text"
              id="gender"
              name="gender"
              required
              value={data.gender}
              onChange={handleChange}
            />
            {error && <p className="error">*{error}</p>}
          </div>
        </span>
        <span className="field">
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
        </span>
        <span className="field">
          {/* <div className="field-div">
            <label htmlFor="height">height(in cm):</label>
            <input
              type="number"
              id="height"
              name="height"
              value={data.height}
              onChange={handleChange}
            />
          </div> */}
          {/* <div className="field-div">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              //   value={data.email}
              //   onChange={handleChange}
            />
          </div> */}
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

{
  /* <div className="field-div">
  <label htmlFor="dob">Date of Birth:</label>
  <input
    type="date"
    id="dob"
    name="dob"
    required
    value={data.dob}
    onChange={handleChange}
  />
</div>; */
}
