NYC Taxi task
Big Data Analytics Assignment
### Topic: Analysis of NYC Taxi Trip Dataset

Dataset
Use the NYC Yellow Taxi Trip Records dataset from NYC TLC Open Data.
You may use Spark, Hive, SQL, or Python (Pandas / PySpark).

🔹 Task 1 — Data Understanding & Cleaning (10 points)
Load the dataset.

Answer:

How many rows and columns are in the dataset?

Which columns contain missing or invalid values?

Perform basic cleaning:

Remove invalid distances and fares

Handle missing tip values

Describe the cleaning steps you applied.

🔹 Task 2 — Descriptive Statistics (10 points)
Compute:

Average trip distance

Average fare amount

Average trip duration (in minutes)

Briefly describe what a “typical” taxi trip looks like based on these statistics.

🔹 Task 3 — Time-Based Demand Analysis (15 points)
Calculate the number of trips for each hour of the day.

Identify:

The hour with minimum demand

The hour with maximum demand

Plot a graph (if possible) and interpret the result.

🔹 Task 4 — Revenue Analysis (15 points)
Compute the total revenue from all trips.

Compute the average revenue per trip.

Find the top 5 pickup locations by total revenue.

Explain why these locations may generate higher revenue.

🔹 Task 5 — Tip Analysis (15 points)
Analyze tipping behavior:

Average tip amount

Percentage of trips with zero tip

Analyze the relationship between fare amount and tip amount

What conclusions can you make about passenger tipping behavior?

🔹 Task 6 — Distance vs Fare Relationship (15 points)
Analyze the correlation between trip distance and fare amount.

Build a simple linear model:

f
a
r
e
=
a
+
b
×
d
i
s
t
a
n
c
e
fare=a+b×distance
Interpret the result.

🔹 Task 7 — Business Insights (20 points)
Based on your analysis, provide at least 3 business insights that could help:

Taxi company management

Drivers

City transport planners

🧪 Bonus Task (Optional, +10 points)
Predict whether a trip will receive a tip (tip > 0) using:

Trip distance

Fare amount

Trip duration

Pickup time

Describe the model and report accuracy.