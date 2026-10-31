from scripts.analysis_common import *
from scripts.fetch_data import ensure_data

PROJECT = 'Telecom_Churn_prediction'

def run(mode='full'):
    data=ensure_data(ROOT/'dataset')
    if PROJECT=='Heart_disease_prediction':
        df=pd.read_csv(data/'heart_v2.csv')
        return tabular_classifier(df,'heart disease',['age','sex','BP','cholestrol'],
            'Research classification of the supplied binary heart-disease label, with minority-class recall and precision reported alongside accuracy.',categorical=['sex'])
    if PROJECT=='Lead_score':
        df=pd.read_csv(data/'Leads.csv')
        # Exclude manual sales labels, IDs, Lead Quality, Tags and post-outcome activity labels.
        features=['Lead Origin','Lead Source','Do Not Email','Do Not Call','TotalVisits','Total Time Spent on Website','Page Views Per Visit','Specialization','What is your current occupation']
        report=tabular_classifier(df,'Converted',features,'Rank historical lead conversion propensity using acquisition attributes and engagement snapshots.')
        report['availability_assumption']='Engagement snapshots must be available before the conversion decision. The data lacks event timestamps, so prospective or causal performance is not established.'
        return finish(report,pd.read_csv(output()/'target_summary.csv'))
    df=pd.read_csv(data/'churn_data.csv').merge(pd.read_csv(data/'customer_data.csv'),on='customerID',validate='one_to_one').merge(pd.read_csv(data/'internet_data.csv'),on='customerID',validate='one_to_one')
    df['Churn']=df['Churn'].map({'Yes':1,'No':0});df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
    features=[c for c in df if c not in ['customerID','Churn']]
    return tabular_classifier(df,'Churn',features,'Classify the supplied customer-churn label and report recall, precision, PR-AUC and calibration, rather than accuracy alone.',categorical=['SeniorCitizen'])
