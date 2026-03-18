#Population in 2020 and 2024 (in millions)
population_2020 = {"UK": 66.7, "China": 1426, "Italy": 59.4, "Brazil": 208.6, "USA": 331.6}
population_2024 = {"UK": 69.2, "China": 1410, "Italy": 58.9, "Brazil": 212.0, "USA": 340.1}
percent_change = {}
#Calculate percentage change in population for each country
for country in population_2020:
    change = ((population_2024[country] - population_2020[country]) /
              population_2020[country]) * 100
    percent_change[country] = change
print("\nPopulation percentage changes:")
for country, change in percent_change.items():
    print(f"{country}: {change:.2f}%")
sorted_changes = sorted(percent_change.items(), key=lambda x: x[1], reverse=True)
print("\nPopulation changes (largest increase → largest decrease):")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")
#Identify largest increase and decrease
largest_increase = sorted_changes[0]#Largest increase: UK
largest_decrease = sorted_changes[-1]#Largest decrease: China
print(f"\nLargest increase: {largest_increase[0]}")
print(f"Largest decrease: {largest_decrease[0]}")
#Generate bar chart
import matplotlib.pyplot as plt
countries = list(percent_change.keys())
changes = list(percent_change.values())
colors = ['#2ECC71' if c > 0 
          else '#E74C3C' for c in changes]#Green for increase, red for decrease
plt.figure()
plt.bar(countries, changes, color=colors)
plt.xlabel("Country")
plt.ylabel("Population Change (%)")
plt.title("Population Change (2020-2024)")
plt.axhline(0, color='grey', linewidth=0.8)
plt.show()
