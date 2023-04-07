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
    mu = x.mean()
    sigma = x.std(ddof=1)
    z = norm.ppf(1 - alpha / 2)
    h = z * sigma / np.sqrt(n)
    left = mu - h
    right = mu + h
    freq_not_in_interval = sum((x < left) | (x > right)) / n
    avg_interval_length = h * 2
    return left, right, freq_not_in_interval, avg_interval_length
