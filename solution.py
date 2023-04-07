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
    x_mean = np.mean(x)
    x_var = np.var(x, ddof=1)
    chi2_l = chi2.ppf(alpha / 2, df=n - 1)
    chi2_r = chi2.ppf(1 - alpha / 2, df=n - 1)
    s_l = np.sqrt((n - 1) * x_var / chi2_r)
    s_r = np.sqrt((n - 1) * x_var / chi2_l)
    interval_len = s_l + s_r
    return x_mean - s_l, x_mean + s_r, interval_len
