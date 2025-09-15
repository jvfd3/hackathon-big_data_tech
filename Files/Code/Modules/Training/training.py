from torch.utils.data import Dataset, DataLoader

#Inicialização do modelo, da loss function e do otimizador

# Hiperparâmetros do modelo
input_size = 30
output_size = 1
batch_size = 32
device = "cuda" if torch.cuda.is_available() else "cpu"

# Inicialização do modelo N-BEATS
model = NBeats(input_size, hidden_size=64, output_size=output_size).to(device)

# Dataset e DataLoader
dataloader = DataLoader(dataset, batch_size, shuffle=False)

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