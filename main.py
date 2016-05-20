#!/usr/bin/env python

import sys
import energy_points_assignment

roleList = energy_points_assignment.import_rolesheet(sys.argv[1])

print roleList
