import os
from synomyms import get_synonyms

def get_directory_files(path):
    cleaned_files = []
    for root, dirs, files in os.walk(path):
        None
    for f in files:
        cleaned_files.append(f.split(".obj")[0])
    return cleaned_files



def check_color(entity):
    if entity['entity'] == "color":
        return entity['value']
    return None


def check_size(entity):
    if entity['entity'] == "size":
        return entity['value']
    return None


def check_object_name(entity):
    if entity['entity'] == "object":
        return entity['value']
    return None


def get_printing_specifications(object):
    operation = object['intent']['name']
    entities = object['entities']
    color, found_c = None, False
    size, found_s = None, False
    name, found_n = None, False
    for entity in entities:
        if not found_c:
            color = check_color(entity)
            if color is not None:
                found_c = True

        if not found_s:
            size = check_size(entity)
            if size is not None:
                found_s = True

        if not found_n:
            name = check_object_name(entity)
            if name is not None:
                found_n = True

        if found_c and found_n and found_s:
            return operation, color, size, name

    return operation, color, size, name


def find_corresponding_model(object_name):
    available_models = get_directory_files("object_models/")
    if object_name in available_models:
        return object_name
    else:
        synonyms = get_synonyms(object_name)
        for synonym in synonyms:
            if synonym in available_models:
                return synonym

    return None


def give_instruction(semantic_frame):
    action, color, size, name = get_printing_specifications(semantic_frame)
    if action is None:
        pass
    if color is None:
        pass
    if size is None:
        pass
    if name is None:
        pass

    match = find_corresponding_model(name)
    if match is not None:
        model_path = "object_models/"+match+".obj"
        return action, model_path, color, size
    else:
        return None


test = {"intent":{"name":"print","confidence":0.7975472808},"entities":[{"start":8,"end":13,"value":"small","entity":"size","confidence":0.998816315,"extractor":"CRFEntityExtractor"},{"start":29,"end":35,"value":"people","entity":"object","confidence":0.5410338733,"extractor":"CRFEntityExtractor"}],"intent_ranking":[{"name":"print","confidence":0.7975472808},{"name":"inform","confidence":0.1343427449},{"name":"ask","confidence":0.0428403467},{"name":"cancel","confidence":0.0094871586},{"name":"deny","confidence":0.0080026835},{"name":"confirm","confidence":0.0077797733}],"text":"it is a small cute chair old people"}

print(give_instruction(test))