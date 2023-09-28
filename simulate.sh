#!/bin/bash

# Array of SWC files
swc_files=("test2.swc" "test1.swc" "test3.swc" "test4.swc" ...)

# Loop through each SWC file
for swc_file in "${swc_files[@]}"
do
    # Run the simulation in the background
    python 20synapses.py "$swc_file" &
done

# Wait for all simulations to finish
wait