import React from "react";
import { Link } from "react-router-dom";
import "./new.css";

function Bikeweather() {
  return (
    <div>
      <Link to="/weatherinput" className="bike-button"> Check bike weather!</Link>
    </div>
  );
}

export default Bikeweather;
