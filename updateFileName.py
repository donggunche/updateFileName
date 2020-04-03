import os

path='G:\理财五本\财大课件\财大\论文资料\EndNote\期刊'
print(path)
fileList=os.listdir(path)
for file in fileList:
    if 'download' not in file:
        oldname=file
        print(oldname)
        newname='download-'+file
        os.rename(os.path.join(path,oldname),os.path.join(path,newname))
