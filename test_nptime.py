#!/usr/bin/env python

from nose.tools import *
from nptime import *
import datetime

def test_creation():
    t = nptime()

def test_addition():
    t = nptime(hour=6, minute=30, second=15, microsecond=3341)
    td = timedelta(seconds=30)
    t1 = t + td
    assert_equal(t.hour, t1.hour)
    assert_equal(t.minute, t1.minute)
    assert_equal(t.second, t1.second - 30)
    assert_equal(t.microsecond, t1.microsecond)

    assert_equal(t + td, td + t)

def test_from_time():
    t = nptime.from_time(datetime.time())

def test_from_timedelta():
    t = nptime.from_timedelta(datetime.timedelta(days=14, hours=3, minutes=40, seconds=3))
    assert_equal(t.hour, 3)
    assert_equal(t.minute, 40)
    assert_equal(t.second, 3)

def test_subtract():
    t1 = nptime(minute=30)
    t2 = nptime(minute=31)

    # There's one minute between those times.
    assert_equal(t2 - t1, timedelta(seconds=60))

    # If you take the interval between the times, and subtract it from one, you
    # get the other.
    assert_equal(t2 - (t2 - t1), t1)

    # Subtraction should be anticommutative
    assert_equal(t2 - t1, -(t1 - t2))


