# rnn-codenames

Ever have those moments where you're thinking of what to name your github project? And ever have those moments where you're too uncreative to actually think of a proper name?

Me too, and that's why I then asked, "Why not just have recurrent neural networks do it for me?"

This project uses [sherjilozair's char-rnn implementation](https://github.com/sherjilozair/char-rnn-tensorflow) for Python.

It scrapes data from Wikipedia and feeds it into an RNN. It currently takes from these pages:
- https://en.wikipedia.org/wiki/List_of_computer_technology_code_names
- *... and more to come!*

## Usage

Call `run.sh` in your shell:
```
$ ./run.sh
```

Wait for it to output words into the console.

