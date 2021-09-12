import os
import argparse
import socket
import sys

from src.common_utils.loggers import logger

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
if files_to_ignore == "":
    logger.warn("No files ignored. Printing all the available files in the target directory.")
else:
    logger.info("Print Job will not print the following files as they are ignored.")

files_to_print = []
for root,dir, files in os.walk(os.path.join(root_dir,'docs'), topdown = False):
    try:
        for file in files:
            if file not in files_to_ignore:
                logger.info("Printing {} from the path {}.".format(file,root))
                os.startfile(os.path.join(root,file), "print")
                files_to_print.append(file)
                logger.info("Print for the file {} completed.".format(file))
            else:
                pass
    except Exception as e:
        logger.info("Stopping the print service, an exception caught.")
        logger.info(e)

# Collect the host name
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
logger.info("Print Job is completed. Below list of files are printed. Please collect the documents.")
logger.info("Hostname: {}, AssignedIP: {}".format(hostname, IPAddr))
