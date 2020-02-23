# PRE: directory
# traverse the directories, and read the filename
# parse the filename into 3 variables: title, channel, date
# write the record into a json file.

from moviepy.editor import VideoFileClip

from pathlib import Path
import json
import os


class Videofile():
    def __init__(self, filename, root):
        self.filename = filename
        self.root = root
        self.path = os.path.join(self.root, filename)
        self.file_dict = {}
        self.get_basics()

    def get_basics(self):
        self.get_duration()
        self.get_size()
        self.parse_filename()

    def get_size(self):
        file_bytes = os.path.getsize(self.path)
        self.file_dict['size'] = self.size_convert(file_bytes)       # str

    def size_convert(self, size):
        K, M, G = 1024, 1024**2, 1024**3
        if size < M:
            return str(round(size/K, 1)) + 'K'
        elif G > size > M:
            return str(round(size/M, 1)) + "M"
        else:
            return str(round(size/G, 1)) + 'G'

    def get_duration(self):
        clip = VideoFileClip(self.path)           # s
        self.file_dict['duration'] = self.time_convert(clip.duration)      # expression
        clip.close()

    def time_convert(self, seconds_sum):
        M, H = 60, 60**2
        hours = seconds_sum//H
        minutes = seconds_sum % H // M
        seconds = seconds_sum % H % M
        return f'{hours} : {minutes} : {seconds}'

    def parse_filename(self):
        """Given a filename string with .extension, return a dict. keys: title, channel, date, format
            A typical filename format: ***-***ls~-***
            WARNING: the title & channel can also have '-'.
            Best option is to start from the right, since channel name that has "-" is more rare than title.
            para: string
            return: dict"""
        (filename_no_ext, ext) = os.path.splitext(self.filename)     # ext str beginning with '.'
        self.file_dict['format'] = ext.lstrip('.')
        filename_list = filename_no_ext.split('-')
        self.file_dict['title'] = filename_list[0]
        try:
            self.file_dict['date'] = filename_list[-1]
            self.file_dict['channel'] = filename_list[-2]
            if filename_list[1:-2]:
                for i in filename_list[1:-2]:
                    self.file_dict['title'] += '-' + i
        except IndexError:
            self.file_dict['date'] = None
            self.file_dict['channel'] = None


def write_bulk_json(path):
    """Given a new directory, traverse and bulk write into a new json file.
    keys: title, channel, date, size, length, format
    para: string
    return: json"""
    movieDB_dict = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.startswith('.'):
                pass
            else:
                file = Videofile(filename, dirpath)
                movieDB_dict.update(file.file_dict)

    return json.dumps(movieDB_dict)


def write_single_json(filename):



if __name__ == "__main__":
    json = write_bulk_json('/Users/suelin/Movies')
    print(json)





