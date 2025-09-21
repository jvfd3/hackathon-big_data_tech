""" get dataset function """

import numpy as np
import torch

# from Files.Code.Modules.models.make_dataset import SingleSeriesDataset

from Modules.models.make_dataset import SingleSeriesDataset

def get_dataset(sample, feature, hyperparams):
    input_size = hyperparams['input_size']
    output_size = hyperparams['output_size']

    # Inicializando os vetores de entrada e os rótulos
    X = []
    y = []

    # Número total de amostras (janelas diferentes) que podem ser extraídas
    # de um mesmo sample
    num_windows = len(sample) - input_size - output_size + 1

    if hyperparams['debug']['verbose']:
        print(f"Número total de janelas extraídas: {num_windows}")
        print(f"Para janelas de tamanho {input_size} e previsão de {output_size} dias à frente.")
    # Extraindo janelas deslizantes
    for i in range(num_windows):

        X_window = sample[i:i+input_size]             # janela de entrada
        feature_window = feature[i:i+input_size]      # janela de entrada

        X_window = np.stack([X_window,feature_window], axis=1)  # shape = (input_size, 4)

        y_window = sample[i+input_size:i+input_size+output_size]  # próximos dias da série

        X.append(X_window)
        y.append(y_window)

    # Convertendo para arrays numpy e depois para tensores PyTorch
    X = np.array(X)  # shape = [num_windows, input_size, num_features]
    y = np.array(y)  # shape = [num_windows, output_size]

    if hyperparams['debug']['verbose']:
        print()
        print("O vetor de entrada antes do flatten")
        print(f"tem shape (num_windows, size_window, num_features): {X.shape}")

    X = torch.tensor(X, dtype=torch.float16)  # shape = [n_samples, input_size, 1]

    y = torch.tensor(y, dtype=torch.float16)  # shape = [n_samples, 1]


    dataset_full = SingleSeriesDataset(X, y)
    return dataset_full, X, y
