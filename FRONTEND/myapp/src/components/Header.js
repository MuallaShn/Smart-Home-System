
import React, { useState, useEffect } from "react";
import { Navbar, Button, Alert } from "react-bootstrap";
import { Sun, Moon, Mic } from "react-bootstrap-icons";

export function Header({ theme, toggleTheme }) {
  const [ledStatus, setLedStatus] = useState("");
  const [voiceStatus, setVoiceStatus] = useState("");

  return (
    <Navbar bg={theme === "dark" ? "dark" : "light"} variant={theme === "dark" ? "dark" : "light"} className="shadow-sm">
      <div className="container">
        <Navbar.Brand href="#home" className="fw-bold fs-4">SmartHome</Navbar.Brand>

        <div className="d-flex align-items-center gap-3">
          <Button variant={theme === "dark" ? "light" : "outline-secondary"} onClick={toggleTheme}>
            {theme === "dark" ? <Sun className="me-1" /> : <Moon className="me-1" />}
          </Button>

          <Button variant="primary" onClick={toggleLed}>
            {ledStatus === "açık" ? "LED Kapat" : "LED Aç"}
          </Button>

          <Button variant="success" onClick={toggleVoiceControl}>
            <Mic className="me-1" />
            
          </Button>
        </div>
      </div>
    </Navbar>
  );
}