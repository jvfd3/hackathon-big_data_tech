""" Get Preditions """

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
    sample = get_sample(clean_data, prediction_col)
    sample, feature = create_feature_rescale(sample)
    dataset_full, X, y = get_dataset(sample, feature, hyperparams)
    X_train, y_train, X_test, y_test, num_features = get_train_validation(dataset_full, X, y, hyperparams)
    model = traininig_func(X_train, y_train, num_features, hyperparams)
    blind_prediction = get_blind_prediction(model, X_train, hyperparams)
    return blind_prediction 

""" Get dataframe predictions """

def get_dataframe_predictions(clean_data, HYPERPARAMS):
    final_predictions = dict()

    # for col in clean_data[:5]:
    for col in clean_data.T[:5].T:
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
        print("Previsão cega não realizada, pois split < 1.0")
        return

    blind_prediction = forecast_blind(model, X_train, blind_horizon, device, output_size)
    return blind_prediction