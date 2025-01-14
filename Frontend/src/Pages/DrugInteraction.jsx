import { useState } from "react";
import { useNavigate } from "react-router-dom";
import search from "../assets/search.png";
import "../Styles/Symptoms.css";

export const DrugInteraction = () => {
  const [data, setData] = useState("");
  const [res, setRes] = useState([]);
  const handleChange = (e) => {
    e.preventDefault();
    setData(e.target.value);
  };
  const navigate = useNavigate();

  const handleSearch = () => {
    if (data === "") return;
    setRes([...res, data]);
    setData("");
    // make api call , if
    setTimeout(() => navigate("/drug-int-res"), 1000);
  };
  return (
    <div className="symp">
      <div className="search-btn">
        <input
          // type="text"
          id="text"
          name="symptom"
          value={data}
          onChange={handleChange}
        />

        <button type="click" onClick={handleSearch}>
          <img src={search} />
        </button>
      </div>
    </div>
  );
};
