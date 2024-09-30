import re

# 1. Read the text file
with open('C:\\Users\\pavan\\PycharmProjects\\SuperStore-Connection-MySQL\\float-file.txt', 'r') as file:
    lines = file.readlines()

# 2. Clean each line to remove 'np.float64()'
cleaned_lines = []
for line in lines:
    # regex to find and replace 'np.float64(123.45)' with '123.45'
    cleaned_line = re.sub(r'np\.float64\(([\d\.]+)\)', r'\1', line)
    cleaned_lines.append(cleaned_line.strip() + ',')

# 3. Write the cleaned lines back to the text file
with open('Sales.txt', 'w') as file:
    for line in cleaned_lines:
        file.write(line + '\n')

# Optional: print the cleaned content
for line in cleaned_lines:
    print(line)
