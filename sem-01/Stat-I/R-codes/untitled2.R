df = read.csv("Data2.csv",header=FALSE)
help("read.csv")
df

df1 = df[c("V2","V3")]
counts = cumsum(table(df1))
counts

newmat = matrix(counts)
newmat
no_languages = length(colnames(table(df1)))
no_countries = length(rownames(table(df1)))

data=matrix(newmat, nrow=no_countries, ncol = no_languages, byrow = FALSE)
data
#data = t(data)
colnames(data) = rownames(table(df1))
data
rownames(data) = colnames(table(df1))
data

# colnames(data)=c("Region")
# rownames(data)=c("A","B","C","D","E")
data
barplot(data,col=c('red','magenta','orange','green','blue'),
        border="white",space=0.04,font.axis=2,xlab="group",
        legend.text=rownames(data))
title(main='Proportion of languages with respect to Country',sub='Divided Bar Diagram')
box()

cumsum(data)
data
