#Credit and Thanks
#https://www.kaggle.com/datasets/midhundasl/co2-emission-of-cars-dataset
#http://www.sthda.com/english/articles/40-regression-analysis/167-simple-linear-regression-in-r/
#http://www.sthda.com/english/articles/40-regression-analysis/168-multiple-linear-regression-in-r

#install.packages(tidyverse)
#install.packages(ggpubr)
library(tidyverse)
library(ggpubr)

data <- read.csv("DATA.csv")
data$Car <- NULL
data$Model <- NULL
data$X <- NULL
#print(head(data))

#print(cor(data$Volume,data$CO2))#correlation coefficient
#print(cor(data$Weight,data$CO2))
#plot(data$Volume, data$CO2,xlab="Volume",ylab="CO2")
#print(ggplot(data, aes(x = Volume, y=CO2)) + geom_point() + stat_smooth())

model <- lm(CO2 ~ Volume, data=data)
#print(model) #CO2 = 83.75 + 0.01135*Volume
#print(ggplot(data, aes(x = CO2, y=Volume)) + geom_point() + stat_smooth(method=lm))
print(summary(model))
print(100 * sigma(model)/mean(data$CO2))#Error

model2 <- lm(CO2 ~ Volume + Weight, data=data)
#print(model2) #CO2 = 79.69 + 0.007805*Volume + 0.007551*Weight
print(summary(model2))
print(100 * sigma(model2)/mean(data$CO2))