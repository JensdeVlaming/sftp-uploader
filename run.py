import pysftp

# ADDRESS OF SERVER
ip = '<HOST>'

# PORT OF SERVER
port = '<PORT>'

# USERNAME OF SERVER
username = '<USERNAME>'

# PASSWORD OF SERVER
password = '<PASSWORD>'

with pysftp.Connection(host=ip, username=username, password=password, port=port) as sftp:
    
    print('Connection succesfully stablished ... ')
    
    # File on localhost
    fileLocal = input('Define the file that you want to upload from your local directorty: ')

    # Path waar het bestand moet komen te staan
    pathServer = input('Define the remote path where the file will be uploaded: ')

    sftp.put(fileLocal, pathServer)
    print('Succesfully uploaded file from local directory to remote server ... ')