#!/usr/bin/python

import os
import sys
import hashlib
import shutil
from subprocess import call

def checksum(file):
    md5 = hashlib.md5()
    md5.update(open(file).read())
    return md5.hexdigest()

def is_contents_same(first, second):
    return checksum(first) == checksum(second)

def log(string):
    log_file = open('/media/thumb/tl.log', 'a')
    log_file.write(string)

def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as err:
        if err.errno != errno.ENOENT:
            raise

def check_media(media_path):
    if os.path.ismount(media_path):
        return True


def save_time_lapse(source, destination, attempt):
    ATTEMPT = attempt
    DESTINATION_PATH = os.path.abspath(destination) + '/' + os.path.basename(source)

    if not check_media('/media/thumb'):
        call(['mount', '/media/thumb'])

    if os.path.isfile(source) and os.path.isdir(destination):
        shutil.copy2(source, destination)

    if is_contents_same(source, DESTINATION_PATH) and ATTEMPT < 10:
        silent_remove(source)
        logStr = """File: {file_name}
Checksum: {checksum}
Size: {file_size}MB
\n""".format(file_name = DESTINATION_PATH,
           checksum  = checksum(os.path.abspath(DESTINATION_PATH)),
           file_size = os.path.getsize(DESTINATION_PATH) / 1000000)
        ATTEMPT = 1
    else:
        logStr = 'ERROR: The files are not the same.\nATTEMPT: {tries}'.format(tries = ATTEMPT)
        save_time_lapse(sys.argv[1], sys.argv[2])
        ATTEMPT = ATTEMPT + 1

        if ATTEMPT > 10:
            logStr = "ERROR: The file couldn't be copied, the source will be kept."

    log(logStr)
    return

save_time_lapse(sys.argv[1], sys.argv[2], 1)
