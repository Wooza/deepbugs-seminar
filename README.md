# How to run this:

* Follow the setup instructions in the [DeepBugs repository](https://github.com/michaelpradel/DeepBugs)
* Train the models according to their descriptions.

Contents:
* `trained_models` contains the trained models, as well as the gathered logs during training and validation and the found anomalies.
* `evaluation/analyze.py` is the script that was used to select warnings to classify.
* `evaluation/sampled.csv` contains the sampled warnings with their classification and a short explaination.
* `evaluation/files/...` contains the source files in which the sampled warnings occur. The path matches the path given in sampled.csv
