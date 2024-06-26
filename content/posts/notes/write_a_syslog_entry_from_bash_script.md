---
Category: note
Date: '2022-09-02'
Modified: '2023-07-12'
Slug: write-a-syslog-entry-from-a-bash-script
Status: published
Summary: Instruction on how to write a message to system log from the bash script using logger-utility
Tags: bash, log, logging, syslog
Title: Write a Syslog Entry From a Bash Script
---
If you want your bash script to write message to syslog you can use `logger` utility. Here is an example of usage.

```sh
logger -t runonce -p local3.info "$file"
```

where:

- `-t` is a tag for the line
- `-p` priority (`local3.info` - INFO level message)
- the last argument `"$file"` is the message

For more information see the man page for `logger`:

```
LOGGER(1)                                                                                   General Commands Manual                                                                                   LOGGER(1)

NAME
     logger – make entries in the system log

SYNOPSIS
     logger [-is] [-f file] [-p pri] [-t tag] [message ...]

DESCRIPTION
     Logger provides a shell command interface to the syslog(3) system log module.

     Options:

     -i       Log the process id of the logger process with each line.

     -s       Log the message to standard error, as well as the system log.

     -f file  Log the specified file.

     -p pri   Enter the message with the specified priority.  The priority may be specified numerically or as a ``facility.level'' pair.  For example, ``-p local3.info'' logs the message(s) as informational
              level in the local3 facility.  The default is ``user.notice.''

     -t tag   Mark every line in the log with the specified tag.

     message  Write the message to log; if not specified, and the -f flag is not provided, standard input is logged.

     The logger utility exits 0 on success, and >0 if an error occurs.

EXAMPLES
           logger System rebooted

           logger -p local0.notice -t HOSTIDM -f /dev/idmc

SEE ALSO
     syslog(3), syslogd(8)

STANDARDS
     The logger utility conforms to IEEE Std 1003.2-1992 (“POSIX.2”).

BSD 4.3
```

up::[[MOC_Shell_Bash_Zsh]]
up::[[MOC_Linux]]
