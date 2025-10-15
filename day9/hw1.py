# Downloading file from FTP using threading Events

from ftplib import FTP
import threading

event = threading.Event()

def download_file(file_name: str, ftype="txt"):
    print(f"Waiting for downloading: {file_name}")
    event.wait()
    
    ftp = FTP()
    ftp.connect("test.rebex.net")
    ftp.login("demo","password")
    ftp.cwd("pub/example")
    
    try:
        if ftype == "txt":
            with open(file_name, "w") as f:
                        ftp.retrlines(f"RETR {file_name}", f.write)
        else: 
            with open(file_name, "wb") as f:
                    ftp.retrbinary(f"RETR {file_name}", f.write)
        print(f"[{file_name}] Download complete.")
    except:
        print(f"Failed to download file: {file_name}")
    ftp.quit()
    
if __name__ == "__main__":
    ftp = FTP()
    ftp.connect("test.rebex.net")
    ftp.login("demo","password")
    ftp.cwd("pub/example")
    print(ftp.dir())
    print("In main: Connection succesfull to ftp server : test.rebex.net")
    ftp.quit()
    
    event.set()

    f_t1 = threading.Thread(target=download_file, args=("readme.txt", "txt"))
    f_t1.start()
    
    f_t2 = threading.Thread(target=download_file, args=("winceclient.png", "png"))
    f_t2.start()
    
    f_t1.join()
    f_t2.join()
    
    print("In main: Done donwloading files..")