from RiA.main import dataset

#This id will be replaced by the serial id that has been retrieved by the RFID reader module.
id = "serial1"

list_set = set(dataset)

def test_dataset():
    assert  id in dataset

    