#Create joblib file for predict score

import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.ensemble import RandomForestRegressor
import joblib




#csv file 
df=pd.read_csv('./Files/ipl_target.csv')

#Encode categorical variable to numeric
venue_encoder=LabelEncoder()    #from sklearn.preprocessing import LabelEncoder
batting_team_encoder=LabelEncoder()
bowling_team_encoder=LabelEncoder()


#Value transform 
df['venue']=venue_encoder.fit_transform(df['venue'])   
df['batting_team']=batting_team_encoder.fit_transform(df['batting_team'])
df['bowling_team']=bowling_team_encoder.fit_transform(df['bowling_team'])


#define x and y variable
x=df[['venue','innings','batting_team','bowling_team','ball','cum_sum','cum_wicket']] #predictor variable
y=df['target']  #target variable

#train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

# #create linear model
# lm=RandomForestRegressor(random_state=42)

# #fit the model
# lm.fit(x_train,y_train)

#create model 

lm = LinearRegression()
lm.fit(x_train,y_train)

#dumb the file in .sav file or use pickle
filename='./Files/predicted_score.sav'
joblib.dump(lm,filename)



