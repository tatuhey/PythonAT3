# Raihan Khalil Abdillah
# AT3.1 Question 1
# File I/O and Pseudo Code

sentence1 = "Python has been an important part of Google since the beginning and remains so as the system grows and evolves."
sentence2 = "\"Today dozens of Google engineers use Python, and we're looking for more people with skills in this language.\" said Peter Norvig, director of search quality at Google, Inc."

# concatenate two strings into a variable
output_string = sentence1 + " " + sentence2

# write output_string into python.txt
file = open("python.txt", "w")
file.writelines(output_string)
file.close()

# write python.txt into input_string
file = open("python.txt", "r")
input_string = file.read()
file.close()

print(input_string)
