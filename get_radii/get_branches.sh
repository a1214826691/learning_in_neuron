#!/bin/bash
#SBATCH --job-name=PythonTest
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=30
#SBATCH --partition=debug

# load the environment

# run python
/public/home/ynhang/gnn/anaconda3-2021/bin/python --version

#Clear the output file
#echo "branch_order,radii"> output.csv

#print current directory
pwd
nproc

# Array of swc files
swc_files=(*.swc)

# Loop through each swc file
for swc_file in "${swc_files[@]}"
do
    #echo $swc_file
    echo "branch_order,radii">"$swc_file"-output.csv
    python get_radii_branch.py "$swc_file" &
done

# Wait for all simulations to finish
wait

