

from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv' , encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def likedArticles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unlikedArticles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    did_not_watch.append(articles)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()
