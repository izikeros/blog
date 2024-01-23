---
Title: Avoid using curl -u “username:secret”!
Slug: avoid-using-curl-u-usernamesecret
Date: 2024-01-20
Modified: 2024-01-20
Status: published
tags: curl, security, shell-history, netrc
Category: note
---

When invoking an endpoint guarded by Basic Authentication, you might resort to the -u username:password feature in curl.

```curl -u "jane@examplewebsite.com:mySecretGuard" http://api.myawesomeapp.com/information```

However, this approach is not the most efficient or secure.

In executing this command, the credentials are archived in your shell history, posing a considerable security threat.

On the bright side, there's a straightforward solution to this issue!

Now you can generate a file in your home directory titled `.netrc` as shown below:

```  
machine api.myawesomeapp.com  
  login jane@examplewebsite.com  
  password mySecretGuard  
```
Afterwards, when running the curl command, just include -n and the credentials will be fetched from the file you just created.

```curl -n http://api.myawesomeapp.com/information```

To give you more context, curl is a command-line tool for getting or sending data using URL syntax. It supports various protocols, including but not limited to HTTP, HTTPS, FTP, and FTPS. Curl is widely used for making API requests.

In addition, the `.netrc` file is a special file that stores login and initialisation information used by the auto-login process. It generally resides in the user's home directory. This file can contain information like the name of the machine to which to connect, and any necessary usernames and passwords.

On a final note, remember that this method works only with the curl command. Other command-line tools may require different approaches to secure authentication. Always prioritise data security by opting for methods that safeguard your login credentials.