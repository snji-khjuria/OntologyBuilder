import re
def replaceMultiWhitespaceWithSingle(str):
    return re.sub('\s+', ' ', str).strip()


def replaceHtmlTags(str):
    notspace =  re.sub('&nbsp;', ' ', str).strip()
    notAmp   = re.sub('&amp;', '&', notspace).strip()
    return notAmp