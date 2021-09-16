import os
from abc import ABC, abstractmethod
from src.common_utils.loggers import logger
from src.src_context import root_dir



class PrintBase(ABC):
    def __init__(self, root_dir, *files_to_ignore):
        self.files_to_ignore = files_to_ignore if files_to_ignore else None
        self.root_dir = root_dir
        logger.info(self.files_to_ignore)

    @abstractmethod
    def print(self):
        if self.files_to_ignore == "":
            logger.warn("No files ignored. Printing all the available files in the target directory.")
        else:
            logger.info("Print Job will not print the following files as they are ignored.")
            logger.info(self.files_to_ignore)

        files_to_print = []
        for root,dir, files in os.walk(os.path.join(root_dir,'docs'), topdown = False):
            try:
                for file in files:
                    if file not in self.files_to_ignore:
                        logger.info("Printing {} from the path {}.".format(file,root))
                        os.startfile(os.path.join(root,file), "print")
                        files_to_print.append(file)
                        logger.info("Print for the file {} completed.".format(file))
                    else:
                        pass
            except Exception as e:
                logger.info("Stopping the print service, an exception caught.")
                logger.info(e)
