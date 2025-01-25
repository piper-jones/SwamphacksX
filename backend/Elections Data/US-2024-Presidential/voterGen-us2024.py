import numpy as np
import pandas as pd

#2024 U.S. Presidential Election, based on statistics from NBC Exit Polls:
#https://www.nbcnews.com/politics/2024-elections/exit-polls

#assigning demographic data (as pecentages)
#added 1% to 65+ and 50-64, as survey data for aged sumed to 98%
ageDist = [0.08, 0.05, 0.15, 0.15, 0.28, 0.29]  # Age groups: 18-24, 25-29, 30-39, 40-49, 50-64, 65+
genderDist = [0.47, 0.53] # Male, Female
#added 1% to black people, as survey data sumed to 99%
raceDist = [0.71, 0.12, 0.11, 0.03, 0.03]  # White, Black, Hispanic/Latino, Asian, Other
incomeDist = [0.27, 0.32, 0.41]      # Low(under 50k), Medium(50-99k), High(100k+)

numVoters = 100000


np.random.seed(42)

age = np.random.choice(['18-24', '25-29', '30-39', '40-49', '50-64', '65+'], p=ageDist, size=numVoters)
gender = np.random.choice(['Male', 'Female'], p=genderDist, size=numVoters)
race = np.random.choice(['White', 'Black', 'Hispanic', 'Asian', 'Other'], p=raceDist, size=numVoters)
income = np.random.choice(['Low', 'Medium', 'High'], p=incomeDist, size=numVoters)

voters = pd.DataFrame({
    'Age': age,
    'Gender': gender,
    'Race': race,
    'Income': income,
})

voters.to_csv('C:\\Users\\piper\\VS Code\\SwamphacksX\\backend\\Elections Data\\US-2024-Presidential\\us-2024-data.csv', index=False)