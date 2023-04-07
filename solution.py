import pandas as pd
import numpy as np

from scipy.stats import chi2, norm


chat_id = 294776608 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    q1 = chi2.ppf(1 - alpha / 2, 2*n)
    q2 = chi2.ppf(alpha / 2, 2*n)
    sigma_hat = np.sqrt(np.mean(x**2) / 2)
    b1 = np.sqrt(n/2) * sigma_hat / np.sqrt(q1)
    b2 = np.sqrt(n/2) * sigma_hat / np.sqrt(q2)
    return b1, b2
