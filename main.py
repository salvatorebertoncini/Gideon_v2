# standard imports
import time
import random
import pprint

# internal imports
import datasets_management
import genetic_functions

if __name__ == "__main__":

    # parameters definition
    dataset_name = "test_dataset"
    dataset_path = "./datasets/"
    dataset_extension = ".txt"
    population_individuals_number = 20
    max_iterations = 10
    probability_crossover = 10
    probability_mutation = 10

    # vars initialization
    UPA_dict = None
    URA_dict = None
    RPA_dict = None
    height = 0

    time_start = time.perf_counter()
    
    # dataset import: dictionary of permissions per user
    UPA_dict, height = datasets_management.read_dataset(dataset_path + dataset_name + dataset_extension)

    RPA_dict = UPA_dict.copy()

    # temporarily vars to be deleted
    parent1 = 1
    parent2 = 1
    gene_to_be_mutated = 1
    population = 1
    new_gene = 1
    new_population = 1

    for i in range(0, max_iterations):
        new_population = genetic_functions.population_generation()
        for x in range(0, height):
            if probability_crossover >= random.randrange(0, 100):
                new_gene = genetic_functions.crossover(parent1, parent2)
        if probability_mutation >= random.randrange(0, 100):
            mutated_gene = genetic_functions.mutation(gene_to_be_mutated)
        new_population = genetic_functions.selection(population)

    pprint.pprint(UPA_dict)
    print(height)

    print(f'time taken: {(time.perf_counter() - time_start):.6f} seconds')
