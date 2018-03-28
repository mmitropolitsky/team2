# Solution
Based on a set of rules (both real time and statistics), our prototype tackles road and car safety by observing the conditions on the road and those of the driver himself. Based on historic data and live feed from the camera we have implemented several *analyzers*, which raise *alarms*. The *analyzers* and *alarms* can be extended even now, due to the way the architecture of the application is designed.

# Analyzers
### Facial recognition
- The real time facial recognition analizer is based on live feed from the camera. If the face of the driver cannot be detected for a given amount of time, an alarm is raised. The implemntation is located in the `PostureAnalyzer` class and uses the `OpenCV` library.
### OBD data
- Data about 4 OBD parameters is collected while the car is moving - the list can be extended by changing the constant `OBD_PARAMS` defined in the ObdAdapter class.
- When the car stops the data is summarized and the average values for 90th percentil and the slopes which wich the data is changing(both up and down) are calculated - this builds the _typical driving style_.
- After every trip the old profile is updated with the newly created summary.
- After about 4 minutes of driving(this can be changed by changing the constant `MIN_LAST_ENTRIES_COUNT` defined in the `ObdAdapter` class; _time = MIN_LAST_ENTRIES_COUNT*5/60 minutes_) the system has enough data for the current trip and begins to check it against the typical driving style.

### Alarms
Due to the short time for development, this functionality is not entirely fleshed out. We were able to implement an alarm system, which based on data from the analyzers can do various things (e.g. print a text, or in the future show a notification, or control some system (e.g. speed or temperature) of the car). Currently, all analyzers report to the same alarm system and if there is a certain amount of times that an exception has been raised, the alram system prints a message. The architecture allows implementation of additional alarm handlers for different levels of the warning. 

Currently implemented alarms are:
- If the driver's face cannot be seen for a configurable amount of cycles, the alarm prints a warning message in the console. This alarm uses data from the `PostureAnalyzer`
- If the deviation from the *normal driving* pattern (according to the statistics) is more than 10%, an exception is raised from the `ObdParamsAnalyzer`.

### Experience
When the app is started, the camera is analyzing the driver visually. For now if the face is not detected for a certain amount of time a warning message is shown.
In the same time data about the trip is gathered and statistics are made ...

# How to run
- Install all major depedencies:
    - scipy
    - opencv
    - python-obd
    - numpy

- _If any dependecy is missing from the list when tring to start the code you should be notified_
- change `project_root/adapter/ObdAdapter.py` on line 9 the serial port from which the OBD should be read`
- point the cam directily at the driver (on the dashboard above the instrumets)
- run `python main.py`


### Team
Thanks for the experience from our team - Vanessa Stoynova, Vladimir Aleksiev, and Milko Mitropolitsky