---
Category: note
Date: 2021-10-20
Modified: 2023-07-12
Slug: time-tracking-apps
Status: published
Summary: Learn about GTime, a manual time-tracking app that helps professionals log their activities efficiently, paired with ActivityWatch for missed entries, to boost productivity and billable hours tracking.
ai_summary: true
Tags:
  - time
  - tracking
  - time
  - management
  - billing
  - tracing
  - monitoring
  - time
  - monitoring
  - productivity
  - monitoring
  - productivity
Title: Time Tracking Apps
citation_needed: false
todo: None
---
In professional work both in corporation or as freelancer there might be a need to track - how much time you spent on different activities. There are already good apps that helps with that.

# Solution that works best for me

## GTime

Manually log time when starting new activity. Consider using it with free, open source [ActivityWatch](https://activitywatch.net/) that will help you estimate time of activity if you miss something.

[GTime](https://mg.pov.lt/gtimelog/) is simple, might be similar to time tracking "Keep Focused" I used on Windows.

![GTime screenshoot](https://linuxinsider.com/article_images/2019/85896_620x390.jpg)

### quick info on how to use it

> Start the app and type in "arrived." After finishing each activity throughout the workday, enter the name of the activity in the GTimeLog prompt.
>
> Naming the activity at the end of working on the task is a key principle. Activities, in general, are categorized as two types. One type is `tasks` that count as billable work. The other type does not. To indicate which activities are not billable, add two asterisks to the activity name. The program calculates your time expenditures and creates an activity report that shows how much time you have spent working and taking breaks.
>
> GTimeLog is loaded with high-end features. For instance, it stores the time log in a simple plain text file. You can edit it by choosing Edit log from the menu (or pressing Ctrl-E). Every line contains a timestamp and the name of the activity that ended at the time. All other lines are ignored, so you can add comments.
>
> The application uses simple configuration options. These include commands to flag specific activities as not related to work, and the option to omit them completely in daily reports.
>
> The display involves three basic views. The first shows all the activities in chronological order, with starting and ending times. The second view groups all entries with the same title into one activity and just shows the total duration. The third view groups all entries from the same categories into one line with the total duration.
>
> GTimeLog lacks a built-in sync system between multiple machines. The workaround is to put its files into Dropbox and create a symlink.
>
> Download GTimeLog from the Python Package Index using this terminal command: `pip install gtimelog` Packages are available in Debian and Ubuntu formats. The released version is notably outdated

## ActivityWatch

open source, privacy-first, cross-platform, and a great alternative to services like RescueTime, ManicTime, and WakaTime.

It can be used to keep track of your productivity, time spent on different projects, bad screen habits, or just to understand how you spend your time.

![ActivityWatch screenshoot 1](https://activitywatch.net/img/screenshot-v0.9.3-activity.png)
![ActivityWatch screenshoot 2](https://activitywatch.net/img/screenshot-v0.8.0b9-timeline.png)

# Alternatives

Alternatives from [linuxinsider](https://linuxinsider.com/story/8-great-linux-time-tracker-apps-to-keep-you-on-task-85896.html):

1. [Hamster](https://projecthamster.wordpress.com/about/) - standard in this category of software but for some reason I decided to use replacement: GTime.
2. [Rachota Timetracker](http://rachota.sourceforge.net/en/index.html) - portable, similar to hamster
3. [ARBTT]() - automated tracking open windows. “Automatic Rule-Based Time-Tracker.” The program recognizes active windows and tracks how long they are open. It calculates that time interval.
4.  [Flowkeeper](https://flowkeeper.org/) - planning, execution & tracking

Rest:

- KTimeTracker: Outdated, but Flexible and Simple
- GnoTime: Tracking Tool Plus
- TimeSlotTracker: Unconventional Yet Useful
- JTimeSched: Lean Design Meets Intuitive Style
- Kimai: open-source time-tracking for teams and individuals.
- Fanurio: time-tracking and billing app for freelancers.
- actiTIME: time-tracking and work management system.

Here’s more information about these tools:
<https://www.actitime.com/productivity-tools/linux-timesheet>

> In the past, on Windows machine I used ManicTime for some time (when it was free).

## Poor-man's solution

Poor-man's solution might be automating capturing screen shoots periodically (e.g. every 5min) and then you can manually browse them and restore your activity in given day. Pros of this solution is that capturing the raw data (screenshots) might be fully automated, run in the background and do not need any involvement from your side. Cons is that you need to process the screenshots.

up::[[MOC_Living]]
up::[[MOC_Job]]
