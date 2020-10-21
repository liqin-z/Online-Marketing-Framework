name1 = "hair_dryer"
name2 = "microwave"
name3 = "pacifier"
name = paste("./data/",name1, "_csv.csv",sep= "")


data<-read.csv(name, header = TRUE)
data$star_rating= data$star_rating -1
data = data.frame(data, helpfulness_rating = data$helpful_votes/data$total_votes)
df = data[!is.nan(data$helpfulness_rating),]
write.csv(data, "hair_dryer.csv")

library(ggpubr)
ggqqplot(df$helpfulness_rating)


plot(df$star_rating, df$helpfulness_rating)
plot(df$helpfulness_rating, df$star_rating)

num_star = table(df$star_rating)
num_star_nan = table(data$star_rating)
diff_num_star = num_star_nan - num_star
barplot(table(df$helpfulness_rating))
barplot(table(data$star_rating))

product = data.frame(table(data$product_parent))

rb = data.frame(data$review_body)
# product每个商品的购买频率
product = data.frame(table(data$product_parent))
write.csv(data$review_body, paste(name1,"rb.csv", sep=""))

df2 = df[df$total_votes>5,]
bar = as.data.frame(table(df2$helpfulness_rating))
df2 = as.data.frame(df2$helpfulness_rating)
data_bar = data.frame()

# s = seq(0.1, 1, 0.1)
# for ( i in s){
#   
#   temp = sum(as.numeric(bar$Freq[as.numeric(as.character(bar$Var1))<i & as.numeric(as.character(bar$Var1))>i-0.1]))
#   data_bar = rbind(data_bar, temp)
# }
#hist(data_bar$X2, names.arg = s, main = "Helpfulness Ratio", col = 'grey', xlab = "Ratio range", ylab = "Freq")
hist(df2$helpfulness_rating, main = "Helpfulness Ratio", col = 'gray', xlab = 'Helfulness Ratings')

library(ggplot2)
library(gridExtra)
p1<-ggplot(data=df2, aes(df$helpfulness_rating))+
  geom_histogram(color='white',fill='gray60')+ 
  ylab(label = 'Frequency') +
  xlab(label = 'helpfulness') +
  geom_line(stat='density') 
##---------------------------------top products------------------------------------------
product<-product[order(-product$Freq),]
top_products = product[product$Freq>20,]
bad_products = product[product$Freq<=20,]
id = top_products$Var1[1]

data_top = data[data$product_parent == as.numeric(as.character(id)),]
# nrow(data_top[!is.na(data_top$helpfulness_rating),])
















