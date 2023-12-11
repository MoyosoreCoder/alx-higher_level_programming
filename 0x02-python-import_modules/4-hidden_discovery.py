#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    x = dir(hidden_4)
    length = len(x)
    for i in range(0, length):
        if x[i][0:2] != "__":
            print(x[i])
