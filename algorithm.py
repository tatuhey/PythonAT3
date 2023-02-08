# Raihan Khalil Abdillah
# AT3.2 Question 1
# Algorithm Development

# set the tuple
dataTuple = ("Windows 10", "Linux Mint", "Mac OS 11", "Android Oreo", "Android Pie", "Android 11", "iOS 14")

# using input() function
searchInput = input("Search: ")

# linear search method
def linearSearch(searchInput) :
    for i in dataTuple:
        if i == searchInput:
            print(dataTuple.index(searchInput))

# calling the linear search method
linearSearch(searchInput)

# demonstrating type() python library function
print("The type of dataTuple is:", type(dataTuple))