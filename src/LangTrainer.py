# main file for LangTrainerPy

from argparse import ArgumentParser
import yaml

# must be run from the project's top level directory
userConfigYamlPath = "./config/language.yaml"

# generic modes for function simplification
MODE_LANG_LIST = 0
MODE_ADD_LANG  = 1

parser = ArgumentParser()
# parser.add_argument("-f", "--filename", type=str, required=True)
# parser.add_argument("-d", "--dump",       nargs="?", default=False, const=True, required=False)

parser.add_argument("-l", "--listlangs", action='store_true', help="List the available languages")
parser.add_argument("-a", "--addlang", type=str, help="Add a language")
parser.add_argument("-r", "--rmlang",  type=str, help="Remove a language") # seems dangerous lol
parser.add_argument("-d", "--demo",    type=str, 
                    help="Run in demo mode, use a default config YAML file for evaluation purposes")
parser.add_argument("--selectlang", type=str, 
                    help="Select a language to modify or practice with")
# TODO: these below args are only valid if a language is selected using --selectlang
parser.add_argument("--addverb", type=str, 
                    help="Add a verb to the selected language")
parser.add_argument("--addnoun", type=str, 
                    help="Add a noun to the selected language")
parser.add_argument("--addadj", type=str, 
                    help="Add a adjective to the selected language")
parser.add_argument("--addprep", type=str, 
                    help="Add a preposition to the selected language")

# TODO: add args to dump all verbs, nouns, adjs, preps individually... Also add functionality
#       to dump uninflected (unconjugated/undeclined) words or alternatively dump with all the inflections
#       indent nicely to make readable... give total word count etc etc
# refer to this answer -> https://stackoverflow.com/questions/16967790/argparse-two-arguments-depend-on-each-other/16968580#16968580

args = parser.parse_args()

list_langs = args.listlangs
add_lang   = args.addlang

# print out the available languages
def dumpYaml(loadedYaml, mode):
    if(mode == MODE_LANG_LIST):
        print("Here are the languages in the user YAML file...")
        for lang in loadedYaml['languages']['list']:
            print('  ' + lang)

# write to specific YAML data field and reload file, returning read-only file handle
def writeToYamlFile(data, loadedYaml, yamlFile, mode):
    
    if(mode == MODE_ADD_LANG):
        # and print out the new list of available languages
        loadedYaml['languages']['list'].append(data)

    # overwrite the current yaml with the newly modified yaml
    with open(yamlFile, 'w') as configYaml:
            yaml.safe_dump(loadedYaml, configYaml)

    # lastly, open the file as read-only and return the handler
    configYaml = open(yamlFile, 'r')
    return configYaml


if __name__ == "__main__":
    
    # open and parse the user config YAML
    with open(userConfigYamlPath) as configYaml:
        loadedYaml = yaml.safe_load(configYaml)

    # print out the available languages in the user config YAML
    if(list_langs):
        dumpYaml(loadedYaml, MODE_LANG_LIST)
    elif(add_lang):
        print("Adding language " + add_lang + " to known languages...\n")
        # add the supplied language to the YAML
        configYaml = writeToYamlFile(add_lang, loadedYaml, userConfigYamlPath, MODE_ADD_LANG)
        dumpYaml(loadedYaml, MODE_LANG_LIST)
    