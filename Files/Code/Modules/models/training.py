
import torch
from torch.utils.data import DataLoader
from torch import nn

# from Files.Code.Modules.models.make_dataset import SingleSeriesDataset
# from Files.Code.Modules.models.NBeats import NBeats
# from Files.Code.Modules.models.WMAPELoss import WMAPELoss

from Modules.models.make_dataset import SingleSeriesDataset
from Modules.models.NBeats import NBeats
from Modules.models.WMAPELoss import WMAPELoss
    
def train_model(model, learning_rate, epochs, device, dataloader, hyperparams):
    """ Training Model """

    # Otimizador da rede neural (Adam - Adaptive Moment Estimation)
    optimizer = torch.optim.Adam(model.parameters(), learning_rate)

    # Função de perda (L1 Loss - Mean Absolute Error)
    criterion = nn.L1Loss()

    # Loop de treinamento
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for x, y in dataloader:
            x, y = x.to(device), y.to(device)

            optimizer.zero_grad()
            forecast = model(x)              # previsão
            loss = criterion(forecast, y)    # compara previsão com real
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
        if hyperparams['debug']['verbose']:
            size = len(str(epochs))
            print(f"Epoch {epoch+1:0{size}d}/{epochs}, Loss: {total_loss/len(dataloader):.4f}")
    print(f"Treinamento concluído. Loss final: {total_loss/len(dataloader):.4f}")
    return model


def traininig_func(X_train, y_train, num_features, hyperparams):
    # Adotando o dataset de treino
    batch_size = hyperparams['batch_size']
    input_size = hyperparams['input_size']
    hidden_size = hyperparams['hidden_size']
    output_size = hyperparams['output_size']
    n_layers = hyperparams['n_layers']
    device = hyperparams['device']
    learning_rate = hyperparams['learning_rate']
    epochs = hyperparams['epochs']
    
    num_features = num_features
    
    dataset = SingleSeriesDataset(X_train, y_train) 
    dataloader = DataLoader(dataset, batch_size, shuffle=False) # shuffle=False para séries temporais

    # Inicialização do modelo N-BEATS (considerando X_train com num_features)
    model = NBeats(input_size*num_features, hidden_size, output_size, n_layers).to(device)
    model = train_model(model, learning_rate, epochs, device, dataloader, hyperparams)
    return model
