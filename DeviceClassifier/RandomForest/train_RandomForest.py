'''
Trains and saves an instance of the one layer feedforward model on the
data directory specified by the first argument.  The model is saved to the
location specified by the second argument.
'''
import json
import sys

from poseidonml.Model import Model
from sklearn.ensemble import RandomForestClassifier


if __name__ == '__main__':
    # Load model params from config
    with open('opts/config.json') as config_file:
        config = json.load(config_file)
        duration = config['duration']
        labels = config['labels']

    # Get the data directory
    if len(sys.argv) < 2:
        data_dir = '/pcaps'
    else:
        data_dir = sys.argv[1]

    m = RandomForestClassifier(
        n_estimators=100,
        min_samples_split=5,
        class_weight='balanced'
    )

    # Initialize the model
    model = Model(
        duration=duration,
        labels=labels,
        model=m,
        model_type='RandomForest'
    )
    # Train the model
    model.train(data_dir)
    # Save the model to the specified path
    if len(sys.argv) == 3:
        save_path = sys.argv[2]
    else:
        save_path = 'models/RandomForestModel.pkl'
    model.save(save_path)
