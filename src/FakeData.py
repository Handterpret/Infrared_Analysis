import numpy as np
import datetime

if __name__ == "__main__":
    for i in range(10):
        arr = np.random.rand(16,8,8)
        np.save(f"data{i}-{str(datetime.datetime.now().timestamp())}.npy", arr)
