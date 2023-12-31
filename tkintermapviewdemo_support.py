#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# ======================================================
#     tkintermapviewdemo_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #
# Written by G.D. Walters
# Copyright © 2023, 2024 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Nov 10, 2023 03:58:36 AM CST  platform: Linux

import sys
import platform
import os

# =============================================================
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import tkinter.messagebox as messagebox

# =============================================================
try:
    from tkintermapview import TkinterMapView
except:
    msg = "You must install tkintermapview using pip."
    print(msg)
    sys.exit()

# =============================================================
import tkintermapviewdemo

_debug = True  # False to eliminate debug printing from callback functions.
location = tkintermapviewdemo._location
programName = "Tkintermapview Demo"
version = "0.1.0"


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = tkintermapviewdemo.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    global map_widget, markerList, defaultZoomLevel
    markerList = []
    defaultZoomLevel = 14
    # ===================================================
    # This block of code sets up the TkinterMapView object,
    #   then places it on the Toplevel form.
    # ===================================================
    map_widget = TkinterMapView(_w1.TFrame2, width=800, height=600, corner_radius=0)
    map_widget.place(x=0, y=0)

    # This will set the active map position by default
    search_marker = map_widget.set_address("Garden of the Gods, Co", marker=True)
    # Set the initial zoom level
    map_widget.set_zoom(defaultZoomLevel)
    # Add a marker and add it to the list
    markerList.append(search_marker)
    cntr = len(markerList)
    # Also set the same in the Search (Entry widget) widget
    _w1.search_address.set("Garden of the Gods, Co")
    _w1.Scrolledlistbox1.insert(cntr, _w1.search_address.get())

    # Set the bindings for the Entry widget
    set_bindings()
    # Show the program information in the Terminal
    show_environ_info()
    # This disables the create marker button (not currently used)
    _w1.btnCreateMarker.config(state=DISABLED)
    # Set the title bar of the program
    _top1.title(f"{programName} version {version}")
    # Finally, centre the screen, show the form and start the program.
    centre_screen(1020, 760)


def on_btnClearMarkers(*args):
    if _debug:
        print("tkintermapviewdemo_support.on_btnClearMarkers")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    global markerList
    for ml in markerList:
        map_widget.delete(ml)
    _w1.Scrolledlistbox1.delete(0, len(markerList))
    markerList = []


def on_btnClearPath(*args):
    if _debug:
        print("tkintermapviewdemo_support.on_btnClearPath")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    map_widget.delete_all_path()


def on_btnCreateMarker(*args):
    if _debug:
        print("tkintermapviewdemo_support.on_btnCreateMarker")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_btnCreatePath(*args):
    if _debug:
        print("tkintermapviewdemo_support.on_btnCreatePath")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    positionList = []
    for marker in markerList:
        positionList.append(marker.position)
    if len(positionList) > 0:
        markerPath = map_widget.set_path(positionList)


def on_btnExit(*args):
    if _debug:
        print("tkintermapviewdemo_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()


def on_btnGo(*args):
    if _debug:
        print("tkintermapviewdemo_support.on_btnGo")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    address = _w1.search_address.get()
    search_marker = map_widget.set_address(address, marker=True)
    if search_marker == False:
        search_marker = None
        titl = "Mapview1 Search Error"
        msg = "The search entry could not be found."
        messagebox.showerror(titl, msg, parent=_top1, icon=messagebox.ERROR)
    else:
        markerList.append(search_marker)
        cntr = len(markerList)
        _w1.Scrolledlistbox1.insert(cntr, address)
        map_widget.set_zoom(defaultZoomLevel)


# Shows information at the beginning of the program that could be helpful for troubleshooting
def show_environ_info():
    osVersion = platform.system()
    release = platform.release()
    platformversion = platform.version()
    pv = platform.python_version()
    print("=" * 35)
    print(f"Program name: {programName} {version}")
    print(f"System running {osVersion} {release}")
    print(f"Running under Python {pv}")
    print(f"Program path: {location}")
    print("=" * 35)


def set_bindings():
    _w1.TEntry1.bind("<KeyRelease>", lambda e: on_entryKeyPress(e))
    _w1.TEntry1.bind("<Button-3>", lambda e: on_EntryBtn3(e))
    _w1.Scrolledlistbox1.bind("<<ListboxSelect>>", on_listboxSelect)


def on_entryKeyPress(e):
    if e.keysym == "Return":
        on_btnGo()


def on_EntryBtn3(e):
    if _debug:
        print("on_EntryBtn3")
    currentPos = root.clipboard_get()
    if currentPos != "":
        _w1.search_address.set("")
        _w1.search_address.set(currentPos)
        on_btnGo()


def on_listboxSelect(e):
    indx = _w1.Scrolledlistbox1.curselection()
    itm = _w1.Scrolledlistbox1.get(indx[0])
    # SelectedItem.set(f"Selected Item: {indx[0]} - {itm}")
    if _debug:
        print(f"Selected Item: {indx[0]} - {itm}")
    search_marker = map_widget.set_address(itm, marker=False)
    map_widget.set_zoom(defaultZoomLevel)


# Shows information at the beginning of the program that could be helpful for troubleshooting
def show_environ_info():
    osVersion = platform.system()
    release = platform.release()
    platformversion = platform.version()
    pv = platform.python_version()
    print("=" * 35)
    print(f"Program name: {programName} {version}")
    print(f"System running {osVersion} {release}")
    print(f"Running under Python {pv}")
    print(f"Program path: {location}")
    print("=" * 35)


def centre_screen(wid, hei):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (wid / 2)
    y = (hs / 2) - (hei / 2)
    root.geometry("%dx%d+%d+%d" % (wid, hei, x, y))


if __name__ == "__main__":
    tkintermapviewdemo.start_up()
