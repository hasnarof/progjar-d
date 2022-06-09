import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def post(self,params=[]):
        try:
            if len(params) < 2:
                return dict(status='OK', data="Parameter kurang dari 2.")
            
            filename = params[0]
            isifile = params[1]

            if os.path.exists(filename):
                return dict(status='ERROR',data="File sudah ada.")  
            
            if (filename == ''):
                return dict(status='ERROR',data="Filename tidak ditemukan.")

            isifile_encoded = base64.b64decode(isifile)
            fp = open(filename,'wb+')
            fp.write(isifile_encoded)
            fp.close()
            return dict(status='OK', data="File berhasil diupload.")
        except Exception as e:
            return dict(status='ERROR',data=str(e))



if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
