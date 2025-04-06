import pandas as pd

# Dataset for 10 students
data = {
    "GRE Score": [330, 310, 320, 300, 315, 290, 305, 310, 325, 335],
    "TOEFL Score": [115, 105, 110, 100, 108, 95, 104, 106, 111, 113],
    "CGPA": [3.8, 3.2, 3.5, 3.0, 3.7, 2.8, 3.1, 3.4, 3.6, 3.9],
    "Research": [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    "Admitted": [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)
print("✅ student_dataset_10.csv created successfully.")


# Explanation:
# GRE Score: Random scores between 290 and 335.

# TOEFL Score: Random scores between 95 and 115.

# CGPA: Between 2.8 and 3.9, realistic academic performance values.

# Research: Binary values indicating whether the student has research experience (1 for yes, 0 for no).

# Admitted: Binary values representing whether the student was admitted (1 for admitted, 0 for not admitted).
