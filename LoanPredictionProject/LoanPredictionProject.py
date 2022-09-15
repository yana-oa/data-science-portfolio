from random import Random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split

# Load Training/Test Dataset

train = pd.read_csv(r"C:\Users\arian\LoanProject\train.csv")
test = pd.read_csv(r"C:\Users\arian\LoanProject\test.csv")
ss = pd.read_csv(r"C:\Users\arian\LoanProject\sample_submission_49d68Cx.csv")

#Data Overview
train.shape
test.shape
train.head()
test.head()

#Data Preprocessing
data = pd.concat([train,test])
data.drop("Loan_ID",axis=1,inplace=True) #dropping Loan ID column
data.isnull().sum() #number of missing values

#Filling Columns with null values using mode

for i in [data]:
    i["Gender"] = i["Gender"].fillna(data.Gender.dropna().mode()[0])
    i["Married"] = i["Married"].fillna(data.Married.dropna().mode()[0])
    i["Dependents"] = i["Dependents"].fillna(data.Dependents.dropna().mode()[0])
    i["Self_Employed"] = i["Self_Employed"].fillna(data.Self_Employed.dropna().mode()[0])
    i["Credit_History"] = i["Credit_History"].fillna(data.Credit_History.dropna().mode()[0])

from sklearn.ensemble import RandomForestRegressor
data1 = data.loc[:, ['LoanAmount','Loan_Amount_Term']] #start filling values for loan amount and term

#Running Imputer
imp = IterativeImputer(RandomForestRegressor(), max_iter = 10, random_state = 0)
data1 = pd.DataFrame(imp.fit_transform(data1), columns=data1.columns)

#Mapping variables to ints

for i in [data]:
    i["Gender"] = i["Gender"].map({"Male":0,"Female":1}).astype(int)
    i["Married"] = i["Married"].map({"No":0,"Yes":1}).astype(int)
    i["Education"] = i["Education"].map({"Not Graduate":0,"Graduate":1}).astype(int)
    i["Self_Employed"] = i["Self_Employed"].map({"No":0,"Yes":1}).astype(int)
    i["Credit_History"] = i["Credit_History"].astype(int)
    

for i in [data]:
    i["Property_Area"] = i["Property_Area"].map({"Urban":0,"Rural":1,"Semiurban":2}).astype(int)
    i["Dependents"] = i["Dependents"].map({"0":0,"1":1,"2":2,"3+":3}).astype(int)

###---EDA---###

#Splitting data to perform EDA
new_train = data.iloc[:614]
new_test = data.iloc[614:]

#Mapping
new_train["Loan_Status"] = new_train["Loan_Status"].map({"N":0,"Y":1}).astype(int)

#Univariate Analysis
#fig,ax to unpack tuple
fig,ax = plt.subplots(2,4,figsize=(16,10))
sns.countplot("Loan_Status",data=new_train, ax=ax[0][0])
sns.countplot("Gender",data=new_train, ax=ax[0][1])
sns.countplot("Married",data=new_train, ax=ax[0][2])
sns.countplot("Education",data=new_train, ax=ax[0][3])
sns.countplot("Self_Employed",data=new_train, ax=ax[1][0])
sns.countplot("Property_Area",data=new_train, ax=ax[1][1])
sns.countplot("Dependents",data=new_train, ax=ax[1][2])
sns.countplot("Credit_History",data=new_train, ax=ax[1][3])
plt.show()

#Observations
#More Loans are approved than rejected
#More males are applicants
#More applicants are married
#More applicants are graduates
#Most applicants are not self-employed
#Applicants live mostly in SemiUrban areas
#Most applicants have no children in their households
#Credit history is present for many applicants