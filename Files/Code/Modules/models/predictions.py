""" Get Preditions """

import concurrent.futures

# from Files.Code.Modules.models.training import traininig_func, get_blind_prediction
# from Files.Code.Modules.models.sample import get_sample, create_feature_rescale
# from Files.Code.Modules.models.dataset import get_dataset
# from Files.Code.Modules.models.train_validation import get_train_validation
# from Files.Code.Modules.models.forecast import forecast_blind

from Modules.evaluation.train_validation import get_train_validation
from Modules.models.training import traininig_func
from Modules.models.sample import get_sample, create_feature_rescale
from Modules.models.dataset import get_dataset
from Modules.models.forecast import forecast_blind

def get_predictions(clean_data, prediction_col, hyperparams):
    sample = get_sample(clean_data, prediction_col, hyperparams['debug']['plot'])
    sample, feature = create_feature_rescale(sample)
    dataset_full, X, y = get_dataset(sample, feature, hyperparams)
    X_train, y_train, X_test, y_test, num_features = get_train_validation(dataset_full, X, y, hyperparams)
    model = traininig_func(X_train, y_train, num_features, hyperparams)
    blind_prediction = get_blind_prediction(model, X_train, hyperparams)
    return blind_prediction 

""" Get dataframe predictions """

def get_dataframe_predictions(clean_data, HYPERPARAMS):
    final_predictions = dict()
    patience = HYPERPARAMS['patience']
    for idx, col in enumerate(clean_data.T[:patience].T):
        print(f"Previsão para a coluna: {idx+1:0{len(str(patience))}d}/{patience}")       
        final_predictions[col] = get_predictions(clean_data, col, HYPERPARAMS)
    return final_predictions


def get_blind_prediction(model, X_train, hyperparams):
    """
    Previsão cega (quando split == 1)
    
    Previsão para envio para o hackathon das 4 primeiras semanas de janeiro/23. Utiliza todo o dataset como treino.
    """

    blind_horizon = hyperparams['blind_horizon']
    device = hyperparams['device']
    output_size = hyperparams['output_size']
    split = hyperparams['split']

    if split != 1.0:
        if hyperparams['debug']['verbose']:
            print("Previsão cega não realizada, pois split < 1.0")
        return

    blind_prediction = forecast_blind(model, X_train, blind_horizon, device, output_size)
    return blind_prediction

def predict_for_column(clean_data, col, HYPERPARAMS):
    # Envolve a função original para também retornar o nome da coluna
    # para re-montar os resultados corretamente.
    try:
        if HYPERPARAMS['debug']['verbose']:
            print(f"Previsão para a coluna: {col}")
        prediction = get_predictions(clean_data, col, HYPERPARAMS)
        return (col, prediction)
    except Exception as e:
        print(f"Error in column {col}: {e}")
        return (col, None)

def get_dataframe_predictions_parallel(clean_data, HYPERPARAMS, num_threads=16):
    final_predictions = {}
    cols = clean_data.columns.tolist()

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_threads) as executor:
        # Envia todas as tarefas para o pool de threads
        future_to_col = {executor.submit(predict_for_column, clean_data, col, HYPERPARAMS): col for col in cols[:HYPERPARAMS['patience']]}
        
        # Conforme os resultados são concluídos, os coleta
        for future in concurrent.futures.as_completed(future_to_col):
            col, prediction = future.result()
            final_predictions[col] = prediction

    return final_predictions