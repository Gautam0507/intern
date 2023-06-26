import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";

const HomePage = () => {
  let [meters, setMeters] = useState([]);
  let { authTokens, logoutUser } = useContext(AuthContext);

  useEffect(() => {
    getMeters();
  }, []);

  let getMeters = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/meters/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setMeters(data);
    } else if (response.statusText === "Unauthorized") {
      logoutUser();
    }
  };
  let paidBill = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/meters/paid/", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();
    if (response.status === 200) {
      setMeters(data);
    } else if (response.statusText === "Unauthorized") {
      logoutUser();
    }
  };

  function calSum() {
    let sum = 0;
    {
      meters.map(
        (meter) =>
          (sum += meter.Last_recorded_reading - meter.Last_billed_reading)
      );
    }
    return sum;
  }
  let sum = calSum();
  return (
    <>
      <table className="table table-striped">
        <thead className="thead-dark">
          <tr>
            <th scope="col">Serial Number</th>
            <th scope="col">Last Billed Reading</th>
            <th scope="col">Last Recorded Reading</th>
            <th scope="col">Last Updated Time</th>
          </tr>
        </thead>
        <tbody>
          {meters.map((meter) => (
            <tr key={meter.id}>
              <td>{meter.Serial_number}</td>
              <td>{meter.Last_billed_reading}</td>
              <td>{meter.Last_recorded_reading}</td>
              <td>{meter.Last_updated_time}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p>
        Your Total Price: {sum > 0 ? sum * 2 : 0} (Total units :{" "}
        {sum > 0 ? sum : 0} * 2)
      </p>
      <button type="submit" onClick={paidBill} className="btn btn-primary">
        Pay Bill
      </button>
    </>
  );
};

export default HomePage;
