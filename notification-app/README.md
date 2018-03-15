### Electron notification App.

    #Consist of Azure function API and Javascript/Electron Frontend


    #Azure functions API

    insertcCommentsFromAppHttp.py
    sendNotificationToAppHtpp.py
    SendNotificationToDbaseTrigger.py

    #To install Frontend 
    install electron
    
        npm install electron --save-dev

        cd <into the notification-app root folder>

    #Then Run the command below to install node mdules and package the source into window executable

        powershell.exe .\packager.ps1