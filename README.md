# studious-octo-fortnight
Coding Exercise

readings in datafile.csv should match observations from here:
https://openweathermap.org/city/5173412
taken at the same time.

------------------------------------------------------------------------

The end user should also register for a new API key, and update
constants.py.

This excercise can be altered by the user by picking a new name place
from here: https://openweathermap.org/city

Once the new city name is properly identified:
- update constants.py
- datafile.csv should be cleared (except for the header row)
- "python weather.py" can be run from crontab or scheduled task
  on an interval of the user's choosing.  5 minute intervals
  work well with an application like PRTG.

------------------------------------------------------------------------

Excercise can be extended to write to database of choice.  Data could
then be analyzed or reported from as required.

Datafile.csv can by opened in excel and a range of data can be
plotted.

Another good destination would be an RRD file and data displayed
with PRTG.
