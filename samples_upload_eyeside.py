import json
import pandas as pd
import copy

# Read file json format
with open("example_classification_75.json") as json_file:
    example = json.load(json_file)

# Get data from CSV file
df = pd.read_csv('./samples/labels.csv')
print(df.head(6))
print('-----------------------------')

filenames = list(df.filename)                   # Image path
labels = list(df.eyeside)                       # Label result
number_results = list(range(1,len(df.index)+1)) # Number of result

def get_image_path(filenames, labels, number_results):
    # Process
    data = copy.deepcopy(example[0])
    image = list(data.values())[0]  
    image_path = list(image.values())[0]
    image_path = image_path[:13] + str(filenames)
    
    # Image path
    dict_image = {'image': image_path}
    data['data'].update(dict_image)

    # Label result
    data['annotations'][0]['result'][0]['id'] = 'result' + str(number_results)

    # Number of result
    dict_choice = {'choices': [str(labels)]}
    data['annotations'][0]['result'][0]['value'].update(dict_choice)
    
    # Output
    print(data)
    print('-----------------------------')
    return data
      

# Result
sample_list = list(map(get_image_path, filenames, labels, number_results))
print(sample_list)


# Save file json format 
with open('label_image_test.json', 'w') as outfile:
    json.dump(sample_list, outfile)

