
import numpy as np
import pandas as pd

players = ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Sachin Tendulkar", "Yuvraj Singh"]
runs = np.array([13848, 11168, 10773, 18426, 8701])

average = np.mean(runs)
highest = np.max(runs)
lowest = np.min(runs)

df = pd.DataFrame({
    "Player": players,
    "Runs": runs
})

print("Cricket Player Statistics")
print(df)

print("\nAverage Runs:", average)
print("Highest Runs:", highest)
print("Lowest Runs:", lowest)

print("\nPlayers scoring more than 5000 runs:")
print(df[df["Runs"] > 5000])
