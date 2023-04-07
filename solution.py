import pandas as pd
import numpy as np

from scipy.stats import chi2, norm


chat_id = 294776608 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x_mean = np.mean(x)
    x_var = np.var(x, ddof=1)
    
    mse = np.sqrt(x_var)
    
    alpha = 1 - p
    left = np.sqrt(x_var / np.percentile(norm.cdf(alpha / 2), 1)) - x_mean
    right = np.sqrt(x_var / np.percentile(norm.cdf(1 - alpha / 2), 1)) - x_mean
    
    return left, right
