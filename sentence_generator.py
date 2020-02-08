import random

nouns = ("apple", "boy", "donkey", "tricycle", "teacher")
verbs = ("ate", "threw", "rode", "washed", "followed")
adv = ("flawlessly", "gracefully", "erratically", "attentively", "amazingly")
adj = ("shiny", "brave", "lowly", "giant", "pretty")

chosen_noun = nouns[random.randrange(0,5)]
chosen_verbs = verbs[random.randrange(0,5)]
chosen_adv = adv[random.randrange(0,5)]
chosen_adj = adj[random.randrange(0,5)]

# If apple is rolled
if chosen_noun is nouns[0]:
    noun_choices = (nouns[1], nouns[2], nouns[4])
    verb_choices = (verbs[0], verbs[1], verbs[3])
    adv_choices = (adv[2], adv[4])
    adj_choices = (adj[0], adj[3], adj[4])

    print('The ' + noun_choices[random.randrange(0,3)] + ' ' + adv_choices[random.randrange(0,2)] + ' ' + verb_choices[random.randrange(0,3)] + ' the ' + adj_choices[random.randrange(0,2)] + ' apple.')

# If boy or teacher is rolled
if chosen_noun is nouns[1] or nouns[4]:
    noun_choices = (nouns[1], nouns[2], nouns[3], nouns[4])
    verb_choices = (verbs[2], verbs[4])
    adv_choices = (adv[0], adv[1], adv[3])
    adj_choices = (adj[1], adj[2], adj[4])

    # If boy is rolled
    if noun_choices[random.randrange(0,4)] is nouns[1]:
        print('The ' + nouns[1] + ' ' + adv_choices[random.randrange(0,3)] + ' ' + verb_choices[random.randrange(0,2)] + ' the ' + adj_choices[random.randrange(0,3)] + ' ' + noun_choices[random.randrange(0,3)])