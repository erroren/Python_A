import ftplib


def ftpconnect(host, username, passwd):
    ftp = ftplib.FTP(host, username, passwd)
    return ftp


def upload(ftp, localfile, remotefile):
    BUFFERSIZE = 1024
    file = open(localfile, "rb")
    ftp.storbinary("STOR " + remotefile, file, BUFFERSIZE)
    file.close()


def download(ftp, localfile, remotefile):
    BUFFERSIZE = 1024
    file = open(localfile, "wb")
    ftp.retrbinary("RETR " + remotefile, file.write, BUFFERSIZE)
    file.close()


if __name__ == '__main__':
    ftp = ftpconnect("192.168.12.155", "test", "123")
    # download(ftp, "f:/readme.txt", "readme.txt")
    upload(ftp, "C:/Users/Administrator/Desktop/b.png", "b.png")
    ftp.quit()
