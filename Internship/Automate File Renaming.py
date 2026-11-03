import os

folder = "C:/Users/ACER/Desktop/AutocadPractice"

files = os.listdir(folder)

count = 1

for file in files:
    old_name = os.path.join(folder, file)

    if os.path.isfile(old_name):
        new_name = "file_" + str(count) + ".txt"
        new_name = os.path.join(folder, new_name)

        os.rename(old_name, new_name)

        print(file, "renamed to", "file_" + str(count) + ".txt")

        count = count + 1

print("All files renamed successfully.")
