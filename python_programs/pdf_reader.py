import pandas as pd
import PyPDF2
from read_files_from_folder import list_of_pdfs


def read_aadhaar(pdf_file):
    """ Function to read text from Aadhaar pdf document """
    with open(pdf_file, 'rb') as pdf_file_obj:
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        page_obj = pdf_reader.pages[0]
        pdf_text = page_obj.extract_text().split('\n')

    # reading the required Text to a dictionary
    output = {"name": ""}
    for i in pdf_text:
        j = i.replace(" ", "")
        if j.isalpha() and j != 'To' and output['name'] == "":
            output['name'] = i
        if j.isnumeric() and len(j) == 12:
            output['aadhaar'] = i
        elif j.isnumeric():
            output['VID'] = i

    return output


# Driving code to read all PDF Files from given folder_path
if __name__ == "__main__":
    out = []
    for pdf_file in list_of_pdfs("Folder path"):
        out.append(read_aadhaar(pdf_file))

    # writing output to CSV File
    columns = {"name": 'Name', "VID": "VID", "aadhaar": "Aadhaar Number"}
    df = pd.DataFrame(out)
    df.rename(columns=columns, inplace=True)

    df.to_csv('D:\\family_aadhaar_details.csv', index=False)


##------------------Sample code snippet to read PDF-------------------------------------##
# creating a pdf file object
# pdf_file_obj = open(pdf_file, 'rb')

# creating a pdf reader object
# pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

# printing number of pages in pdf file
# print("Num of Pages: ", len(pdf_reader.pages))

# creating a page object
# page_obj = pdf_reader.pages[0]

# extracting text from page
# pdf_text = page_obj.extract_text().split('\n')
# print(pdf_text)

# closing the pdf file object
# pdf_file_obj.close()
##------------------Sample code snippet to read PDF-------------------------------------##
