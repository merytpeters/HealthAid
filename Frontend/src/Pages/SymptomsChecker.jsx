import { useState } from "react";
import "../Styles/Symptoms.css";
import search from "../assets/search.png";

export const SymptomsChecker = () => {
  const [data, setData] = useState("");
  const [res, setRes] = useState([]);

  const handleChange = (e) => {
    e.preventDefault();
    setData(e.target.value);
  };

  const handleSearch = () => {
    if (data === "") return;
    setRes([...res, data]);
    setData("");
  };
  return (
    <div className="symp">
      <div className="search-btn">
        <input
          type="text"
          id="text"
          name="symptom"
          value={data}
          onChange={handleChange}
        />

        <button type="click" onClick={handleSearch}>
          <img src={search} />
        </button>
      </div>

      <div className="symptoms">
        {res.length > 0 &&
          res.map((item, index) => (
            <div className="item" key={index}>
              {item}
            </div>
          ))}
      </div>
    </div>
  );
};
