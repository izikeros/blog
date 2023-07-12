---
Category: note
Date: '2023-07-10'
Modified: '2023-07-12'
Slug: Boosting Productivity and Automation with AppleScript on macOS
Status: published
Tags: macos, automation, script, osascropt, applescript
Title: Boosting Productivity and Automation With AppleScript on macOS
---

## Introduction
In today's fast-paced digital world, maximizing productivity and finding ways to automate tasks are essential skills. macOS provides a powerful tool called AppleScript, which allows users to write scripts and automate various processes. In this blog post, we will explore the capabilities of AppleScript, discuss cool tricks, and highlight its alternatives.

<!-- MarkdownTOC levels="2,3,4" autolink="true" autoanchor="true" -->

- [Getting Started with AppleScript](#getting-started-with-applescript)
- [Increasing Productivity with AppleScript](#increasing-productivity-with-applescript)
	- [Customized Workflow](#customized-workflow)
	- [Application Control](#application-control)
	- [System Automation](#system-automation)
- [Cool Tricks with AppleScript](#cool-tricks-with-applescript)
	- [Displaying Notifications](#displaying-notifications)
	- [Text Manipulation](#text-manipulation)
	- [GUI Automation](#gui-automation)
- [Alternatives to AppleScript](#alternatives-to-applescript)
	- [Automator](#automator)
	- [Hammerspoon](#hammerspoon)
	- [Keyboard Maestro](#keyboard-maestro)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="getting-started-with-applescript"></a>
### Getting Started with AppleScript
AppleScript is a scripting language that enables users to control applications and perform tasks on macOS. It utilizes the `osascript` command-line utility to execute AppleScript code. To begin using AppleScript, open the Terminal on your Mac and enter the desired commands preceded by `osascript -e`.

The osascript website provide examples:

```sh
Open or switch to Safari:  
$ osascript -e 'tell app "Safari" to activate'

Close safari:  
$ osascript -e 'quit app "safari.app"'

Empty the trash:  
$ osascript -e 'tell application "Finder" to empty trash'

Set the output volume to 50%  
$ sudo osascript -e 'set volume output volume 50'

Input volume and Alert volume can also be set from 0 to 100%:  
$ sudo osascript -e 'set volume input volume 40'  
$ sudo osascript -e 'set volume alert volume 75'  

Mute the output volume (True/False):  
$ osascript -e 'set volume output muted TRUE'

Toggle volume muting:  
$ osascript -e 'set volume output muted not (output muted of (get volume settings))'

Toggle system theme:  
$ osascript -e 'tell application "System Events" to tell appearance preferences to set dark mode to not dark mode'

Shut down without asking for confirmation:  
$ osascript -e 'tell app "System Events" to shut down'

Restart without asking for confirmation:  
$ osascript -e 'tell app "System Events" to restart'
```
<a id="increasing-productivity-with-applescript"></a>
### Increasing Productivity with AppleScript
<a id="customized-workflow"></a>
#### Customized Workflow
AppleScript enables you to create personalized workflows by automating repetitive tasks. For example, you can write a script that renames and moves files based on specific criteria, saving you time and effort.

> Example Script 1: **Automating File Organization**
```
tell application "Finder"
    set sourceFolder to choose folder with prompt "Select the source folder"
    set destinationFolder to choose folder with prompt "Select the destination folder"
    set fileList to every file of sourceFolder
    repeat with aFile in fileList
        move aFile to destinationFolder
    end repeat
end tell

```
> This script allows you to select a source folder and a destination folder. It moves all files from the source folder to the destination folder, simplifying your file organization process.

<a id="application-control"></a>
#### Application Control
With AppleScript, you can interact with various macOS applications. You could automate tasks like sending emails, creating documents, or extracting data from spreadsheets, helping streamline your workflow.

>Example Script 2: Creating New Email in Apple Mail
```
tell application "Mail"
    set newMessage to make new outgoing message with properties {subject:"Hello", content:"Just wanted to say hi!"}
    tell newMessage
        make new to recipient at end of to recipients with properties {address:"example@email.com"}
        open
    end tell
end tell
```
> This script automates the process of creating a new email in Apple Mail. It sets the subject and content of the email and adds a recipient, ready for you to send your message swiftly.

<a id="system-automation"></a>
#### System Automation
AppleScript allows you to control system settings and perform actions like changing the display resolution, adjusting volume, or toggling Wi-Fi—all with a single script.

>Example Script 3: Adjusting Display Brightness
```
tell application "System Preferences"
    reveal anchor "displaysDisplayTab" of pane id "com.apple.preference.displays"
    activate
end tell

tell application "System Events"
    tell process "System Preferences"
        tell slider 1 of window 1
            set value to 75 -- Change brightness level (0-100)
        end tell
    end tell
end tell

tell application "System Preferences" to quit
```
> This script opens the Display preferences in System Preferences, adjusts the brightness slider to the desired level, and then closes System Preferences. This allows you to quickly customize your display brightness without navigating through menus.

<a id="cool-tricks-with-applescript"></a>
### Cool Tricks with AppleScript
<a id="displaying-notifications"></a>
#### Displaying Notifications
As discussed earlier, you can use AppleScript to display notifications on the screen. This feature is particularly useful for receiving alerts or reminders during time-sensitive tasks.

>Example Script 4: Notifying Important Task Deadlines
```
display notification "Don't forget to submit the report by 5 PM!" with title "Task Reminder"
```
> This script displays a notification with a reminder for an important task deadline. You can set up similar notifications for time-sensitive activities to keep you on track.

<a id="text-manipulation"></a>
#### Text Manipulation
AppleScript offers powerful text manipulation capabilities. You can automate tasks such as extracting specific information from a text file, finding and replacing text across multiple documents, or formatting text according to predefined rules.

> Example Script 5: Find and Replace Text in Multiple Files
```
set searchText to "oldText"
set replaceText to "newText"

tell application "Finder"
    set folderPath to choose folder with prompt "Select the folder"
    set fileList to every file of folderPath
    repeat with aFile in fileList
        set fileContents to read aFile as «class utf8»
        set modifiedContents to replaceTextInString(fileContents, searchText, replaceText)
        set writeResult to write modifiedContents to aFile as «class utf8»
    end repeat
end tell

on replaceTextInString(textString, oldText, newText)
    set AppleScript's text item delimiters to the oldText
    set textItems to every text item of textString
    set AppleScript's text item delimiters to the newText
    return textItems as text
end replaceTextInString
```
> This script prompts you to select a folder and replaces all occurrences of "oldText" with "newText" in the contents of every file within that folder. This can be useful for batch text replacements across multiple documents.

<a id="gui-automation"></a>
#### GUI Automation
AppleScript can simulate user interactions with graphical user interfaces (GUI). You can automate tasks that involve clicking buttons, selecting options from menus, or filling out forms in applications, saving you from repetitive manual operations.
> Example Script 6: Automating Safari Website Login
```
tell application "Safari"
    activate
    open location "https://example.com/login"
    delay 2 -- Add a delay if needed for the page to load
end tell

tell application "System Events"
    tell process "Safari"
        set frontmost to true
        keystroke "username"
        keystroke tab
        keystroke "password"
        keystroke return
    end tell
end tell
```
> This script automates the process of opening a specific website in Safari, entering a username, password, and submitting the login form. You can adapt this script to automate various web-based actions.
<a id="alternatives-to-applescript"></a>
### Alternatives to AppleScript
While AppleScript is a robust tool, other alternatives can also help achieve automation and productivity on macOS:

<a id="automator"></a>
#### Automator
![automator logo](https://help.apple.com/assets/61E87B255FBFB2628709732E/61E87B275FBFB26287097336/en_GB/573f95d708cbb258343f5c78cc439bcb.png)
[Automator](https://support.apple.com/en-gb/guide/automator/welcome/mac) is a visual automation tool built into macOS. It provides a drag-and-drop interface to create workflows without writing code. Automator supports a wide range of actions and can be an excellent choice for users who prefer a more intuitive approach.
<a id="hammerspoon"></a>
#### Hammerspoon
![Hammerspoon logo](https://www.hammerspoon.org/images/hammerspoon.png) 
[Hammerspoon](https://www.hammerspoon.org/) is a powerful automation tool that uses the Lua scripting language. It offers extensive customization and control over macOS, allowing users to create complex workflows and automation routines.

<a id="keyboard-maestro"></a>
#### Keyboard Maestro
![Keyboard Maestro logo](https://www.keyboardmaestro.com/img/keyboardmaestro-64.png)
[Keyboard Maestro](https://www.keyboardmaestro.com/main/) is a comprehensive automation tool that focuses on keyboard and mouse automation. It provides a user-friendly interface to create macros, trigger actions based on specific events, and automate repetitive tasks efficiently.

<a id="conclusion"></a>
## Conclusion
AppleScript is a versatile tool for increasing productivity and automating tasks on macOS. Its ability to control applications, system settings, and perform various actions make it a valuable asset. Additionally, cool tricks like displaying notifications and GUI automation enhance the overall experience. However, alternatives like Automator, Hammerspoon, and Keyboard Maestro offer different approaches to automation, catering to diverse user preferences. Explore these tools and find the one that best fits your workflow to unlock new levels of productivity and efficiency on your Mac.

## References
- [Introduction to AppleScript Language Guide](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [osascript Man Page - macOS - SS64.com](https://ss64.com/osx/osascript.html)
- [osacompile](https://ss64.com/osx/osacompile.html) - Compile AppleScripts and other OSA language scripts.
