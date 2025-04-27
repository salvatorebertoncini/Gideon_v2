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
    dataset = dataset_raw_txt.split()

    # dataset is returned as a list in which the odd index elements are the user permissions
    # and the even index elements are the user IDs.
    dataset_user_permissions = dataset[1::2]
    dataset_user_IDs = dataset[::2]

    return dataset_user_IDs, dataset_user_permissions
