# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from datetime import datetime, date, timedelta
from unittest import TestCase

class Deadline(object):
    def __init__(self,frequency,mode):
        self.frequency = frequency
        self.mode = mode

    def next(self, as_of):
        return self.frequency.next_date(as_of,self._get_offset())

#      Deadline class converts the modes "Following" or "That" to the currect offsets.
    def _get_offset(self):
        if self.mode == "Following":
            return 1
        return 0


class Month(object):
    def __init__(self,day):
        self.day = day

#    Offset is any valid offset > 0. Month knows that offset means months.
    def next_date(self, as_of,offset):
        if as_of.day > self.day:
            return None
        return date(as_of.year, as_of.month + offset, self.day)

class TestDeadline(TestCase):
    def test_should_return_next_deadline_date_for_current_month(self):
        deadline = Deadline(frequency=Month(24),mode="That")
        self.assertEqual(date(2011,9,24), deadline.next(date(2011,9,15)))

    def test_should_return_next_deadline_date_for_current_month_and_asof_as_deadline_day(self):
        deadline = Deadline(frequency=Month(24),mode="That")
        self.assertEqual(date(2011,9,24), deadline.next(date(2011,9,24)))

    def test_should_return_next_deadline_date_for_current_month_and_asof_post_deadline_day(self):
        deadline = Deadline(frequency=Month(24),mode="That")
        self.assertEqual(None, deadline.next(date(2011,9,30)))

    def test_should_return_next_deadline_date_for_following_month(self):
        deadline = Deadline(frequency=Month(24),mode="Following")
        self.assertEqual(date(2011,10,24), deadline.next(date(2011,9,15)))
