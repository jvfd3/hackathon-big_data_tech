import torch

def get_hyperparams():
    HYPERPARAMS = {
        'debug': { # Parameters for debugging and verbosity
            'verbose': True,        # Print debug information
            'plot': True,           # Plot training and validation losses
            'time': True,           # Print time taken for training
        },
        # Neural Network Global Parameters
        'input_size': 30,       # Number of past days to use as input
        'output_size': 7,       # Number of future days to predict
        'batch_size': 28,       # Batch size for training
        'n_layers': 4,          # Number of layers in the N-BEATS model
        'hidden_size': 128,     # Number of hidden units in each layer

        # Training parameters
        'learning_rate': 1e-3,  # Learning rate for the optimizer
        'epochs': 10,          # Number of training epochs (iterations over the entire dataset)
        'device': torch.device("cuda" if torch.cuda.is_available() else "cpu"),  # Use GPU if available
        'blind_horizon': 4,     # Number of days to exclude from the end of the training set for hard test
        'split': 1,             # Proportion of data to use for training (1.0 for validation)
        'seed': 42,             # Random seed for reproducibility
    }
    return HYPERPARAMS
