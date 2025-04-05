import { useEffect, useState } from "react";
import axios from "axios";

function FeatureImportance() {
  const [images, setImages] = useState({});

  useEffect(() => {
    axios
      .get("http://localhost:5000/analytics/feature-importance")
      .then((res) => setImages(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-3xl font-bold mb-4">Feature Importance</h2>
      <div className="flex justify-center">
        <div>
          {images.bar_chart && (
            <div>
              <img
                src={`http://localhost:5000${images.bar_chart}`}
                alt="Bar Chart"
              />
            </div>
          )}
        </div>
        <div>
          {images.heatmap && (
            <div className="mt-4">
              <img
                src={`http://localhost:5000${images.heatmap}`}
                alt="Heatmap"
              />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default FeatureImportance;
