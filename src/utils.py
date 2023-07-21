import joblib
import yaml


def pickle_load(file_path):
    #Function to load pickle file
    return joblib.load(file_path)

def pickle_dump(data, file_path):
    #Function to dump data into pivkle
    joblib.dump(data,file_path)


def config_load():
    #Function to load config files
    
    try:
        with open(CONFIG DIR, 'r') as file:
        