# Module 2 Homework – Workflow-orchestration

This repository contains my solution for **Module 2: Workflow Orchestration** from the Data Engineering Zoomcamp.

---

## Question 1: File Size
Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/d59eafb2-df87-41e1-b098-2c4807f211cc" />


#### Ans : 128.3 MiB 
This answer was obtained using the following Kestra flow:

- [`00_file_size.yaml`](./flows/00_file_size.yaml)


## Question 2: Varible 
What is the rendered value of the variable file when the inputs taxi is set to `green`, year is set to `2020`, and month is set to `04` during execution?

#### Logic : 
` file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv" `
#### Ans : green_tripdata_2020-04.csv


## Question 3: Yellow Taxi data 2020 Row
How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/00d3af7f-094d-4169-991f-d16e250d3ff8" />

#### Ans : 24,648,499
This answer was obtained using the following Kestra flow:
- [`00_row_counter.yaml`](./flows/00_row_counter.yaml)


## Question 4: Green Taxi data 2020 Row
How many rows are there for the Green Taxi data for all CSV files in the year 2020?
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/7715f5cc-7998-4e91-a474-d63e87127def" />

#### Ans : 1,734,051
This answer was obtained using the following Kestra flow:
- [`00_row_counter.yaml`](./flows/00_row_counter.yaml)


## Question 5: Yellow Taxi data for the March 2021
How many rows are there for the Yellow Taxi data for the March 2021 CSV file?
SELECT count(*) FROM public.yellow_tripdata
where filename = 'yellow_tripdata_2021-03.csv'

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/3696f0ae-9374-4544-a80b-0a5c0f7e331f" />

#### Ans : 1,925,152
