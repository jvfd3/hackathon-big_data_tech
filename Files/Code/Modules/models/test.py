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
    

def hard_test1(model, dataloader, device, criterion,input_size, n_features):
    """
    Avalia o modelo em um dataset de validação, sem teacher forcing (usa sempre ground truth como entrada).
    """
    model.eval()
    total_loss = 0
    all_preds, all_targets = [], []

    with torch.no_grad():
        for x, y in dataloader:
            x, y = x.to(device), y.to(device)
            
            idx_last = (input_size - 1) * n_features
            x[:, idx_last] = forecast[:, -1]  # atualiza a feature principal do último timestep

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