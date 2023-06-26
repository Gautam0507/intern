import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

const LoginPage = () => {
  let { loginUser } = useContext(AuthContext);
  return (
    <div className="container">
      <form onSubmit={loginUser}>
        <div className="form-group">
          <label>Email Address</label>
          <input
            type="text"
            name="username"
            placeholder="Enter Username"
            className="form-control"
          />
          <label>Password</label>
          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            className="form-control"
          />

          <input type="submit" className="btn btn-primary mt-3" />
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
