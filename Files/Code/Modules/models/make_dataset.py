import torch
from torch.utils.data import Dataset, DataLoader
import random

" Definindo o Dataset e DataLoader do PyTorch para uma série"
class SingleSeriesDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
    


" Definindo o Dataset e DataLoader do PyTorch para múltiplas séries"
class MultiSeriesDataset(Dataset):
    def __init__(self, series_list, input_window, horizon):
        self.samples = []
        for sid, s in enumerate(series_list):
            L = len(s)
            for i in range(L - input_window - horizon + 1):
                x = s[i:i+input_window]
                y = s[i+input_window : i+input_window+horizon]
                self.samples.append((x, y, sid))
        random.shuffle(self.samples)
    def __len__(self):
        return len(self.samples)
    def __getitem__(self, idx):
        x,y,sid = self.samples[idx]
        return torch.from_numpy(x).float(), torch.from_numpy(y).float(), torch.tensor(sid, dtype=torch.long)
