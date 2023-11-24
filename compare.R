library(ggpubr)

# 从两个 CSV 文件中加载数据
ours_df = read.csv("F:/python/mouse/mouse_neurons_preprocessed_output.csv")
allen_df = read.csv("F:/python/mouse/allen_mouse_output.csv")


# 为每个数据帧添加一个新列，以标记数据来源
ours_df$source <- "ours"
allen_df$source <- "allen"
head(ours_df)
head(allen_df)
# 合并两个数据帧
combined_df <- rbind(ours_df, allen_df)

# 使用 ggplot 绘制箱线图
p=ggboxplot(fwp,x="branch_order",y="radii",color = "source")
p+rotate_x_text(angle = 90)+scale_y_log10()
