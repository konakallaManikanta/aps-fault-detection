import pymongo
import pandas as pd
import json
client= pymongo.MongoClient("mongodb+srv://konakallamanikanta:Mani123@cluster0.ef0ztqt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DATA_FILE_PATH="aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    #Convert dataframe into JSON so that we can dump these records in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



