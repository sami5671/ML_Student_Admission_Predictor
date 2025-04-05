import axios from "axios";
import "./App.css";
import { useState } from "react";
import FeatureImportance from "./components/AnalyticsChart/FeatureImportance";

function App() {
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const data = {
      gre: formData.get("gre"),
      toefl: formData.get("toefl"),
      cgpa: formData.get("cgpa"),
      research: formData.get("research"),
    };

    console.log("Form Data:", data);
    try {
      const res = await axios.post("http://localhost:5001/api/predict", data);
      setResult(res.data.admission ? "🎉 Admitted!" : "❌ Not Admitted");
    } catch {
      setResult("Error occurred");
    }
  };

  return (
    <>
      <header>
        <main>
          <div
            style={{
              maxWidth: "400px",
              margin: "50px auto",
              textAlign: "center",
            }}
          >
            <h2>Admission Predictor</h2>
            <form onSubmit={handleSubmit}>
              <input
                type="number"
                name="gre"
                placeholder="GRE Score"
                style={{
                  display: "block",
                  width: "100%",
                  marginBottom: "10px",
                }}
              />
              <input
                type="number"
                name="toefl"
                placeholder="TOEFL Score"
                style={{
                  display: "block",
                  width: "100%",
                  marginBottom: "10px",
                }}
              />
              <input
                type="number"
                step="0.01"
                name="cgpa"
                placeholder="CGPA"
                style={{
                  display: "block",
                  width: "100%",
                  marginBottom: "10px",
                }}
              />
              <select
                name="research"
                style={{
                  display: "block",
                  width: "100%",
                  marginBottom: "10px",
                }}
              >
                <option value="">Research Experience?</option>
                <option value="1">Yes</option>
                <option value="0">No</option>
              </select>
              <button type="submit">Submit</button>
            </form>

            {result && <p style={{ marginTop: "20px" }}>{result}</p>}
          </div>

          {/* analytics graph  */}
          <div>
            <FeatureImportance />
          </div>
        </main>
      </header>
    </>
  );
}

export default App;
