import os
import random
import numpy as np

data='/ASD/mansi_flyby/large_set_surf_sa_ct_sd_depth_norm_seq'
data_set='/ASD/mansi_flyby/large_set_surf_sa_ct_sd_depth_norm_DL_sets'
train_path='/ASD/mansi_flyby/large_set_surf_sa_ct_sd_depth_norm_DL_sets/train.csv'
test_path='/ASD/mansi_flyby/large_set_surf_sa_ct_sd_depth_norm_DL_sets/test.csv'
val_path='/ASD/mansi_flyby/large_set_surf_sa_ct_sd_depth_norm_DL_sets/val.csv'
    
data_list = []
    
#create folder for all train, test, val csv
if not os.path.exists(data_set):
    os.makedirs(data_set)

#Open and empty train, test, val csv:
train_file = open(train_path, "w")
train_file.write("File_path, Label\n")
train_file.close()

test_file = open(test_path, "w")
test_file.write("File_path, Label\n")
test_file.close()

val_file = open(val_path, "w")
val_file.write("File_path, Label\n")
val_file.close()

for filename in os.listdir(data):
    #get sub_id of each case
    start = filename.find('neo')
    end = filename.find('year', start)
    sub_id = (filename[start:end])
    label = filename[start:end][-1]
    data_list.append(sub_id)
    #print(sub_id)
    #print(label)

#remove duplicate sub_ids from list:
data_list = list(set(data_list))

#randomize list:
random.shuffle(data_list)

#split list into 70% train, 20% test, 10% val
train, test, val = np.split(data_list, [int(len(data_list)*0.7), int(len(data_list)*0.9)])

#print(len(train))
#print(len(test))
#print(len(val))


for filename in os.listdir(data):
    #get sub_id of each case
    start = filename.find('neo')
    end = filename.find('year', start)
    sub_id = (filename[start:end])
    label = filename[start:end][-1]

    #train csv
    if sub_id in train:
        full_path = (os.path.join(data, filename))
        train_file = open(train_path, "a")
        train_file.write(full_path+","+ label+"\n")
        train_file.close()


    #test csv
    if sub_id in test:
        full_path = (os.path.join(data, filename))
        test_file = open(test_path, "a")
        test_file.write(full_path+","+ label+"\n")
        test_file.close()

    #val csv
    if sub_id in val:
        full_path = (os.path.join(data, filename))
        val_file = open(val_path, "a")
        val_file.write(full_path+","+ label+"\n")
        val_file.close()
