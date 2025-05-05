# custom imports
import numpy as np

def open_file(path:str):
    file = open(path, 'r')
    file_to_read = file.read()
    file.close()

    return file_to_read

def read_dataset(dataset_path:str):    
    dataset_raw_txt = open_file(dataset_path) 

    # dataset split default is str. astype(int) casts the array to int 
    dataset = np.array(dataset_raw_txt.split())
    dataset = dataset.astype(int)
    
    # dataset is returned as a list in which the odd index elements are the user permissions
    # and the even index elements are the user IDs.
    dataset_user_permissions = np.array(dataset[1::2])
    dataset_user_IDs = np.array(dataset[::2])

    dataset_dictionary = {}
    max_permission = 0

    for i in range(0, len(dataset_user_IDs)):
        if dataset_user_IDs[i] in dataset_dictionary:
            dataset_dictionary[dataset_user_IDs[i]] = np.append(dataset_dictionary[dataset_user_IDs[i]], dataset_user_permissions[i])
        else:
            dataset_dictionary[dataset_user_IDs[i]] = np.array([dataset_user_permissions[i]])
        
        if dataset_user_permissions[i] > max_permission:
            max_permission = dataset_user_permissions[i]

    return dataset_dictionary, min(len(dataset_dictionary), max_permission)
