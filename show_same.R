# 读取CSV文件
data <- read.csv("f:/python/mouse/SameRegion.csv")

x <- data$Region

y1 <- data$Allen
y2 <- data$Ours

# 创建柱状图
barplot(rbind(y1, y2), beside = TRUE, names.arg = x, legend.text = c("Allen", "Ours"))
