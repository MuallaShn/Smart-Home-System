import React from "react";
import { Navbar, Nav, Button } from "react-bootstrap";
import { Sun, Moon } from "react-bootstrap-icons";

export function Header() {
  return (
    <Navbar
      bg="light"
      variant="light"
      expand="md"
      className="border-bottom shadow-sm"
      style={{ backdropFilter: "blur(10px)", background: "rgba(255, 255, 255, 0.9)" }}
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
            <Nav.Link href="#scenes" className="px-3">
              Senaryolar
            </Nav.Link>
            <Nav.Link href="#stats" className="px-3">
              İstatistikler
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>

        <div className="d-flex align-items-center gap-3">
          <Button variant="outline-secondary" className="d-flex align-items-center">
            <Sun className="me-1" />
          </Button>
          <Button variant="primary">Giriş Yap</Button>
        </div>
      </div>
    </Navbar>
  );
}
