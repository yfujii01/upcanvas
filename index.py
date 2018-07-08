import sys
import up
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
canvas_id = os.environ.get("canvas_id")
canvas_ps = os.environ.get("canvas_ps")


if __name__ == "__main__":
    argvs = sys.argv
    argc = len(argvs)

    if (argc != 2):
        print('Usage: # python %s uploadFile' % argvs[0])
        quit()

    # change full path
    f = argvs[1]
    file = os.path.abspath(f)
    # print(file)

    # upload file
    up.upload(file, canvas_id, canvas_ps)
