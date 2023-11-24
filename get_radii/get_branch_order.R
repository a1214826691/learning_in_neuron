args <- commandArgs(trailingOnly = TRUE)
filepath <- args[1]

library(nat)
n <- read.neuron(filepath)

branch_order <- function(n){
  n$d$bo <-NA
  
  for(i in n$EndPoints){
    bo <- 1
    walkid <- i
    while(n$d$Parent[walkid]!=-1){
      if(walkid %in% n$BranchPoints) bo<-bo+1
      walkid <- n$d$Parent[n$d$PointNo == walkid]
    }
    walkid <- i
    while(n$d$Parent[walkid]!=-1){
      if(walkid %in% n$BranchPoints) bo<-bo-1
      n$d$bo[n$d$PointNo == walkid] <-bo
      walkid <- n$d$Parent[n$d$PointNo == walkid]
    }
    n$d$bo[n$d$Parent == -1] <-0
  }
  
  return(n$d$bo)
}

branch_order(n)

library(ggpubr)
radii <- n$d$W
df <-  data.frame(branch_order=branch_order(n),radii=radii)
#ggbarplot(df, 'radii','branch_order', add="mean_se")

output_file <- paste0(filepath, "-output.csv")
write.csv(df, file = output_file, row.names = FALSE)