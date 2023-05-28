#!/bin/bash


date >> /root/90/code/cronjob_Log

file_path="/root/90/proxy/proxy.csv"

if [ -f "$file_path" ]; then
  rm "$file_path"
  echo "File deleted successfully!"
else
  echo "File does not exist."
fi

unique_folder=$(date +"%Y%m%d%H%M%S")

# Create the unique folder
mkdir "/root/90/code/outputs/${unique_folder}"

# Generate unique ID based on date and time
# unique_id=$(date +"%Y%m%d%H%M%S")

# Specify the filename with the unique ID
indexfile_="/root/90/code/outputs/${unique_folder}/index.txt"
freeproxyworld2_="/root/90/code/outputs/${unique_folder}/freeproxy.world2.txt"
proxyhub1_200_="/root/90/code/outputs/${unique_folder}/proxyhub1_200.txt"
proxyhub400_600_="/root/90/code/outputs/${unique_folder}/proxyhub400_600.txt"
freeproxy_world_="/root/90/code/outputs/${unique_folder}/freeproxy.world.txt"
proxyhub200_400_="/root/90/code/outputs/${unique_folder}/proxyhub200_400.txt"


python3 /root/90/code/index.py > "$indexfile_" &
python3 /root/90/code/scraapers/freeproxy.world2.py > "$freeproxyworld2_"&
python3 /root/90/code/scraapers/proxyhub1_200.py > "$proxyhub1_200_"&
python3 /root/90/code/scraapers/proxyhub400_600.py > "$proxyhub400_600_"&
python3 /root/90/code/scraapers/freeproxy.world.py > "$freeproxy_world_"&
python3 /root/90/code/scraapers/proxyhub200_400.py > "$proxyhub200_400_" &