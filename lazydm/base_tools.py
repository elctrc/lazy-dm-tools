import os
import random
from data import npcnames

class DMTools:
    """Base class for all tools
    
    Attributes:
        campaign (string): Name of your current campaign
        names = Initalizing a list of lists which will contain all NPC names
    
    """
    def __init__(self, campaign="default"):
        self.campaign = campaign
        random.seed()
        self.names = []


    def generate_name(self, name_type="fantasy", fullname=False):
        self.names = self.get_names_from_text()
        print(self.names)
        if name_type == "fantasy":
            names = npcnames.fgiven
        else:
            names = npcnames.fgiven
        rand = random.randint(0, len(names) - 1)
        return names[rand]


    def get_names_from_text(self, filename=None, get_all=True, path="data"):
        os.chdir(path)

        if get_all:
            for file in os.listdir():
                if file.endswith(".txt"):
                    file_path = f"{path}\{file}"

                    self.read_text_file(file_path)

        else:
            file_path = f"{path}\{filename}"
            self.read_text_file(file_path)


    def read_text_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()