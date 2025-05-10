// src/components/SubmitJob.js
import React, { useState } from "react";
import { submitJob } from "../api";

export default function SubmitJob({ token }) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await submitJob(token, { prompt });
      alert(res.data.msg);
    } catch (err) {
      alert("Failed to submit job");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Submit AI Job</h2>
      <input placeholder="Enter prompt" onChange={e => setPrompt(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
}
