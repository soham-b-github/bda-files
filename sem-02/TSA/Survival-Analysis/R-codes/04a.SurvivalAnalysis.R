#=========================================================================
# Prepare Environment
#-------------------------------------------------------------------------
library(survival)
library(MASS)
library(fitdistrplus)
#=========================================================================
# Step 0. Get the data
# Here in R-code as per Sir, Bad==1
# In the dataset, Bad==0
#-------------------------------------------------------------------------

myCredit=read.csv("GermanCredit.csv")   # Extract the German Credit Data
head(myCredit)        # Have a glimpse of data
names(myCredit)       # the column names of the data
str(myCredit)         # types of variables

summary(myCredit)     # descriptive statistics

#=========================================================================
# Step 1. Preparing Right Censor Data
#-------------------------------------------------------------------------

Lifetime = myCredit$Duration                 # Right Censor Survival Data
# Status = ifelse(myCredit$Class=="Bad",1,0)    
# Censoring indicator variable (1 for complete obs, 0 for censored)

Status = ifelse(myCredit$Class=="Bad",1,0)
# Data preparation for AFT parametric fit

# Censor Data
CensorData = data.frame(cbind(Lifetime,Status))      
# Survival Object
SurvObject = Surv(myCredit$Duration,Status)

## BAD = 1; uncensored; event ghote gachhe
## GOOD = 0; censored; event pore ghotbe

# Preparing right-censored data for parametric fit
# left=right for failed and NA for censored
left = Lifetime; 
right = Lifetime; 
right[which(Status==0)] = NA 
LRdata = data.frame(cbind(left,right))


#=========================================================================
# Step 3a. Parametric Survival Function Estimation without Co-variate
#-------------------------------------------------------------------------

# Parametric estimate of survival function
FitG = fitdistcens(LRdata,"gamma"); ShapeG = FitG$est[1]; RateG = FitG$est[2]
FitW = fitdistcens(LRdata,"weibull"); ShapeW = FitW$est[1]; ScaleW = FitW$est[2]
FitLN = fitdistcens(LRdata,"lnorm"); LocationLN=FitLN$est[1]; ShapeLN = FitLN$est[2]

library(actuar)

FitLL = fitdistcens(LRdata,"llogis"); ShapeLL = FitLL$est[1];   ScaleLL = FitLL$est[2]

par(mfrow=c(1,1))

trange = (0:max(na.omit(LRdata[,2])))                 # 0 to maximum failure time

# gamma MLE
plot(trange,1-pgamma(trange, shape = ShapeG, rate = RateG),xlab="Time", 
      ylab="Survival probability",ylim=c(0,1),col=2,type='l')

# Weibull MLE
lines(trange,1-pweibull(trange, shape = ShapeW, scale = ScaleW),col=4)

# lognormal MLE
lines(trange,1-plnorm(trange,meanlog = LocationLN,sdlog = ShapeLN),col=6)

# loglogistic MLE
lines(trange,1-pllogis(trange, shape = ShapeLL, scale = ScaleLL),col=8)

title("Figure 4")
legend('bottomleft',c("gamma MLE-S(t)","Weibull MLE-S(t)","log-Normal MLE-S(t)",
                      "log-Logistic MLE-S(t)"),lty=c(1,1,1,1),col=c(2,4,6,8),cex=.8)

#=========================================================================
# Step 3b. Parametric Survival Function Estimation using Covariate 
# [Regression for right censored data]

#-------------------------------------------------------------------------
# Weibull regression

ResultW = survreg(SurvObject ~ Age+Amount+InstallmentRatePercentage+
                    NumberExistingCredits+NumberPeopleMaintenance, data=myCredit, dist="weibull") 
summary(ResultW)


ResultW = survreg(SurvObject ~ Age+Amount+InstallmentRatePercentage, data=myCredit,
                  dist="weibull") 
summary(ResultW)
1/summary(ResultW)$scale      # shape parameter

#-------------------------------------------------------------------------
# lognormal regression

ResultLN = survreg(SurvObject ~ Age+Amount+InstallmentRatePercentage+
                     NumberExistingCredits+NumberPeopleMaintenance, data=myCredit, dist="lognormal")
summary(ResultLN)
ResultLN = survreg(SurvObject ~ Age+Amount+InstallmentRatePercentage, 
                   data=myCredit, dist="lognormal")
summary(ResultLN)

#-------------------------------------------------------------------------
# loglogistic regression

ResultLL = survreg(SurvObject ~ Age+Amount+InstallmentRatePercentage+
                     NumberExistingCredits+NumberPeopleMaintenance, data=myCredit, dist="loglogistic")
summary(ResultLL)
ResultLL = survreg(SurvObject ~ age+amount+installment_rate, 
                   data=myCredit, dist="loglogistic")
summary(ResultLL)


################################# END #########################################