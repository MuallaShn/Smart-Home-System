import React, { useState } from "react";
import { Header } from "./components/Header";
import { SceneViewer } from "./components/SceneViewer";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
  };

  const textColor = theme === "dark" ? "rgba(255, 255, 255, 0.7)" : "rgba(0, 0, 0, 0.85)";

  return (
    <div style={{ backgroundColor: theme === "dark" ? "#121212" : "white" }}>
      <Header theme={theme} toggleTheme={toggleTheme} />
      <main style={{ marginTop: "80px" }}>
        <section className={`py-5 text-center ${theme === "dark" ? "bg-dark text-white" : "bg-light text-dark"}`}>
          <h1 className="display-4 fw-bold">Akıllı Ev Kontrolü</h1>
          <p className="lead" style={{ color: textColor }}>
            Evinizi tek bir yerden kontrol edin
          </p>
        </section>
        <section id="devices" className="py-5">
          <SceneViewer theme={theme} />
        </section>
      </main>
    </div>
  );
}

export default App;
