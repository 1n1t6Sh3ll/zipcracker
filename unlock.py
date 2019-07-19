
import optparse
import zipfile
from threading import Thread
print("      ZiP                               FiLe                          UnLoCkEr")
print("")
print("                            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("                            MMMMMMMMMMMM        MMMMMMMMMMMM")
print("                            MMMMMMMMMM            MMMMMMMMMM")
print("                            MMMMMMMMM              MMMMMMMMM")
print("                            MMMMMMMM                MMMMMMMM")
print("                            MMMMMMM                 MMMMMMMM")
print("                            MMMMMMM                  MMMMMMM")
print("                            MMMMMMM                  MMMMMMM")
print("                            MMMMMMM    MMM    MMM    MMMMMMM")
print("                            MMMMMMM   MMMMM   MMMM   MMMMMMM")
print("                            MMMMMMM   MMMMM   MMMM   MMMMMMM")
print("                            MMMMMMMM   MMMM M MMMM  MMMMMMMM")
print("                            MMVKMMMM        M        MMMMMMM")
print("                            MMMMMMMM       MMM      MMMMMMMM")
print("                            MMMMMMMMMMMM   MMM  MMMMMMMMMMMM")
print("                            MMMMMMMMMM MM       M  MMMMMMMMM")
print("                            MMMMMMMMMM  M M M M M MMMMMMMMMM")
print("                            MMMM  MMMMM MMMMMMMMM MMMMM   MM")
print("                            MMM    MMMM M MMMMM M MMMM    MM")
print("                            MMM    MMMM   M M M  MMMMM   MMM")
print("                            MMMM    MMMM         MMM      MM")
print("                            MMM       MMMM     MMMM       MM")
print("                            MMM         MMMMMMMM      M  MMM")
print("                            MMMM  MMM      MMM      MMMMMMMM")
print("                            MMMMMMMMMMM  MM       MMMMMMM  M")
print("                            MMM  MMMMMMM       MMMMMMMMM   M")
print("                            MM    MMM        MM            M")
print("                            MM            MMMM            MM")
print("                            MMM        MMMMMMMMMMMMM       M")
print("                            MM      MMMMMMMMMMMMMMMMMMM    M")
print("                            MMM   MMMMMMMMMMMMMMMMMMMMMM   M")
print("                            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("                        BlAcK                              DeVil")
print("")
print("")
print("All About:")
print("This tool is used to crack zip files.")
print("For more information and syntax or other information to read,")
print("So please read 'README file' first...")
print("")
def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print "[+] Password Found: " + password + '\n'
    except:
        pass

def main():    
    parser = optparse.OptionParser("All About Tool"+\
                                "   -h <Help>   -f <ZipFile>   -w <WordList>")
    parser.add_option('-f', dest='zname', type='string',\
                      help='specify zip file')
    parser.add_option('-w', dest='dname', type='string',\
                      help='specify dictionary file')
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()

