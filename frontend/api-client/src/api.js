import axios from "axios";

const API = axios.create({
  baseURL: "https://fastapi-cloud-dev.onrender.com",
});

export const signup = (data) => API.post("/signup", data);
export const login = (data) => API.post("/login", data);
export const submitJob = (token, data) =>
  API.post("/submit-job", data, {
    headers: { Authorization: `Bearer ${token}` },
  });

export default API;
