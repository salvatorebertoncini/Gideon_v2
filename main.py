# standard imports
import time

# internal imports
import datasets_management

if __name__ == "__main__":

    # parameters definition
    dataset_name = "test_dataset"

    time_start = time.perf_counter()
    
    # dataset import
    datasets_management.read_dataset(dataset_name)

    print(f'time taken: {(time.perf_counter() - time_start):.6f} seconds')