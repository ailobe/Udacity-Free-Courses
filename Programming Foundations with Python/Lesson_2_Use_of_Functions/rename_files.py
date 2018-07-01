import os


def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\miriam\PycharmProjects\Udacity\Programming Foundations with Python\Lesson_2_Use_of_Functions\prank")
    # print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is: " + saved_path)
    os.chdir(r"C:\Users\miriam\PycharmProjects\Udacity\Programming Foundations with Python\Lesson_2_Use_of_Functions\prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        new_name = ''.join([c for c in file_name if c not in "1234567890"])  # creates a new name without the numbers.
        print("Old Name - " + file_name)
        print("New Name - " + new_name)
        os.rename(file_name, new_name)
    os.chdir(saved_path)

rename_files()
