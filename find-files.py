import fnmatch
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='find-files.log',
                    filemode='a')


def main():
    rootPath = '/Users/herna/'
    pattern = '*.mp4'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            logging.debug("Searching...")
            print(os.path.join(root, filename))
            logging.info(os.path.join(root, filename))


if __name__ == '__main__':
    main()
