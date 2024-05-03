# Password Dump
## NDG/Active Directory


= = = For this flag you will be using the NDG Virual Enviroment = = =

You've been able to elevate to admin on the Kiosk, and you notice there is an local account that is also on that computer, that happens to be an administrator. I wonder if we can dump and crack the admin account's credentails and use the on the Employee Workstation.  

= = = = = = = = = = = = = = = = = = = = =.
Your Login foir Kali is : 

root : toor

Your employee for Windows is :

player.one : P@33word

= = = = = = = = = = = = = = = = = = = = =

For this flag you will need to find the admin user's password, and submit it in the format below.

selu{PASSWORD}

##
Connection Link : 
**[https://cnalab.selu.edu/](https://cnalab.selu.edu/)**

Value : 200 points

## Hints

### Hint 1
```
You can use share files between 2 machines by either running an apache web server or by creating an SMB Share.
```

### Hint 2
```
I recommend using Mimikatz to dump the Hashes and John the Ripper to crack them. 

[How to use Mimikatz and John](https://sanjumalhotra26.medium.com/dumping-credentials-from-sam-file-using-mimikatz-and-cracking-with-john-the-ripper-and-hashcat-ce5bbf2f4f5a)
```


##
Created and Implimented by Joshua Cantu