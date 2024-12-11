import React, { useState } from "react";
import { Header } from "./components/Header";
import { SceneViewer } from "./components/SceneViewer";
import { DeviceControls } from "./components/DeviceControls";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [isLightOn, setIsLightOn] = useState(false);
  const [brightness, setBrightness] = useState(50);


  return (
    <div>
      <Header />
      <main style={{ marginTop: "80px" }}>
        <section className="py-5 bg-light text-center">
          <h1 className="display-4 fw-bold">Akıllı Ev Kontrolü</h1>
          <p className="lead text-muted">Evinizi tek bir yerden kontrol edin</p>
        </section>

        <section id="devices" className="py-5">
          <SceneViewer isLightOn={isLightOn} brightness={brightness} />
        </section>

        <section id="scenes" className="py-5 bg-light">
          <div className="container">
            <h2 className="text-center fw-bold mb-4">Cihaz Kontrolleri</h2>
            <DeviceControls
              isLightOn={isLightOn}
              setIsLightOn={setIsLightOn}
              brightness={brightness}
              setBrightness={setBrightness}
            />
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
