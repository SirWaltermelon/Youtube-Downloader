from tkinter import Tk
from tkinter.filedialog import askdirectory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)
  #### Attemot to use Beautiful Soup to grab input value from the input id ####
  
   # with open("templates/index.html") as fp:
    #   soup = BeautifulSoup(fp, "html.parser")
    # inputs = soup.find(id = "yturl")
    # print(inputs)




#### Prompted simple dialog boxes to enter the link and what user wanted to name it ####

    # user_inp = inputs
    
    # simpledialog.askstring(title = 'test', 
    #                                     prompt = "Enter YT Link:")

    # user_inp2 = simpledialog.askstring(title = 'File Name',
    #                                     prompt = "Enter File Name") 



########## Tried to allow user to rename file after it was downloaded #############################
       # try:
    #     print("Changing Name")
    #     base, ext = os.path.splitext(out_file)
    #     new_file = user_inp2 + '.mp4'
    #     os.rename(out_file, new_file)
        
    # except:
    #     print("Error changing file name")
    # print("Name Changed")