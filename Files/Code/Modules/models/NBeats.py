
import torch
import torch.nn as nn

class NBeatsBlock(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=4):
        super().__init__()
        layers = []
        for _ in range(n_layers):
            layers.append(nn.Linear(input_size if _ == 0 else hidden_size, hidden_size))
            layers.append(nn.ReLU())
        self.fc = nn.Sequential(*layers)
        self.backcast = nn.Linear(hidden_size, input_size)
        self.forecast = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc(x)
        return self.backcast(x), self.forecast(x)

class NBeats(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_blocks=3):
        super().__init__()
        self.blocks = nn.ModuleList([
            NBeatsBlock(input_size, hidden_size, output_size)
            for _ in range(n_blocks)
        ])

    def forward(self, x):
        forecast = 0
        for block in self.blocks:
            backcast, block_forecast = block(x)
            x = x - backcast
            forecast += block_forecast
        return forecast


