
import torch
from torch.utils.data import DataLoader

# from Files.Code.Modules.models.make_dataset import SingleSeriesDataset
# from Files.Code.Modules.models.NBeats import NBeats
# from Files.Code.Modules.models.WMAPELoss import WMAPELoss

from Modules.models.make_dataset import SingleSeriesDataset
from Modules.models.NBeats import NBeats
from Modules.models.WMAPELoss import WMAPELoss
    
def train_model(model, learning_rate, epochs, device, dataloader):
    """ Training Model """

    # Otimizador da rede neural (Adam - Adaptive Moment Estimation)
    optimizer = torch.optim.Adam(model.parameters(), learning_rate)

    # Função de perda (Mean Squared Error) TROCAR SE NECESSÁRIO
    criterion = WMAPELoss()

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

        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(dataloader):.4f}")

    return model


