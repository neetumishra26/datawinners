# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from mangrove.errors.MangroveException import NumberNotRegisteredException
from mangrove.transport.reporter import find_reporter, find_reporter_entity

def unique(dbm, telephone_number):
    try:
        reporter_list = find_reporter_entity(dbm, telephone_number)
    except NumberNotRegisteredException:
        return True
    return False
