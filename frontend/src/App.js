import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState("");

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

  return (
    <div>
      <header>
        <h1>Hello from React!</h1>
        <h1>{data}</h1>
      </header>
    </div>
  );
}

export default App;
