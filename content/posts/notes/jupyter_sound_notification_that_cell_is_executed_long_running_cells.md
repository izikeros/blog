---
Title: Audio Notifications in Jupyter Notebooks Across Platforms
Slug: audio-notifications-in-jupyter-notebooks-across-platforms
Date: 2024-09-13
Modified: 2024-09-13
Status: published
tags:
  - jupyter-notebooks
  - audio-notifications
  - python
  - macos
  - windows
  - cross-platform
  - beepy
  - text-to-speech
  - afplay
  - playsound
  - winsound
  - javascript-audio
  - productivity
  - long-running-operations
  - workflow-enhancement
  - coding-alerts
  - custom-notifications
  - system-sounds
  - multiplatform-development
  - interactive-computing
Category: note
---
**Enhancing Your Notebook Experience with Sound Notifications**

When working with long-running operations in Jupyter notebooks or other interactive computing environments, it's often helpful to have audible notifications to alert you when tasks are complete. This is particularly useful when you're multitasking or working on time-consuming processes. In this post, we'll explore various methods to implement sound notifications across different platforms, with a special focus on macOS.

## 1. The Beepy Package: Cross-Platform Simplicity

The `beepy` package offers a straightforward, cross-platform solution for playing notification sounds in Python. It's easy to install and use, making it an excellent choice for beginners and experienced users alike.

```python
import beepy

# Play a notification sound
beepy.beep(sound=1)
```

The `beepy` package comes with several pre-defined sounds, identified by numbers 1-7. Here's a quick reference:

1. 'coin'
2. 'robot_error'
3. 'error'
4. 'ping'
5. 'ready'
6. 'success'
7. 'wilhelm'

To use `beepy`, first install it via pip:

```
pip install beepy
```

Then, you can easily integrate it into your notebook cells:

```python
from time import sleep

# Simulate a long-running operation
sleep(5)

# Play a notification sound
beepy.beep(sound=5)  # 'ready' sound
print("Operation complete!")
```

## 2. MacOS 'say' Command: Text-to-Speech Notifications

For macOS users, the built-in `say` command provides a unique way to create custom voice notifications. This method turns text into speech, allowing for more informative alerts.

```python
import os

def notify(message):
    os.system(f'say "{message}"')

# Usage
notify("I'm done now with the data processing task.")
```

You can customize the voice and speaking rate:

```python
os.system('say -v Samantha -r 200 "Your analysis is complete"')
```

## 3. MacOS 'afplay' Command: System Sound Playback

The `afplay` command in macOS allows you to play system sounds or custom audio files. First, you can list available system sounds:

```python
!ls /System/Library/Sounds/
```

Then, play a specific sound:

```python
import os

def play_sound(sound_name):
    os.system(f'afplay /System/Library/Sounds/{sound_name}.aiff')

# Usage
play_sound("Hero")
```

## 4. Playsound Library: Another Cross-Platform Option

The `playsound` library offers a simple, cross-platform solution for playing sound files:

```python
from playsound import playsound

# Play an MP3 file
playsound('path/to/your/soundfile.mp3')
```

Install it using pip:

```
pip install playsound
```

## 5. Windows-Specific Solution: Winsound

For Windows users, the built-in `winsound` module provides a platform-specific option:

```python
import winsound

# Play a system sound
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

# Play a custom WAV file
winsound.PlaySound("path/to/your/sound.wav", winsound.SND_FILENAME)
```

## 6. Web-Based Notebooks: JavaScript Audio

For web-based notebooks like Google Colab, you can use JavaScript to play audio:

```python
from IPython.display import Javascript, display

def play_audio(url):
    display(Javascript(f"""
        var audio = new Audio('{url}');
        audio.play();
    """))

# Usage
play_audio('https://example.com/notification.mp3')
```

Happy coding, and may your long-running operations always end with a satisfying ding!
