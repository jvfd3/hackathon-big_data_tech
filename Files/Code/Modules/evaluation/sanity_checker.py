
""" Sanity check do modelo treinado """

import matplotlib.pyplot as plt
import torch

def sanity_check_plot(model, dataloader, device, output_size):
    """
    Plota previsões vs ground truth no período de treino
    """
    model.eval()
    all_preds, all_targets = [], []

    with torch.no_grad():
        for x, y in dataloader:
            x, y = x.to(device), y.to(device)

            preds = model(x)
            
            # Se seu modelo retorna (batch, output_size)
            preds = preds.cpu().numpy().flatten()
            y = y.cpu().numpy().flatten()

            all_preds.extend(preds)
            all_targets.extend(y)

    # Plot
    plt.figure(figsize=(12, 5))
    plt.plot(all_targets, label="Ground truth", linewidth=2)
    plt.plot(all_preds, label="Previsões", linewidth=2, alpha=0.7)
    plt.title("Sanity check - Previsões vs Ground Truth (treino)")
    plt.legend()
    plt.show()