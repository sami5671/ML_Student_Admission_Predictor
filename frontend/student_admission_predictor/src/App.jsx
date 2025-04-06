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
      gre: parseFloat(formData.get("gre")),
      toefl: parseFloat(formData.get("toefl")),
      cgpa: parseFloat(formData.get("cgpa")),
      research: parseInt(formData.get("research")),
    };

    console.log("Form Data:", data);
    try {
      const res = await axios.post("http://localhost:5001/api/predict", data);
      setResult(res.data);
      console.log(res.data);
    } catch {
      setResult("Error occurred");
    }
  };

  return (
    <>
      <header>
        <main>
          <div className="max-w-lg mx-auto my-12 p-6 bg-gray-100 rounded-lg shadow-md text-center">
            <h2 className="text-2xl font-semibold mb-6">Admission Predictor</h2>
            <form onSubmit={handleSubmit}>
              <input
                type="number"
                name="gre"
                placeholder="GRE Score"
                className="block w-full mb-4 p-2 border border-gray-300 rounded"
              />
              <input
                type="number"
                name="toefl"
                placeholder="TOEFL Score"
                className="block w-full mb-4 p-2 border border-gray-300 rounded"
              />
              <input
                type="number"
                step="0.01"
                name="cgpa"
                placeholder="CGPA"
                className="block w-full mb-4 p-2 border border-gray-300 rounded"
              />
              <select
                name="research"
                className="block w-full mb-4 p-2 border border-gray-300 rounded"
              >
                <option value="">Research Experience?</option>
                <option value="1">Yes</option>
                <option value="0">No</option>
              </select>
              <button
                type="submit"
                className="w-full py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                Predict
              </button>
            </form>

            {result && (
              <div className="mt-6">
                <h1>🧠 Admission Chance: {result.admission_chance}%</h1>
                <div>
                  {" "}
                  <h3>✅ Recommendations 🎯 </h3>
                  <p className="text-red-700 font-semibold">
                    {result.recommendations}
                  </p>
                </div>

                <img
                  src={`http://localhost:5000${result.suggestion_graph}`}
                  alt="Improvement Chart"
                />
              </div>
            )}
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
