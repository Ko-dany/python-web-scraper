import React from "react";
import { Outlet, Link } from "react-router-dom";

const Test: React.FC = () => {
  return (
    <div style={{ margin: "50px" }}>
      <h2>Hi, This is a test page!</h2>
      <button>
        <Link to="/">Back to Home</Link>
      </button>
      <Outlet />
    </div>
  );
};

export default Test;
