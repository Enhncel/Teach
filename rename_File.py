import os
def rename_files():
    file_list = os.listdir(r"F:\1\123accd")
    saved_path = os.getcwd()
    print("work:"+saved_path)
    os.chdir(r"F:\1\123accd")
    print(file_list)
    for file_name in file_list:
        print ("old:"+ file_name)
        print ("new:"+ file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()
