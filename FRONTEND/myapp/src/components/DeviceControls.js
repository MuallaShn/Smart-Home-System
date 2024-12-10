import React from "react";
import { Card, Button, Form } from "react-bootstrap";
import { Lightbulb, LightbulbFill, VolumeUp } from "react-bootstrap-icons";

export function DeviceControls({ isLightOn, setIsLightOn, brightness, setBrightness, volume, setVolume }) {


const toggleLight = () => {
  // Işığın yeni durumunu hesapla
  const newLightState = !isLightOn;

  // Işığın durumunu güncelle
  setIsLightOn(newLightState);

  // API endpointini seç ve POST isteğini yap
  const apiEndpoint = newLightState
    ? "http://127.0.0.1:5000/turn" // Işığı aç
    : "http://127.0.0.1:5000/turn_off"; // Işığı kapat

  fetch(apiEndpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ komut: newLightState ? "ışığı aç" : "ışığı kapat" }),
  })
    .then((response) => {
      if (response.ok) {
        console.log(
          "Backend'e ışık komutu gönderildi:",
          newLightState ? "Aç" : "Kapat"
        );
      } else {
        console.error("Hata oluştu:", response.status);
      }
    })
    .catch((error) => {
      console.error("Bağlantı hatası:", error.message);
    });
};





  return (
    <div className="row justify-content-center" style={{ columnGap: "8rem" }}>

      {/* Işık Kontrolü */}
      <div className="col-md-6 col-lg-4 d-flex justify-content-center">
        <Card className="shadow-sm w-100">
          <Card.Body style={{ height: "170px" }}>
            <div className="d-flex justify-content-between align-items-center mb-5">
              <h5 className="fw-bold">Işık Kontrolü</h5>
              <Button
                variant={isLightOn ? "success" : "outline-secondary"}
                //onClick={() => setIsLightOn(!isLightOn)}
                onClick={toggleLight}
              >
                {isLightOn ? <LightbulbFill /> : <Lightbulb />}
              </Button>
            </div>
            <div className="d-flex align-items-center gap-3">
              <Lightbulb size={20} />
              <Form.Range
                value={brightness}
                onChange={(e) => setBrightness(Number(e.target.value))}
                max={100}
              />
            </div>
          </Card.Body>
        </Card>
      </div>

      {/* Ses Kontrolü */}
      <div className="col-md-6 col-lg-4 d-flex justify-content-center">
        <Card className="shadow-sm w-100">
          <Card.Body style={{ height: "170px" }}>
            <div className="d-flex justify-content-between align-items-center mb-5">
              <h5 className="fw-bold">Ses Kontrolü</h5>
              <Button variant="outline-secondary">
                <VolumeUp />
              </Button>
            </div>
            <div className="d-flex align-items-center gap-3">
              <VolumeUp size={20} />
              <Form.Range
                value={volume}
                onChange={(e) => setVolume(Number(e.target.value))}
                max={100}
              />
            </div>
          </Card.Body>
        </Card>
      </div>
    </div>
  );
}
