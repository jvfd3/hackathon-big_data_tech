import torch

def forecast_blind(model, X_train, blind_horizon, device, output_size):
    " Função de previsão cega - previsão autoregressiva das primeiras 4 semanas após o treino"
    # Inicialização
    model.eval() # Coloca o modelo em modo de avaliação
    all_preds = []


    # Ponto de partida: última janela do conjunto de treino
    X_test_blind = X_train[-1]

    for i in range(blind_horizon):

        # Enviando para o dispositivo (GPU/CPU)
        X_test_blind = X_test_blind.to(device)
        
        # Fazendo a previsão do modelo
        forecast = model(X_test_blind)

        # Atualizando a entrada para a próxima previsão (autoregressivo)
        X_test_blind = torch.cat((X_test_blind[output_size:], forecast), dim=0)

        # Armazenando previsões e rótulos
        all_preds.append(forecast.cpu())

    return torch.cat(all_preds, dim=0)