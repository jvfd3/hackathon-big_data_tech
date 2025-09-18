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
            
            all_preds.append(forecast.cpu())
            all_targets.append(y.cpu())

    # Concatena tudo em tensores
    all_preds = torch.cat(all_preds, dim=0)
    all_targets = torch.cat(all_targets, dim=0)

    if criterion is not None:
        avg_loss = total_loss / len(dataloader)
        print(f"Average Loss - Soft Test: {avg_loss:.4f}")
    else:
        avg_loss = None

    return all_preds, all_targets, avg_loss



def hard_test1(model, dataloader, device, criterion, forecast_horizon):
    """
    Calcula a perda média de um teste autoregressivo para o modelo N-BEATS.

    Nesse modo, a previsão de um passo de tempo é usada como a entrada
    para o próximo passo de tempo, simulando uma previsão de longo prazo
    onde o modelo se baseia apenas nas suas próprias saídas.

    Args:
        model (torch.nn.Module): O modelo N-BEATS a ser testado.
        dataloader (torch.utils.data.DataLoader): O dataloader do conjunto de teste.
        device (torch.device): O dispositivo (CPU ou GPU) onde o modelo e os dados estão.
        criterion (torch.nn.Module): A função de perda (ex: MSELoss, MAELoss).
        forecast_horizon (int): O horizonte de previsão que o modelo deve gerar.

    Returns:
        float: A perda média do teste.
    """
    model.eval()  # Coloca o modelo em modo de avaliação
    total_loss = 0.0
    num_batches = 0

    with torch.no_grad():  # Desativa o cálculo de gradientes
        for batch_features, batch_targets in dataloader:
            # Envia os dados para o dispositivo especificado
            batch_features = batch_features.to(device)
            batch_targets = batch_targets.to(device)

            # Extrai a última parte da janela de entrada para ser a primeira entrada da previsão
            # Isso simula o comportamento autoregressivo
            autoregressive_input = batch_features[:, -1:, :]

            # Inicializa a lista para armazenar as previsões do horizonte completo
            forecasted_sequence = []

            # Loop autoregressivo para gerar a previsão completa
            for _ in range(forecast_horizon):
                # O modelo N-BEATS normalmente requer uma entrada de um determinado tamanho.
                # Aqui, estamos assumindo que ele recebe uma única entrada e prevê o próximo passo.
                # Se o seu modelo for diferente, adapte essa parte.
                
                # A dimensão da entrada do seu modelo NBeats pode variar. 
                # Certifique-se de que autoregressive_input tenha a forma correta.
                
                # Faz a previsão do próximo passo de tempo
                prediction = model(autoregressive_input)

                # Adiciona a previsão à sequência de saída
                forecasted_sequence.append(prediction)

                # A previsão atual se torna a entrada para o próximo passo
                autoregressive_input = prediction

            # Concatena as previsões para formar a sequência completa de saída
            full_forecast = torch.cat(forecasted_sequence, dim=1)

            # Calcula a perda entre a previsão completa e os alvos reais
            # Certifique-se de que a dimensão do full_forecast é compatível com batch_targets
            loss = criterion(full_forecast, batch_targets[:, :forecast_horizon, :])

            # Acumula a perda
            total_loss += loss.item()
            num_batches += 1

    # Retorna a perda média
    return total_loss / num_batches






def hard_test(model, dataloader, device, criterion):
    """
    Avalia o modelo em modo hard test (iterativo).
    Para output_size=1: a previsão é usada como último input do próximo passo.
    """
    model.eval()
    all_preds, all_targets = [], []
    total_loss = 0.0

    with torch.no_grad():
        for x, y in dataloader:  # batch_size = 1
            x, y = x.to(device), y.to(device)

            # histórico inicial
            history = x.clone()  # (1, input_size)

            # previsão do próximo passo
            forecast = model(history)  # saída do modelo
            next_pred = forecast[:, -1].unsqueeze(1)  # (1, 1)

            # se quiser continuar prevendo mais passos, usar o predicted como input
            history = torch.cat([history[:, 1:], next_pred], dim=1)

            preds = next_pred.squeeze(0)  # (1,)

            if criterion is not None:
                loss = criterion(preds.to(device), y[:1])
                total_loss += loss.item()

            all_preds.append(preds.cpu())
            all_targets.append(y[:1].cpu())

    all_preds = torch.cat(all_preds, dim=0)      # (n_samples,)
    all_targets = torch.cat(all_targets, dim=0)  # (n_samples,)

    avg_loss = total_loss / len(dataloader) if criterion is not None else None
    if avg_loss is not None:
        print(f"Average Loss - Hard Test: {avg_loss:.4f}")

    return all_preds, all_targets, avg_loss
    