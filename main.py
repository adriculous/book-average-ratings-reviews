import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

sns.scatterplot(x="average_rating", y="ratings_count", size="ratings_count", hue="ratings_count", sizes=(20, 180), data=data)

plt.xlabel("Average Book Ratings")
plt.ylabel("Total Number of Ratings")
plt.title("Book Average Ratings and Total of Ratings")
plt.savefig("bookratings_scatter.png")