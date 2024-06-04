This is a file that will outline the proces it took to create the database of Entrance Pharmacy and populate it with data. Using POSTGRESQL


#Create a database
CREATE DATABASE entaph;

#Connect to the database
\c entaph;

#Creating the tables present in the DB 
 Theses are commands used to create a new table in a database. since there are 4  

(cutomers) 
CREATE TABLE customers (
    cus_id SERIAL PRIMARY KEY,
    cus_fullname VARCHAR(255) NOT NULL,
    cus_healthissue VARCHAR(255) NOT NULL,
    cus_appointmentday VARCHAR(255) NOT NULL
);

(employees)
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(255) NOT NULL,
    emp_position VARCHAR(255) NOT NULL,
    emp_age INT NOT NULL
);

(pharmaceutical_staff)
CREATE TABLE employees (
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    position VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

(shareholders)
CREATE TABLE shareholders (
    sha_id SERIAL PRIMARY KEY,
    sha_gender VARCAHR (6),
    sha_marital_status VARCAHRCHAR(4) ,
    sha_age INT NOT NULL
);

(pharmacylocation)
CREATE TABLE pharmacylocation (
    trading_name VARCHAR(255) NOT NULL,
    owner_name VARCHAR(255) NOT NULL,
    current_address TEXT NOT NULL,
    gphc_registration_number BIGINT NOT NULL,
    status VARCHAR(255) NOT NULL
);



#Inserting data into the various tables

(cutomers) 
INSERT INTO customers cus_fullname, cus_healthissue, cus_appointmentday) VALUES
(1, 'John Doe', 'Asthma', 'Monday'),
(2, 'Jane Smith', 'Diabetes', 'Tuesday');



(employees)
INSERT INTO employees (emp_name, emp_position, emp_age) VALUES
(1, Dr. Alice Green', 'Medical Director', 45),
(2, 'Nurse Sarah Lee', 'Head Nurse', 38);



(Shareholders)
INSERT INTO shareholders (sha_id, sha_gender, sha_marital_status, sha_age) VALUES
(458989, 'Female', 'Yes', 36),
(458994, 'Male', 'Yes', 37),
(458996, 'Female', 'Yes', 69);

#This is a command used to import data from a CSV file in to a particular
table which in this case is shareholders.

--\copy shareholders (sha_id, sha_gender, sha_marital_status, sha_age)
FROM '/path/to/your/shareholders.csv'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');--



(pharmacylocation)
INSERT INTO pharmacylocation (trading_name, owner_name, current_address, gphc_registration_number, status) VALUES
('118 Pharmacy', '118 Pharmacy Ltd', '9 High Street, Walsall Wood, WALSALL, WS9 9LR, UK', 1112046, 'Registered'),
('3Q Pharmacy', 'KRG Healthcare Limited', '3 Queen Street, WELLINGBOROUGH, Northamptonshire, NN8 4RW, UK', 1105385, 'Registered');

#This is a command used to import data from a CSV file in to a particular
table which in this case is pharmacylocation.

--\copy pharmacylocation (trading_name, owner_name, current_address, gphc_registration_number, status)
FROM '/path/to/your/pharmacylocation.csv'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');--



(pharmaceutical_staff)
INSERT INTO pharmaceutical_staff(first_name, last_name, age, position, location) VALUES
('Donna', 'Mcdonald', 54, 'Medical Sales Representative', 'Lauremouth'),
('Brianna', 'Williams', 46, 'Biostatistician', 'New Rebekahhaven'),
('Jennifer', 'Malone', 55, 'Medical Sales Representative', 'Leemouth');

This particular data was generate with the python commands below,

import pandas as pd
import random
import faker

# Initialize Faker
fake = faker.Faker()

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
 

# This is a command used to import data from a CSV file in to a particular
table which in this case is pharmaceutical_staff.

--\copy pharmaceutical_staff (first_name, last_name, age, position, location)
FROM '/path/to/your/pharmaceuticalstaff.csv'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');--
