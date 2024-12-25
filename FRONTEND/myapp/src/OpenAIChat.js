import React, { useState } from "react";
import { Button, Form, Container, Row, Col } from "react-bootstrap";

export function OpenAIChat() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const sendToOpenAI = async () => {
    if (!input.trim()) {
      setResponse("Please enter a question before submitting.");
      return;
    }

    try {
      const res = await fetch("http://127.0.0.1:5000/openai", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: input }),
      });

      const data = await res.json();
      if (data.response) {
        setResponse(data.response);
      } else if (data.error) {
        setResponse(`Error: ${data.error}`);
        console.error("API Error:", data.error);
      }
    } catch (error) {
      setResponse("An error occurred. Please try again.");
      console.error("Fetch Error:", error);
    }
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col xs={12} md={6}>
          <Form>
            <Form.Group className="mb-3">
              <Form.Label>Ask OpenAI:</Form.Label>
              <Form.Control
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask a question (e.g., What is the capital of Turkey?)"
              />
            </Form.Group>
            <Button variant="primary" onClick={sendToOpenAI}>
              Send to OpenAI
            </Button>
          </Form>
          {response && (
            <div className="mt-4">
              <h5>Response:</h5>
              <pre style={{ backgroundColor: "#f8f9fa", padding: "10px", borderRadius: "5px" }}>
                {response}
              </pre>
            </div>
          )}
        </Col>
      </Row>
    </Container>
  );
}


