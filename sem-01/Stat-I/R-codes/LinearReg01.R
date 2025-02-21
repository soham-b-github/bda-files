# =======================================================
# Simple Linear Regression
# =======================================================
# ------ Exploration for Regression line
# -------------------------------------------------------
V_x=seq(0.1,2,.1)
I_o=0.001
n=length(V_x)
# R=1/3;C=1/R;(I_y=I_o+C*V_x+rnorm(n,0,.8))
I_y=c(1.2356944, 0.6222869, 1.5367321, 0.8726905, 1.2445278, 2.7061478,
      3.3503630, 3.3157266, 1.9141435, 2.2689164, 3.4973482, 4.7011925,
      2.8814472, 4.3415420, 4.1035050, 4.5308454, 4.5518887, 5.9140701,
      5.3923533, 6.6609229)    
datasheet=data.frame(V_x,I_y)
datasheet
plot(V_x,I_y,xlab = 'Voltage',ylab = 'Current',col='blue',ylim = c(-1,9))
beta0=0.001
beta1=1                             # Three Choices 1, 2, 4
abline(a=beta0,b=beta1,col='black')     # Possible lines 
title(main=paste('Current=',beta0,"+",beta1,"*Voltage"))
I_hat_y=beta0+beta1*V_x
points(V_x,I_hat_y,col='green')
legend("topleft",legend=c('Observed Current value (I_y)',expression(paste('Predicted Current value (I_',hat(y),')'))), cex=1,bg='transparent',box.lty = 0,fill=c('blue','green'))            # add legend to chart
segments(x0=V_x,y0=I_y,x1=V_x,y1=I_hat_y,lty=2)
title(sub=paste('RSS=',round(sum((I_y-I_hat_y)^2),3)))
# -------------------------------------------------------
# ------ Regression Analysis in R
# -------------------------------------------------------
plot(V_x,I_y,xlab = 'Voltage',ylab = 'Current',col='blue',ylim = c(-1,9))
# lines(x=V_x,y=I_o+(1/R)*V_x,col='magenta',lwd='3')
beta1hat=sum((I_y-mean(I_y))*(V_x-mean(V_x)))/sum((V_x-mean(V_x))^2);print(beta1hat)
beta0hat=mean(I_y)-beta1hat*mean(V_x);print(beta0hat);
abline(c(beta0hat,beta1hat), col='blue', lwd="2")
title(main = paste("I_y = ",round(beta0hat,3),"+",round(beta1hat,3),"*V_x"))
lmY <- lm(I_y ~ V_x, data = data.frame(V_x,I_y))
lmY$coefficients
# -------------------------------------------------------
# ------ Exploring Output of Regression in R
# -------------------------------------------------------
I_hat_y=lmY$fitted.values   #(=lmY$coefficients[1]*V_x)
points(V_x,I_hat_y,col='green')
segments(x0=V_x,y0=I_y,x1=V_x,y1=I_hat_y,lty=2)
E_yx=lmY$residuals          #(=I_y-I_hat_y)
plot(V_x,E_yx,col='red',ylab='Residuals');abline(h=0)
RSS=sum(E_yx^2);print(RSS)
RSE=sqrt(RSS/(n-2));print(RSE)
TSS=sum((I_y-mean(I_y))^2);print(TSS)
Multi_R2=1-RSS/TSS;print(Multi_R2)

summary(lmY)
SE=RSE/sqrt(sum(V_x*V_x)-n*mean(V_x)^2);print(SE)

R=1/3
C=1/R
# For Unbiasedness and CI
NoOfIteration=1000
lmCoef=array(0,NoOfIteration)
TrueBeta1inRange=array(0,NoOfIteration)
for (i in 1:NoOfIteration) 
{
  I_yin=I_o+C*V_x+rnorm(length(V_x),0,.8)
  lmYin <- lm(I_yin ~ V_x, data = data.frame(V_x,I_yin))
  lmCoef[i]=lmYin$coefficients[2]
  if(coef(summary(lmYin))[2,"Estimate"]-2*coef(summary(lmYin))[2,"Std. Error"]<C 
     & C<coef(summary(lmYin))[2,"Estimate"]+2*coef(summary(lmYin))[2,"Std. Error"] )
    TrueBeta1inRange[i]=1
}
mean(lmCoef)            # Sample Mean
mean(TrueBeta1inRange)  # % of CI containing true value

plot(V_x,I_y,col='black')
abline(lmY,col='blue')
col_arr=c('red','yellow')
for(i in c(-3,-2,2,3))
{
  abline(a=coef(summary(lmY))[1,"Estimate"],b=coef(summary(lmY))[2,"Estimate"]
         +i*coef(summary(lmY))[1,"Std. Error"],col=col_arr[4-abs(i)])
}
legend("topleft",legend=c('Point Estimate','95% CI','99% CI'), cex=1,bg='transparent',box.lty = 0,fill=c('blue','yellow','red'))            # add legend to chart
# =======================================================