# helper methods


def get_names(response):
    rv = []
    for dict in response["competitions"]:
        rv.append(dict["name"])
    return rv
