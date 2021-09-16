import os
import argparse
from Build.Print import PrintBase

current_dir = os.getcwd()
root_dir = current_dir[:-4]

parser = argparse.ArgumentParser()
parser.add_argument('--notrequired', type = list, help = "files/folder to ignore", default = ["Accenture_required_docs_print.txt",
                                                                                              "Accenture_OfferLetter_2021.pdf",
                                                                                              "Declaration.pdf",
                                                                                              "CapitalNumbers_Releiving letter.pdf",
                                                                                              "LTIReleaseLetter.pdf"])
args = parser.parse_args()
files_to_ignore = args.notrequired

A = PrintBase(root_dir, files_to_ignore)
A.files_to_ignore