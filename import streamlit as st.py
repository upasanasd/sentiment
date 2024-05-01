import streamlit as st 
import joblib
#load the trained model
model = joblib.load("sentiment-model.pkl")
#define sentiment labels
sentiment_label={'1':'POSITIVE','0':'NEGATIVE'}
#CREATE STREAMLIT APP
st.title("Sentiment Analysis")
#input text area
user_input=st.text_area("Enter your  text in here:")
#prediction 
if st.button("Predict"):
    #perform sentiment prediction
    print(user_input)
    predicted_sentiment =model.predict([user_input])[0]
    print("Predicted Label: "+str(predicted_sentiment))
    predicted_sentiment_label=sentiment_label[str(predicted_sentiment)]

    st.info(f"Predicted Sentiment: {predicted_sentiment_label}")