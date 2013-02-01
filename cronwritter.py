# !/usr/bin/env pthon2.7

# cron jobs are written in the file /etc/crontab
# this is the file read by the cron process to schedule task execution in linux

import pygtk
pygtk.require('2.0')
import gtk
import getpass
import os
import sys

class CronWrite:
    def write(self, widget, data=None):
        # self.account = getpass.getuser()
        # print account
        # text = self.text.get_text()
        minute = self.entry1.get_text()
        minute_offset = self.entry8.get_text()
        hour = self.entry2.get_text()
        hour_offset = self.entry9.get_text()
        day_of_month = self.entry3.get_text()
        daily_offset = self.entry10.get_text()
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
        output.write(minute + "\\" + minute_offset + ' ' + hour + "\\" + hourly_offset + ' ' + day_of_month + "\\" + daily_offset + ' ' + month + "\\" + monthly_offset + ' ' + day_of_week + "\\" + day_offset + ' ' + account + ' ' + command + '\n')
        output.close()
        # os.chmod(cron_file, '644')

    def close_event(self, widget, event, data=None):
        print "You closed the program"
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.close_event)
        window.connect("destroy", self.destroy)
        window.set_border_width(150)

        vbox = gtk.VBox(False, 0)
        # hbox = gtk.HBOX(False, 5)
        window.add(vbox)
        # window.add(hbox)
        # hbox.pack_start(vbox, False, False, 0)
        # window.set_border_width()
        vbox.show()


        self.label1 = gtk.Label()
        self.label1.set_text("Minute")
        self.label1.set_justify(gtk.JUSTIFY_FILL)
        self.label1.set_line_wrap(True)
        vbox.pack_start(self.label1)

        self.entry1 = gtk.Entry()
        self.entry1.set_text('minute')
        vbox.pack_start(self.entry1, True, True, 0)

        self.entry8 = gtk.Entry()
        self.entry8.set_text('minute_offset')
        vbox.pack_start(self.entry8, True, True, 0)

        self.entry2 = gtk.Entry()
        self.entry2.set_text('hour')
        vbox.pack_start(self.entry2, True, True, 0)

        self.entry9 = gtk.Entry()
        self.entry9.set_text('hourly_offset')
        vbox.pack_start(self.entry9, True, True, 0)

        self.entry3 = gtk.Entry()
        self.entry3.set_text('day of the month')
        vbox.pack_start(self.entry3, True, True, 0)

        self.entry10 = gtk.Entry()
        self.entry10.set_text('daily_offset')
        vbox.pack_start(self.entry10, True, True, 0)

        self.entry4 = gtk.Entry()
        self.entry4.set_text('month')
        vbox.pack_start(self.entry4, True, True, 0)

        self.entry11 = gtk.Entry()
        self.entry11.set_text('monthly_offset')
        vbox.pack_start(self.entry11, True, True, 0)

        self.entry5 = gtk.Entry()
        self.entry5.set_text('day of the week')
        vbox.pack_start(self.entry5, True, True, 0)

        self.entry12 = gtk.Entry()
        self.entry12.set_text('day_offset')
        vbox.pack_start(self.entry12, True, True, 0)

        self.entry6 = gtk.Entry()
        self.entry6.set_text(getpass.getuser())
        vbox.pack_start(self.entry6, True, True, 0)

        self.entry7 = gtk.Entry()
        self.entry7.set_text('command')
        vbox.pack_start(self.entry7, False, True, 0)



        button = gtk.Button("Write")
        button.connect("clicked", self.write, None)
        vbox.pack_start(button, True, True, 0)
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
    CronWrite()
    main()
