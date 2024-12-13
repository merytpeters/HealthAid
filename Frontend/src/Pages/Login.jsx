import { useState } from "react";

import "../Styles/login.css";
import pic from "../assets/exercise.jpg";

export const Login = () => {
  const [data, setData] = useState({ email: "", password: "" });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };
  const submitHandler = (e) => {
    e.preventDefault();
    console.log(data);
  };
  return (
    <div className="main">
      <div className="image">
        <img src={pic} alt="woman exercising" />
      </div>
      <div className="form-div">
        <form className="form" onSubmit={submitHandler}>
          <h2>Login</h2>
          <div>
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              value={data.email}
              onChange={handleChange}
            />
          </div>
          <div>
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              value={data.password}
              onChange={handleChange}
            />
          </div>
          <div className="btn">
            <button type="submit">Login</button>
          </div>
          <span className="other">
            {/* <div className="sign-up"></div>
            <div className="forgot"></div> */}
            <div className="sign-up">
              <p>
                New Here? <a className="links">signup</a>
              </p>
            </div>
            <div className="forgot">
                <p className="links">Forgot password</p>
            </div>
          </span>
        </form>
      </div>
    </div>
  );
};
