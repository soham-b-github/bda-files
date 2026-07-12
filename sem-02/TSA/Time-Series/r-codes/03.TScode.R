# setwd("/SUDIPTA RKMV University/Time Series/CodeClass")



############################# HYPOTHESIS ################################
# H_0 : The data are independent and identically distributed (i.i.d.) 
#       → No autocorrelation up to the given lag.
# H_1 : The data are not i.i.d.
#       → some autocorrelations are non-zero up to the specified lag.


#########################################################################
# Simple Random Process
#########################################################################
# -----------------------------------------------------------------------
# Bernoulli iid
# -----------------------------------------------------------------------

b = (2*rbinom(500,1,0.5)-1)
par(mfrow=c(2,1))
plot.ts(b, main="binary process")                   # stationary
s = cumsum(b)
plot.ts(s, main="simple random walk")               # non-stationary

# -----------------------------------------------------------------------
# White Noise
# -----------------------------------------------------------------------

w = rnorm(500,0,1)
par(mfrow=c(2,1))
plot.ts(w, main="white noise")                      # stationary

# Random Walk
r = cumsum(w)
plot.ts(r, main="random walk")                      # non-stationary



#########################################################################
# Checking hypothesis of IID processes (randomness)
#########################################################################
# -----------------------------------------------------------------------
# White Noise
# -----------------------------------------------------------------------


t=seq(1:200);set.seed(12)
xt = rnorm(200,0,.5)                        # White noise
par(mfrow=c(3,1))
plot(t/10,xt, main="WhiteNoise")         

# check ACF
acf(xt,lag.max = 40)      

# all ACF together (sum of std normal i.e., chi-square)
Box.test(xt, lag = 40, type = "Ljung-Box", fitdf = 0)  


library(randtests)

# [y(i-1)<y(i)>y(i+1) or y(i-1)>y(i)<y(i+1)] testing of IID hypothesis
turning.point.test(xt)       

# # [y(i)<y(i+1)] testing of no trend hypothesis
# difference.sign.test(xt)                              
# # [y(i)<y(j)] testing of no trend hypothesis
# rank.test(xt)   
# qq plot testing for normality

qqnorm(xt)


# Shapiro Francia (checking of normality)
library(nortest)
sf.test(xt)

# Shapiro Wilk (checking of normality)
# shapiro.test(xt)
# # checking of normality
# ks.test(xt, "pnorm")


#########################################################################
#########################################################################
# Checking hypothesis of IID processes (randomness)
#########################################################################
# -----------------------------------------------------------------------
# Signal plus Noise
# -----------------------------------------------------------------------

t=seq(1:200);set.seed(12)
xt = t/2+cos(t/10*pi/180)+rnorm(200,0,.5)      # Mixing signal and noise
par(mfrow=c(3,1))
plot(t/10,xt, main="Signal plus Noise")         
# check ACF 
acf(xt,lag.max = 40)      
# all ACF together (sum of stzd normal i.e., chi-suare)
pacf(xt,lag.max = 40)

Box.test(xt, lag = 40, type = "Ljung-Box", fitdf = 0)  
library(randtests)
# [y(i-1)<y(i)>y(i+1) or y(i-1)>y(i)<y(i+1)] testing of iid ness

turning.point.test(xt)       
# # [y(i)<y(i+1)] testing of iid ness
# difference.sign.test(xt)                              
# # [y(i)<y(j)] testing of iid nes
# rank.test(xt)   

# qq plot
qqnorm(xt)
# Shapiro Francis (checking of normality)
sf.test(xt)
# Shapiro Wilk (checking of normality)
shapiro.test(xt)
# # checking of normality
# ks.test(xt, "pnorm")                                  
#########################################################################