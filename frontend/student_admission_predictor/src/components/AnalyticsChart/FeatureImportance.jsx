import { useEffect, useState } from "react";
import axios from "axios";
import { IoMdAnalytics } from "react-icons/io";
import { PiStudentFill } from "react-icons/pi";

function FeatureImportance() {
  const [images, setImages] = useState({});

  useEffect(() => {
    axios
      .get("http://localhost:5000/analytics/feature-importance")
      .then((res) => setImages(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <>
      <h2 className="text-3xl font-bold mb-4 text-green-600 flex items-center justify-center">
        Student Admission Predictor{" "}
        <PiStudentFill className="ml-2 mt-1 text-black" />
      </h2>
      {/* Feature Box Plots */}
      <section className="px-12 mt-24">
        {images.boxplots && (
          <div>
            <h3 className="text-3xl font-bold underline text-center mb-12 flex items-center">
              Feature vs Admission{" "}
              <IoMdAnalytics className="flex items-center ml-2 mt-2 text-4xl" />
            </h3>
            <div className="flex">
              {Object.entries(images.boxplots).map(([feature, path]) => (
                <div key={feature} className="">
                  <h4 className="text-lg font-medium mb-2 text-center">
                    {feature}
                  </h4>
                  <img
                    src={`http://localhost:5000${path}`}
                    alt={`${feature} Boxplot`}
                    className=""
                  />
                </div>
              ))}
            </div>
          </div>
        )}
      </section>
      {/* Feature Importance Bar Chart */}
      {/* <section>
        {images.bar_chart && (
          <div className="mb-6">
            <h3 className="text-xl font-semibold mb-2">Bar Chart</h3>
            <img
              src={`http://localhost:5000${images.bar_chart}`}
              alt="Bar Chart"
              className="mx-auto"
            />
          </div>
        )}
      </section> */}
    </>
  );
}

export default FeatureImportance;
