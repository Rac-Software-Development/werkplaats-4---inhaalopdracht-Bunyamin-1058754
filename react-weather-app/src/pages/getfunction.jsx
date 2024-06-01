import React , { useEffect, useState }  from "react";
import axios from 'axios';


const Get = () => {
  const [data, setData] = useState('');

  
  useEffect((city) => {
   if (city){
    axios.get(`http://127.0.0.1:5000/predict/${city}`)
    .then((res) => {
      setData(data);
      console.log(res.data)
    });
   
}});
  
;

return (
    <>
      <h1>{data['city']}</h1>
      <h2>ddf</h2>
    </>
  );
};

export default Get;
