####################### SURVIVAL ANALYSIS QUESTIONS ############################

library(survival)
library(survminer)

#----------------------- READING THE DATA---------------------------------------
data = read.csv("LabTestDataSurv.csv")
head(data)
names(data)
str(data)

summary(data)

# ==============================================================================
# Step 1. Preparing Right Censor Data
# ------------------------------------------------------------------------------

Lifetime = data$val                 # Right Censor Survival Data
Status = data$sta
# Censoring indicator variable (1 for complete obs (uncensored), 0 for censored)

# Censor Data
CensorData = data.frame(cbind(Lifetime,Status))      
# Survival Object
SurvObject = Surv(Lifetime,Status)

## BAD = 1; uncensored; event ghote gachhe
## GOOD = 0; censored; event pore ghotbe

# Preparing right-censored data for parametric fit
# left=right for failed and NA for censored
left = Lifetime; 
right = Lifetime;
right[which(Status==0)] = NA 
LRdata = data.frame(cbind(left,right))


# ==============================================================================
# Step 2. Checking Difference between 2 groups
# ------------------------------------------------------------------------------
# Grouping on Gender (male=1 & female=2)
#-------------------------------------------------------------------------------

Group = rep(1,length(Lifetime));
Group[(data$gen=="female")]=2
head(cbind(Lifetime,Status,Group))

par(mfrow=c(1,2))

# Right censored data: graphical comparison of two groups

# KAPLAR-MEIER
KM_G=survfit(Surv(Lifetime,Status)~Group)

plot(KM_G,col=c(1,2),xlab="time",ylab="survival probability",
     xlim=c(0,max(KM_G$time)+1),ylim=c(0,1.05))

legend('topright',c("Male","Female"),lty=c(1,1),col=c(1,2),cex=.6)
title(main='Survival Function Comparison',sub="KM Surv Fn")

# NELSON-AALEN
NA_G=survfit(Surv(Lifetime,Status)~Group,stype=2,ctype=1)
# NA_G=survfit(Surv(Lifetime,Status)~Group)

plot(NA_G$time, NA_G$cumhaz,col=c(1,2),xlab="time",ylab="cumulative hazard",type='s',
     xlim=c(0,max(NA_G$time)+1),ylim=c(0,ceiling(max(NA_G$cumhaz))+.1))

legend('topleft',c("Male","Female"),lty=c(1,1),col=c(1,2),cex=.6)
title(sub="NA Cum Haz")

# Right censored data: statistical comparison of two groups
s1=survdiff(Surv(Lifetime,Status)~Group,rho = 0)           # logrank test
s2=survdiff(Surv(Lifetime,Status)~Group,rho = 1)           # Gehan-Wilcoxon test


# ==============================================================================
# Step 3. Build Cox proportional hazard models Semi-Parametric
#-------------------------------------------------------------------------
# Cox proportional hazards model regression

# Building the coxph model

ResultSP = coxph(SurvObject ~ gen, data=data)     
summary(ResultSP)

BaselineHazard=basehaz(ResultSP)
plot(BaselineHazard$time,BaselineHazard$hazard,type='s',xlab='Time',ylab='Baseline Hazard')

legend('topleft',"H0(t) 1 covariate")
title("Cox's proportional hazard model")


################################## END #########################################
