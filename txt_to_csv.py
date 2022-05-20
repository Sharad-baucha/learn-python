import pandas as pd

print("Hello")
textdatafile = pd.read_txt("example.txt")

textdatafile.to_csv("conv_example.csv", index = None)
