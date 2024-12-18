import { useState } from "react";
import { Button, Container, Row, Col, Card } from "react-bootstrap";
import { Tv, TvFill, Phone, PhoneFill, Lightbulb, LightbulbFill } from "react-bootstrap-icons";

export function SceneViewer({ theme }) {
  const [deviceStates, setDeviceStates] = useState({
    tv: false,
    phone: false,
    light: false, // Ampül durumu
  });

  const toggleDevice = async (device) => {
    const newState = !deviceStates[device];
    setDeviceStates((prevStates) => ({
      ...prevStates,
      [device]: newState,
    }));

    // Sunucuya POST isteği gönder
    await fetch(`http://192.168.137.1:5000/toggle/${device}`, { method: "POST" });
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        {/* Başlık ve Açıklama */}
        <Col md={12} className="text-center">
          <h2
            className="fw-bold"
            style={{
              color: theme === "dark" ? "white" : "black",
            }}
          >
            Cihazlar
          </h2>
        </Col>
      </Row>
      <Row className="justify-content-center mt-4">
        {/* PC Kartı */}
        <Col xs={12} md={4} className="mb-4">
          <Card
            className="shadow-sm text-center"
            style={{
              minHeight: "200px",
              padding: "20px",
              backgroundColor: theme === "dark" ? "#1E1E1E" : "white",
              color: theme === "dark" ? "white" : "black",
            }}
          >
            <Card.Body>
              <h5 className="mb-4">Bilgisayar</h5>
              <Button
                variant={deviceStates.tv ? "success" : theme === "dark" ? "outline-light" : "outline-secondary"}
                onClick={() => toggleDevice("tv")}
              >
                {deviceStates.tv ? <TvFill size={40} /> : <Tv size={40} />}
              </Button>
            </Card.Body>
          </Card>
        </Col>
        {/* Telefon Kartı */}
        <Col xs={12} md={4} className="mb-4">
          <Card
            className="shadow-sm text-center"
            style={{
              minHeight: "200px",
              padding: "20px",
              backgroundColor: theme === "dark" ? "#1E1E1E" : "white",
              color: theme === "dark" ? "white" : "black",
            }}
          >
            <Card.Body>
              <h5 className="mb-4">Telefon</h5>
              <Button
                variant={deviceStates.phone ? "success" : theme === "dark" ? "outline-light" : "outline-secondary"}
                onClick={() => toggleDevice("phone")}
              >
                {deviceStates.phone ? <PhoneFill size={40} /> : <Phone size={40} />}
              </Button>
            </Card.Body>
          </Card>
        </Col>
        {/* Ampül Kartı */}
        <Col xs={12} md={4} className="mb-4">
          <Card
            className="shadow-sm text-center"
            style={{
              minHeight: "200px",
              padding: "20px",
              backgroundColor: theme === "dark" ? "#1E1E1E" : "white",
              color: theme === "dark" ? "white" : "black",
            }}
          >
            <Card.Body>
              <h5 className="mb-4">Led</h5>
              <Button
                variant={deviceStates.light ? "success" : theme === "dark" ? "outline-light" : "outline-secondary"}
                onClick={() => toggleDevice("light")}
              >
                {deviceStates.light ? <LightbulbFill size={40} /> : <Lightbulb size={40} />}
              </Button>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}
