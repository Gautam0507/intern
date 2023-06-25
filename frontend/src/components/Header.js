import React, { useContext } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Header = () => {
  let { user, logoutUser } = useContext(AuthContext);
  return (
    <nav className="navbar navbar-light bg-dark">
      <div className="container">
        <div className="nav-item text-white">
          <Link to="/">Home</Link>
        </div>
        <span> | </span>
        {user ? (
          <a className="text-white nav-item" onClick={logoutUser}>
            Logout
          </a>
        ) : (
          <Link className="text-white" to="/login">
            Login
          </Link>
        )}

        {user && <p>Hello {user.username}</p>}
      </div>
    </nav>
  );
};

export default Header;
