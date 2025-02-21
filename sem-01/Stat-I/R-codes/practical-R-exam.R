df = read.csv("Data2.csv",header=FALSE)
help("read.csv")
df

colnames(df)
colnames(df) = c("Serial-No","Language","Country")
df
class(df)
table(df)
df1 = df[c("Language","Country")]
df1
counts = table(df1)

newmat = as.matrix(counts)
newmat

class(rownames(newmat))
help(barplot)

barplot(newmat,main = "total expenditure",names.arg = rownames(newmat),xlab = "Languages",
        ylab = "expenditure",col = colors)

Table = as.data.frame(table(df["Language"]))
Table

languages = Table["Language"]
languages = as.list(languages)
class(languages)
languages = languages$Language
languages


Table1 = as.data.frame(table(df["Country"]))
Table1

countries = Table1["Country"]
countries
countries = as.list(countries)
class(countries)
countries
countries = countries$Country
countries


