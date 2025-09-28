import os,random,string

while True:
    try:
        folder_name = ''.join(random.choices(string.ascii_lowercase,k=10))
        folder_path = os.path.join("/sdcard/",folder_name)
        os.makedirs(folder_path,exist_ok=True)
    except:
        pass
