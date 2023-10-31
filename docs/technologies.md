# Technologies Used

As discussed, the project has two main sub-projects, them being GeCoS, and RiA.

## GeCoS

## RiA

RiA uses HF RFID at 13.6 MHz to recognize RFID tags. The RFID reader data is relayed to an Arduino Uno, which will relay the data to the centeral server where the attendance is recorded.

### System Schematics

The system will use two mini-datasets, one temporary(DBt) and one permanent(DBp).
DBt will have the same data as the DBp, but the IDs will be deleted once the teacher is recorded as present —> this will decrease the total amount of data that has to be processed and hence improve efficiency. This is especially important because the system will use a microcontroller and not a microprocessor. Microcontrollers have very limited processing power, and hence any efficiency improvements will go a long way.
Whenever a teacher signs out, the ID of the teacher will be added back to DBt.

DBp will be used when the teacher signs out, to verify if the ID of the teacher is present on the dataset. This is to prevent scanning and storing data of other random RFID and NFC tags.
