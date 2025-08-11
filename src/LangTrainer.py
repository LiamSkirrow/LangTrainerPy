# main file for LangTrainerPy

from argparse import ArgumentParser
import yaml
import pprint

# must be run from the project's top level directory
userConfigYamlPath = "./config/language.yaml"
specYamlPath       = "./config/spec.yaml"

# generic modes for function simplification
MODE_LANG_LIST    = 0
MODE_ADD_LANG     = 1
CHECK_LANG_EXISTS = 2
# MODE_ADD_VOCAB    = 3
MODE_ADD_NOUN     = 4
MODE_ADD_ADJ      = 5
MODE_ADD_PREP     = 6
MODE_ADD_VERB     = 7

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
parser.add_argument("--addnoun", type=str, nargs=2,
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
def writeToYamlFile(data, loadedYaml, loadedSpecYaml, yamlFile, vocab_class, mode):
    newEntry = {}

    # create the new language according to the spec file
    if(mode == MODE_ADD_LANG):
        # add the (gendered) nouns list(s)
        for gender in loadedSpecYaml['specs'][data]['genders']:
            newEntry['nouns-'+gender] = []
        for inflection in loadedSpecYaml['specs'][data]['cases']:
            newEntry['nouns-'+inflection] = {}
        # add the (conjugated) verbs list(s)
        newEntry['verbs'] = []
        for subject in loadedSpecYaml['specs'][data]['verbConjugations']:
            newEntry['verbs-'+subject] = {}
        # add the preposition list and dict (if cases are used in the lang)
        newEntry['preps'] = []
        if(loadedSpecYaml['specs'][data]['numCases'] > 0):
            newEntry['prep-cases'] = {}
        # add the adjective list
        newEntry['adjs'] = []

        # finally, add the new language dictionary
        loadedYaml['languages'][data] = newEntry

    # TODO: move declaration of lang and langSpec to top of this function
    # TODO: instead of duplicating across all the elifs below

    elif(mode == MODE_ADD_NOUN):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        langSpec = loadedSpecYaml['specs'][data[0]]
        # user input required to determine noun gender
        userInputGender = input('Enter noun gender: ')
        if(userInputGender in langSpec['genders']):
            # append the new vocab to the existing vocab list
            lang['nouns-'+userInputGender].append(data[1])
            # enter the different declined forms of the nouns, only for languages where there are inflected noun forms
            if(loadedSpecYaml['specs'][data[0]]['numCases'] > 0 and loadedSpecYaml['specs'][data[0]]['nounsInflect']):
                for case in langSpec['cases']:
                    lang['nouns-'+case][data[1]] = input(case + ': ')
        else:
            print('Language ' + data[0] + ' doesn\'t recognise gender: <' + 
                  userInputGender + '>... Exiting')
    elif(mode == MODE_ADD_VERB):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        langSpec = loadedSpecYaml['specs'][data[0]]
        # append the new vocab to the existing vocab list
        lang['verbs'].append(data[1])
        # enter the different conjugated forms of the verbs
        for subject in langSpec['verbConjugations']:
            lang['verbs-'+subject][data[1]] = input(subject + ': ')
    elif(mode == MODE_ADD_PREP):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        langSpec = loadedSpecYaml['specs'][data[0]]
        # append the new vocab to the existing vocab list
        lang['preps'].append(data[1])
        # enter the required case to be used in conjunction with the preposition
        lang['prep-cases'][data[1]] = input('Required case: ')
    elif(mode == MODE_ADD_ADJ):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        langSpec = loadedSpecYaml['specs'][data[0]]
        # append the new vocab to the existing vocab list
        lang['adjs'].append(data[1])
            


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
    with open(specYamlPath) as langSpecYaml:
        loadedSpecYaml = yaml.safe_load(langSpecYaml)

    # print out the available languages in the user config YAML
    if(list_langs):
        inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_lang):
        # check if language already exists
        if(add_lang not in loadedSpecYaml['specs']):
            print('Language: ' + add_lang + ' not present in spec.yaml... Exiting')
            exit()
        if(add_lang in loadedYaml['languages']):
            print('Language: ' + add_lang + ' already present in language.yaml... Exiting')
        else:
            print("Adding language " + add_lang + " to known languages...\n")
            # add the supplied language to the YAML
            configYaml = writeToYamlFile(add_lang, loadedYaml, loadedSpecYaml, userConfigYamlPath, '', MODE_ADD_LANG)
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    
    ### TODO:
    ### TODO: surely this repetition doesn't have to be here
    ### TODO: try to make it more succinct...
    
    elif(add_verb):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_verb[0])):
            writeToYamlFile(add_verb, loadedYaml, loadedSpecYaml, userConfigYamlPath, 'verbs', MODE_ADD_VERB)
        else:
            print('Unrecognised language \'' + add_verb[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_adj):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_adj[0])):
            writeToYamlFile(add_adj, loadedYaml, loadedSpecYaml, userConfigYamlPath, 'adjs', MODE_ADD_ADJ)
        else:
            print('Unrecognised language \'' + add_adj[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    elif(add_prep):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_prep[0])):
            writeToYamlFile(add_prep, loadedYaml, loadedSpecYaml, userConfigYamlPath, 'preps', MODE_ADD_PREP)
        else:
            print('Unrecognised language \'' + add_prep[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')
    # nouns are treated a little differently
    elif(add_noun):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, add_noun[0])):
            writeToYamlFile(add_noun, loadedYaml, loadedSpecYaml, userConfigYamlPath, 'nouns', MODE_ADD_NOUN)
        else:
            print('Unrecognised language \'' + add_noun[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')

    # TODO:
    # we're up to the implementation of the training mode now...
    # start a training session and store the correct and incorrect responses
    # in a buffer (or separate buffers) to be displayed when the session ends
    # Maybe even include a session.yaml.log file which gets autogenerated and 
    # stored in some 'practice-sessions' directory with a timestamp on it for future use
    # or possibly in developing the statistics for a given wordset...