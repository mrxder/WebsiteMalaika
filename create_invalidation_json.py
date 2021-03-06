from os import listdir
from os.path import isfile, isdir, join
from urllib.parse import quote
from datetime import datetime
import sys
import random


def recursive_file_lister(root_path, actual_path, all_files):

    full_path_of_dir = join(root_path, actual_path)

    content_of_dir = listdir(full_path_of_dir)

    for i in content_of_dir:

        full_path_of_file = (join(root_path, actual_path, i))
        relative_path_of_file = (join(actual_path, i))

        if isfile(full_path_of_file):
            aws_path_for_file = quote("/"+relative_path_of_file)
            all_files.append(aws_path_for_file)
        elif isdir(full_path_of_file):
            recursive_file_lister(root_path, relative_path_of_file, all_files)


def create_json_for_invalidation(all_files, path_prefix, refernece):

    print("{")
    print(" \"Paths\": {")
    print("     \"Quantity\":", str(len(all_files))+",")
    print("     \"Items\": [")

    for i in range(len(all_files)):
        if(i < (len(all_files)-1)):
            print("         \""+path_prefix+all_files[i]+"\",")
        else:
            print("         \""+path_prefix+all_files[i]+"\"")
    print("     ]")
    print("   },")
    print("  \"CallerReference\": \""+refernece+"\"")
    print("}")


if len(sys.argv) < 2:
    print("Usage")
    print("create_invalidation_json.py dir path_prefix")
else:
    all_files = ["/"]
    recursive_file_lister(sys.argv[1], "", all_files)

    path_prefix = ""
    if len(sys.argv) >= 3:
        path_prefix = sys.argv[2]

    create_json_for_invalidation(all_files, path_prefix, "auto_deploy_script_"+str(
        datetime.now().strftime("%I_%M%p_%B_%d_%Y_"))+str(random.randint(1, 999999999999)))
