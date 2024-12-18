import { useState } from "react";
import { Button, Container, Row, Col, Card } from "react-bootstrap";
import { Tv, TvFill, PcFill, Pc, Lightbulb, LightbulbFill } from "react-bootstrap-icons";

export function SceneViewer({ theme }) {
  const [deviceStates, setDeviceStates] = useState({
    tv: false,
    phone: false,
    light: false,
  });



  const toggleDevice = async (device) => {
  const newState = !deviceStates[device];
  setDeviceStates((prevStates) => ({
    ...prevStates,
    [device]: newState,
  }));

  const state = newState ? "turn_on" : "turn_off";

  try {
    const response = await fetch(`http://127.0.0.1:5000/${device}/${state}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Fetch error:", error);
  }
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
  {/* Bilgisayar Kartı */}
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
          variant={deviceStates["pc"] ? "success" : theme === "dark" ? "outline-light" : "outline-secondary"}
          onClick={() => toggleDevice("pc")}
          style={{ width: "50px", height: "50px" }}
        >
          {deviceStates["pc"] ? <TvFill size={24} /> : <Tv size={24} />}
        </Button>
      </Card.Body>
    </Card>
  </Col>

  {/* TV Kartı */}
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
        <h5 className="mb-4">TV</h5>
        <Button
          variant={deviceStates["tv"] ? "success" : theme === "dark" ? "outline-light" : "outline-secondary"}
          onClick={() => toggleDevice("tv")}
          style={{ width: "50px", height: "50px" }}
        >
          {deviceStates["tv"] ? <TvFill size={24} /> : <Tv size={24} />}
        </Button>
      </Card.Body>
    </Card>
  </Col>

  {/* Priz*/}
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
        <h5 className="mb-4">Priz</h5>
        <div className="d-flex justify-content-between">
          {["light1", "light2", "light3", "light4"].map((device, index) => (
            <Button
              key={index}
              variant={deviceStates[device] ? "success" : theme === "dark" ? "outline-light" : "outline-secondary"}
              onClick={() => toggleDevice(device)}
              style={{ width: "50px", height: "50px" }}
            >
              {deviceStates[device] ? (
                <LightbulbFill size={24} />
              ) : (
                <Lightbulb size={24} />
              )}
            </Button>
          ))}
        </div>
      </Card.Body>
    </Card>
  </Col>
</Row>
    </Container>
  );
}
