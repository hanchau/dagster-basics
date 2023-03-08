import csv
import requests
from dagster import asset
import pandas as pd


@asset
def extract():
    path = 'data/raw/cereals.py'
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereal_rows = [row for row in csv.DictReader(lines)]
    df = pd.DataFrame(cereal_rows)    
    df.to_csv(path)
    return path

@asset
def transform(extract):
    path = 'data/processed/wheat_cereals.py'
    df = pd.read_csv(extract)
    df = df[df['name'].str.contains('Wheat')]
    df.to_csv(path)
    return path

@asset
def load(transform):
    path = 'data/load/wheat_cereals.py'
    df = pd.read_csv(transform)
    df.to_csv(path)
    return path
