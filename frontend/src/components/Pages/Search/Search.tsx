import React, { useState, useEffect } from "react";
import { Outlet, Link } from "react-router-dom";
import axios from "axios";

import "./Search.css";
import {
  Box,
  Button,
  CircularProgress,
  Divider,
  LinearProgress,
  TextField,
  Typography,
} from "@mui/material";
import Result from "../Result/Result";

function Search() {
  // const [data, setData] = useState(false);
  const [loadingJobs, setLoadingJobs] = useState(false);
  const [jobs, setJobs] = useState<any>(null);
  const [exportRef, setExportRef] = useState<string | null>(null);
  const [keyword, setKeyword] = useState<string>("");
  const [response, setResponse] = useState<string>("");

  // Inital Fetching
  // useEffect(() => {
  //   axios
  //     .get("http://127.0.0.1:5000/api/data")
  //     .then((response) => {
  //       setData(response.data.message);
  //     })
  //     .catch((error) => {
  //       console.error("Error fetching data: ", error);
  //     });
  // }, []);

  const handleSubmit = async (event: any) => {
    event.preventDefault();
    setLoadingJobs(true);

    console.log(keyword);
    try {
      console.log("Starting Playwright...");
      const responseJobs: any = await axios.post(
        "http://localhost:5000/search",
        {
          keyword: keyword,
        }
      );

      console.log("Finishing Playwright...");
      setJobs(responseJobs.data);
      console.log(jobs);

      setResponse("");
      setKeyword("");
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        // console.log(error.response.data);
        setResponse(error.response.data);
      } else {
        // console.log("Error occurred: ", error, response);
        setResponse("Error: Could not get a response from the server.");
      }
    } finally {
      setLoadingJobs(false);
    }
  };

  // const handleExport = async () => {
  //   try {
  //     const responseExport = await axios.post(
  //       "http://localhost:5000/export",
  //       { keyword },
  //       { responseType: "blob" }
  //     );

  //     const url = window.URL.createObjectURL(
  //       new Blob([responseExport.data], { type: "text/csv" })
  //     );
  //     const link = document.createElement("a");
  //     link.href = url;
  //     link.setAttribute("download", `${keyword}.csv`);
  //     document.body.appendChild(link);
  //     link.click();
  //     document.body.removeChild(link);
  //   } catch (error) {
  //     console.error("Error exporting data:", error);
  //   }
  // };

  return (
    <Box sx={{ m: 5 }}>
      <header>
        <Typography variant="h2" align="center">
          GET THE JOB LIST
        </Typography>
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
            sx={{ width: "100%", mb: 3 }}
          >
            SEARCH
          </Button>
          {loadingJobs && <LinearProgress />}
          {!loadingJobs && jobs && (
            <Box>
              {/* <Button onClick={handleExport} sx={{ width: "100%", mb: 3 }}>
                EXPORT
              </Button> */}
              <Result jobs={jobs} />
            </Box>
          )}
        </Box>
      </main>
      <footer>
        <Typography align="center">CREATED BY DAHYUN KO</Typography>
      </footer>
    </Box>
  );
}

export default Search;
