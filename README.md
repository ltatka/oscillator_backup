# oscillator_backup

## Set up
This module requires: 
* pymongo
* bson

Either use the included conda environment or pip install these otherwise you will be sad.

## Basic use
### From the command line:

1. Navigate to repo
2. ```python ./mongoBackup.py```


## Log

* Back up 2021-08-23 LT
* Back up 2021-10-07 LT (364 3-node oscillators)
* Back up 2021-10-09 LT (processed 364 3-nodes)
* Back up 2021-10-10 LT (processed 605 3-nodes)
* Back up 2021-10-14 LT (605 definite oscillators that don't go to infinity, but had to reset some because errors in processing script. These will be labelled as {"processed": False}