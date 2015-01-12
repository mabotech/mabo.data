


myProp <- read.table("conf.ini", header=FALSE, sep="=", row.names=1, strip.white=TRUE, na.strings="NA", stringsAsFactors=FALSE)

myProp

myProp["a", 1]

myProp["b", 1]

myProp["c", 1]

myPropVec <- setNames(myProp[,1],row.names(myProp))

myPropVec["a"]
myPropVec["b"]
myPropVec["c"]