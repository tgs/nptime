#!/usr/bin/env python
"""Non-Pedantic Time
=================

.. moduleauthor:: Thomas Grenfell Smith <thomathom@gmail.com>

Python's :mod:`datetime` module has many uses, but it has a difficulty: you
can't do any arithmetic with :class:`datetime.time`.  Only with
:class:`datetime.datetime`.  Now, there are good reasons for this:  "What time
will it be, 24 hours from now" has a lot of corner cases, including daylight
savings time, leap seconds, historical timezone changes, leap years, and so on.
But sometimes you really *do* need the simple case.  Sometimes the perfect is
the enemy of the good.  And that's why you have this module.  This module will
allow you to cocoon yourself in the comforting illusion that, in 24 hours, it
will be the same time as it is right now.

And what freedom this illusion gives you!  You can add a
:class:`datetime.timedelta` object to an :mod:`nptime` object, and it works!
It will cycle around 24 hours, like modular arithmetic.  You can ask "what time
comes 1 day and 36 minutes after 12:24 pm?" and it will let you know: 1:00 pm.
How lovely!

>>> from nptime import nptime
>>> from datetime import timedelta
>>> afternoon = nptime(12, 24) + timedelta(days=1, minutes=36)
>>> afternoon
nptime(13, 0)
>>> str(afternoon)
'13:00:00'

You can also ask "How long is it between 9:00 AM and 5:00 PM?  It sure
feels like a million years!"

>>> workday = nptime(hour=17) - nptime(hour=9)
>>> workday
datetime.timedelta(0, 28800)
>>> print workday
8:00:00

Nope, only 8 hours, how strange.  Anyway, please use this module.  It will
be convenient.  But don't use it when talking about concrete time, time in
a particular place, or anything like that.  In fact, it doesn't even notice
:class:`datetime.tzinfo` objects right now.  Good luck.

.. note:: 
    You can find the newest version at https://github.com/tgs/nptime .  You can find online documentation at http://tgs.github.com/nptime/ .

"""

from datetime import *


class nptime(time):
    """nptime - a non-pedantic time object
    
    Inherits from :class:`datetime.time`.  You can't do arithmetic with that class,
    but with ``nptime`` you can:

    * Add a :class:`datetime.timedelta` to an :class:`nptime` (commutative)
    * Subtract a ``timedelta`` from an ``nptime``
    * Subtract an ``nptime`` from another ``nptime``

    You can use the class methods :func:`from_timedelta` and :func:`from_time` to
    construct an ``nptime`` from those ``datetime`` classes.
    """

    _std_date = date(year=1000, month=1, day=1)

    @classmethod
    def from_time(cls, other):
        """Construct an :class:`nptime` object from a :class:`datetime.time`
        
        .. note::
            This *ignores* the :class:`datetime.tzinfo` that may be part
            of the ``time`` object.
        """
        return cls(other.hour, other.minute, other.second, other.microsecond)

    @classmethod
    def from_timedelta(cls, other):
        """Construct an :class:`nptime` object from a :class:`datetime.timedelta`.
        
        The ``timedelta`` is taken to be the amount of time since midnight."""
        return cls() + other

    def _to_timedelta(self):
        return timedelta(hours=self.hour, minutes=self.minute,
                seconds=self.second, microseconds=self.microsecond)

    def __add__(self, other):
        """Add nptime and timedelta"""
        self_dt = datetime.combine(self._std_date, self)
        sum = self_dt + other
        return nptime.from_time(sum.time())

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            diff = self._to_timedelta() - other._to_timedelta()
        else:
            diff = self._to_timedelta() - other

        return diff
            
        




