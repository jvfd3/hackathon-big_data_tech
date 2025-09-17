from torch.utils.data import Dataset, DataLoader

# Função de treinamento
def train_model_NBeats(model, learning_rate, epochs, device):

    # Otimizador da rede neural (Adam - Adaptive Moment Estimation)
    optimizer = torch.optim.Adam(model.parameters(), learning_rate)

    # Função de perda (Mean Squared Error) TROCAR SE NECESSÁRIO
    criterion = nn.MSELoss()

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


    return model, criterion, optimizer