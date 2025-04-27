# standard imports
import time

# internal imports
import datasets_management

if __name__ == "__main__":

    # parameters definition
    dataset_name = "test_dataset"

    # vars initialization
    dataset_user_IDs = None
    dataset_user_permissions = None

    time_start = time.perf_counter()
    
    # dataset import
    dataset_user_IDs, dataset_user_permissions  = datasets_management.read_dataset(dataset_name)
    print(dataset_user_IDs, dataset_user_permissions)

    print(f'time taken: {(time.perf_counter() - time_start):.6f} seconds')
