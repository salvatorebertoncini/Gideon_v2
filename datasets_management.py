# custom imports
import numpy as np

def open_file(path:str):
    file = open(path, 'r')
    file_to_read = file.read()
    file.close()

    return file_to_read

def read_dataset(dataset_name:str):
    dataset_path:str = "./datasets/"
    dataset_extension:str = ".txt"
    
    dataset_raw_txt = open_file(dataset_path + dataset_name + dataset_extension) 

    # dataset split default is str. astype(int) casts the array to int 
    dataset = np.array(dataset_raw_txt.split())
    dataset = dataset.astype(int)
    
    # dataset is returned as a list in which the odd index elements are the user permissions
    # and the even index elements are the user IDs.
    dataset_user_permissions = np.array(dataset[1::2])
    dataset_user_IDs = np.array(dataset[::2])
    
    print(dataset_user_IDs)
    print(dataset_user_permissions)

    dataset_dictionary = {}

    for i in range(0, len(dataset_user_permissions)):
        if dataset_user_permissions[i] in dataset_dictionary:
            dataset_dictionary[dataset_user_permissions[i]] = np.append(dataset_dictionary[dataset_user_permissions[i]], dataset_user_IDs[i])
        else:
            dataset_dictionary[dataset_user_permissions[i]] = np.array([dataset_user_IDs[i]])
    
    return dataset_dictionary