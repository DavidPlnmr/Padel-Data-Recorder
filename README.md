# Padel Data Recorder

This project aims to have a software able to help recording data from padel matches. The idea is to have a software that can be used by a single person to record the data of a match, and then be able to analyze the data to get some insights.

## Dependancies
To run the app correctly, you need to have Python installed.
Then install the requirements by running:
```bash
pip install -r requirements.txt
```

## Running the app
To run the app, you can run the following command:
```bash
python main.py
```

## How to work with the app?
Once executed, a window will open.

At the bottom-left corner, there is a button that allows you to browse your files and select the video of the match you wish to visualize.

Once the video is loaded, you have the following commands at your disposal:

1) To play/pause the video, press the 's' key.
2) To fast forward/rewind the video by 1 minute, press the 'c/z' keys.
3) To fast forward/rewind the video by 2 seconds, press the 'd/a' keys.
4) To fast forward/rewind the video by 0.01 seconds, press the 'e/q' keys.

At the top-right corner, in the fields labeled "Team 1" and "Team 2" enter the names of the teams participating in the match you are visualizing.

To start the visualization, press the "Start" button.

Before the rally begins, indicate which team is serving.

To keep track of the number of shots, we suggest pausing the video whenever a player executes a shot, and then pressing the 'j' key to indicate that a shot has been made.

If you make a mistake, you can remove the last entry using the "Remove last event" button.

Once the rally is finished, stop the video and indicate the winning team by pressing the corresponding button at the bottom-right corner.

Proceed to the next rally.

## Download a YouTube video
You can also download a video using the following link:
```bash
python utils/download_video.py [link of your youtube video]
```