
# importing required modules
import PyPDF2
import os
import glob

# Get the list of all files and directories
path = "BUFFER\\"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

class FileCombiner:
    def __init__(self) -> None:
        self.files_names=[]

    def get_filesname_from(self,folder,ext="pdf",prefix=None):
        ext=ext or ""
        prefix=prefix or ""
        self.files_list=glob.glob(folder+prefix+"*"+ext)
        return self.files_list

    def merger(self,fileslist=None,output="Merged.pdf"):
        merger=PyPDF2.PdfFileMerger()
        fileslist=fileslist or self.files_list
        for file in fileslist:
            merger.append(file)

        with open(output, 'wb') as f:
            merger.write(f)
        

if __name__ == "__main__":

    pdf_merger=FileCombiner()
    pdf_merger.get_filesname_from(path,ext="pdf",prefix="")
    pdf_merger.merger(output="ECU-s.pdf")
 