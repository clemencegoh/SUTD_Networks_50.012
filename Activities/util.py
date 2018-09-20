import os


def documentInFile(filename, title, content):
    if os.path.exists(filename):
        write_mode = 'a'
    else:
        write_mode = 'w'
    
    f = open(filename, write_mode)
    f.write(title + ": " + str(content) + "\n\n")
    f.close()
