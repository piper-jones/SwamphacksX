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


#Assigning probabilities for each demographic
# [Republican, Democrat, Other]

ageProbabilities = {
    '18-24': [0.43, 0.54, 0.03],  
    '25-29': [0.45, 0.53, 0.02],  
    '30-39': [0.45, 0.51, 0.04],  
    '40-49': [0.49, 0.49, 0.02],  
    '50-64': [0.56, 0.43, 0.01],  
    '65+': [0.50, 0.49, 0.01],    
}

genderProbabilities = {
    'Male': [0.55, 0.43, 0.02], 
    'Female': [0.45, 0.53, 0.02],  
}

racePobabilities = {
    'White': [0.57, 0.42, 0.01], 
    'Black': [0.13, 0.86, 0.01],  
    'Hispanic': [0.46, 0.51, 0.03],  
    'Asian': [0.41, 0.55, 0.04],   
    'Other': [0.52, 0.44, 0.04], 
}

incomeProbabilities = {
    'Low': [0.50, 0.48, 0.02], 
    'Medium': [0.52, 0.46, 0.02], 
    'High': [0.47, 0.51, 0.02],   
}


# Initialize a column for storing the final probabilities
voters['Probabilities'] = None

# Assign probabilities based on age or income, depending on the approach
voters['Probabilities'] = voters.apply(
    lambda row: 
        # Using multiple demographic factors for probability distribution
        ageProbabilities[row['Age']] if row['Income'] == 'Low' else
        (genderProbabilities[row['Gender']] if row['Race'] == 'White' else
         (incomeProbabilities[row['Income']])),
    axis=1
)

# Simulate each voter's choice based on the assigned probabilities
candidates = ['Republican', 'Democrat', 'Third Party']  
choices = []

for i, row in voters.iterrows():
    probabilities = row['Probabilities']
    choice = np.random.choice(candidates, p=probabilities)
    choices.append(choice)

voters['Voter_Choice'] = choices
    

voters.to_csv('C:\\Users\\piper\\VS Code\\SwamphacksX\\backend\\Elections Data\\US-2024-Presidential\\demData-us2024.csv', index=False)