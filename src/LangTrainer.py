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
    
    # TODO: need to check for duplicate languages since this would cause issues...
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
    


