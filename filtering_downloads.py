import os 
import pathlib
import time
from dotenv import load_dotenv

class FileManager():

    load_dotenv()

    def __init__(self) -> None:

        self.downloads_path = os.getenv('DOWNLOADS_PATH')
        self.refresh_time_span = int(os.getenv('REFRESH_TIME_SPAN'))
        self.folder_names = tuple(os.getenv('FOLDER_NAMES').split(','))
        self.filter_extension = {}

        self.collecting_filter_extensions()


    def checking_path(self, path_checked: str):

        if os.path.exists(path_checked) and os.path.isdir(path_checked):
            
            return True
        
        else: return False


    def is_filtering_valid(self, filters: list):

        if len(filters) == len(self.folder_names):
            return True

        return False
    

    def collecting_filter_extensions(self):

        extensions = os.getenv('FILTER_EXTENSTIONS').split('|')

        for i, filter in enumerate(extensions):

            final_filter = filter.split('/')

            extensions[i] = final_filter

        if self.is_filtering_valid(extensions):
            
            self.filter_extension = dict.fromkeys(self.folder_names)

            for i, key in enumerate(self.folder_names):

                self.filter_extension[key] = extensions[i]


    def creating_folders(self):

        if self.checking_path(self.downloads_path):

            for folder_name in self.folder_names:
                dir = self.downloads_path + os.sep + folder_name
                dir = pathlib.Path(dir)
                dir.mkdir(parents=True, exist_ok=True)
        else:

            print("Invalid path in .env file, please change It to proper one...")


    def is_suffix_in_filters(self, file_suffix: str): #TODO

        for key, filter in self.filter_extension.items():

            if file_suffix in filter:
                return (key, True)
            
            elif self.filter_extension[key][0] == 'ALL_OTHER':
                return (key, True)
            
        return ('', False)


    def replace_data(self):
        
        data_path = pathlib.Path(self.downloads_path)

        for file_name in data_path.iterdir():

            if file_name.is_file():

                file_suffix = pathlib.Path(file_name).suffix
                to_filter = self.is_suffix_in_filters(file_suffix)

                if to_filter[1] is True:

                    dir_to_replace = pathlib.Path(self.downloads_path + os.sep + to_filter[0] + os.sep + file_name.name)
                    file_to_replace = pathlib.Path(file_name)
                    file_to_replace.replace(dir_to_replace)


    def running_script(self):

        while(1):

            try:

                self.creating_folders()
                self.replace_data()

            except:

                break
            
            time.sleep(self.refresh_time_span * 60)


        

s = FileManager()
s.running_script()


