colors = {'red':'#FF0000',
          'green':'#009900',
          'blue':'#0000FF',
          'yellow':'#FFFF00',
          'brown':'#663300',
          'black':'#FFFFFF',
          'white':'#0000FF',
}

sizes = ['small', 'medium', 'large']

intents = ['print a', 'try to print a', 'could you please print a', 'can you please print a', 'can you print a',
           'make a', 'i want a', 'give me a', 'produce a', 'i need a', ]

inform_intents = ['make sure it\'s', 'make sure it\'s a', 'make sure it is a', 'make sure it is', 'it\'s a',
                  'it\'s', 'it is a', 'it is', 'let it be a', 'let it be']

def get_objects():
    uncleaned = []
    objects = []
    with open('/content/nlu-model/data/dataSet/clean_ds/data.txt', 'r') as f:
        uncleaned = f.readlines()

        for o in uncleaned:
           objects.append(o.rstrip().lower())
    return objects
