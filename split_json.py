from sklearn.model_selection import train_test_split
import json
from random import shuffle

with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data_50k/legal_50k.json', 'r') as f:
  data = json.load(f)

shuffle(data["sentences"])
shuffled_json = {"sentences" : []}
shuffled_json["sentences"] = data["sentences"]

print("wholde data size",len(shuffled_json["sentences"]))

with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data_50k/legal_50k_shuffled.json', 'w', encoding='utf-8') as f:
    json.dump(shuffled_json, f, ensure_ascii=False, indent=4)
   
test_size = round(0.1 * len(shuffled_json["sentences"]))
print(test_size)

train_json = {"sentences" : []}  
test_json = {"sentences" : []}   
val_json = {"sentences" : []}     


test = shuffled_json["sentences"][0:test_size]
val = shuffled_json["sentences"][test_size:test_size*2]
train = shuffled_json["sentences"][test_size*2:]

train_json["sentences"] = train
val_json["sentences"] = val
test_json["sentences"] = test

print("test data size",len(test_json["sentences"]))
print("val data size",len(val_json["sentences"]))
print("train data size",len(train_json["sentences"]))



with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data_50k/train.json', 'w', encoding='utf-8') as f:
    json.dump(train_json, f, ensure_ascii=False, indent=4)

with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data_50k/test.json', 'w', encoding='utf-8') as f:
    json.dump(test_json, f, ensure_ascii=False, indent=4)

with open('/media/anamika/DATA/WPI_COURSES/NLP-DR/ilm/data/raw_data/legal_data_50k/valid.json', 'w', encoding='utf-8') as f:
    json.dump(val_json, f, ensure_ascii=False, indent=4)