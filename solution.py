import pandas as pd
import numpy as np

from scipy.stats import chi2, norm


chat_id = 294776608 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    chi_sq = norm.ppf(1 - alpha / 2)**2
    left = np.sqrt((len(x) - 1) * np.var(x)) / np.sqrt(chi_sq)
    right = np.sqrt((len(x) - 1) * np.var(x)) / np.sqrt(chi_sq)
    return loc - right, loc + left
