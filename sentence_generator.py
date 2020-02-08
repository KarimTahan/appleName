import random
import spacy

nlp = spacy.load('en_core_web_sm')

nouns = ("apple", "boy", "donkey", "tricycle", "teacher")
verbs = ("ate", "threw", "rode", "washed", "followed")
adv = ("flawlessly", "gracefully", "erratically", "attentively", "amazingly")
adj = ("new", "brave", "lowly", "giant", "pretty")

main_character = (nouns[1], nouns[2], nouns[4])


def generate_sentence(chosen_noun, chosen_verbs, chosen_adv, chosen_adj):
    # If boy is rolled
    if chosen_noun is nouns[1]:
        noun_choices = (nouns[0], nouns[2], nouns[3], nouns[4])

        # If boy ate or threw
        if chosen_verbs is verbs[0] or chosen_verbs is verbs[1]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[0] + '.')

        # If boy rode or washed
        elif chosen_verbs is verbs[2] or chosen_verbs is verbs[3]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[random.randrange(1, 3)] + '.')

        # If boy followed
        elif chosen_verbs is verbs[4]:
            restricted_choices = (noun_choices[1], noun_choices[3])
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    restricted_choices[random.randrange(0, 2)] + '.')

    # If donkey is rolled
    elif chosen_noun is nouns[2]:
        noun_choices = (nouns[0], nouns[1], nouns[4])

        # If donkey ate or threw
        if chosen_verbs is verbs[0] or chosen_verbs is verbs[1]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[0] + '.')

        # If donkey followed
        elif chosen_verbs is verbs[4]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[random.randrange(1, 3)] + '.')

        # If donkey rode
        elif chosen_verbs is verbs[2]:
            doc = nlp(chosen_verbs)
            for token in doc:
                root_verb = token.lemma_
            return 'Only silly donkeys try to ' + root_verb + ' things.'

        # If donkey washed
        elif chosen_verbs is verbs[3]:
            doc = nlp(chosen_verbs)
            for token in doc:
                root_verb = token.lemma_
            return 'It\'s hard for a donkey to ' + root_verb + ' anything without hands!'

    # If teacher is rolled
    elif chosen_noun is nouns[4]:
        noun_choices = (nouns[0], nouns[1], nouns[2], nouns[3])

        # If teacher ate or threw
        if chosen_verbs is verbs[0] or chosen_verbs is verbs[1]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[0] + '.')

        # If teacher rode
        elif chosen_verbs is verbs[2]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[2] + '.')

        # If teacher washed
        elif chosen_verbs is verbs[3]:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[random.randrange(2, 4)] + '.')

        # If teacher followed
        else:
            return ('The ' + chosen_noun + ' ' + chosen_adv + ' ' + chosen_verbs + ' the ' + chosen_adj + ' ' +
                    noun_choices[random.randrange(1, 3)] + '.')


# Generate 20 sentences
for _ in range(20):
    print(generate_sentence(main_character[random.randrange(0, 3)], verbs[random.randrange(0, 5)],
                            adv[random.randrange(0, 5)], adj[random.randrange(0, 5)]
                            ))
