import React from "react";
import { Navbar, Nav, Button } from "react-bootstrap";
import { Sun, Moon } from "react-bootstrap-icons";

export function Header({ theme, toggleTheme }) {
  return (
    <Navbar
    bg={theme === "dark" ? "dark" : "light"}
    variant={theme === "dark" ? "dark" : "light"}
    expand="md"
    className="shadow-sm"
    style={{
      backdropFilter: "blur(10px)",
      background: theme === "dark" ? "rgba(0, 0, 0, 0.9)" : "rgba(255, 255, 255, 0.9)",
      borderBottom: theme === "dark" ? "1px solid black" : "1px solid rgba(0, 0, 0, 0.1)", // Dinamik renk
    }}
  >
  
      <div className="container">
        <Navbar.Brand href="#home" className="fw-bold fs-4">
          SmartHome
        </Navbar.Brand>

        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#devices" className="px-3">
              Cihazlar
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>

        <div className="d-flex align-items-center gap-3">
          <Button
            variant={theme === "dark" ? "light" : "outline-secondary"}
            className="d-flex align-items-center"
            onClick={toggleTheme}
          >
            {theme === "dark" ? <Sun className="me-1" /> : <Moon className="me-1" />}
          </Button>
          <Button variant="primary">Giriş Yap</Button>
        </div>
      </div>
    </Navbar>
  );
}