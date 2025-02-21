#########################################################################
#########################################################################
#                       Data IO in R [6]
#########################################################################
#########################################################################
# =======================================================
# Data Importing-Export from/to Terminal
# =======================================================
# Terminal Input
# -------------------------------------------------------

# file = read.xlsx("D:\Soham-Bhattacharya\1-College\3-RKMVERI\1-Semester-01\Stat-1\Correlation.xlsx")
help(cat)
input = scan()
numeric_input = scan()                                      # Numeric input (by default)
charecter_input = scan("",what = "char")                    # Character input
string_input=readline(prompt = "Please enter your input:")  # String input
# -------------------------------------------------------
# Terminal Output
# -------------------------------------------------------
print(5)                    # Single output
cat(5,"abc","123\n","ab")   # Multiple output
# =======================================================
# Data Importing From File
# =======================================================
# Reading from .txt file 
# -------------------------------------------------------
# By default Header adjusted, sep="", fill=False
shpData = read.table("Shopt.txt")
class(shpData)

  # Variant:- different delimiter, changed to NA, will take unequal length of data
  shpData1 = read.table("Shopt1.txt",sep = ":",
                       na.strings = "Blank")            #Error
  shpData1 = read.table("Shopt1.txt",sep = ":",
                        na.strings = "Blank",fill=TRUE) #No Error
  print(shpData1$V5)    # Factor
  # Variant:- make factor to string
  shpData1 = read.table("Shopt1.txt",sep = ":",
                       na.strings = "Blank",fill=TRUE,stringsAsFactors=FALSE)
  print(shpData1$V5)    # String
  # Variant Delimiter:- by default header=T; fill=T and sep=tab, only
  shpData1 = read.delim("Shopt.txt",header = FALSE)
# -------------------------------------------------------
# Reading .csv file
# -------------------------------------------------------
# By default Header adjusted, sep="", fill=True
advData <- read.csv("Advertising.csv",header = FALSE)  
  # Reading .csv file from web
advData <- read.csv("trial.csv",header = TRUE)
class(advData)
advData
class(advData$Households_in_occupied_private_dwellings)
# -------------------------------------------------------
# Reading from .xlsx file
# -------------------------------------------------------
library(readxl)
help(readxl)
shpData <- read_excel("Correlation.xlsx")
class(shpData)
shpData

# mean of variable x from shpData
mean(shpData$x)
shpData$x
X = as.integer(shpData$x)
indices_to_be_removed = which(is.na(X))
indices_to_be_removed
X = X[-indices_to_be_removed]
X
# =======================================================
# Data Exportation to File
# =======================================================
# Writing to .txt file (Tab Delimited Text File):
# -------------------------------------------------------
write.table(advData,paste(getwd(),"/outdata.txt",sep=""), sep="\t")
  # Variant:- Sl Number is discarded
  write.table(advData,paste(getwd(),"/outdata.txt",sep=""), 
            sep="\t",row.names = F,col.names = F)
# -------------------------------------------------------
# Writing to .csv file
# -------------------------------------------------------
write.table(advData,paste(getwd(),"/outdata.csv",sep=""),sep=",")
  # Variant:- Sl Number is discarded
  write.table(advData,paste(getwd(),"/outdata.csv",sep=""),sep=",",
              row.names=F,col.names = F)
# -------------------------------------------------------
# Writing to .xlsx file
# -------------------------------------------------------
write.xlsx(advData,paste(getwd(),"/outdata.xlsx",sep=""),sheetName = "Sheet1")
  # Variant:- Sl Number is discarded
  write.xlsx(advData,paste(getwd(),"/outdata.xlsx",sep=""),sheetName = "Sheet1",
             row.names=F,col.names = F)
# =======================================================
# Data Importing from Web
# =======================================================
# Scrape Table from Web
# -------------------------------------------------------
# system('defaults write org.R-project.R force.LANG en_US.UTF-8')  
library(XML)
library(bitops)
library(RCurl)
library(rlist)
# Singapore Wikipedia  
sngurl <- "https://en.wikipedia.org/wiki/Singapore"
sngurlData <- getURL(sngurl)
tables <- readHTMLTable(sngurlData,which = 2)
# India Election Commission
elcurl <- "http://eciresults.nic.in"
elcurlData <- getURL(elcurl)
tables <- readHTMLTable(elcurlData,which = 1,stringsAsFactors = FALSE)
  # Sanitize the table for clarity
GoaResults <- tables[seq(19,26),-5]
ManResults <- tables[seq(31,39),-5]
PunResults <- tables[seq(44,50),-5]
UtpResults <- tables[seq(55,65),-5]
UtkResults <- tables[seq(70,74),-5]
# -------------------------------------------------------
# Scraping Data from Web-page to creat Table
# -------------------------------------------------------
library(xml2)
library(rvest)
#Reading the web page
mywebpage=read_html("http://www.imdb.com/search/title?count=100&release_date=2016,2016&title_type=feature")
mywebpage
#Extracting rank node from web page
MovieRank=html_nodes(mywebpage,'.text-primary')
#Converting the ranks into text  and then to numerical
MovieRank_text=html_text(MovieRank)               
MovieRank_numeric=as.numeric(MovieRank_text)  

#Reading Title of the movies.
Title = html_nodes(mywebpage,".lister-item-header a")
#Converting the title data to text
Title_text = html_text(Title)                     

#Reading Rating of a movie
Rating = html_nodes(mywebpage,'.ratings-imdb-rating strong')
#Converting the ratings data to text and then to numerical
Rating_text = html_text(Rating)
Rating_Numeric = as.numeric(Rating_text)

#Reading votes for a movie
Votes = html_nodes(mywebpage,'.sort-num_votes-visible span:nth-child(2)')
#Converting the votes data to text
votes_text = html_text(Votes)
#Data-Preprocessing: removing commas
votes_data = gsub(",","",votes_text)
#Data-Preprocessing: converting votes to numerical
votes = as.numeric(votes_data)

#Preparing data frame
MData<-data.frame(Rank = MovieRank_numeric, Title = Title_text, Rating = Rating_Numeric, Votes = votes)

  # Inaddition
  #Reading metascore for movie
  metascore_data = html_nodes(mywebpage,'.metascore')
  #Converting metascore node to text.
  metascore_text = html_text(metascore_data)
  #Adding NA to correct places.
  for (i in c(10,18,28,47,53))
  {
    m1 = metascore_text[1:(i-1)]
    m2 = metascore_text[i:length(metascore_text)]
    metascore_text = append(m1,list("NA"))
    metascore_text = append(metascore_text,m2)
  }
  #Converting metascore to numerical
  metascore = as.numeric(metascore_data)
  summary(metascore)