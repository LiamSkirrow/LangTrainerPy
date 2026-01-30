# return the correct verb ending, depending on the language, tense and subject
def derive_ending(lang, subject, tense):
    if(lang == 'Spanish'):
        if(tense == 'conditional'):
            if(subject == '1psing'):
                retval = 'ia'
            elif(subject == '1ppl'):
                retval = 'iamos'
            elif(subject == '2pfam'):
                retval = 'ias'
            elif(subject == '2pfampl'):
                retval = 'ian'
            elif(subject == '2ppol'):
                retval = 'ia'
            elif(subject == '2ppolpl'):
                retval = 'ian'
            elif(subject == '3psing'):
                retval = 'ia'
            elif(subject == '3ppl'):
                retval = 'ian'
            else:
                print('Unrecognised subject! Bug detected, exiting...')
                exit(0)
    
    return retval
