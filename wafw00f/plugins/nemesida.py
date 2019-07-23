#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Nemesida (PentestIt)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Suspicious.activity.detected.+?Access.to.the.site.is.blocked.'),
        self.matchContent(r'nwaf@.+\..+')
    ]
    if any(i for i in schemes):
        return True
    return False