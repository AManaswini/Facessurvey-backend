import pandas as pd
import random

csv_path = ''
def createFacesRelease1():
    actual_data = pd.read_csv(csv_path+'training-image-pairs.csv', usecols=['arrest_id_left','image_url_left','description_left','arrest_id_right','image_url_right','description_right','correct_response'])
    actual_pattern = random.sample(range(29), 15)
    img_array = []
    for actual_img_idx in range(1):
        pattern_idx = actual_pattern[actual_img_idx]
        actual_img_a = actual_data.iloc[[pattern_idx]]['arrest_id_left'].item()
        actual_img_b = actual_data.iloc[[pattern_idx]]['arrest_id_right'].item()
        url_a = actual_data.iloc[[pattern_idx]]['image_url_left'].item()
        url_b = actual_data.iloc[[pattern_idx]]['image_url_right'].item()
        desca=actual_data.iloc[[pattern_idx]]['description_left'].item()
        desc_a=dict(subString.split(":") for subString in desca.split("\n"))
        descb=actual_data.iloc[[pattern_idx]]['description_right'].item()
        desc_b=dict(subString.split(":") for subString in descb.split("\n"))
        actual_img_flag = actual_data.iloc[[pattern_idx]]['correct_response'].item()
        if actual_img_flag == 'right':
            res = 'b'
        else:
            res = 'a'
        actual_img_json = {'img_a': actual_img_a,
                           'img_b': actual_img_b,
                           'res': res,
                           'type': 'actual',
                           'url_a': url_a,
                           'url_b': url_b,
                           'desc_a': desc_a,
                           'desc_b': desc_b
                           },
                           
        img_array.append(actual_img_json)
    return img_array

    
def createFacesReleaseevaluation1():
    actual_data = pd.read_csv(csv_path + 'evaluation-image-pairs-final.csv', usecols=['image_url_left', 'image_url_right', 'arrest_id_left', 'arrest_id_right','description_left','description_right'])
    # actual_decsription = pd.read_csv(csv_path + 'evaluation-descriptions.csv', usecols=['arrest_id', 'description', 'f_race', 'f_sex', 'f_age'])
    # descriptions = random.sample(range(0, 100), 70)
    actual_pattern = []
    img_array = []
    # i = 0
    # k = 0
    even = []
    for i in range(0,102):
        if i%2==0:
            even.append(i)
    print(even)
    indices = random.sample(even,50)
    print(indices)
    for i in indices:
        x = random.sample(range(i, i+2), 1)
        for sample in x:
            actual_pattern.append(sample)
    # print(actual_pattern)
    #this is comment from here
    # while i < 1000 and len(actual_pattern) < 35:
    #     x = random.sample(range(i, i+2), 1)
    #     for sample in x:
    #         actual_pattern.append(sample)
    #     i += 2
    #k = 0
    #actual_pattern = random.sample(range(98), 35)
    print(actual_pattern)
    for actual_img_idx in range(2):
        pattern_idx = actual_pattern[actual_img_idx]
        img_a = actual_data.iloc[[pattern_idx]]['arrest_id_left'].item()
        img_b = actual_data.iloc[[pattern_idx]]['arrest_id_right'].item()
        url_a = actual_data.iloc[[pattern_idx]]['image_url_left'].item()
        url_b = actual_data.iloc[[pattern_idx]]['image_url_right'].item()
        # desca = actual_decsription.iloc[descriptions[k]]['description']
        # desca_id = str(actual_decsription.iloc[descriptions[k]]['arrest_id'])
        # desc_a = dict(subString.split(":") for subString in desca.split("\n"))
        # #k += 1
        # descb_id = str(actual_decsription.iloc[descriptions[k]]['arrest_id'])
        # descb = actual_decsription.iloc[descriptions[k]]['description']
        # desc_b = dict(subString.split(":") for subString in descb.split("\n"))
        
        #k += 1
        desca=actual_data.iloc[[pattern_idx]]['description_left'].item()
        desc_a=dict(subString.split(":") for subString in desca.split("\n"))
        descb=actual_data.iloc[[pattern_idx]]['description_right'].item()
        desc_b=dict(subString.split(":") for subString in descb.split("\n"))
        actual_img_json = {'type': 'eval',
                           'url_a': url_a,
                           'url_b': url_b,
                            'desc_a': desc_a,
                            'desc_b': desc_b,
                            'img_a': img_a,
                            'img_b': img_b,
                            # 'desca_id': desca_id,
                            # 'descb_id': descb_id 
                           },
        img_array.append(actual_img_json)
    return img_array

    
