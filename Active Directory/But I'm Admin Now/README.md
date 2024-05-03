# But I'm Admin Now
## NDG/Active Directory


= = = For this flag you will be using the NDG Virual Enviroment = = =

You were able to get the the desktop, but when you try to run something as an Administrator you get prompted for an admin password. You were able to login with your employee login and check lusrmgr. msc and see that the kiosk user is part of the Administrators groups. You must need the users password in order to run anything as admin, I wonder how you will find it. . . 

= = = = = = = = = = = = = = = = = = = = =.

Your employee login is : 

player.one : P@33word

You can logout of the kiosk user by pressing Ctr-Alt-Del
= = = = = = = = = = = = = = = = = = = = =

For this flag you will need to find the kiosk user's password, and submit it in the format below.

selu{PASSWORD}

##
Connection Link : 
**[https://cnalab.selu.edu/](https://cnalab.selu.edu/)**

Value : 100 points

## Hints

### Hint 1
```
How does auto login work on a windows machine?
```

### Hint 2
```
When a user is set to login automaticly, their password is stored in plain text in the regestry. 

[Automatic Logon on Windows](https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon)
```