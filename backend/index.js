const express = require("express");
const app = express();
require("dotenv").config();
const cors = require("cors");
const port = process.env.PORT || 5001;
const axios = require("axios");

// ------------------- middleware ----------------------------------------------------------------
const corsOptions = {
  // origin: ["https://dream-car-68b89.web.app"],
  origin: ["http://localhost:5173", "http://localhost:5174"],
  credentials: true,
  optionSuccessStatus: 200,
};

app.use(cors(corsOptions));
app.use(express.json());
app.use(express.urlencoded());

// ---------------------------------------------------------------------------------------------
app.post("/api/predict", async (req, res) => {
  console.log(req.body);
  try {
    const response = await axios.post(
      "http://localhost:5000/predict",
      req.body
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "Prediction failed" });
  }
});

app.get("/", (req, res) => {
  res.send("Student Admission Server is Alive.............");
});

app.listen(port, () => {
  console.log(`Student Admission Server is running on port ${port}`);
});
