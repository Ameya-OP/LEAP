
id = "serial1"

#This will link to the database of teahcer IDs that wll be encrypted to prevent any data breaches.
dataset = ["serial1", "serial2"]

print(dataset[0])

#This function is called in the test to delete the assigned ID fromt he dataset, so that it is marked as present.
def remover(ids): # The function accepts any object, which in this context will be the serial id.
    return dataset.remove(ids) # Calling the remove method to remove the specified id.

permanent_dataset = ["serial1", "serial2", "serial3", "serial4"]

#This function recovers the `dataset` list according to the `permanent_dataset`
def recover_dataset(dataset, permanent_dataset):
    dataset = permanent_dataset
    return dataset
    

#Debugging 

recover_dataset(dataset, permanent_dataset)
print(dataset, "    hello")