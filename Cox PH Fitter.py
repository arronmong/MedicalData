import pandas as pd
from lifelines import CoxPHFitter
import matplotlib.pyplot as plt
from lifelines.datasets import load_rossi



rossi = load_rossi()

cph = CoxPHFitter()
cph.fit(rossi, duration_col='week', event_col='arrest')


cph.plot_survival_function()
plt.title('Kaplan-Meier Survival Curve')
plt.xlabel('Time')
plt.ylabel('Survival Probability')
plt.show()

