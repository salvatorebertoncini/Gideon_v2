# standard imports
import time

# internal imports
import datasets_management

if __name__ == "__main__":

    # parameters definition
    dataset_name = "hc"

    # vars initialization
    dataset_dictionary = None

    time_start = time.perf_counter()
    
    # dataset import
    dataset_dictionary = datasets_management.read_dataset(dataset_name)
    
    print(f'time taken: {(time.perf_counter() - time_start):.6f} seconds')
