import os
import socket
from collections import Counter
import string

# Setting path variables
base_dir = '/home/data'
output_dir = '/home/output'

# Accessing all text files in the given directory
# txt_files = [f for f in os.listdir(base_dir) if f.endswith('.txt')]
files = os.listdir("/home/data")

# Locating target files
if_file_path = os.path.join(base_dir, 'IF.txt')
limerick_file_path = os.path.join(base_dir, 'Limerick.txt')
res_file_path = os.path.join(output_dir, 'result.txt')

# Function to count words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        return len(file.read().split())

# Counting words in IF.txt and Limerick-1.txt
wc_if = count_words_in_file(if_file_path)
wc_lim = count_words_in_file(limerick_file_path)

# Computing top 3 frequent words in IF.txt
with open(if_file_path, 'r') as file:
    words = file.read().split()
    words = [word.strip(string.punctuation).capitalize() for word in words]
    top_words = Counter(words).most_common(3)

# Getting the host machine's IP address
IP_address = socket.gethostbyname(socket.gethostname())

# Writing output to result.txt
with open(res_file_path, 'w') as res_file:
    res_file.write("List of all the text files in the directory:\n")
    res_file.writelines(f"{file}\n" for file in files)
    res_file.write(f"No of words in Limerick.txt: {wc_lim}\n")
    res_file.write(f"No of words in IF.txt: {wc_if}\n")
    res_file.write(f"Total of words: {wc_if + wc_lim}\n")
    res_file.write("Top 3 words with their counts in IF.txt:\n")
    res_file.writelines(f"{word} -> count: {count}\n" for word, count in top_words)
    res_file.write(f"IP address of the machine: {IP_address}\n")

# Displaying output from result.txt file
with open(res_file_path, 'r') as res_file:
    print(res_file.read())
