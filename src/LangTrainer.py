# main file for LangTrainerPy

from argparse import ArgumentParser

parser = ArgumentParser()
# parser.add_argument("-f", "--filename", type=str, required=True)
# parser.add_argument("-d", "--dump",       nargs="?", default=False, const=True, required=False)

parser.add_argument("-l", "--listlangs", action='store_true')

args = parser.parse_args()

list_langs = args.listlangs

if __name__ == "__main__":
    
    # print out the available languages
    if(list_langs):
        print("Test")
