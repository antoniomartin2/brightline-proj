# Container to hold all of our sensors
import os
import pickle


class GeoContainer:
    def __init__(self, dict):
        self.dict = dict

    def merge_dict(self, input):
        for id in input.keys():
            if id in self.dict.keys():
                self.dict[id].address = input[id][0]
                self.dict[id].coords = tuple([input[id][1], input[id][2]])

    def save(self):
        filehandler = open(os.getcwd()+'/resources/.data/{}.container'.format(str(self.__hash__())), "wb")
        pickle.dump(self, filehandler)

    def get_dict(self):
        return self.dict

    def __str__(self):
        print('Hip hip hooray! You did it!')
