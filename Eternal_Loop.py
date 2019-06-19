import os
import zipfile

zipname = '37366.zip'	# First zip filename
autoclear = True	# Autoremove old files

# Extract function
def extractFile(zipname):
    try:
        file = zipfile.ZipFile(zipname)
        filename =  file.infolist()[0].filename
        password = filename.split(".")[0]
        file.extractall(pwd = password)
        print "[*] Extracting " + zipname + " with password " + password
        if autoclear:
            os.remove(zipname)
        extractFile(filename)
    except:
        print "[!] End of loop or scrip failed"
        print "[*] Last file was " + zipname + " try other stuff on it"

# Main function
def main():
    print "[*] Starting unzipping loop from file " + zipname
    extractFile(zipname)

if __name__ == '__main__':
    main()
