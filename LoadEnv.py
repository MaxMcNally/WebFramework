import os
from os.path import exists
files = ['.local.env', '.qa.env', '.staging.env', '.env']
def load_env():

    for file in files:
        if exists(file):
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    
                    split = line.split("=")
                    os.environ[split[0]] = split[1].rstrip('\n')
                return
                
