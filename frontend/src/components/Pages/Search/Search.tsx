import React, { useState, useEffect } from "react";
import { Outlet, Link } from "react-router-dom";
import axios from "axios";

import "./Search.css";
import { Box, Button, Divider, TextField, Typography } from "@mui/material";
import Result from "../Result/Result";

function Search() {
  const [data, setData] = useState(false);
  const [jobs, setJobs] = useState(false);

  const [keyword, setKeyword] = useState("");
  const [response, setResponse] = useState("");

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
        <Typography variant="h4">{data}</Typography>
        <Typography variant="h2">GET THE JOB LIST</Typography>
      </header>
      <main>
        <Box sx={{ m: 3 }}>
          <TextField
            id="standard-basic"
            label="KEYWORD"
            color="primary"
            variant="outlined"
            value={keyword}
            onChange={(e) => {
              setKeyword(e.target.value);
            }}
            sx={{
              width: "100%",
              my: 2,
            }}
          />
          <Button
            variant="outlined"
            onClick={handleSubmit}
            sx={{ width: "100%" }}
          >
            SEARCH
          </Button>
        </Box>
        {jobs && <Result jobs={jobs}></Result>}
        {/*<Divider></Divider>
         <Box>
          <Button>
            <Link to="/test">GO TO TEST PAGE</Link>
          </Button>
          <Outlet />
        </Box> */}
      </main>
    </Box>
  );
}

export default Search;
