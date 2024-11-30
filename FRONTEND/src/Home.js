import React, { useState } from "react";
import { Container, Button, Row, Col, Card } from "react-bootstrap";
import { Header } from "./Header"; // Header bileşenini buradan alıyoruz
import { SceneViewer } from "./SceneViewer"; // SceneViewer bileşeni
import { DeviceControls } from "./DeviceControls"; // DeviceControls bileşeni
import { StatsSection } from "./StatsSection"; // StatsSection bileşeni

export default function Home() {
  const [isLightOn, setIsLightOn] = useState(false);
  const [brightness, setBrightness] = useState(100);

  return (
    <div className="bg-light min-vh-100">
      <Header />

      <Container className="pt-5 pb-3">
        {/* Hero Bölümü */}
        <Row className="text-center mb-5">
          <Col>
            <h1 className="display-4 fw-bold">Akıllı Ev Kontrolü</h1>
            <p className="lead text-muted">
              Evinizi tek bir yerden kontrol edin
            </p>
          </Col>
        </Row>

        {/* 3D Sahne */}
        <Row className="mb-20" id="devices">
          <Col>
            <Card className="shadow"  style={{ width: "100%", height: "500px" }}>
              <Card.Body>
                <SceneViewer isLightOn={isLightOn} brightness={brightness}  style={{ width: "800px", height: "500px" }}  />
              </Card.Body>
            </Card>
          </Col>
        </Row>

        {/* Cihaz Kontrolleri */}
        <Row className="mb-5" id="scenes">
          <Col>
            <h2 className="fw-bold mb-4">Cihaz Kontrolleri</h2>
            
            <DeviceControls
              isLightOn={isLightOn}
              setIsLightOn={setIsLightOn}
              brightness={brightness}
              setBrightness={setBrightness}
            />
      
          </Col>
        </Row>

        {/* İstatistikler */}
        <Row className="mb-5" id="stats">
          <Col>
            <h2 className="fw-bold mb-4">İstatistikler</h2>
            <StatsSection />
          </Col>
        </Row>
      </Container>

      {/* Footer */}
      <footer className="bg-dark text-white text-center py-3">
        <Container>
          <p className="mb-0">© 2024 SmartHome. Tüm hakları saklıdır.</p>
        </Container>
      </footer>
    </div>
  );
}
