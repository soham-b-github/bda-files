#=========================================================================
# Prepare Environment
#-------------------------------------------------------------------------

library(survival)
library(survminer)
library(MASS)

#=========================================================================
# Step 0. Get the data
#-------------------------------------------------------------------------

myCredit=read.csv('GermanCredit.csv')   # Extract the German Credit Data
head(myCredit)        # Have a glimpse of data

#=========================================================================
# Step 1. Preparing Right Censor Data
#-------------------------------------------------------------------------

# Right Censor Survival Data
Lifetime = myCredit$Duration
# Censoring indicator variable (1 for complete obs, 0 for censored)
Status = ifelse(myCredit$Class=="Bad",1,0)

# Data preparation for KM estimation but not for parametric fit

# Censor Data
CensorData = data.frame(cbind(Lifetime,Status))
# Survival Object
SurvObject = Surv(myCredit$Duration,Status)

#=========================================================================
# Step 2. Non-parametric Survival Function/Hazard Estimation
#-------------------------------------------------------------------------

## KAPLAN MEIER estimate of survival function
# stype=1: direct method (i.e. KM) to estimate S(t)
Result = survfit(Surv(Lifetime,Status)~1,
                 CensorData,stype=1)


# NELSON AALEN estimate of survival function
# stype=2,ctype=1: indirect method to estimate S(t) from H(t)
ResultH = survfit(Surv(Lifetime,Status)~1,CensorData,conf.type="plain",
                  stype=2,ctype=1)

par(mfrow=c(1,2))

plot(Result,xlab="time",ylab="Survival probability",ylim=c(0,1),col=1)           
title(main='Figure 7A',sub="KM Surv Fn")

plot(ResultH$cumhaz,xlab="time",ylab="Cumulative hazard",ylim=c(0,3),type="s",col=1)

lines(ResultH$cumhaz+1.96*ResultH$std.err,type="s",lty=2,col=1)
lines(ResultH$cumhaz-1.96*ResultH$std.err,type="s",lty=2,col=1)

title(sub="NA Cum Haz")

#-------------------------------------------------------------------------
# Step 3. Comparison of survival/Hazard functions between groups [KM/NA]
#-------------------------------------------------------------------------

# Grouping on Gender (Male=1 & Female=2)
#---------------------------------------------------------------

Group = rep(1,length(Lifetime));
Group[(myCredit$personal_status_sex.female.divorced==1) | (myCredit$personal_state_sex.female.single==1)]=2
head(cbind(Lifetime,Status,Group))

# par(mfrow=c(1,2))
# Right censored data: graphical comparison of two groups

# KM_G=survfit(Surv(Lifetime,Status)~Group)

# plot(KM_G,col=c(1,2),xlab="time",ylab="survival probability",
#     xlim=c(0,max(KM_G$time)+1),ylim=c(0,1.05))
# legend('topright',c("Male","Female"),lty=c(1,1),col=c(1,2),cex=.6)
# title(main='Figure 7B',sub="KM Surv Fn")

# NA_G=survfit(Surv(Lifetime,Status)~Group,stype=2,ctype=1)
# stype=2 means exp(cum_hazard)
# ctype=1 means NA formula

# plot(NA_G$time[seq(1,32)],NA_G$cumhaz[seq(1,32)],col=c(1),
#     xlab="time",ylab="cumulative hazard",type='s',
#     xlim=c(0,max(NA_G$time)+1),ylim=c(0,ceiling(max(NA_G$cumhaz))+.1))

# lines(NA_G$time[seq(33,55)],NA_G$cumhaz[seq(33,55)],col=c(2),type='s')
 
# legend('topleft',c("Male","Female"),lty=c(1,1),col=c(1,2),cex=.6)
# title(sub="NA Cum Haz")

# Right censored data: statistical comparison of two groups
s1=survdiff(Surv(Lifetime,Status)~Group,rho = 0)           # logrank test
s2=survdiff(Surv(Lifetime,Status)~Group,rho = 1)           # Gehan-Wilcoxon test

#-------------------------------------------------------------------------
# Grouping on skillset (Unskilled=1, Skilled=2 & Highly Skilled=3)
#---------------------------------------------------------------

Group = rep(1,length(Lifetime));
Group[(myCredit$Job.SkilledEmployee==1)]=2
Group[(myCredit$Job.Management.SelfEmp.HighlyQualified==1)]=3

head(cbind(Lifetime,Status,Group))
par(mfrow=c(1,2))

# Right censored data: graphical comparison between groups

KM_G=survfit(Surv(Lifetime,Status)~Group)

plot(KM_G,col=c(1,2,3),xlab="time",ylab="survival probability",
     xlim=c(0,max(KM_G$time)+1),ylim=c(0,1.05))
legend('topright',c("G1=USkl","G2=Skl","G3=HSkl"),lty=c(1,1,1),col=c(1,2,3),cex=.6)
title(main='Figure 7C',sub="KM Surv Fn")

NA_G=survfit(Surv(Lifetime,Status)~Group,stype=2,ctype=1)

plot(NA_G$time[seq(1,26)],NA_G$cumhaz[seq(1,26)],col=c(1),
     xlab="time",ylab="cumulative hazard",type='s',
     xlim=c(0,max(NA_G$time)+1),ylim=c(0,ceiling(max(NA_G$cumhaz))+.1))
lines(NA_G$time[seq(27,57)],NA_G$cumhaz[seq(27,57)],col=c(2),type='s')
lines(NA_G$time[seq(58,77)],NA_G$cumhaz[seq(58,77)],col=c(3),type='s')

legend('topleft',c("G1=USkl","G2=Skl","G3=HSkl"),lty=c(1,1,1),col=c(1,2,3),cex=.6)
title(sub="NA Cum Haz")

# Right censored data: statistical comparison between groups
#All groups at a time
# Between all of them at together [H0:= survival functions of three groups are same]

survdiff(Surv(Lifetime,Status)~Group,rho = 0)           # logrank test
survdiff(Surv(Lifetime,Status)~Group,rho = 1)           # Gehan-Wilcoxon test

#Two groups at a time
# Between skilled and highly qualified

# logrank test
survdiff(Surv(Lifetime[Group!=1],Status[Group!=1])~Group[Group!=1],rho = 0)           
# Gehan-Wilcoxon test
survdiff(Surv(Lifetime[Group!=1],Status[Group!=1])~Group[Group!=1],rho = 1)


#### Between skilled and unskilled

# logrank test
survdiff(Surv(Lifetime[Group!=3],Status[Group!=3])~Group[Group!=3],rho = 0)
# Gehan-Wilcoxon test
survdiff(Surv(Lifetime[Group!=3],Status[Group!=3])~Group[Group!=3],rho = 1)


#### Between unskilled and highly qualified

# logrank test
survdiff(Surv(Lifetime[Group!=2],Status[Group!=2])~Group[Group!=2],rho = 0)
# Gehan-Wilcoxon test
survdiff(Surv(Lifetime[Group!=2],Status[Group!=2])~Group[Group!=2],rho = 1)

################################ END ##########################################
