# LangTrainerPy
A more simple version of what my LangTrainer desktop app was aiming to be...

### TODO
- Spanish:
  - there are additional tenses that can only be expressed with the subjunctive. This needs to be implemented too, things like "will have eaten", or the variations on the imperative mood for example.

## Default Behaviour
- This is a language practice program, optimised for *drilling* a given target language. It is *not* intended for memorisation of vocab, that's a job for Anki. LangTrainer is dead simple, it allows you to enter in (primarily) nouns and verbs for a specific language, and it will then present you these same (primarily) nouns and verbs, asking you to conjugate/decline them accordingly and notifying you when/if you get any wrong. That's it... 

Features
- the default behaviour should be that the user can keep practicing over and over until they terminate the program manually, with no card/time limit.

- specifically for German, it'd be useful to also include possessive pronouns since they also decline based on case... Try to add these in as well!
- specifically for Russian, it'd be great to be able to select a specific case (instrumental for example) and then have to decline a bunch of examples of nouns across all the genders to be able to nail my noun declensions. 
- should also add all verb tenses too -> past, present, future etc.
- don't forget about participle forms for these languages too!

## Training mode
- additional args can be used to narrow down the specific area of study, be it specific verb tenses/conjugations or declining nouns for a certain subset of genders etc, things like that.

## Extension Modes
- include a Pimsleur-like mode, that reads out with a TTS engine, the random assortment of sentences (somehow only reading out the valid generated sentences that you'd actually find in the real world), and waiting with a short pause, for the user to repeat out loud. Maybe include the English version, and then make the user say the spoken version out loud before playing it via the TTS engine or something like this. This would force the user to come up with the conjugations and declensions on the spot, which would be invaluable practice.
