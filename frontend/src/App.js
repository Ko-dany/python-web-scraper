import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState("");
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

  const getKeyword = (event) => {
    setKeyword(event.target.value);
    console.log(event.target.value);
  };

  const onClick = () => {};

  const handleSubmit = async (event) => {
    event.preventDefault();

    console.log(keyword);
    try {
      const response = await axios.post("http://localhost:5000/search", {
        keyword: keyword,
      });
      setResponse(response.data.message);
      console.log(response);

      setKeyword("");
    } catch (error) {
      console.log("Error occurred: ", error);
      setResponse("Error: Could not get a response from the server.");
      console.log(response);
    }
  };

  return (
    <div>
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
      </main>
    </div>
  );
}

export default App;
