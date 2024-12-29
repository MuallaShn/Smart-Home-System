import React from "react";
import { Navbar, Button } from "react-bootstrap";
import { Sun, Moon } from "react-bootstrap-icons";

export function Header({ theme, toggleTheme }) {


  return (
    <Navbar bg={theme === "dark" ? "dark" : "light"} variant={theme === "dark" ? "dark" : "light"} className="shadow-sm">
      <div className="container">
        <Navbar.Brand href="#home" className="fw-bold fs-4">SmartHome</Navbar.Brand>

        <div className="d-flex align-items-center gap-3">
          <Button variant={theme === "dark" ? "light" : "outline-secondary"} onClick={toggleTheme}>
            {theme === "dark" ? <Sun className="me-1" /> : <Moon className="me-1" />}
          </Button>

        </div>
      </div>

    </Navbar>
  );
}