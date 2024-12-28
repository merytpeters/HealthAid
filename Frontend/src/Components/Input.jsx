import React from "react";

export const Input = ({type, newStyle= {}, placeholder = ""}) => {

  return (
    <div>
      <form>
        <label htmlFor="type"></label>
        <input 
        type={type}
        name="symptomInput"
        placeholder={placeholder}
        style={{...newStyle}}
        />
      </form>
    </div>
  );
};
