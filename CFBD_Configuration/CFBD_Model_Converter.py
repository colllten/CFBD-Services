from cfbd import Conference


def conference_to_dict(conference: Conference):
    conf_dict = {}
    conf_dict.update({"id": conference.id})
    conf_dict.update({"name": conference.name})
    conf_dict.update({"short_name": conference.short_name})
    conf_dict.update({"abbreviation": conference.abbreviation})
    conf_dict.update({"classification": conference.classification.rstrip()})
    return conf_dict

