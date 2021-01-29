# Medical-Data-Visualizer

The aim of this project is to visualize and make calculations from medical examination data using Matplotlib, NumPy, seaborn and pandas. 

This assignment was set as part of the Data Analysis with Python Projects course on [freeCodeCamp.org](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer). Please note, some variable names have been reformatted from the original file.

### Data description

File name: [medical_examination.csv](https://github.com/agolikova/Medical-Data-Visualizer/blob/main/medical_examination.csv)

Rows in the dataset represent patients and columns represent data including body measurements, results from various blood tests and lifestyle choices. The dataset is used to explore the relationship between cardiac disease, body measurements, blood markers and lifestyle choices.

|Variable|Type|Data type|
|-------|-------------|----------|
|Age|Objective feature|int (days)|
|Height|Objective feature|int (cm)|
|Weight|Objective feature|float (kg)|
|Gender|Objective feature|Categorical code (1/2)|
|Systolic blood pressure|Examination feature|int|
|Diastolic blood pressure|Examination feature|int|
|Cholesterol|Examination feature|1: normal, 2: above normal, 3: well above normal|
|Glucose|Examination feature|1: normal, 2: above normal, 3: well above normal|
|Smoking|Subjective feature|0: non-smoker, 1: smoker|
|Alcohol intake|Subjective feature|0: low, 1: high|
|Physical activity|Subjective feature|0: high, 1: low|
|Cardiovascular disease (CVD)|Target variable|0: absent, 1: present|

### Tasks

* Add an 'overweight' column to the data by calculating BMI. If that value is > 25 then use 1 for overweight, 0 for not overweight
* Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' = 1, make the value 0. If value > 1, make the value 1
* Create a categorical chart showing the counts of good and bad outcomes for cholesterol, gluc, alco, active and smoke for patients with cardio=1 and cardio=0 in different panels

* Clean the data by filtering out the following patient segments that represent incorrect data:
  * Diastolic pressure is higher than systolic
  * Height < 2.5th percentile or > 97.5th percentile
  * Weight < 2.5th percentile or > 97.5th percentile
  
* Create a correlation matrix using seaborn's heatmap() function, masking the upper triangle
