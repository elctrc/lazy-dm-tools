import os
import random

class DMTools:
    """Base class for all tools
    
    Attributes:
        campaign (string): Name of your current campaign
        names = Initalizing a list of lists which will contain all NPC names
    
    """
    def __init__(self, campaign='default', genre='fantasy'):
        random.seed()
        self.campaign = campaign
        self.genre = genre
        # Initalize our resources by loading in all files
        self.resources = self.load_resources()


    def get_new_name(self, fullname=True):
        """
        Get a single randomly generated name, either just first name or both first and last
        """
        checkout = []
        for r in self.resources:
            if r['filename'].startswith(self.genre) and r['filename'].endswith('names.txt'):
                checkout.append(r['content'])

        if fullname:
            first = self.get_random_item(checkout[0])
            last = self.get_random_item(checkout[1])
            name = f'{first} {last}'
        else:
            name = self.get_random_item(checkout[0])

        return name


    def get_random_item(self, item_list):
        r = random.randint(0, len(item_list) - 1)
        return item_list[r]


    def load_resources(self, get_all=True, file_name=None, path='data'):
        os.chdir(path)
        files = []

        if get_all:
            for file in os.listdir():
                if file.endswith('.txt'):
                    files.append({'filename': file, 'content': self.read_text_file(file)})
        else:
            files = self.read_text_file(file_name)

        return files


    def read_text_file(self, file_path):
        with open(file_path, 'r') as f:
            s = f.read()
            self.clean_text_list = self._clean_text(s)

            return self.clean_text_list


    def _clean_text(self, text):
        """Take string of text and return clean list of text"""
        text_list = text.split(',')

        return [t.replace('\n', '').strip() for t in text_list]
