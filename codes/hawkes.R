library(lubridate)
name = '732252283'
data<-read.csv('/Users/siyinm/Documents/MCM2020/hd131415.csv', header = TRUE)
#data<-read.csv('/Users/siyinm/Documents/MCM2020/data/sentiment/origin/hair_dryer/131415.csv', header = TRUE)
N = nrow(data[data$product_parent==name, ])
df = data[data$product_parent==name, ]

df = df[df$total_votes>0,]

df$review_date = as.Date(df$review_date)
df = df[year(df$review_date)>=2015,]


df = cbind(df,temp = df$review_date )
df$temp[2:nrow(df)] = df$review_date[1:nrow(df)-1]

df$date_diff <- as.Date(as.character(df$temp))-
  as.Date(as.character(df$review_date))

x = df$date_diff
y = df$total_votes

plot(df$review_date, y, pch =16, cex = 0.7,xlab = 'Time', ylab = 'Total Vote for Helpfulness')
for (i in seq(1, nrow(df))){
  segments(df$review_date[i], 0, x1 = df$review_date[i], y1 = df$total_votes[i] ,lty = 3)
}
df$count<- seq( nrow(df),1,-1)
plot(df$review_date, df$count, pch = 16, cex =0.7, xlab = 'Time', ylab = 'Amount of Review')
points(df$review_date[2:nrow(df)-2], seq(nrow(df)-1, 2, -1), cex =0.5)
for (i in seq(, nrow(df)-2)){
  segments(df$review_date[i], df$count[i]-1, x1 = df$review_date[i+1], y1 = df$count[i]-1 ,lty = 1)
}
