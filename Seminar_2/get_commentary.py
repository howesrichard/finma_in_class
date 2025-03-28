# Read commentary from a text file
def read_commentary(file_path):
    commentary = ""
    with open(file_path, "r") as file:
        commentary = file.read()
    return commentary