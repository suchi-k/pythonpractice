import os


def list_of_pdfs(folder_path):
    """ iterate through all files from the given folder_path """

    # Change the directory
    os.chdir(folder_path)

    list_of_pdfs = []
    for file in os.listdir():
        # Check whether file is in PDF format or not
        if file.endswith(".pdf"):
            file_path = f"{folder_path}\{file}"
            list_of_pdfs.append(file_path)

    # print([f"{folder_path}\{file}" for file in os.listdir() if file.endswith(".pdf")])
    return list_of_pdfs


if __name__ == '__main__':
    list_of_pdfs("folder path")
