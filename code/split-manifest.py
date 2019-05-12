import os
import json
import random
import time
import numpy as np
import boto3

BUCKET = '<< YOUR S3 BUCKET NAME >>'
assert BUCKET != '<< YOUR S3 BUCKET NAME >>', 'Please provide a custom S3 bucket name.'
EXP_NAME = 'ground-truth-ic-demo' # Any valid S3 prefix.

with open('output.manifest', 'r') as f:
    output = [json.loads(line) for line in f.readlines()]

# Shuffle output in place.
np.random.shuffle(output)
    
dataset_size = len(output)
train_test_split_index = round(dataset_size*0.8)

train_data = output[:train_test_split_index]
validation_data = output[train_test_split_index:]

num_training_samples = 0
with open('train.manifest', 'w') as f:
    for line in train_data:
        f.write(json.dumps(line))
        f.write('\n')
        num_training_samples += 1
    
with open('validation.manifest', 'w') as f:
    for line in validation_data:
        f.write(json.dumps(line))
        f.write('\n')
