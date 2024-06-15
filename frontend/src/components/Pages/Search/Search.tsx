import React, { useState, useEffect, lazy } from "react";
import { Outlet, Link } from "react-router-dom";
import axios from "axios";

import "./Search.css";

const Test = lazy(() => import("../../Test"));

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
      const res = await axios.post("http://localhost:5000/search", {
        keyword: keyword,
      });
      setJobs(res.data);
      console.log(jobs);

      setResponse("");
      setKeyword("");
    } catch (error) {
      console.log("Error occurred: ", error);
      setResponse("Error: Could not get a response from the server.");
    }
  };

  return (
    <div className="classApp">
      <header>
        <h1>Hello from React!</h1>
        <h1>{data}</h1>
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
        <div>
          <button>
            <Link to="/test">Go to Test Page</Link>
          </button>
          <Outlet />
        </div>
      </main>
    </div>
  );
}

export default Search;
