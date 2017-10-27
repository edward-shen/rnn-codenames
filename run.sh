#!/bin/bash
python3 getWikipedia.py
cd char-rnn-tensorflow-master
python3 train.py --num_epochs=200
python3 sample.py
