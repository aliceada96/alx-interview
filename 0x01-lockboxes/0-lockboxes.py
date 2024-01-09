#!/usr/bin/python3
"""LOCKBOXES"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
    When you have a list of boxes that may/maynot contain keys
    A key with the same number as a box opens it amd
    the first box is ope."""
    open_boxes = [0]
    count = 0
    i = 0
    allBoxes = len(boxes)

    while i < len(open_boxes):
        setBox = open_boxes[i]
        for key in boxes[setBox]:
            if key not in open_boxes and key < allBoxes and key > 0:
                open_boxes.append(key)
                count += 1
        i += 1

    if count == allBoxes-1:
        return True
    else:
        return False
