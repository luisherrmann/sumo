#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to select mode
netedit.selectMode()

# select first POILane
netedit.leftClick(referencePosition, 140, 215)

# select second POILane
netedit.leftClick(referencePosition, 200, 215)

# go to inspect mode
netedit.inspectMode()

# inspect first POILane
netedit.leftClick(referencePosition, 140, 215)

# Change parameter 11 with a non valid value (dummy)
netedit.modifyAttribute(9, "dummyAngle")

# Change parameter 11 with a valid value (negative)
netedit.modifyAttribute(9, "-12")

# Change parameter 11 with a valid value (> 360)
netedit.modifyAttribute(9, "500")

# Change parameter 11 with a valid value
netedit.modifyAttribute(9, "30")

# Check undos and redos
netedit.undo(referencePosition, 4)
netedit.redo(referencePosition, 4)

# save shapes
netedit.saveShapes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)