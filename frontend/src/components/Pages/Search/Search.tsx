import React, { useState, useEffect } from "react";
import { Outlet, Link } from "react-router-dom";
import axios from "axios";

import "./Search.css";
import { Box, Typography } from "@mui/material";

function Search() {
  const [data, setData] = useState("");
  const [keyword, setKeyword] = useState("");
  const [response, setResponse] = useState("");
  const [jobs, setJobs] = useState("");

  // Inital Fetching
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/data")
      .then((response) => {
        setData(response.data.message);
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  }, []);

  const handleSubmit = async (event: any) => {
    event.preventDefault();

    console.log(keyword);
    try {
      console.log("Starting Playwright...");
      const res: any = await axios.post("http://localhost:5000/search", {
        keyword: keyword,
      });

      console.log("Finishing Playwright...");

      setJobs(res.data);
      console.log(jobs);

      setResponse("");
      setKeyword("");
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        console.log(error.response.data);
        setResponse(error.response.data);
      } else {
        setResponse("Error: Could not get a response from the server.");
        console.log("Error occurred: ", error, response);
      }
    }
  };

  return (
    <Box sx={{ m: 5 }}>
      <header>
        <Typography variant="h2">GET THE JOB LIST</Typography>
      </header>
      <main>
        <input
          type="text"
          value={keyword}
          onChange={(e) => {
            setKeyword(e.target.value);
          }}
        />
        <button onClick={handleSubmit}>Search</button>
        <Box>
          <button>
            <Link to="/test">Go to Test Page</Link>
          </button>
          <Outlet />
        </Box>
      </main>
    </Box>
  );
}

export default Search;
