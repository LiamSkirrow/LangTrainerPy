# main file for LangTrainerPy

from argparse import ArgumentParser
import yaml, random
from helperFunctions import derive_ending, map_subject_to_pronoun

# must be run from the project's top level directory
userConfigYamlPath = "./config/language.yaml"
specYamlPath       = "./config/spec.yaml"

# generic modes for function simplification
MODE_LANG_LIST    = 0
MODE_ADD_LANG     = 1
CHECK_LANG_EXISTS = 2
MODE_ADD_NOUN     = 3
MODE_ADD_ADJ      = 4
MODE_ADD_PREP     = 5
MODE_ADD_VERB     = 6
MODE_GET_VERB     = 7
MODE_GET_VERBS    = 8
MODE_EDIT_VERB    = 9

parser = ArgumentParser()
# parser.add_argument("-f", "--filename", type=str, required=True)
# parser.add_argument("-d", "--dump",       nargs="?", default=False, const=True, required=False)

parser.add_argument("-l", "--listlangs", action='store_true', help="List the available languages")
parser.add_argument("-a", "--addlang", type=str, help="Add a language")

# TODO:
parser.add_argument("-r", "--rmlang",  type=str, help="Remove a language") # seems dangerous lol
# TODO:

parser.add_argument("--addverb", type=str, nargs=2,
                    help="Add a verb to the selected language")
parser.add_argument("--addnoun", type=str, nargs=2,
                    help="Add a noun to the selected language")
parser.add_argument("--addadj", type=str, nargs=2,
                    help="Add a adjective to the selected language")
parser.add_argument("--addprep", type=str, nargs=2,
                    help="Add a preposition to the selected language")

parser.add_argument("--getverb", type=str, nargs=2,
                    help="Get a specific verb from the selected language")
parser.add_argument("--getverbs", type=str, nargs=1,
                    help="Get all verbs from the selected language")
# TODO: do this ^^^ for the rest of the classes of vocabulary

parser.add_argument("--editverb", type=str, nargs=2,
                    help="Edit a verb from the selected language")
# parser.add_argument("--addnoun", type=str, nargs=2,
#                     help="Edit a noun from the selected language")
# parser.add_argument("--addadj", type=str, nargs=2,
#                     help="Edit a adjective from the selected language")
# parser.add_argument("--addprep", type=str, nargs=2,
#                     help="Edit a preposition from the selected language")

parser.add_argument("-t", "--trainverbs", type=str, nargs='+',
                    help="Enter training mode, drill existing vocab")

# TODO: add args to dump all verbs, nouns, adjs, preps individually... Also add functionality
#       to dump uninflected (unconjugated/undeclined) words or alternatively dump with all the inflections
#       indent nicely to make readable... give total word count etc etc
# refer to this answer -> https://stackoverflow.com/questions/16967790/argparse-two-arguments-depend-on-each-other/16968580#16968580

args = parser.parse_args()

list_langs  = args.listlangs
add_lang    = args.addlang
add_verb    = args.addverb
add_noun    = args.addnoun
add_adj     = args.addadj
add_prep    = args.addprep
edit_verb   = args.editverb
# edit_noun   = args.editnoun
# edit_adj    = args.editadj
# edit_prep   = args.editprep
get_verb    = args.getverb
get_verbs   = args.getverbs
train_verbs = args.trainverbs

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
def readFromYamlFile(data, loadedYaml, loadedSpecYaml, mode):
    # lookup the lang and lang spec
    lang = loadedYaml['languages'][data[0]]
    langSpec = loadedSpecYaml['specs'][data[0]]

    if(mode == MODE_GET_VERBS):
        print(lang['verbs'])

    elif(mode == MODE_GET_VERB):
        # search for every conjugated version of the supplied 
        for tense in langSpec['tenses']:
            for subject in langSpec['verbConjugations']:
                print(tense + ', ' + subject + ': ' + lang['verbs-'+tense+'-'+subject][data[1]])
            print() # newline

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
            for tense in loadedSpecYaml['specs'][data]['tenses']:
                newEntry['verbs-'+tense+'-'+subject] = {}
        # get the English infinitive and simple past
        newEntry['verbs-en-inf']         = {}
        newEntry['verbs-en-simple-past'] = {}
        # add the preposition list and dict (if cases are used in the lang)
        newEntry['preps'] = []
        if(loadedSpecYaml['specs'][data]['numCases'] > 0):
            newEntry['prep-cases'] = {}
        # add the adjective list
        newEntry['adjs'] = []

        # finally, add the new language dictionary
        loadedYaml['languages'][data] = newEntry

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
        lang['verbs-en-inf'][data[1]]         = input('Enter English infinitive: ')
        lang['verbs-en-simple-past'][data[1]] = input('Enter English simple past: ')
        # automatically fill in all the verb tenses that exist in the language, for every possible subject
        for tense in langSpec['tenses']:
            for subject in langSpec['verbConjugations']:
                lang['verbs-'+tense+'-'+subject][data[1]] = derive_ending(data[0], data[1], 'verb', subject, tense)

    elif(mode == MODE_ADD_PREP):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        langSpec = loadedSpecYaml['specs'][data[0]]
        # append the new vocab to the existing vocab list
        lang['preps'].append(data[1])
        # enter the required case to be used in conjunction with the preposition
        lang['prep-cases'][data[1]] = input('Required case: ')
    elif(mode == MODE_ADD_ADJ):
        # append the new vocab to the existing vocab list
        lang['adjs'].append(data[1])

    elif(mode == MODE_EDIT_VERB):
        # lookup the lang in the dictionary to get the sub-dictionary with the word data
        lang = loadedYaml['languages'][data[0]]
        langSpec = loadedSpecYaml['specs'][data[0]]
        # search for every conjugated version of the supplied 
        for tense in langSpec['tenses']:
            for subject in langSpec['verbConjugations']:
                print(tense + ', ' + subject + ': ' + lang['verbs-'+tense+'-'+subject][data[1]] + ' -> ', end='')
                user_resp = input()
                if(user_resp == ''):
                    continue
                else:
                    lang['verbs-'+tense+'-'+subject][data[1]] = user_resp

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
            exit(0)
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

    elif(get_verb):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, get_verb[0])):
            readFromYamlFile(get_verb, loadedYaml, loadedSpecYaml, MODE_GET_VERB)
        else:
            print('Unrecognised language \'' + get_verb[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')

    elif(get_verbs):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, get_verbs[0])):
            readFromYamlFile(get_verbs, loadedYaml, loadedSpecYaml, MODE_GET_VERBS)
        else:
            print('Unrecognised language \'' + get_verbs[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')

    # TODO: get the remainder of the vocab classes, not just for verbs!

    elif(edit_verb):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, edit_verb[0])):
            writeToYamlFile(edit_verb, loadedYaml, loadedSpecYaml, userConfigYamlPath, 'nouns', MODE_EDIT_VERB)
        else:
            print('Unrecognised language \'' + edit_verb[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')


    # TODO:
    # training... start off with the train-verbs mode, which with no args trains 
    # knowledge of standalone verb conjugations, and with args trains only those specified verbs.

    # Maybe even include a session.yaml.log file which gets autogenerated and 
    # stored in some 'practice-sessions' directory with a timestamp on it for future use
    # or possibly in developing the statistics for a given wordset...
    # enter training mode, drill the existing vocab in randomly formed sentences
    elif(train_verbs):
        # check if the user input language exists
        if(inspectYaml(loadedYaml, CHECK_LANG_EXISTS, train_verbs[0])):
            lang = loadedYaml['languages'][train_verbs[0]]
            langSpec = loadedSpecYaml['specs'][train_verbs[0]]
            verbs = lang['verbs']
            verb_selection = []
            if(len(train_verbs) == 1):
                verb_selection = verbs
            else:
                # iterate over the supplied verbs in argument
                for verb in train_verbs[1:]:
                    # check verb exists in language yaml
                    if(verb not in verbs):
                        print('Error! Unrecognised verb: ' + verb + '\n\nRerun with supported verbs only, or add new verb with arg --addverb')
                        exit(0)
                    verb_selection.append(verb)                    
                        
        else:
            print('Unrecognised language \'' + train_verbs[0] + '\'...\n')
            inspectYaml(loadedYaml, MODE_LANG_LIST, '')


        # print(verb_selection)

        while(True):
            # randomly select an infinitive from the available verbs
            random_verb = random.choice(verb_selection)
            random_verb_en = lang['verbs-en-inf'][random_verb]

            # print(random_verb)

            # given the size of tenses and verbConjugations in lang spec, index the lists using a random number and 
            # select an entry from tense and verbConjugations.
            random_tense   = random.choice(langSpec['tenses'])
            random_subject = random.choice(langSpec['verbConjugations'])

            # concatenate 'verbs' with 'tense' with 'verbConjugations' to give something like verbs-future-1ppl
            concat_str = 'verbs-' + random_tense + '-' + random_subject

            # print(concat_str)

            # use this generated string to look up the relevant language yaml dict, and grab a word from there
            training_verb = lang[concat_str][random_verb]

            # print(training_verb)

            # create a card to be answered by the user, displaying the pronoun
            # as well as the tense to be supplied, and maybe mood as well in a future version (indicative, subjunctive, imperative...)
            training_pronoun = map_subject_to_pronoun(train_verbs[0], random_subject)

            print(random_verb_en + ', ' + random_tense + '\n' + training_pronoun + '_____?\n')
            user_resp = input()
            if(user_resp == training_verb):
                print('Correct!\n')
            else:
                print('Incorrect! Answer was ' + training_verb + '\n')

            # - add fancy terminal UI for use after all the above is done
            # - add a way to log the responses, keep track of incorrectly answered responses and print summary on exit. 
        


        # TODO: note:
        # don't foget to indicate both tense=[past, present, future] and also aspect=[perf, imperf] for the Slavic languages...
