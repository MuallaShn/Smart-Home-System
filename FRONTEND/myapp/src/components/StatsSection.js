import React, { useState } from "react";
import { Button, Container, Row, Col } from "react-bootstrap"; // Bootstrap bileşenleri
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment } from "@react-three/drei";
import { LightbulbIcon as LightBulbIcon, LightbulbOffIcon } from "lucide-react";

function Scene({ isLightOn }) {
  return (
    <>
      {/* Ortam ışığı */}
      <ambientLight intensity={0.1} />
      
      {/* Spot ışık - dinamik kontrol */}
      <spotLight
        position={[0, 5, 0]}
        intensity={isLightOn ? 1 : 0}
        angle={0.5}
        penumbra={0.5}
        color="#ffffff"
      />

      {/* Alexa benzeri cihaz modeli */}
      <mesh position={[0, 0, 0]}>
        <cylinderGeometry args={[2, 2, 4, 32]} /> {/* Boyutları artırdık */}
        <meshStandardMaterial
          color="#333333"
          metalness={0.8}
          roughness={0.2}
        />
      </mesh>

      {/* Işık halkası */}
      <mesh position={[0, 1.5, 0]}> {/* Yüksekliği artırdık */}
        <torusGeometry args={[2, 0.1, 16, 100]} /> {/* Boyutları artırdık */}
        <meshStandardMaterial
          color={isLightOn ? "#00ff00" : "#333333"}
          emissive={isLightOn ? "#00ff00" : "#000000"}
          emissiveIntensity={isLightOn ? 2 : 0}
        />
      </mesh>

      {/* Zemin */}
      <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -2, 0]}> {/* Zemin boyutunu büyüttük */}
        <planeGeometry args={[20, 20]} /> {/* Boyutları artırdık */}
        <meshStandardMaterial color="#f0f0f0" />
      </mesh>
    </>
  );
}

export default function SmartHome() {
  const [isLightOn, setIsLightOn] = useState(false);

  return (
    <div className="bg-gradient-to-b from-gray-900 to-gray-800">
      <Container fluid className="h-screen p-0">
        {/* Canvas ile 3D sahne */}
        <Canvas camera={{ position: [6, 6, 6], fov: 50 }} className="h-full"> {/* Kamera konumunu büyüttük */}
          <Scene isLightOn={isLightOn} />
          <OrbitControls enableZoom={false} />
          <Environment preset="city" />
        </Canvas>

        {/* Kontrol butonları */}
        <Row className="position-absolute bottom-0 w-100 justify-content-center mb-4">
          <Col xs="auto">
            <Button
              onClick={() => setIsLightOn(true)}
              disabled={isLightOn}
              className="d-flex align-items-center gap-2"
            >
              <LightBulbIcon className="w-4 h-4" />
              Işığı Aç
            </Button>
          </Col>
          <Col xs="auto">
            <Button
              onClick={() => setIsLightOn(false)}
              disabled={!isLightOn}
              variant="outline"
              className="d-flex align-items-center gap-2"
            >
              <LightbulbOffIcon className="w-4 h-4" />
              Işığı Kapat
            </Button>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
