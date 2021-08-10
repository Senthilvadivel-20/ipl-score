from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')

# initial render
def home(request):
    return render(request,'home.html')


# Result generater
def result(request):

    df=pd.read_csv('./Files/ipl_target.csv')

    lm=joblib.load('./Files/predicted_score.sav')

    
    venue_encoder=LabelEncoder()
    batting_team_encoder=LabelEncoder()
    bowling_team_encoder=LabelEncoder()

    df['venue']=venue_encoder.fit_transform(df['venue'])
    df['batting_team']=batting_team_encoder.fit_transform(df['batting_team'])
    df['bowling_team']=bowling_team_encoder.fit_transform(df['bowling_team'])


    bowled=str(request.GET['over'])+'.'+str(request.GET['balls'])

    venue=venue_encoder.transform([request.GET['venue']])[0]
    innings=int(request.GET['innings'])
    batting_team=batting_team_encoder.transform([request.GET['batting_team']])[0]
    bowling_team=bowling_team_encoder.transform([request.GET['bowling_team']])[0]
    ball=float(bowled)
    run=int(request.GET['run'])
    wicket=int(request.GET['wicket'])

    predictor=[[venue,innings,batting_team,bowling_team,ball,run,wicket]]

    bat=request.GET['batting_team']
    bowl=request.GET['bowling_team']

    
    target=lm.predict(predictor)[0]
    target=round(target)


    return render(request,'result.html',locals())

  