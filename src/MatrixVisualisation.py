import numpy as np
import argparse
import os
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument("--input", default=".", help="Input folder with data to plot")
parser.add_argument("--output", default="./viz", help="Output folder for images")

args = parser.parse_args()

if __name__ == "__main__":
    fig, ax = plt.subplots()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    for file in [file for file in os.listdir(args.input) if file.endswith(".npy")]:
        matrix = np.load(os.path.join(args.input, file))
        matrix = np.mean(matrix, axis=0)
        ax.matshow(matrix, cmap=plt.cm.Blues)
        for i in range(8):
            for j in range(8):
                c = matrix[j,i]
                ax.text(i, j, str("%.2f" % c), va='center', ha='center')
        plt.savefig(os.path.join(args.output, f"img_{file[:5]}.png"))