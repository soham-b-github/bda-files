library(astsa)

## IN R, INDEXING starts from 1 (ONE)

## READING files
## csv files: read.csv(directory, header=TRUE)
## excel file: read.xlsx(directory, sheet=1) using "openxlsx" package
## excel file: read_excel(file_path) using "readxl" package

######################### Figure 1.01 ##########################

plot(jj, type="o", ylab="Quarterly Earnings per Share",main="Figure 1.01")
## Johnson and Johnson Quarterly Earnings per Share
## ## use help(jj)

######################### Figure 1.02 ##########################

plot(gtemp_both, type="o", ylab="Global Temperature Deviations",main="Figure 1.02")
## Has ocean and land temperature deviations
## Write gtemp. to get more options
## ## use help(gtemp_both)

######################### Figure 1.03 ##########################

plot(speech,main="Figure 1.03")
## Speech Recordings .1 second (1000 points) of the phrase "aaa...hhh"
## use help(speech)

######################### Figure 1.04 ##########################

plot(nyse, ylab="NYSE Returns",main="Figure 1.04")
## New York Stock Exchange
## ## use help(nyse)

######################### Figure 1.05 ##########################

par(mfrow = c(2,1)) # set up the graphics
plot(soi, ylab="", xlab="", main="Southern Oscillation Index")
## The Southern Oscillation Index (SOI) is a standardized index that measures 
## the difference in air pressure between Tahiti and Darwin, Australia.
## use help(soi)

plot(rec, ylab="", xlab="", main="Recruitment")
## In fisheries and ecology, recruitment refers to the number of new individuals
## (fish, in this case) entering a population — typically those that have reached a certain size or age where they become susceptible to being caught or observed in a survey.
## use help(rec)

######################### Figure 1.06 ##########################

par(mfrow=c(2,1), mar=c(3,2,1,0)+.5, mgp=c(1.6,.6,0))
ts.plot(fmri1[,2:5], lty=c(1,2,4,5), ylab="BOLD", xlab="",
          main="Cortex")
ts.plot(fmri1[,6:9], lty=c(1,2,4,5), ylab="BOLD", xlab="",
          main="Thalamus & Cerebellum")
mtext("Time (1 pt = 2 sec)", side=1, line=2)
## fmri1 is a built-in dataset in the astsa package.
## It contains BOLD (Blood Oxygen Level Dependent) signals from fMRI scans.
## use help(fmri)

######################### Figure 1.07 ##########################

par(mfrow=c(2,1))
plot(EQ5, main="Earthquake")
plot(EXP6, main="Explosion")
## use help(EQ5)
## use help(EXP6)

######################### Figure 1.08 ##########################

## WHITE NOISE
w = rnorm(500,0,1) # 500 N(0,1) variates
## MOVING AVERAGE
v = filter(w, sides=2, rep(1/3,3)) # moving average
## sides=2 means two sided moving average or centered moving average
## sides=1 means one sided moving average (causal)
par(mfrow=c(2,1))
plot.ts(w, main="white noise")
plot.ts(v, main="moving average")

######################### Figure 1.09 ##########################

w = rnorm(500,0,1)
# w = rnorm(550,0,1) # 50 extra to avoid startup problems
x = filter(w, filter=c(1,-.9), method="recursive")[-(1:50)]
## filter=c(1,-.9) means x_t = 0.9x_t-1 + w_t
## method="recursive" means AUTOREGRESSIVE process
par(mfrow=c(2,1))
plot.ts(w, main="white noise")
plot.ts(x, main="autoregression")

######################### Figure 1.10 ##########################

set.seed(154) # so you can reproduce the results
w = rnorm(200,0,1); x = cumsum(w) # two commands in one line
wd = w +.2; xd = cumsum(wd)
plot.ts(xd, ylim=c(-5,55), main="random walk")
lines(x); lines(.2*(1:200), lty="dashed")


########################## set.seed() ##########################


## set.seed() fixes the randomness so your results are reproducible.
## It's like setting the same initial conditions for an experiment every time
## you run it.

## The number in set.seed() acts as a key to generate a specific, deterministic
## sequence of random numbers.



set.seed(1)
rnorm(3)

rnorm(5)

set.seed(1)
rnorm(5)

######################### Figure 1.11 ##########################

## EFFECT of WHITE NOISE
cs = 2*cos(2*pi*1:500/50 + .6*pi)
w = rnorm(500,0,1)
par(mfrow=c(3,1), mar=c(3,2,2,1), cex.main=1.5)
plot.ts(cs, main=expression(2*cos(2*pi*t/50+.6*pi)))
plot.ts(cs+w, main=expression(2*cos(2*pi*t/50+.6*pi) + N(0,1)))
plot.ts(cs+5*w, main=expression(2*cos(2*pi*t/50+.6*pi) + N(0,25)))

######################### Figure 1.13 ##########################

## Auto-correlation function
acf(speech,250)

######################### Figure 1.14 ##########################

par(mfrow=c(3,1))
acf(soi, 48, main="Southern Oscillation Index")
acf(rec, 48, main="Recruitment")
ccf(soi, rec, 48, main="SOI vs Recruitment", ylab="CCF")
## Cross-correlation function

######################### Figure 1.15 ##########################

persp(1:64, 1:36, soiltemp, phi=30, theta=30, scale=FALSE, expand=4,
      ticktype="detailed", xlab="rows", ylab="cols",
      zlab="temperature")
## Spatial Grid of Surface Soil Temperatures (data in astsa package)
## A 64 by 36 matrix of surface soil temperatures.

######################### Figure 1.16 ##########################

plot.ts(rowMeans(soiltemp), xlab="row", ylab="Average Temperature")
## Row Means of soiltemp data from astsa package

######################### Figure 1.17 ##########################

fs = abs(fft(soiltemp-mean(soiltemp)))^2/(64*36)
## Fast Discrete Fourier Transform (FFT)
cs = Re(fft(fs, inverse=TRUE)/sqrt(64*36)) 
## ACovF
rs = cs/cs[1,1] 
## ACF

rs2 = cbind(rs[1:41,21:2], rs[1:41,1:21])
rs3 = rbind(rs2[41:2,], rs2)
par(mar = c(1,2.5,0,0)+.1)
persp(-40:40, -20:20, rs3, phi=30, theta=30, expand=30,
      scale="FALSE", ticktype="detailed", xlab="row lags",
      ylab="column lags", zlab="ACF")

