from os import listdir
from os.path import isfile, isdir, join
import sys

def recursive_file_lister(root_path, actual_path, all_files):

    full_path_of_dir = join(root_path, actual_path)

    content_of_dir = listdir(full_path_of_dir)

    for i in content_of_dir:

        full_path_of_file = (join(root_path, actual_path, i))
        relative_path_of_file = (join(actual_path, i))

        if isfile(full_path_of_file):
            aws_path_for_file = "/"+relative_path_of_file.replace(" ", "\ ")
            all_files.append(aws_path_for_file)
        elif isdir(full_path_of_file):
            recursive_file_lister(root_path, relative_path_of_file, all_files)

def create_json_for_invalidation(all_files, refernece):

    print("{")
    print(" \"Paths\": {")
    print("     \"Quantity\":", str(len(all_files))+",")
    print("     \"Items\": [")

    for i in range(len(all_files)):
        if(i < (len(all_files)-1)):
            print("         \""+all_files[i]+"\",")
        else:
            print("         \""+all_files[i]+"\"")
    print("     ]")
    print("   },")
    print("  \"CallerReference\": \""+refernece+"\"")
    print("}")
    


if len(sys.argv) != 2:
    print("Usage")
    print("create_invalidation_json.py dir")
else:
    all_files = []
    recursive_file_lister(sys.argv[1], "", all_files)

    create_json_for_invalidation(all_files, "auto_deploy_script")






