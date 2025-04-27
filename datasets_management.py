def open_file(path:str):
    file = open(path, 'r')
    file_to_read = file.read()
    file.close()

    return file_to_read

def read_dataset(dataset_name:str):
    dataset_path:str = "./datasets/"
    dataset_extension:str = ".txt"
    
    dataset = open_file(dataset_path + dataset_name + dataset_extension) 
    
    print(dataset_name)
    print(dataset)


