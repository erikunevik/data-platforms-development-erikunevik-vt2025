import pandas as pd
from pathlib import Path


data_path = Path(__file__).parent / "data" ## File är själva filen vi jobbar i. Parent hoppar upp en nivå från vart den är för att styra in den till filen.  

df = pd.read_csv(data_path / "calories.csv")

print(df.head())

# Så här gör man för att öppna en csvfil

