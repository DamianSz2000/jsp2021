import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Python", "C", "Java", "C++", "C#", "Visual Basic", "JavaScript", "Assembly Language", "SQL", "SWIFT"])
y = np.array([12.9, 11.8, 10.12, 7.73, 6.4, 5.4, 2.3, 2.25, 1.79, 1.76])


plt.bar(x,y)
plt.title("Top 10 najpopularniejszych języków programowania 2021.")
plt.xlabel("Język programowania")
plt.ylabel("Popularność w %")
plt.show()