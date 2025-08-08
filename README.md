# LangTrainerPy
A more simple version of what my LangTrainer desktop app was aiming to be...

Features
- the user can specify --coverage x% to specify that in that given training session, a total coverage of x% of all the conjugations/declensions for all of the vocab for the specified language will be chosen before the session is ended and the script returns prints out the stats for that session (% correct/wrong etc etc).
- there should also be a --free-practice mode, where there is no coverage target for the vocab, instead the user can just keep practicing over and over until they terminate the program manually. Not sure if stats should be tracked in this case? Maybe only per practice session, track long term stats separately to with-coverage stats? Needs thinking...
- More advanced features to come...

- add an evaluation mode with a default sample of vocab to get people started who have stumbled upon this project. Add --demo or something with common/basic vocab that most learners are bound to know, that way they can quickly check it out and go from there.
- should probably contain two yaml files, one is the standard user-specific file that contains all the metadata specific to the individual user (that is gitignored since it's specific to the user and of interest to nobody else), whilst the other *should* be included in the git index and it should contain the (simplified) grammar construct for each supported language... This way the universal grammar yaml (call it the gramml) is tracked and it is available for everyone who stumbles upon the project...
- specifically for German, it'd be useful to also include possessive pronouns since they also decline based on case... Try to add these in as well!
- specifically for Russian, it'd be great to be able to select a specific case (instrumental for example) and then have to decline a bunch of examples of nouns across all the genders to be able to nail my noun declensions. 
- should also add all verb tenses too -> past, present, future etc.

## Training mode
- the default mode should be to run in schedule mode, with the coverage being what's already been calculated for the specific day that week
  - the correct/incorrect response rate should be stored for each session and given at the end of the week maybe?
- optionally --freemode can be supplied and additional args can narrow down the specific area of study, be it verb conjugations or declining nouns for a specific subset of genders etc, things like that.
  - the responses to these drills should not affect the answer rate statistics for the schedule mode, they should be independent.

## Extension Modes
- include a Pimsleur-like mode, that reads out with a TTS engine, the random assortment of sentences (somehow only reading out the valid generated sentences that you'd actually find in the real world), and waiting with a short pause, for the user to repeat out loud. Maybe include the English version, and then make the user say the spoken version out loud before playing it via the TTS engine or something like this. This would force the user to come up with the conjugations and declensions on the spot, which would be invaluable practice.
