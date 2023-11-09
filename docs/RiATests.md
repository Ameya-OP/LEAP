# Tests in RiA

This is the detailed documentation for the testing system of RiA used during development.

## main_test.py

Line one: imports the (list)`dataset` and the function `remover()` from the file main(that is present in the `src` directory)

The `id` is the id that has been read by the system RFID Reader module It has been set to `serial1` for testing purposes.

The test_dataset function checks for the unique `id` in the list `dataset`. It will pass or fail the test accordingly.
