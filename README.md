# LangTrainerPy
A more simple version of what my LangTrainer desktop app was aiming to be...

Flow of program:
- type langtrain.py --add-lang Polish
   - now Polish is added as an entry/section in the YAML/JSON
- type langtrain.py -a-dd-verb byc
  - now 'byc' has been added to the YAML/JSON. langtrain should now either pull from wiktionary or just go through each grammatical subject so that the user has to enter in manually.
- keep doing this in a loop using either add-verb, add-noun, add-adj etc etc....
- now we can train... type langtrain.py --list to list the available languages. Type langtrain.py --lang Polish to select Polish
- the script will pull from the 'Polish' section of the YAML/JSON and will autogenerate sentences with blank spaces (ala clozemaster) to be filled in by the user, using the correct conjugation or declension.
- the user can specify --coverage x% to specify that in that given training session, a total coverage of x% of all the conjugations/declensions for all of the vocab for the specified language will be chosen before the session is ended and the script returns prints out the stats for that session (% correct/wrong etc etc).
- there should also be a --free-practice, where there is no coverage target for the vocab, instead the user can just keep practicing over and over until they terminate the program manually. Not sure if stats should be tracked in this case? Maybe only per practice session, track long term stats separately to with-coverage stats? Needs thinking...
- More advanced features to come...
