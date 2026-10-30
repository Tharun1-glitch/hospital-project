# HOSPITAL-PROJECT
Machine Learning project to predict patient readmissions

OBJECTIVE:

The goal of this project is to train three classifiers [Linear Regression, Decision Tree, K-Near Neighbors] to find out the patients dataset whether they are readmitted in last 30 days.(by returning 1 for yes or 0 for No)

Comparison Table:

         Model           |  Accuracy  |   Precision  |  Recall  | F1 Score  |
Logistic Regression (LR)      89.6%         84.8%        79.6%      82.1%
Decision Tree ((DT)           79.8%         65.7%        67.9%      66.8%
K-Nearest Neighbors (KNN)     77.3%         66.5%        49.0%      56.4%

Questions & Answers :

• Q1. What is the class distribution of the target? Is the dataset balanced or imbalanced, and why does that matter?
A. Yes, The dataset is imbalanced. because the patients who are not readmitted were more compared to those who were admitted this gives confusion to the model because the model predicts the value by depending on majority class.

• Q2. What preprocessing steps did you perform? For each step, explain why it was necessary and whether it was fitted using training data only.
A.   -Manually dropped 'Patient ID' column because the id will have a unique number and the model cannot learn medical patterns and throws error.
     -Used 'pd.get_dummies' to turn text columns into 1 and 0
   
• Q3. Why does Logistic Regression generally require scaled numeric features less critically than KNN, while KNN is strongly affected by feature scale?
A. KNN classifier relies on distance between the features. If one of the feature have higher value and one feature has lower value, this causes the model to use high calculations. Whereas Logistic Regression uses coefficients where they actually balance themselves while training.

• Q4. What value of k did you use for KNN? Show how you selected it. Discuss what happens when k is too small versus too large?
A. I used k=5. If I put k=1(least) causes overfitting because the model will evaluate each value. If k=100(highest) causes underfitting because the classifier just randomly guess. 

• Q6. Compare all three models using Accuracy, Precision, Recall, F1-score, and ROC-AUC. Which model is best for this problem, and what evidence supports your choice?
A. The model that performed well is Logistic Regression. It has given the best accuracy and balanced values.

• Q7. Which metric should receive the most attention in a healthcare readmission setting? There is no automatic correct answer - justify your choice based on the consequences of false positives and false negatives.
A. 'RECALL' is the most important metric as if it gives False Negative(FN) the risk of patient health increases.

• Q8. Does any model appear to be overfitting? Use the training-versus-test results to support your answer?
A. Decision Tree because it is more capable of drawing accurate scores but dropped to 79.8 accuracy.

• Q9. Does any model appear to be underfitting? Again, use evidence from both training and test performance?
A. KNN is the underfitting model as it has the lowest score recorded and causing low predictions.

• Q12. Is the model with the highest accuracy necessarily the best model? Use your results to prove or disprove this statement?
A. No, Recall is also important because it tells the patient will be getting risk or not. Since LR gave results of high accuracy and high recall value we picked it. If the other model gives higher recall value we would have picked that one only.

• Q14. What are the limitations of your best model? Identify at least three limitations or risks before claiming it is suitable for real-world hospital deployment?
A. My best model is Logistic Regression 
Limitations :
=> The model tracks only yes or no for the readmission but cannot tell whether they readmitted from any day between 30 days.


Submission Checklist :

 Dataset loaded and inspected [Y] 
 Target identified and encoded correctly [Y] 
 Missing values / categorical variables handled and explained [Y] 
 Data leakage checked[ Y ] Train/test split created correctly [Y] 
 Logistic Regression trained [Y] 
 KNN trained [Y] 
 Decision Tree trained [Y]
 Accuracy, Precision, Recall, F1, ROC-AUC reported [Y] 
 Confusion matrix created for all three models [Y] 
 ROC curves compared Train vs test performance compared Done? []
 Overfitting/underfitting discussed with evidence Ways to fix overfitting/underfitting proposed [Y] 
 Best model selected and justified [Y]











