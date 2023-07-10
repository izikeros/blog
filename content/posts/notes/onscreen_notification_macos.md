---
Title: Display a Notification on the Screen in macOS
Slug: display-a-notification-on-the-screen-in-macos
Date: 2023-07-10
Modified: 2023-07-10
Status: published
Tags: macos, notification, pop-up-window
Category: note
---
up::[[MOC_macOS]]

To display a notification on the screen near the menu bar in macOS using the terminal, you can make use of the `osascript` command to execute AppleScript code. Here's an example command you can run:

```bash
osascript -e 'display notification "Hello, World!" with title "Notification"'
```

This command will display a notification with the message "Hello, World!" and the title "Notification" near the menu bar on macOS.

You can customize the message and title by modifying the strings inside the double quotes in the `osascript` command.

Note that starting from macOS Big Sur (11.0), AppleScript-based notifications require user authorization. The first time you run this command, you will be prompted to grant permission to Terminal (or whichever application you are using) to send notifications.

## reading
- [What is Osascript?. Learning about Osascript started with… | by Victor Scholz | Medium](https://victorscholz.medium.com/what-is-osascript-e48f11b8dec6)
- [osascript Man Page - macOS - SS64.com](https://ss64.com/osx/osascript.html)
