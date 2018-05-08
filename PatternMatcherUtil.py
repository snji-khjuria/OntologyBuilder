from FileUtil import readPlainHtmlPageContent

from MatchersUtil import getAllEntitiesInsideLeftRightPattern, getAllRelations, getClusterInsideLeftRightPattern, getElementsOfCluster
def extractProductTitle(pageContent, titlePattern):
    (leftTitlePattern, rightTitlePattern) = titlePattern
    return getAllEntitiesInsideLeftRightPattern(pageContent, leftTitlePattern, rightTitlePattern)


def extractProductTitles(pageContent, titlePatterns):
    output = []
    for titlePattern in titlePatterns:
        output.extend(extractProductTitle(pageContent, titlePattern))
    return output


def extractProductSpec(pageContent, productSpecsPattern):
    (leftSpecsPattern, insideSpecsPattern, rightSpecsPattern) = productSpecsPattern
    found = getClusterInsideLeftRightPattern(pageContent, leftSpecsPattern, insideSpecsPattern, rightSpecsPattern)
    totalFound = []
    for cluster in found:
        clusterItems = getElementsOfCluster(cluster, insideSpecsPattern)
        totalFound.extend(clusterItems)
    totalFound = set(totalFound)
    return list(totalFound)
    # return getClusterInsideLeftRightPattern(pageContent, leftSpecsPattern, insideSpecsPattern, rightSpecsPattern)

def extractProductSpecs(pageContent, productSpecsPatterns):
    output = []
    for pattern in productSpecsPatterns:
        output.extend(extractProductSpec(pageContent, pattern))
    return output


def extractProductRelation(pageContent, productRelationPattern):
    (leftTablePattern, middleTablePattern, rightTablePattern) = productRelationPattern
    found = getAllRelations(leftTablePattern, middleTablePattern, rightTablePattern, pageContent)
    return found

def extractProductRelations(pageContent, productRelationPatterns):
    output = []
    for pattern in productRelationPatterns:
        output.extend(extractProductRelation(pageContent, pattern))
    return output

from ProductInfo import ProductInfo
def getProdInfo(patterns, pageLocation):
    pageContent        = readPlainHtmlPageContent(pageLocation)
    titlePatterns      = patterns.getProductTitlePatterns()
    specsPatterns      = patterns.getProductSpecsPatterns()
    relationPatterns   = patterns.getProductRelationPatterns()
    productTitles      = extractProductTitles(pageContent, titlePatterns)
    productSpecs       = extractProductSpecs(pageContent, specsPatterns)
    productRelations   = extractProductRelations(pageContent, relationPatterns)
    return ProductInfo(pageLocation, productTitles, productSpecs, productRelations)