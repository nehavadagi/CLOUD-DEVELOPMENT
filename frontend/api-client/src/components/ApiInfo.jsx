// src/components/ApiInfo.js
export default function ApiInfo() {
  return (
    <div>
      <h2>API Design Justification</h2>
      <p>This API uses JWT for auth, SendGrid for notifications, and follows secure, modular FastAPI architecture.</p>
      <h3>Architecture Diagram</h3>
      <img src="/api-architecture.png" alt="Architecture Diagram" style={{ maxWidth: "100%" }} />
      <a href="/api_design.pdf" download>Download API Design PDF</a>
    </div>
  );
}
