import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

# Sample data
# 'durations' contains the durations of each individual's time to event or censoring
# 'event_observed' indicates if the event was observed (1) or censored (0)
data = {
    'durations': [5, 6, 6g, 2.5, 4, 4, 4, 8, 8, 9, 10],
    'event_observed': [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a KaplanMeierFitter instance
kmf = KaplanMeierFitter()

# Fit the data to the KaplanMeierFitter
kmf.fit(df['durations'], event_observed=df['event_observed'])

# Plot the survival function
kmf.plot_survival_function()
plt.title('Kaplan-Meier Survival Curve')
plt.xlabel('Time')
plt.ylabel('Survival Probability')
plt.show()
