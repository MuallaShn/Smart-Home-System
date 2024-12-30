import { useState } from "react";
import { Button, Container, Row, Col, Card } from "react-bootstrap";
import { Tv, TvFill, Lightbulb, LightbulbFill } from "react-bootstrap-icons";

// theme parametresi ile sayfanın açık veya koyu temaya uyarlanması sağlanır
export function SceneViewer({ theme }) {
  // Verilen stateler sayesinde cihazların durumları kontrol edilir ve güncellenir
  const [deviceStates, setDeviceStates] = useState({
    tv: false,
    pc: true,
    light: false,
  });

  // Bu fonksiyon sayesinde cihazların durumları değiştirilir
  const toggleDevice = async (device) => {
    // Yeni durumu, cihazın durumunun tersini hesaplayarak ayarlarız
    const newState = !deviceStates[device];
    setDeviceStates((prevStates) => ({
      ...prevStates, // Diğer cihazlarun mevcut durumu korundu
      [device]: newState,
    }));

    //Backend'e hangi işlemin yapılacağını belirtmek için kullanılır.
    const state = newState ? "turn_on" : "turn_off";

    // Backende fetch api ile post isteği gönderiyoruz
    try {
      const response = await fetch(`http://127.0.0.1:5000/${device}/${state}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Json formatında veri gönderileceği belirlendi
        },
      });
      //Gelen yanıtın başarılı olup olmadığı kontrolü yapılır başarısızsa hata atılır
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json(); // Gelen yanıt JSON formatında okunur ve "data" değişkenine atanır.
      console.log(data); // Backend'den gelen veri konsola yazdırılır.
    } catch (error) {
      console.error("Fetch error:", error); // Herhangi bir hata oluşursa konsola yazdırılır
    }
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-center mt-4">
  {/* Bilgisayar Kartı */}
  <Col xs={12} md={4} className="mb-4">
    <Card
      className="shadow-sm text-center"
      style={{
        width: "380px",
        height: "250px",
        padding: "20px",
        backgroundColor: theme === "dark" ? "#1E1E1E" : "white", // Tema koyuysa arka plan rengini "#1E1E1E" olarak ayarlar, aksi halde "white" yapar.
        color: theme === "dark" ? "white" : "black", // Tema koyuysa metin rengini "white" olarak ayarlar, aksi halde "black" yapar.
      }}
    >
      <Card.Body>
        <h5 className="mb-4">Bilgisayar</h5>
        <Button // Butona tıklandığında duruma göre renk değişikliği olur aynı zamanda sayfanın tema değişikliğine göre de değişiklik olur
          variant={
            deviceStates["pc"]
              ? "success"
              : theme === "dark"
              ? "outline-light"
              : "outline-secondary"
          }
          // Eğer bilgisayar true ise, TvFill gösterilir. Kapalı durumdaysa, Tv gösterilir.
          onClick={() => toggleDevice("pc")}
          style={{ width: "55px", height: "55px" }}
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
        width: "380px",
        height: "250px",
        padding: "20px",
        backgroundColor: theme === "dark" ? "#1E1E1E" : "white",
        color: theme === "dark" ? "white" : "black",
      }}
    >
      <Card.Body>
        <h5 className="mb-4">TV</h5>




          {/* TV Aç/Kapat Butonu */}
          <Button
            variant={
              deviceStates["tv"]// Butona tıklandığında duruma göre renk değişikliği olur aynı zamanda sayfanın tema değişikliğine göre de değişiklik olur
                ? "success"
                : theme === "dark"
                ? "outline-light"
                : "outline-secondary"
            }
            onClick={() => toggleDevice("tv")}
            style={{ width: "55px", height: "55px" }}
          >
            {deviceStates["tv"] ? <TvFill size={24} /> : <Tv size={24} />}
          </Button>

      </Card.Body>
    </Card>
  </Col>

  {/* Priz Kartı */}
  <Col xs={12} md={4} className="mb-4">
    <Card
      className="shadow-sm text-center"
      style={{
        width: "380px",
        height: "250px",
        padding: "20px",
        backgroundColor: theme === "dark" ? "#1E1E1E" : "white",
        color: theme === "dark" ? "white" : "black",
      }}
    >
      <Card.Body>
        <h5 className="mb-4">Priz</h5>
        <div className="d-flex justify-content-between">
          {["light1", "light2", "light3", "light4"].map((device, index) => (
            // "map" fonksiyonu ile liste oluşturulur. Her bir cihaz için buton oluşturulur ve device değişkeni ile cihazların adı temsil edilir
            <Button
              key={index}
              variant={
                deviceStates[device]
                  ? "success"
                  : theme === "dark"
                  ? "outline-light"
                  : "outline-secondary"
              }
              onClick={() => toggleDevice(device)}
              style={{ width: "55px", height: "55px" }}
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
