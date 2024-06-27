---
Title: Remove Noise From Screen Recording
Slug: remove-noise-from-screen-recording
Date: 2024-06-27
Modified: 2024-06-27
Status: published
tags: noise, denoising, video, video-editing, video-processing, audio-processing, video,postprocessing
Category: note
---
To remove noise from the speaker audio in your screen capture video, I can recommend a solution using the tools FFmpeg and Audacity as well as some free alternatives. Here's a step-by-step approach.

## 1. Extract the audio with ffmpeg
Use FFmpeg to extract the audio from your video:

```sh
ffmpeg -i input_video.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output_audio.wav
```

## 2. Noise reduction with Audacity (Free, open-source)
- Import the extracted audio into Audacity
- Select a portion of the audio that contains only background noise
- Go to `Effect > Noise Reduction`
- Click "Get Noise Profile"
- Select the entire audio track
- Go to `Effect > Noise Reduction` again
- Adjust settings and preview until satisfied
- Click "OK" to apply

Export the cleaned audio: `File > Export > Export as WAV`

## 3. Recombine audio with video:
Use FFmpeg to merge the cleaned audio with the original video:

```sh
ffmpeg -i input_video.mp4 -i cleaned_audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output_video.mp4
```

### Alternative free, video editing tools

#### 1. DaVinci Resolve (Free version)
- Powerful video editor with built-in noise reduction
- Import video, separate audio, apply `Fairlight FX > Noise Reduction`
- Export the final video

#### 2. Kdenlive (Free, open-source)
- Video editor with basic noise reduction capabilities
- Import video, separate audio, apply `Audio Effects > Noise Reduction`
- Export the final video

#### 3. Olive Video Editor (Free, open-source)
- Another video editor with audio filtering options
- Import video, separate audio, apply audio effects
- Export the final video

For best results, experiment with different tools and settings. The effectiveness of noise reduction depends on the type and amount of noise in your original recording.

## Noise removal from CLI alternatives
There are CLI (Command Line Interface) tools available for macOS that can help you remove noise from audio. Here are some options:

### 1. FFmpeg with FFmpeg-normalize
FFmpeg itself doesn't have advanced noise reduction capabilities, but when combined with FFmpeg-normalize, you can apply some basic noise reduction.

First, install FFmpeg and FFmpeg-normalize if you haven't already:

```sh
brew install ffmpeg
pip install ffmpeg-normalize
```

Then, you can use this command:

```sh
ffmpeg-normalize input_audio.wav -o output_audio.wav --normalization-type ebu --target-level -23 --audio-codec pcm_s16le --audio-bitrate 192k --keep-loudness-range-target --loudness-range-target 7 --true-peak -2 --offset 0.5
```

This command normalizes the audio, which can help reduce some background noise.

### 2. SoX (Sound eXchange)
SoX is a powerful command-line audio processing tool that includes noise reduction capabilities.

Install SoX:

```sh
brew install sox
```

Use SoX for noise reduction:

```sh
sox input_audio.wav output_audio.wav noisered noise_profile 0.21
```

Note: You'll need to create a noise profile first:

```sh
sox input_audio.wav -n trim 0 0.5 noiseprof noise_profile
```

This captures the first 0.5 seconds of the audio as the noise profile.

### 3. AFNI's 3dTcorrMap
AFNI is a set of C programs for processing, analyzing, and displaying functional MRI (fMRI) data, but it includes some audio processing tools.

Install AFNI:

```sh
brew install --cask afni
```

Use 3dTcorrMap for noise reduction:

```sh
3dTcorrMap -prefix output_audio.wav -input input_audio.wav -mask_only_targets
```

### 4. RNNoise
RNNoise is a noise suppression library based on a recurrent neural network. While it's not a standalone CLI tool, you can use it with FFmpeg if you compile FFmpeg with RNNoise support.

Here's a general approach (requires advanced setup):

```sh
ffmpeg -i input_audio.wav -af arnndn=m=./rnnoise-models/sh.rnnn output_audio.wav
```

> **Note:** that this requires compiling FFmpeg with RNNoise support, which is a more advanced process.

