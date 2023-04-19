import os
import datetime
import subprocess
import shutil

#function: change content of a tex file
def change_content(file, my_dict, newfile):
  # Open the file in read mode
  with open(file, 'r', encoding="utf8") as f:
    # Read the contents of the file
    content = f.read()

  # Modify the content of the file
  for old_text in my_dict.keys():
    # Replace the old text with the new text if it is present in the "text" variable
    #if isinstance(my_dict[old_text], int):
     # my_dict[old_text] = str(my_dict[old_text])
    #elif isinstance(my_dict[old_text], str):
    #  my_dict[old_text] = my_dict[old_text]
    content = content.replace(old_text, str(my_dict[old_text]))

    # Open the file in write mode
    with open(newfile, 'w') as nf:
      # Write the modified content to the file
      nf.write(content)


# function: read the external latext file and execute to pdf
def latex_nestDicts_PDFs(file_latex, nest_dict, output_folder):
  for newfile in nest_dict.keys():
    newfile_tex=os.path.join(output_folder,newfile+".tex")
    change_content(file_latex,nest_dict[newfile],newfile_tex)  # modify content

    subprocess.run(["pdflatex", "-interaction=batchmode", newfile_tex],cwd=output_folder) # get file pdf and save in output_folder
    #subprocess.run(["pdflatex", newfile_tex],cwd=output_folder)  # get file pdf and save in output_folder

# Current Directory of original Latex file
current_path=os.getcwd()

#source directory/ FIXED
source_dir=os.path.join(current_path,'1-Report_Template')
filename='EngCalcPaper_CFC.tex'
# Get the full path of the file in the source directory
file_path = os.path.join(source_dir, filename)




#destination directory/ CAN BE MODIFIED
destination_dir=os.path.join(current_path,'2-Calculation_Output')
# Copy the file to the destination directory
file_tex_copy=shutil.copy(file_path, destination_dir)


# Create a temporary output_folder
output_folder = os.path.join(destination_dir, "output_folder")
os.makedirs(output_folder, mode=0o777, exist_ok=True)


#Input Dictionary: Content that we want to change in latex file
today=datetime.date.today()
# nest_Dict is to change
Dict1={'-VAR1-': "Hola Dict1", '-VAR2-': 999, '-PROJECTNAME-': 'CEBU 1234567', '-VARfig1-': 'fii_s003.pdf','-VARfig2-': 'fi_s004.pdf','-DATE-': str(today)}
Dict2={'-VAR1-': 20000000, '-VAR2-': 2999, '-PROJECTNAME-': 'Bilbao', '-VARfig1-': 'fii_s003.pdf','-VARfig2-': 'fi_s004.pdf','-DATE-': str(today)}
Dict3={'-VAR1-': "Hola Dict3", '-VAR2-': 999, '-PROJECTNAME-': 'PUENTE DE ATOCHA', '-VARfig1-': 'fii_s003.pdf','-VARfig2-': 'fi_s004.pdf','-DATE-': str(today)}
Dict4={'-VAR1-': 12345678, '-VAR2-': 2999, '-PROJECTNAME-': 'MALAGA', '-VARfig1-': 'fii_s003.pdf','-VARfig2-': 'fi_s004.pdf','-DATE-': str(today)}
nest_dict={'file1': Dict1, 'file2': Dict2,'file3': Dict3, 'file4': Dict4}

file_latex=os.path.join(destination_dir,file_tex_copy)



latex_nestDicts_PDFs(file_latex, nest_dict, output_folder)


# Copy all pdf files into the folder '3-Calculation_Report'

report_dir=os.path.join(current_path, '3-Calculation_Report')

PDF_folder_dir=os.path.join(report_dir,'PDF_folder')
os.makedirs(PDF_folder_dir, mode=0o777, exist_ok=True)

for f in os.listdir(output_folder):
  if f.endswith('.pdf'):
    # Get the full path of the file in the source folder
    source_file_path = os.path.join(output_folder, f)
    # Copy the file to the destination folder
    shutil.copy(source_file_path, PDF_folder_dir)


  # now we delete all files in output_folder/ OPTIONAL
  # Get the full path of the file
  file_path = os.path.join(output_folder, f)
  try:
    # Use the os.remove() function to delete the file
    os.remove(file_path)
  except Exception as e:
    print(f"Error deleting {file_path}: {e}")


# Use the shutil.rmtree() function to delete the folder and all its contents
#shutil.rmtree(output_folder)















