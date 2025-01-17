import pandas as pd
import numpy as np

from scipy.stats import chi2, norm


chat_id = 294776608 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t_val = t.ppf(1 - alpha / 2, n - 1) 
    left = mean - t_val * std / np.sqrt(n)
    right = mean + t_val * std / np.sqrt(n)
    return (left, right)
