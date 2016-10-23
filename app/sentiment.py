from flask import Flask, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/<string:text>', methods=['GET'])
def get_sentiment(text):
    sid = SentimentIntensityAnalyzer(lexicon_file='../nltk_data/sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt')
    score = sid.polarity_scores(text)
    return jsonify(score)
