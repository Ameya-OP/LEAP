from LEAP.RiA.main import dataset

#This id will be replaced by the serial id that has been retrieved by the RFID reader module.
id = "serial4"

list_set = set(dataset)

contains_word = lambda s, l: any(map(lambda x: x in s, l))

def test_dataset():
    assert  id == contains_word(id, list_set)
