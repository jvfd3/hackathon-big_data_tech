import torch
import torch.nn as nn

# Definição da WMAPE Loss (Weighted Mean Absolute Percentage Error)
class WMAPELoss(nn.Module):
    def __init__(self, epsilon=1e-8):
        super(WMAPELoss, self).__init__()
        self.epsilon = epsilon  # evitar divisão por zero

    def forward(self, y_pred, y_true):
        # Erro absoluto
        abs_error = torch.abs(y_true - y_pred)
        # Soma dos valores reais (evita divisão por zero)
        denom = torch.sum(torch.abs(y_true)) + self.epsilon
        # WMAPE
        loss = torch.sum(abs_error) / denom
        return loss