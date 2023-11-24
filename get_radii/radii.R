fwp=read.csv("F:/python/PythonProject/neuron/result_test2/output.csv")
library(ggpubr)
p=ggboxplot(fwp,x="branch_order",y="radii",color = "neuron_region")
p+rotate_x_text(angle = 90)+scale_y_log10()

data_x1=subset(fwp,branch_order==1)
max_v=max(data_x1$radii)
print(max_v)

q3_values=tapply(data_x1$radii, data_x1$neuron_region, quantile, probs = 0.75)
print(q3_value)

fwp=read.csv("F:/python/PythonProject/neuron/human/human_tapered_top10_v2_iso/IFG.csv")
p=ggboxplot(fwp,x="branch_order",y="radii",color = "ours_allen")
p+rotate_x_text(angle = 90)+scale_y_log10()
