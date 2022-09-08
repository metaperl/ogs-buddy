from ogs_buddy.anki_connect import invoke

def call(x, *args):
    r = invoke(x, *args)
    print(r)

call('deckNames')