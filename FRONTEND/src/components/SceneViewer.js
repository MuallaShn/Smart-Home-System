import { useState } from "react";
import { Button, Container, Row, Col } from "react-bootstrap"; // Bootstrap bileşenleri
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment } from "@react-three/drei";

// Scene bileşenindeki props'u JavaScript'e uyumlu hale getiriyoruz
function Scene({ isLightOn, brightness }) {
  const lightIntensity = (brightness / 100) * (isLightOn ? 1 : 0);

  return (
    <>
      <ambientLight intensity={0.1} />
      <spotLight
        position={[0, 5, 0]}
        intensity={lightIntensity}
        angle={0.5}
        penumbra={0.5}
        color="#ffffff"
      />
      <mesh position={[0, 0, 0]}>
        <cylinderGeometry args={[1, 1, 2, 32]} />
        <meshStandardMaterial color="#333333" metalness={0.8} roughness={0.2} />
      </mesh>
      <mesh position={[0, 0.9, 0]}>
        <torusGeometry args={[1.1, 0.05, 16, 100]} />
        <meshStandardMaterial
          color={isLightOn ? "#00ff00" : "#333333"}
          emissive={isLightOn ? "#00ff00" : "#000000"}
          emissiveIntensity={lightIntensity * 2}
        />
      </mesh>
      <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -1, 0]}>
        <planeGeometry args={[10, 10]} />
        <meshStandardMaterial color="#f0f0f0" />
      </mesh>
    </>
  );
}

export function SceneViewer({ isLightOn, brightness }) {
  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col md={8}>
          <div className="border rounded-3 shadow-sm overflow-hidden">
            <Canvas camera={{ position: [4, 4, 4], fov: 50 }}  style={{ width: "100%", height: "400px" }}>
              <Scene isLightOn={isLightOn} brightness={brightness} />
              <OrbitControls enableZoom={false} />
              <Environment preset="city" />
            </Canvas>
          </div>
        </Col>
      </Row>
    </Container>
  );
}
