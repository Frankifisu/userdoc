import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import csv

def help_n_exit(message):
    print(message)
    sys.exit(1)

#----------------------------------------------------------------------#
#                          MAIN                                        #
#----------------------------------------------------------------------#
if __name__ == '__main__':

    stress_yy = []
    strain_y = []

    with open('stress-strain-curve.csv','r') as csvfile:
        datapoints = csv.reader(csvfile, delimiter=' ')
        next(datapoints) # read the first line and skip it
        for row in datapoints:               
            stress_yy.append(float(row[4]))
            strain_y.append(float(row[1]))

    plt.plot(strain_y,stress_yy)
    plt.xlabel('Strain Y')
    plt.ylabel('Stress YY')
    plt.tight_layout()
    plt.savefig("stress-curve.png")
    print("Read: stress-strain-curve.csv, PNG: was saved to stress-curve.png")

