data<-read.csv('/Users/siyinm/Documents/MCM2020/data/sentiment/origin/hair_dryer/131415.csv', header = TRUE)
# data<-read.csv('/Users/siyinm/Documents/MCM2020/data/microwave_csv.csv', header = TRUE)
# data<-read.csv('/Users/siyinm/Documents/MCM2020/data/pacifier_csv.csv', header = TRUE)
# data = data[c(1:5000),]
product = data.frame(table(data$product_parent))
product<-product[order(-product$Freq),]
top_products = product[product$Freq>1,]
write.csv(top_products, file = "temp.csv")
top<-read.csv('temp.csv', header = TRUE)

t = data.frame(mean = rep(0, nrow(top)))
top = cbind(top, t)



for (val in top$Var1){
  temp = data[data$product_parent==val,]
  m = mean(temp$star_rating)
  top[top$Var1 == val,]$mean = m
  # df= rbind(df,data[data$product_parent==val,])
}
write.csv(top, file = "temp.csv")
top<-read.csv('temp3.csv', header = TRUE)

# plot(top$mean, top$Freq, xlim = c(5, 1), xlab = 'Average Star Ratings', ylab = 'Amount of Reviews',main = 'Hair Dryer')




fit <- lm(top$Freq ~ poly(top$mean, 3, raw=TRUE))
p = data.frame(mean = top$mean, val = fit$fitted.values)
p = p[order(p$mean),]
plot(p$mean, p$val,col = 'red',type = 'l',xlim = c(5, 1), xlab = 'Average Star Ratings', ylab = 'Amount of Reviews', ylim = c(1, 500))
points(top$mean, top$Freq)
