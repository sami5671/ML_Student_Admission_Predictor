import axios from "axios";
import "./App.css";
import { useState } from "react";
import FeatureImportance from "./components/AnalyticsChart/FeatureImportance";

function App() {
  const [result, setResult] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResult("");

    const form = e.target;
    const formData = new FormData(form);

    const gre = parseFloat(formData.get("gre"));
    const toefl = parseFloat(formData.get("toefl"));
    const cgpa = parseFloat(formData.get("cgpa"));
    const research = parseInt(formData.get("research"));

    // Input validation
    if (gre < 260 || gre > 340) {
      return setError("GRE score must be between 260 and 340.");
    }
    if (toefl < 0 || toefl > 120) {
      return setError("TOEFL score must be between 0 and 120.");
    }
    if (cgpa < 0 || cgpa > 4.0) {
      return setError("CGPA must be between 0.0 and 4.0.");
    }
    if (![0, 1].includes(research)) {
      return setError("Please select a valid research experience.");
    }

    const data = { gre, toefl, cgpa, research };

    try {
      const res = await axios.post("http://localhost:5001/api/predict", data);
      setResult(res.data);
      console.log(res.data);
    } catch {
      setError("An error occurred while predicting. Try again.");
    }
  };

  return (
    <>
      <header>
        <main className="p-12">
          {/* analytics graph  */}
          <div>
            <FeatureImportance />
          </div>
          <div className="my-12 p-6 bg-gray-100 rounded-lg shadow-md text-center flex justify-between gap-6">
            <div className="w-1/3">
              <h2 className="text-2xl font-semibold mb-6">
                Enter Your Data to Predict
              </h2>
              {error && (
                <p className="mb-4 text-red-600 font-semibold">{error}</p>
              )}
              <form onSubmit={handleSubmit}>
                <input
                  type="number"
                  name="gre"
                  placeholder="GRE Score (260-340)"
                  min="260"
                  max="340"
                  required
                  className="block w-full mb-4 p-2 border border-gray-300 rounded"
                />
                <input
                  type="number"
                  name="toefl"
                  placeholder="TOEFL Score (0-120)"
                  min="0"
                  max="120"
                  required
                  className="block w-full mb-4 p-2 border border-gray-300 rounded"
                />
                <input
                  type="number"
                  step="0.01"
                  name="cgpa"
                  placeholder="CGPA (0.0-4.0)"
                  min="0"
                  max="4"
                  required
                  className="block w-full mb-4 p-2 border border-gray-300 rounded"
                />
                <select
                  name="research"
                  required
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
            </div>

            <div className="w-1/2">
              {result && (
                <div className="mt-6">
                  <h1>🧠 Admission Chance: {result.admission_chance}%</h1>
                  <div>
                    <h3>✅ Recommendations 🎯 </h3>
                    <p className="text-red-700 font-semibold">
                      {result.recommendations}
                    </p>
                  </div>

                  <img
                    src={`http://localhost:5000${result.improvement_graph}`}
                    alt="Improvement Chart"
                  />
                </div>
              )}
            </div>
          </div>
        </main>
      </header>
    </>
  );
}

export default App;
