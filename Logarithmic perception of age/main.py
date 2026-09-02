import math
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

dob = input("Date of birth (dd-mm-yyyy): ")
dob = datetime.strptime(dob, "%d-%m-%Y")

r = (datetime.now() - dob).days / 365.25
r0 = 1

s = math.log(r / r0)

R = np.linspace(r0, 100, 500)
S = np.log(R / r0)

plt.figure(figsize=(8, 5))
plt.plot(R, R, label="Objective age")
plt.plot(R, S, label="Subjective age")
plt.scatter([r], [r], color="black", zorder=2)
plt.scatter([r], [s], color="black", zorder=2)
plt.annotate(f"Age: {r:.1f}", (r, r))
plt.annotate(f"Perception: {s:.2f}", (r, s))

plt.xlim(0, 100)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Current age (R):", r)
print("Subjective age (S):", s)
