import axios from "axios";

//post request
export const postRequest = async (data, action) => {
  console.log(data, action);
  try {
    const response = await axios.post(
      `http://localhost:5000/auth/${action}`,
      data
    );
    return {
      error: false,
      data: response.data,
    };
  } catch (err) {
    return {
      error: true,
      data: err?.message || err,
    };
  }
};

export const getRequest = async (action) => {
  console.log(action);
  try {
    const res = await axios.get(`http://localhost:5000/${action}`);
    console.log(res);
    return {
      error: false,
      data: res.data,
    };
  } catch (err) {
    return {
      error: true,
      data: err?.message || err,
    };
  }
};
