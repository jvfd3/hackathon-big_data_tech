""" Separando treino e validação """

import torch
from torch.utils.data import DataLoader
from matplotlib import pyplot as plt

# from Files.Code.Modules.models.make_dataset import SingleSeriesDataset
# from Files.Code.Modules.models.test import hard_test, soft_test

from Modules.models.make_dataset import SingleSeriesDataset
from Modules.models.test import hard_test, soft_test

def get_train_validation(dataset_full, X, y, hyperparams):
    split = hyperparams['split']

    X_test, y_test = None, None
    X_train, y_train = None, None
    
    # Ponto de separação entre treino e validação (Caso seja para envio, não há validação)
    if split < 1:
        split_point = int(split * len(dataset_full))
        # Separação cronológica das janelas
        X_train, X_test = X[:split_point], X[split_point:]
        y_train, y_test = y[:split_point], y[split_point:]
    else:
        X_train = X
        y_train = y

    num_features = X_train.shape[2]
    
    # Flatten do tensor para entrar na rede
    X_train = X_train.view(X_train.shape[0], -1)  # shape = [num_windows_train, input_size * n_features]

    if split < 1:
        X_test  = X_test.view(X_test.shape[0], -1) # shape = [num_windows_test, input_size * n_features]

    if hyperparams['debug']['verbose']:
        print(f"Há um total de {len(dataset_full)} janelas e o split ocorre em {split*100:.0f}% do dataset")
        print(f" O shape de X_train é {X_train.shape} e o shape de X_test é {X_test.shape}") if split < 1 else ""
        print(f" O shape de y_train é {y_train.shape} e o shape de y_test é {y_test.shape}") if split < 1 else ""

    return X_train, y_train, X_test, y_test, num_features



def validate_model(model, dataset_full, criterion, X_train, y_train, X_test, y_test, hyperparams, verbose: bool=True):
    """
    Validação do modelo treinado
    """
    split = hyperparams['split']
    batch_size = hyperparams['batch_size']
    device = hyperparams['device']
    output_size = hyperparams['output_size']
    blind_horizon = hyperparams['blind_horizon']
    split_point = int(split * len(dataset_full))
    

    if split < 1: # Validando o modelo quando o split é menor que 1
        # Adotando o dataset de validação (soft)
        dataset = SingleSeriesDataset(X_test, y_test)
        dataloader = DataLoader(dataset, batch_size, shuffle=False) # shuffle=False para séries temporais

        all_preds_S, all_targets_S, avg_loss_test_S = soft_test(model, dataloader, device, criterion)

        # Validação hard - previsão cega das primeiras blind_horizon semanas
        all_preds_H, all_targets_H, avg_loss_test_H = hard_test(model, X_train, y_train, y_test, split_point, device, criterion, blind_horizon, output_size)

        " Sanity check da validação do modelo (preds and targets)"
        all_preds_array = []
        all_targets_array = []

        # Convert lists to tensors before flattening
        all_preds_tensor = torch.cat([t.unsqueeze(0) if t.dim() == 1 else t for t in all_preds_H], dim=0).flatten()
        all_targets_tensor = torch.cat([t.unsqueeze(0) if t.dim() == 1 else t for t in all_targets_H], dim=0).flatten()

        for t in all_preds_tensor:
            all_preds_array.append(t.detach().numpy())
        for t in all_targets_tensor:
            all_targets_array.append(t.detach().numpy())

        if verbose:
            plt.figure(figsize=(12, 5))
            plt.plot(all_targets_array, label="Ground truth", linewidth=2)
            plt.plot(all_preds_array, label="Previsões", linewidth=2, alpha=0.7)
            plt.legend()
