from django import template

register = template.Library()

@register.filter(name='htmlPerso')
def htmlPerso(publi):
    # for k, v in publi.items():
    #     print(k, v)

    # get names and urls
    try:
        namesLinked = []
        searchUrl = "https://hal.archives-ouvertes.fr/search/index/q/*"
        for _ in publi["authFullNameIdHal_fs"]:
            name, idHal = _.split("_FacetSep_")
            searchType = "authIdHal_s" if idHal else "authFullName_s"
            searchString = idHal if idHal else name.replace(" ", "+")
            url = "{}/{}/{}".format(searchUrl, searchType, searchString)
            namesLinked.append('<a href="{}" target="_blank">{}</a>'.format(url, name))
        cite = [', '.join(namesLinked)]
    except:
        cite = [', '.join(publi["authLastNameFirstName_s"])]

    #  get title and url
    try:
        cite.append('<b>"<a href="{}" target="_blank">{}</a>"</b>'.format(publi["uri_s"], publi["title_s"][0]))
    except:
        print("uri_s not found in: ", publi["title_s"][0])
        pass

    # get journal
    try:
        cite.append('<em>{}</em>'.format(publi["journalTitle_s"]))
    except:
        print("journalTitle_s not found in: ", publi["title_s"][0])
        pass

    # get volume
    try:
        cite.append('Vol. {}'.format(publi["volume_s"]))
    except:
        print("volume_s not found in: ", publi["title_s"][0])
        pass

    # get pages
    try:
        cite.append('pp. {}'.format(publi["page_s"]))
    except:
        print("page_s not found in: ", publi["title_s"][0])
        pass

    # get year
    try:
        cite.append('{}'.format(publi["releasedDateY_i"]))
    except:
        print("releasedDateY_i not found in: ", publi["title_s"][0])
        pass
    return ', '.join(cite) + '.'
