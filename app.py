import streamlit as st
import pickle as pl


model = pl.load(open('model.pkl', 'rb' ))



def value(step, type ,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFlaggedFraud):
    pre = model.predict([[step, type ,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFlaggedFraud]])
    
    print(pre)
    return pre


def res():
    
    st.title('Online Fruad Detection')
    
    step = st.text_input('step')
    type = st.text_input('type')
    amount = st.text_input('amount')
    oldbalanceOrg = st.text_input('oldbalanceOrg')
    newbalanceOrig = st.text_input('newbalanceOrig')
    oldbalanceDest = st.text_input('oldbalanceDest')
    newbalanceDest = st.text_input('newbalanceDest')
    isFlaggedFraud = st.text_input('isFlaggedFraud')
    result1 = ''
    if st.button('Predict'):
        result1 = value(step, type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud)
    
    if result1 == 1:
        st.header('Fruad')
    else:
        st.header('Not fr')
    
    
    
    
if __name__ == '__main__':
    res()