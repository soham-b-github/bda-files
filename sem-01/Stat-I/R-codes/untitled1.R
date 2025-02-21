df = read.csv("Data2.csv",header=FALSE)
help("read.csv")
df

df1 = df[c("V2","V3")]
counts = table(df1)
counts

newmat = matrix(counts)
newmat
no_languages = length(colnames(counts))
no_countries = length(rownames(counts))

data=matrix(newmat, nrow=no_countries, ncol = no_languages, byrow = FALSE)
data
data = t(data)
colnames(data) = rownames(counts)
data
rownames(data) = colnames(counts)
data

# colnames(data)=c("Region")
# rownames(data)=c("A","B","C","D","E")
data
barplot(data,col=c('red','magenta','orange','green','blue'),
        border="white",space=0.04,font.axis=2,xlab="group",
        legend.text=rownames(data))
title(main='Proportion of languages with respect to Country',sub='Divided Bar Diagram')
box()

new_data = c()
sums = c()
for (i in colnames(data))
{
  new_data = c(new_data, cumsum(data[,i]))
  sums = c(sums, sum(data[,i]))
  #print(sum(data[,i]))
}

newData = matrix(new_data, nrow = no_languages, ncol=no_countries,byrow=FALSE)
new_data
data[,"Bangla"]
data
newData
colnames(newData) = colnames(data)
rownames(newData) = rownames(data)
newData
#sums

help(range)
sum[2]
sums[2]

j=1
sums[j]

newData1 = matrix(0,nrow=rownames(newData),ncol=colnames(newData))
for (i in 1:length(rownames))
{
  for (j in 1:length(colnames))
  {
    #print(newData[i,j])
    print(j)
    newData[i,j] = newData[i,j]/sums[j]
    #k=k+1;
  }
}

newData
newData[0,1]
