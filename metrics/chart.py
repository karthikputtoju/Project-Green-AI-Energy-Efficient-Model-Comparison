import pandas as pd
import matplotlib.pyplot as plt

# Constants for metric keys
ENERGY_CONSUMPTION = "Energy consumption (kWh)"
CO2_EMISSIONS_KG = "CO₂ emissions (kg)"
CO2_EMISSIONS_G = "CO₂ emissions (g)"
INFERENCE_TIME_S = "Inference time (s)"
OUTPUT_QUALITY_CHARS = "Output quality (chars)"
TIME_RATING = "Time Rating"
OUTPUT_RATING = "Output Rating"
CO2_RATING = "CO₂ Rating"

# Your metrics JSON
metrics_json = {
    "distilgpt2": {
        INFERENCE_TIME_S: 7.923,
        OUTPUT_QUALITY_CHARS: 1214
    },
    "gpt2": {
        CO2_EMISSIONS_KG: 5.7e-05,
        INFERENCE_TIME_S: 8.242,
        OUTPUT_QUALITY_CHARS: 1280
    }
}

# Convert to DataFrame
df = pd.DataFrame(metrics_json).T.reset_index().rename(columns={"index": "Model"})
df[CO2_EMISSIONS_G] = df[CO2_EMISSIONS_KG] * 1000
df = df.drop(columns=[CO2_EMISSIONS_KG])
df = df.drop(columns=[CO2_EMISSIONS_KG])
df = df.drop(columns=[CO2_EMISSIONS_KG])

# Rating function
def rate_from_values(series, better="lower"):
    if better == "lower":
        return ["Good" if v == series.min() else "Bad" if v == series.max() else "Better" for v in series]
# Apply ratings
df[TIME_RATING] = rate_from_values(df[INFERENCE_TIME_S], better="lower")
df[OUTPUT_RATING] = rate_from_values(df[OUTPUT_QUALITY_CHARS], better="higher")
df[CO2_RATING] = rate_from_values(df[CO2_EMISSIONS_G], better="lower")
df[CO2_RATING] = rate_from_values(df[CO2_EMISSIONS_G], better="lower")
df["CO₂ Rating"] = rate_from_values(df[CO2_EMISSIONS_G], better="lower")
df[OUTPUT_RATING] = rate_from_values(df[OUTPUT_QUALITY_CHARS], better="higher")
df[OUTPUT_RATING] = rate_from_values(df[OUTPUT_QUALITY_CHARS], better="higher")

# Color map
color_map = {"Good": "green", "Better": "orange", "Bad": "red"}

# Create subplots for the 2x2 grid of charts
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Energy consumption
axes[0, 0].bar(df["Model"], df[ENERGY_CONSUMPTION], 
               color=[color_map[r] for r in df["Energy Rating"]])
axes[0, 0].set_title("Energy Consumption (kWh)")
for i, v in enumerate(df[ENERGY_CONSUMPTION]):
    axes[0, 0].text(i, v, f"{v:.6f}", ha='center', va='bottom')
axes[0, 0].set_title("Energy Consumption (kWh)")
for i, v in enumerate(df[ENERGY_CONSUMPTION]):
    axes[0, 0].text(i, v, f"{v:.6f}", ha='center', va='bottom')
axes[0, 1].bar(df["Model"], df[CO2_EMISSIONS_G], 
               color=[color_map[r] for r in df[CO2_RATING]])
axes[0, 1].set_title("CO₂ Emissions (grams)")
for i, v in enumerate(df[CO2_EMISSIONS_G]):
    axes[0, 1].text(i, v, f"{v:.3f}", ha='center', va='bottom')
    axes[0, 1].text(i, v, f"{v:.3f}", ha='center', va='bottom')
axes[1, 0].bar(df["Model"], df[INFERENCE_TIME_S], 
               color=[color_map[r] for r in df[TIME_RATING]])
axes[1, 0].set_title("Inference Time (seconds)")
for i, v in enumerate(df[INFERENCE_TIME_S]):
    axes[1, 0].text(i, v, f"{v:.3f}", ha='center', va='bottom')
    axes[1, 0].text(i, v, f"{v:.3f}", ha='center', va='bottom')
    axes[1, 0].text(i, v, f"{v:.3f}", ha='center', va='bottom')
axes[1, 1].bar(df["Model"], df[OUTPUT_QUALITY_CHARS], 
               color=[color_map[r] for r in df[OUTPUT_RATING]])
axes[1, 1].set_title("Output Quality (chars)")
for i, v in enumerate(df[OUTPUT_QUALITY_CHARS]):
    axes[1, 1].text(i, v, f"{v}", ha='center', va='bottom')
    axes[1, 1].text(i, v, f"{v}", ha='center', va='bottom')
    axes[1, 1].text(i, v, f"{v}", ha='center', va='bottom')

plt.tight_layout()
plt.show()
