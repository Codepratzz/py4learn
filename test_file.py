import argparse
import os
import time

data = [1, 2, 3, 4, 5, 6]
parser = argparse.ArgumentParser()
parser.add_argument('--output_dir', help='Path to save the outputted files in', default='network/')
parser.add_argument('--output_dir1', help='Path to save the outputted files in', default='output/')

args = parser.parse_args()

output_dir = args.output_dir
output_dir1 = args.output_dir1
print(f"Writing data to file...")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(output_dir1):
    os.makedirs(output_dir1)
old = data
print(old)
with open(f"{output_dir}/{time.strftime('%y.%d.%m')}_country_codevideos.txt", "a+", encoding='utf-8') as file:
    for row in old, data:
        file.write(f"{row}\n")
    new = old + data
    print(new)
    # for row in new:
    # file.write(f"new data: {row}\n")

"""
with open(f"{output_dir1}/{time.strftime('%y.%d.%m')}_country_codevideos.csv", "a+", encoding='utf-8') as file:
    for row in data:
        file.write(f"{row}\n")
    for row in range(len(data)):
        file.write(f"{row}\n")
"""
