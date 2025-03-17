#!/usr/bin/env Rscript 
#vector 
v = c(9, 4, 3, 5, 2, 7, 6, 10, 8, 1)
v
# concatinate
cat (v, "This string is added")

# data frames are like spreadsheets
df <- data.frame(name=c("Abebeb", "Kebede", "Belete", "Chaltu", "Almaz", "Bulcha"), age=c(22000, 15000, 30000, 25000, 17000, 40000), sex=c("M", "M", "M", "F", "F", "M"))

# view structure of  a dataframe
str(df)
#output:
#  $ name: chr  "Abebeb" "Kebede" "Belete" "Chaltu" ...
#  $ age : num  22000 15000 30000 25000 17000 40000
#  $ sex : chr  "M" "M" "M" "F" ...
summary(df)
# write to a file 
write.csv(df, "writen.csv")
#read from a file
dfd <- read.csv("UN_IdealPoints.csv")
# print(head(dfd))

for (num in df) {
    print("loop")
    print(num)
}
