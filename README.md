## End to end machine learning project
**Student Performance Prediction - README**

*Introduction About the Data:*

This project aims to predict students' academic performance based on various features related to their background and educational environment. The dataset includes information such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and scores in math, reading, and writing

**Dataset Overview:**

The dataset consists of the following features:

1. gender: Gender of the student (e.g., Male, Female).
2. race_ethnicity: Race or ethnicity group the student belongs to.
3. parental_level_of_education: Educational level of the student's parents.
4. lunch: Type of lunch the student receives (e.g., Standard, Free/Reduced).
5. test_preparation_course: Whether the student completed a test preparation course (Yes/No).
6. math_score: Score obtained in the math exam.
7. reading_score: Score obtained in the reading exam.
8. writing_score: Score obtained in the writing exam


*RENDER Deployment Link:*
[Link to RENDER Deployment](https://model-deployment1-6fod.onrender.com)

*Screenshots :*

- **Homepage UI:** [Screenshot](provide_link_here)





**Project Approach:**

1. **Data Ingestion:**
   - The dataset is read as a CSV file.
   - Data is split into training and testing sets and saved as CSV files.

2. **Data Transformation:**
   - ColumnTransformer Pipeline is created.
   - For numeric variables, SimpleImputer is applied with the strategy median, followed by 
     Standard Scaling.
   - For categorical variables, SimpleImputer with the most frequent strategy is applied, 
      followed by ordinal encoding and scaling with Standard Scaler.
   - The preprocessor is saved as a pickle file.

3. **Model Training:**
   - A base model is tested, and the best model identified is the Linear Regressor.
   - Hyperparameter tuning is performed on different models.
   - The model is saved as a pickle file.

4. **Prediction Pipeline:**
   - The pipeline converts given data into a DataFrame.
   - Various functions load pickle files and predict the final results in Python.

5. **Flask App Creation:**
   - A Flask app is created with a user interface to predict student performance within a web 
     application.

*Exploratory Data Analysis Notebook:*
[EDA Notebook](https://github.com/Vaibhavreddyv/mlprojects/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb)

*Model Training Approach Notebook:*
[Model Training Notebook](https://github.com/Vaibhavreddyv/mlprojects/blob/main/notebook/2.%20MODEL%20TRAINING.ipynb)

