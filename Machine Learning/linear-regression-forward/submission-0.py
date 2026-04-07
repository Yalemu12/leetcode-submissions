import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # Compute Y_hat = X @ W (matrix multiplication)
        prediction = np.matmul(X, weights)
        return np.round(prediction, 5)
    
        # X is (n, 3), weights is (3,) -> result is (n,) predictions
        # Return np.round(result, 5)
        

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute MSE = mean((predictions - truth)^2)
        error = np.mean(np.square(model_prediction - ground_truth))
        # Use np.mean() and np.square()
        # Return round(result, 5)
        return round(error, 5)
        
