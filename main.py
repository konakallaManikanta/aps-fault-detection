import pymongo
client= pymongo.MongoClient("mongodb+srv://konakallamanikanta:Mani123@cluster0.ef0ztqt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

#Database 
dataBase = client["NeuroLab"]

#Collection Name
collection = dataBase['Products']



