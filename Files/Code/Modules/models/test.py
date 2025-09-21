import torch
import torch.nn as nn

def soft_test(model, dataloader, device, criterion):
    """
    Avalia o modelo em um dataset de validação, sem teacher forcing (usa sempre ground truth como entrada).
    """
    model.eval()
    total_loss = 0
    all_preds, all_targets = [], []

    with torch.no_grad():
        for x, y in dataloader:
            x, y = x.to(device), y.to(device)
            
            forecast = model(x)  # previsão do modelo
            if criterion is not None:
                loss = criterion(forecast, y)
                total_loss += loss.item()
            
            all_preds.append(forecast.to(device))
            all_targets.append(y.to(device))

    # Concatena tudo em tensores
    all_preds = torch.cat(all_preds, dim=0)
    all_targets = torch.cat(all_targets, dim=0)

    if criterion is not None:
        avg_loss = total_loss / len(dataloader)
        print(f"Average Loss - Soft Test: {avg_loss:.4f}")
    else:
        avg_loss = None

    return all_preds, all_targets, avg_loss

def hard_test(model, X_train, y_train, y_test, split_point, device, criterion, blind_horizon, output_size, debug):
    " Função de teste hard - previsão autoregressiva das últimas 4 semanas"
    
    # Inicialização
    model.eval() # Coloca o modelo em modo de avaliação
    total_loss = 0 
    all_preds = []
    all_targets = []

    # Ponto de partida: última janela do conjunto de treino
    X_test_blind = X_train[split_point - 1]
    y_test_blind = y_train[split_point - 1]

    for i in range(blind_horizon):

        # Enviando para o dispositivo (GPU/CPU)
        X_test_blind = X_test_blind.to(device)
        
        # Fazendo a previsão do modelo
        forecast = model(X_test_blind)

        # Atualizando a entrada para a próxima previsão (autoregressivo)
        X_test_blind = torch.cat((X_test_blind[output_size:], forecast), dim=0)
        y_test_blind = y_test[(i+1)*output_size - 1]

        # Armazenando previsões e rótulos
        all_preds.append(forecast.to(device))
        all_targets.append(y_test_blind.to(device))

        loss = criterion(forecast, y_test_blind)
        total_loss += loss.item()

    avg_loss = total_loss / blind_horizon
    if debug['verbose']:
        print(f"Average Loss - Hard Test: {avg_loss:.4f}")
    
    return all_preds, all_targets, avg_loss