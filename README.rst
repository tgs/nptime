
Non-Pedantic Time
*****************

Python's "datetime" module has many uses, but it has a difficulty: you
can't do any arithmetic with "datetime.time".  Only with
"datetime.datetime".  Now, there are good reasons for this:  "What
time will it be, 24 hours from now" has a lot of corner cases,
including daylight savings time, leap seconds, historical timezone
changes, and so on.  But sometimes you really *do* need the simple
case.  Sometimes the perfect is the enemy of the good.  And that's why
you have this module.  This module will allow you to cocoon yourself
in the comforting illusion that, in 24 hours, it will be the same time
as it is right now.

And what freedom this illusion gives you!  You can add a
"datetime.timedelta" object to an "nptime" object, and it works! It
will cycle around 24 hours, like modular arithmetic.  You can ask
"what time comes 1 day and 36 minutes after 12:24 pm?" and it will let
you know: 1:00 pm. How lovely!

>>> from nptime import nptime
>>> from datetime import timedelta, date, datetime
>>> afternoon = nptime(12, 24) + timedelta(days=1, minutes=36)
>>> afternoon
nptime(13, 0)
>>> str(afternoon)
'13:00:00'

Maybe we're talking about the afternoon of Guido van Rossum's
birthday.  Lucky, we can combine "nptime" objects with "date" objects:

>>> datetime.combine(date(1956, 1, 31), afternoon)
datetime.datetime(1956, 1, 31, 13, 0)

You can also ask "How long is it between 9:00 AM and 5:00 PM?  It sure
feels like a million years!"

>>> workday = nptime(hour=17) - nptime(hour=9)
>>> workday
datetime.timedelta(0, 28800)
>>> print(workday)
8:00:00

Nope, only 8 hours, how strange.  Anyway, please use this module.  It
will be convenient.  But don't use it when talking about concrete
time, time in a particular place, or anything like that.  In fact, it
doesn't even notice "datetime.tzinfo" objects right now.  Good luck.

Note: You can find the newest version at
  https://github.com/tgs/nptime . You can find online documentation at
  http://tgs.github.com/nptime/ . The package is available for
  download from PyPi:  *easy_install nptime*.   This software is
  licensed under the 3-clause BSD License.

