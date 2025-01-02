import React from "react";
import { Navbar, Button } from "react-bootstrap"; // React-Bootstrap'tan Navbar ve Button bileşenlerini içe aktarıyoruz.
import { Sun, Moon } from "react-bootstrap-icons"; // React-Bootstrap-Icons'tan Güneş ve Ay ikonlarını içe aktarıyoruz.

// Header bileşeni tanımlanıyor. Tema durumu ve temayı değiştirme işlevi props olarak alınıyor.
export function Header({ theme, toggleTheme }) {

  return (
    // Navbar bileşeni, temaya göre arka plan ve varyantını dinamik olarak belirliyor.
    // Arka plan rengi tema "dark" ise koyu, aksi halde açık olacak.
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