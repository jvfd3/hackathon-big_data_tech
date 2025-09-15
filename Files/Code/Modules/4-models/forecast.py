
# Coloca o modelo em modo avaliação: desativa dropout, usa estatísticas fixas do batchnorm,
# e sinaliza que estamos em inferência (comportamento diferente do modo treino).
model.eval()

# Abre um contexto que desativa o cálculo de gradientes. Isso reduz uso de memória e torna
# a inferência mais rápida — não queremos gradientes na hora de prever.
with torch.no_grad():
    # Extrai os últimos `input_size` pontos da série original (vetor 1D).
    # Ex.: series[-input_size:] retorna um array com shape (input_size,).
    x_test = torch.tensor(series[-input_size:], dtype=torch.float32)
    
    # Adiciona a dimensão de batch no início: transforma shape (input_size,) em (1, input_size).
    # Modelos PyTorch esperam geralmente (batch_size, features).
    x_test = x_test.unsqueeze(0)
    
    # Move o tensor para o mesmo device (CPU ou GPU) onde o modelo está alocado.
    # Sem isso, se o modelo estiver na GPU e o tensor na CPU, ocorrerá erro.
    x_test = x_test.to(device)
    
    # Forward pass: passa o input pelo modelo para obter a previsão (tensor no mesmo device).
    pred_tensor = model(x_test)
    
    # Move a previsão para a CPU — necessário antes de converter para NumPy.
    pred_cpu = pred_tensor.cpu()
    
    # Converte o tensor em um array NumPy para facilidade de manipulação/visualização.
    pred_np = pred_cpu.numpy()
    
    # Achata o array: por exemplo de shape (1, output_size) para (output_size,).
    # Facilita imprimir/usar os valores previstos.
    pred = pred_np.flatten()
    
    # Imprime a previsão final (vetor com output_size valores previstos).
    print("Previsão:", pred)