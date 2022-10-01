# import json

# from sklearn.model_selection import train_test_split

import json
  
# Opening JSON file
f = open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data/legal_10K.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

test = data["sentences"][0:100]
valid = data["sentences"][100:200]
train = data["sentences"][200:300]
    


train_j = {"sentences" : train}
valid_j = {"sentences" : valid}
test_j = {"sentences" : test}


with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data/train.json', 'w') as f:
    json.dump(train_j, f)

with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data/valid.json', 'w') as f:
    json.dump(valid_j, f)

with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data/test.json', 'w') as f:
    json.dump(test_j, f)




