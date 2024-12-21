// Write an interceptor. It will intercept any request we're going to send, and automatically add the correct headers so we don't need to manually write it a lot of times. We'll use axios interceptors for this. Axios is a JS library used to make HTTP requests for the browser and Node.js.

import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; // Attach the token to the Authorization header on all requests.
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
