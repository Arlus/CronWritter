# !/usr/bin/env pthon2.7

# cron jobs are written in the file /etc/crontab
# this is the file read by the cron process to schedule task execution in linux
# we used the python driver for gtk
# gtk is the windowing system for linux

# demo commands
# mplayer /home/arlus/Documents/CronWritter/test.mp3
# echo "it worked" >> /home/arlus/Documents/CronWritter/outputfile.txt
# cd /home/arlus/Documents/CronWritter/ && python test_email.py

import pygtk
pygtk.require('2.0')
import gtk
import getpass
import os
import sys
import psutil


class CronWrite:
    def write(self, widget, data=None):
        minute = self.entry1.get_text()
        minute_offset = self.entry8.get_text()
        hour = self.entry2.get_text()
        hour_offset = self.entry9.get_text()
        date_of_month = self.entry3.get_text()
        date_offset = self.entry10.get_text()
        month = self.entry4.get_text()
        monthly_offset = self.entry11.get_text()
        day_of_week = self.entry5.get_text()
        day_offset = self.entry12.get_text()
        user = self.entry6.get_text()
        command = self.entry7.get_text()
        cron_file = '/etc/crontab'
        # os.chmod(cron_file, 755)
        print cron_file
        output = open(cron_file, 'a')
        string = '%s%s %s%s %s%s %s%s %s%s %s %s\n' % (minute, "/" + minute_offset if minute_offset != '' else '', hour, "/" + hour_offset if hour_offset != '' else '', date_of_month, "/" + date_offset if date_offset != '' else '', month, "/" + monthly_offset if monthly_offset != '' else '', day_of_week, "/" + day_offset if day_offset != '' else '', user, command)
        output.write(string)
        output.close()
        # os.chmod(cron_file, '644')

    def close_event(self, widget, event, data=None):
        print "You closed the program"
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        def draw_pixbuf(widget, event):
            path = 'pic2.gif'
            pixbuf = gtk.gdk.pixbuf_new_from_file(path)
            widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0, 0)
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.close_event)
        window.connect("destroy", self.destroy)
        window.set_default_size(235, 60)
        # window.set_border_width(150)

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.connect('expose-event', draw_pixbuf)
        vbox.show()


        self.label1 = gtk.Label()
        self.label1.set_text("Minute")
        self.label1.set_justify(gtk.JUSTIFY_FILL)
        self.label1.set_line_wrap(True)
        vbox.pack_start(self.label1)

        self.entry1 = gtk.Entry()
        self.entry1.set_text('*')
        vbox.pack_start(self.entry1, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Minute offset")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry8 = gtk.Entry()
        # self.entry8.set_text('*')
        vbox.pack_start(self.entry8, False, False, 2)


        self.label = gtk.Label()
        self.label.set_text("Hour of the day")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry2 = gtk.Entry()
        self.entry2.set_text('*')
        vbox.pack_start(self.entry2, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Hour offset")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry9 = gtk.Entry()
        # self.entry9.set_text('*')
        vbox.pack_start(self.entry9, False, False, 2)


        self.label = gtk.Label()
        self.label.set_text("Date of month")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry3 = gtk.Entry()
        self.entry3.set_text('*')
        vbox.pack_start(self.entry3, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Date offset")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry10 = gtk.Entry()
        # self.entry10.set_text('*')
        vbox.pack_start(self.entry10, True, True, 2)

        self.label = gtk.Label()
        self.label.set_text("Month")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry4 = gtk.Entry()
        self.entry4.set_text('*')
        vbox.pack_start(self.entry4, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Month offset")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry11 = gtk.Entry()
        # self.entry11.set_text('*')
        vbox.pack_start(self.entry11, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Day of week")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry5 = gtk.Entry()
        self.entry5.set_text('*')
        vbox.pack_start(self.entry5, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Day of week offset")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry12 = gtk.Entry()
        # self.entry12.set_text('*')
        vbox.pack_start(self.entry12, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Username")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry6 = gtk.Entry()
        self.entry6.set_text(getpass.getuser())
        vbox.pack_start(self.entry6, False, False, 2)

        self.label = gtk.Label()
        self.label.set_text("Command being scheduled")
        self.label.set_justify(gtk.JUSTIFY_FILL)
        self.label.set_line_wrap(True)
        vbox.pack_start(self.label)

        self.entry7 = gtk.Entry()
        # self.entry7.set_text('command')
        vbox.pack_start(self.entry7, False, False, 2)



        button = gtk.Button("Schedule Command")
        button.connect("clicked", self.write, None)
        vbox.pack_start(button, True, True, 10)
        button.connect_object("clicked", gtk.Widget.destroy, window)

        # self.text.show()

        window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    # to run as root
    euid = os.getuid()
    if euid != 0:
        print "You need root permissions"
        args = ['gksudo', sys.executable] + sys.argv + [os.environ]
        # the next line replaces the currently-running process with the sudo
        os.execlpe('gksudo', *args)
    print 'Running. Your euid is', euid
    # process files are usually in /proc/, so we test if the cron process exists
    PROCESSNAME = "cron"
    PROCESSRUNNING = False
    # test crond for redhat systems
    for process in psutil.process_iter():
        if process.name == PROCESSNAME:
            print "Cron process running...."
            PROCESSRUNNING = True
    if PROCESSRUNNING == True:
        CronWrite()
        main()

    else:
        print "Cron not running on your system, Please try running 'sudo service cron start'"

