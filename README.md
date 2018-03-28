# Description

The idea of the project is to monitor the driver's behaviour and notify(and take action if possible) about untypical actions.
It is done by monitoring the OBD data provided from the car and the driver himself. The algorithm is:
- collect data from the car and create a typical driving profile
- the camera is used to captura the driver and monitor for his reactions; if he is awake or falling asleep, etc.
- if the current driving style is off by 10% from the created profile for an extended period of time an exception is raised
- if the driver is out of the image(falled on one side, possibly asleep) another exception is raised
- when a number of exceptions are gathered and alarm is triggered
- the alam has 3 levels and in an extended version of the project the system should be able to limit the performance of the car if no action is taken by the driver

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

# OBD data
- data about 4 OBD parameters is collected while the car is moving - the list can be extended by changing the constant `OBD_PARAMS` defined in the ObdAdapter class
- when the car stops the data is summarized and the average values for 90th percentil and the slopes which wich the data is changing(both up and down) are calculated - this builds the typical driving style
- after every trip the old profile is updated with the newly created summary
- after about 4 minutes of driving(this can be changed by changing the constant `MIN_LAST_ENTRIES_COUNT` defined in the ObdAdapter class; _time = MIN_LAST_ENTRIES_COUNT*5/60 minutes_) the system has enough data for the current trip and begins to check it against the typical driving style
- if deviation of 10% is noticed and exception is raised
