#Sentiment Analyzer using VADER algorithm in nltk package

##installation (pip and bash)

pip install -r requirements.txt

##start server:
cd app
export FLASK_APP=sentiment.py
python -m flask run

##usage examples:
> curl -i http://localhost:5000/the%20client%20is%20very%20happy

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 70
Server: Werkzeug/0.11.11 Python/2.7.6
Date: Sun, 23 Oct 2016 02:21:24 GMT

{
  "compound": 0.6115, 
  "neg": 0.0, 
  "neu": 0.5, 
  "pos": 0.5
}

> curl -i http://localhost:5000/the%20client%20is%20not%20very%20happy
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 75
Server: Werkzeug/0.11.11 Python/2.7.6
Date: Sun, 23 Oct 2016 02:21:34 GMT

{
  "compound": -0.4964, 
  "neg": 0.391, 
  "neu": 0.609, 
  "pos": 0.0
}

