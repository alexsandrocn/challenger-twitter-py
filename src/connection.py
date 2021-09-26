from pymongo import MongoClient

# Conectando ao servidor local

client = MongoClient("mongodb://localhost:27017/")

db = client.trendTopics

trends_collection = db.trends
