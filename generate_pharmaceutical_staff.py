import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define positions in the pharmaceutical company
positions = [
    "Pharmacist", "Lab Technician", "Research Scientist", 
    "Quality Control Specialist", "Regulatory Affairs Specialist", 
    "Clinical Trial Manager", "Medical Sales Representative", 
    "Pharmacy Technician", "Biostatistician", "Pharmaceutical Engineer"
]

# Generate 400 staff records
num_records = 400
data = []
for _ in range(num_records):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(22, 65)
    position = random.choice(positions)
    location = fake.city()
    data.append([first_name, last_name, age, position, location])

# Create DataFrame
columns = ["First Name", "Last Name", "Age", "Position", "Location"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
file_path = "pharmaceutical_staff.csv"
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
