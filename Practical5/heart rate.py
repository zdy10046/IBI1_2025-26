import matplotlib.pyplot as plt
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients

print(f"\nThere are {num_patients} patients and the mean heart rate is {mean_hr:.2f} bpm.")

# Categorise heart rates
low = 0
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1
#Identify if the heart rate is low, normal or high and count the number of patients in each category
print(f"Low heart rate patients: {low}")
print(f"Normal heart rate patients: {normal}")
print(f"High heart rate patients: {high}")

# Find largest category
categories = {"Low": low, "Normal": normal, "High": high}
largest_category = max(categories, key=categories.get)

print(f"The largest category is: {largest_category}")

# Pie chart
labels = categories.keys()
sizes = categories.values()

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Heart Rate Category Distribution")
plt.show()

