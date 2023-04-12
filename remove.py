import os
import shutil

list_dir = ['backup-82118','odoo-db','odoo-file','spi-backup']
for dirr_main in  list_dir:
    a = list(os.listdir(os.getcwd()+'/'+dirr_main))
    #print(a)
    if len(a)>30:
        a.sort()
        b = len(a) - 30
        print(b)
        for i in range(b):
            print(i)
            dirr = os.getcwd()+'/'+dirr_main+'/'+a[i]
            print(dirr)
            if os.path.exists(dirr):
                #os.removedirs(dirr)
                shutil.rmtree(dirr , ignore_errors=True)
