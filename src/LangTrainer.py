# main file for LangTrainerPy

from argparse import ArgumentParser
import yaml
import pprint

# must be run from the project's top level directory
userConfigYamlPath = "./config/language.yaml"

# generic modes for function simplification
MODE_LANG_LIST    = 0
MODE_ADD_LANG     = 1
CHECK_LANG_EXISTS = 2
MODE_ADD_VOCAB    = 3
MODE_ADD_NOUN     = 4

parser = ArgumentParser()
# parser.add_argument("-f", "--filename", type=str, required=True)
# parser.add_argument("-d", "--dump",       nargs="?", default=False, const=True, required=False)

parser.add_argument("-l", "--listlangs", action='store_true', help="List the available languages")
parser.add_argument("-a", "--addlang", type=str, help="Add a language")

# TODO:
parser.add_argument("-r", "--rmlang",  type=str, help="Remove a language") # seems dangerous lol
parser.add_argument("-d", "--demo",    type=str, 
                    help="Run in demo mode, use a default config YAML file for evaluation purposes")
# TODO:

parser.add_argument("--addverb", type=str, nargs=2,
                    help="Add a verb to the selected language")
parser.add_argument("--addnoun", type=str, nargs=3,
                    help="Add a noun to the selected language")
parser.add_argument("--addadj", type=str, nargs=2,
                    help="Add a adjective to the selected language")
parser.add_argument("--addprep", type=str, nargs=2,
                    help="Add a preposition to the selected language")

# TODO: add args to dump all verbs, nouns, adjs, preps individually... Also add functionality
#       to dump uninflected (unconjugated/undeclined) words or alternatively dump with all the inflections
#       indent nicely to make readable... give total word count etc etc
# refer to this answer -> https://stackoverflow.com/questions/16967790/argparse-two-arguments-depend-on-each-other/16968580#16968580

args = parser.parse_args()

list_langs = args.listlangs
add_lang   = args.addlang
add_verb   = args.addverb
add_noun   = args.addnoun
add_adj    = args.addadj
add_prep   = args.addprep

# print out the available languages
def inspectYaml(loadedYaml, mode, lang_name):

    if(mode == MODE_LANG_LIST):
        print("Here are the languages in the user YAML file...")
        for lang in loadedYaml['languages']:
            print('  ' + lang)
    elif(mode == CHECK_LANG_EXISTS):
        if lang_name not in loadedYaml['languages']:
            return False
        
    return True


# write to specific YAML data field and reload file, returning read-only file handle
def writeToYamlFile(data, loadedYaml, yamlFile, vocab_class, mode):
    newEntry = {}
    iterator = 0

    if(mode == MODE_ADD_LANG):
        # first prepare the dict with the new entry
        newEntry['name'] = data
        newEntry['nouns'] = []
        loadedYaml['languages'].append(newEntry)
    elif(mode == MODE_ADD_VOCAB):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        # if the language matches, then append the new vocab to the existing vocab list
        lang[vocab_class].append(data[1])
    elif(mode == MODE_ADD_NOUN):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        # if the language matches, then append the new vocab to the existing vocab list
        lang['nouns-'+data[2]].append(data[1])
        # TODO:
        # TODO: it's very easy to pass in an unregonised gender... this needs a better way of handling things

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
        inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_lang):
        print("Adding language " + add_lang + " to known languages...\n")
        # add the supplied language to the YAML
        configYaml = writeToYamlFile(add_lang, loadedYaml, userConfigYamlPath, '', MODE_ADD_LANG)
        inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_verb):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_verb[0])):
            writeToYamlFile(add_verb, loadedYaml, userConfigYamlPath, 'verbs', MODE_ADD_VOCAB)
        else:
            print('Unrecognised language \'' + add_verb[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_adj):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_adj[0])):
            writeToYamlFile(add_adj, loadedYaml, userConfigYamlPath, 'adjs', MODE_ADD_VOCAB)
        else:
            print('Unrecognised language \'' + add_adj[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_prep):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_prep[0])):
            writeToYamlFile(add_prep, loadedYaml, userConfigYamlPath, 'preps', MODE_ADD_VOCAB)
        else:
            print('Unrecognised language \'' + add_prep[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    # nouns are treated a little differently
    elif(add_noun):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_noun[0])):
            writeToYamlFile(add_noun, loadedYaml, userConfigYamlPath, 'nouns', MODE_ADD_NOUN)
        else:
            print('Unrecognised language \'' + add_noun[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')


    
    # pprint.pp(loadedYaml['languages'][0]['nouns'])
    
    """
    - in the YAML, I need to split up all nouns based on their gender so they can be drilled
      independently. 
    - (?) also need to store both the singular and plural so they can also be drilled
    - 
    """