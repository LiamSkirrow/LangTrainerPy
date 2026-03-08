# return the correct verb ending, depending on the language, tense and subject
def derive_ending(lang, word, mode, subject, tense):
    if(lang == 'Spanish'):
        if(mode == 'verb'):
            if(tense == 'present'):
                if(word[-2:] == 'ar'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = word[0:-2] + 'o'
                    elif(subject == '1ppl'):
                        retval = word[0:-2] + 'amos'
                    elif(subject == '2pfam'):
                        retval = word[0:-2] + 'as'
                    elif(subject == '2pfampl'):
                        retval = word[0:-2] + 'an'
                    elif(subject == '2ppol'):
                        retval = word[0:-2] + 'a'
                    elif(subject == '2ppolpl'):
                        retval = word[0:-2] + 'an'
                    elif(subject == '3psing'):
                        retval = word[0:-2] + 'a'
                    elif(subject == '3ppl'):
                        retval = word[0:-2] + 'an'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
                elif(word[-2:] == 'er' or word[-2:] == 'ir'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = word[0:-2] + 'o'
                    elif(subject == '1ppl'):
                        if(word[-2:] == 'er'):
                            retval = word[0:-2] + 'emos' # TODO: potential index out of bounds bug
                        elif(word[-2:] == 'ir'):
                            retval = word[0:-2] + 'imos' # TODO: potential index out of bounds bug
                    elif(subject == '2pfam'):
                        retval = word[0:-2] + 'es'
                    elif(subject == '2pfampl'):
                        retval = word[0:-2] + 'en'
                    elif(subject == '2ppol'):
                        retval = word[0:-2] + 'e'
                    elif(subject == '2ppolpl'):
                        retval = word[0:-2] + 'en'
                    elif(subject == '3psing'):
                        retval = word[0:-2] + 'e'
                    elif(subject == '3ppl'):
                        retval = word[0:-2] + 'en'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)

            elif(tense == 'simple-past'):
                if(word[-2:] == 'ar'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = word[0:-2] + 'é'
                    elif(subject == '1ppl'):
                        retval = word[0:-2] + 'amos'
                    elif(subject == '2pfam'):
                        retval = word[0:-2] + 'aste'
                    elif(subject == '2pfampl'):
                        retval = word[0:-2] + 'aron'
                    elif(subject == '2ppol'):
                        retval = word[0:-2] + 'ó'
                    elif(subject == '2ppolpl'):
                        retval = word[0:-2] + 'aron'
                    elif(subject == '3psing'):
                        retval = word[0:-2] + 'ó'
                    elif(subject == '3ppl'):
                        retval = word[0:-2] + 'aron'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
                elif(word[-2:] == 'er' or word[-2:] == 'ir'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = word[0:-2] + 'í'
                    elif(subject == '1ppl'):
                        retval = word[0:-2] + 'imos' # TODO: potential index out of bounds bug
                    elif(subject == '2pfam'):
                        retval = word[0:-2] + 'iste'
                    elif(subject == '2pfampl'):
                        retval = word[0:-2] + 'ieron'
                    elif(subject == '2ppol'):
                        retval = word[0:-2] + 'ió'
                    elif(subject == '2ppolpl'):
                        retval = word[0:-2] + 'ieron'
                    elif(subject == '3psing'):
                        retval = word[0:-2] + 'ió'
                    elif(subject == '3ppl'):
                        retval = word[0:-2] + 'ieron'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)

            elif(tense == 'present-cont'):
                if(word[-2:] == 'ar'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = 'estoy ' + word[0:-2] + 'ando'
                    elif(subject == '1ppl'):
                        retval = 'estamos ' + word[0:-2] + 'ando'
                    elif(subject == '2pfam'):
                        retval = 'estas ' + word[0:-2] + 'ando'
                    elif(subject == '2pfampl'):
                        retval = 'estan ' + word[0:-2] + 'ando'
                    elif(subject == '2ppol'):
                        retval = 'esta ' + word[0:-2] + 'ando'
                    elif(subject == '2ppolpl'):
                        retval = 'estan ' + word[0:-2] + 'ando'
                    elif(subject == '3psing'):
                        retval = 'esta ' + word[0:-2] + 'ando'
                    elif(subject == '3ppl'):
                        retval = 'estan ' + word[0:-2] + 'ando'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
                elif(word[-2:] == 'er' or word[-2:] == 'ir'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = 'estoy ' + word[0:-2] + 'iendo'
                    elif(subject == '1ppl'):
                        retval = 'estamos ' + word[0:-2] + 'iendo'
                    elif(subject == '2pfam'):
                        retval = 'estas ' + word[0:-2] + 'iendo'
                    elif(subject == '2pfampl'):
                        retval = 'estan ' + word[0:-2] + 'iendo'
                    elif(subject == '2ppol'):
                        retval = 'esta ' + word[0:-2] + 'iendo'
                    elif(subject == '2ppolpl'):
                        retval = 'estan ' + word[0:-2] + 'iendo'
                    elif(subject == '3psing'):
                        retval = 'esta ' + word[0:-2] + 'iendo'
                    elif(subject == '3ppl'):
                        retval = 'estan ' + word[0:-2] + 'iendo'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
            
            elif(tense == 'present-perf'):
                if(word[-2:] == 'ar'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = 'he ' + word[0:-2] + 'ado'
                    elif(subject == '1ppl'):
                        retval = 'hemos ' + word[0:-2] + 'ado'
                    elif(subject == '2pfam'):
                        retval = 'has ' + word[0:-2] + 'ado'
                    elif(subject == '2pfampl'):
                        retval = 'han ' + word[0:-2] + 'ado'
                    elif(subject == '2ppol'):
                        retval = 'ha ' + word[0:-2] + 'ado'
                    elif(subject == '2ppolpl'):
                        retval = 'han ' + word[0:-2] + 'ado'
                    elif(subject == '3psing'):
                        retval = 'ha ' + word[0:-2] + 'ado'
                    elif(subject == '3ppl'):
                        retval = 'han ' + word[0:-2] + 'ado'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
                elif(word[-2:] == 'er' or word[-2:] == 'ir'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = 'he ' + word[0:-2] + 'ido'
                    elif(subject == '1ppl'):
                        retval = 'hemos ' + word[0:-2] + 'ido'
                    elif(subject == '2pfam'):
                        retval = 'has ' + word[0:-2] + 'ido'
                    elif(subject == '2pfampl'):
                        retval = 'han ' + word[0:-2] + 'ido'
                    elif(subject == '2ppol'):
                        retval = 'ha ' + word[0:-2] + 'ido'
                    elif(subject == '2ppolpl'):
                        retval = 'han ' + word[0:-2] + 'ido'
                    elif(subject == '3psing'):
                        retval = 'ha ' + word[0:-2] + 'ido'
                    elif(subject == '3ppl'):
                        retval = 'han ' + word[0:-2] + 'ido'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)

            elif(tense == 'imperfect-past'):
                if(word[-2:] == 'ar'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = word[0:-2] + 'aba'
                    elif(subject == '1ppl'):
                        retval = word[0:-2] + 'abamos'
                    elif(subject == '2pfam'):
                        retval = word[0:-2] + 'abas'
                    elif(subject == '2pfampl'):
                        retval = word[0:-2] + 'aban'
                    elif(subject == '2ppol'):
                        retval = word[0:-2] + 'aba'
                    elif(subject == '2ppolpl'):
                        retval = word[0:-2] + 'aban'
                    elif(subject == '3psing'):
                        retval = word[0:-2] + 'aba'
                    elif(subject == '3ppl'):
                        retval = word[0:-2] + 'aban'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
                elif(word[-2:] == 'er' or word[-2:] == 'ir'): # TODO: potential index out of bounds bug
                    if(subject == '1psing'):
                        retval = word[0:-2] + 'ía'
                    elif(subject == '1ppl'):
                        retval = word[0:-2] + 'íamos'
                    elif(subject == '2pfam'):
                        retval = word[0:-2] + 'ías'
                    elif(subject == '2pfampl'):
                        retval = word[0:-2] + 'ían'
                    elif(subject == '2ppol'):
                        retval = word[0:-2] + 'ía'
                    elif(subject == '2ppolpl'):
                        retval = word[0:-2] + 'ían'
                    elif(subject == '3psing'):
                        retval = word[0:-2] + 'ía'
                    elif(subject == '3ppl'):
                        retval = word[0:-2] + 'ían'
                    else:
                        print('Unrecognised subject! Bug detected, exiting...')
                        exit(0)
            
            elif(tense == 'conditional'):
                if(subject == '1psing'):
                    retval = word + 'ía'
                elif(subject == '1ppl'):
                    retval = word + 'íamos'
                elif(subject == '2pfam'):
                    retval = word + 'ías'
                elif(subject == '2pfampl'):
                    retval = word + 'ían'
                elif(subject == '2ppol'):
                    retval = word + 'ía'
                elif(subject == '2ppolpl'):
                    retval = word + 'ían'
                elif(subject == '3psing'):
                    retval = word + 'ía'
                elif(subject == '3ppl'):
                    retval = word + 'ían'
                else:
                    print('Unrecognised subject! Bug detected, exiting...')
                    exit(0)

            elif(tense == 'future'):
                if(subject == '1psing'):
                    retval = word + 'é'
                elif(subject == '1ppl'):
                    retval = word + 'emos'
                elif(subject == '2pfam'):
                    retval = word + 'ás'
                elif(subject == '2pfampl'):
                    retval = word + 'án'
                elif(subject == '2ppol'):
                    retval = word + 'á'
                elif(subject == '2ppolpl'):
                    retval = word + 'án'
                elif(subject == '3psing'):
                    retval = word + 'á'
                elif(subject == '3ppl'):
                    retval = word + 'án'
                else:
                    print('Unrecognised subject! Bug detected, exiting...')
                    exit(0)

            else:
                print('Unrecognised tense!')
    
    return retval
