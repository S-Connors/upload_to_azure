# upload_to_azure
Big Data - Lab 1

Using a VM in Azure went to the url below, connected to the API. 
Grabbed the publication date, job title, job type, job location and company name.
Turned this intoa data frame. Transformed it and saved it into Azure blob container


1) Set up a Virtural Machine in Azure 
2) Set up blob storage in Azure
3) Installed AzCopy
    wget https://s3.amazonaws.com/weclouddata/data/data/install-AzCopy.sh
    chmod 400 install-AzCopy.sh
    bash install-AzCopy.sh
4) Test by creating an empty file and uploading to storage container
    touch file1.txt
    azcopy "file1.txt" "<token>" --recursive=true
5) Check storage container to see if the upload was successful
6) Set up virtual enviroment
    sudo apt-get install software-properties-common
    sudo apt-add-repository universe
    sudo apt install python3-virtualenv -y
    virtualenv --python="/usr/bin/python3.8" sandbox
    source sandbox/bin/activate
7) install requirements 
    pip install -r requirements.txt
8) run file
    python3 main.py