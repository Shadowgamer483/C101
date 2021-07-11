
from os import access
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="fCSnMk2rVa8AAAAAAAAAAZfrCR_ahZLtVQ9lY0Iz_nVnA1n36lUfE6ck3MaXN89b"
    infotransfer=TransferData(access_token)
    file_from=input("enter file part to transfer")
    file_to=input("enter full path to upload to DropBox")
    infotransfer.upload_file(file_from,file_to)
    print("THE FILE HAS BEEN MOVED")
main()


























































