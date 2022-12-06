# importing the module
import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np

filename = open('statistics.csv', 'r')

file = csv.DictReader(filename)
age = []
gender = []
iq = []
nationality = []

for col in file:
    age.append(int(col['age']))
    gender.append(col['gender'])
    iq.append(int(col['IQ']))
    nationality.append(col['nationality'])


def choose():
    column = input("What column do you wish to analyze? Please type one of the four: 'age','gender',"
                   "'iq' or 'nationality'.\n")
    column = column.lower()
    if column == "age":
        print("You can see the mean, the median, the standard deviation, the minimum, the maximum, the quartile, \n"
              "the covariance and the correlation coefficient between age and IQ, plus a representative  plot.\n")
        print("Mean: ", statistics.mean(age))
        print("Median: ", statistics.median(age))
        print("Standard deviation: ", statistics.stdev(age))
        print("Minimum: ", min(age))
        print("Maximum: ", max(age))
        print("Quantiles: ", statistics.quantiles(age))
        print("Covariance: ", statistics.covariance(age, iq))
        print("Correlation: ", statistics.correlation(age, iq))
    if column == "gender":
        print("You can see the correlation coefficient between age and IQ represented through a  plot."),
    if column == "iq":
        print("You can see the mean, the median, the standard deviation, the minimum, the maximum, the quartile, \n"
              "the covariance and the correlation coefficient between age and IQ represented through a  plot.")
        print("Mean: ", statistics.mean(iq))
        print("Median: ", statistics.median(iq))
        print("Standard deviation: ", statistics.stdev(iq))
        print("Minimum: ", min(iq))
        print("Maximum: ", max(iq))
        print("Quantiles: ", statistics.quantiles(iq))
        print("Covariance: ", statistics.covariance(age, iq))
        print("Correlation: ", statistics.correlation(age, iq))
    if column == "nationality":
        print("You can see the correlation coefficient between age and IQ represented through a  plot."),
    plt.scatter(age, iq)
    plt.plot(np.unique(age), np.poly1d(np.polyfit(age, iq, 1))(np.unique(age)), color='pink')
    plt.xlabel('age axis')
    plt.ylabel('iq axis')
    plt.show()


choose()
