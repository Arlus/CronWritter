#!/usr/bin/env pthon2.7

#cron jobs are written in the file /var/spool/cron/crontabs/<account_name>

import pygtk
pygtk.require('2.0')
import gtk
import getpass
import os
#import sys

class CronWrite:
    def write(self, widget, data=None):
        account = getpass.getuser()
        print account
        #text = self.text.get_text()
        minute = self.entry1.get_text()
        hour = self.entry2.get_text()
        day_of_month = self.entry3.get_text()
        month = self.entry4.get_text()
        day_of_week = self.entry5.get_text()
        command = self.entry6.get_text()
        cron_file = '/var/spool/cron/crontabs/' + account
        os.chmod(cron_file, 755)
        print cron_file
        output = open(cron_file, 'a')
        output.write(minute + ' ' + hour + ' ' + day_of_month + ' ' + month + ' ' + day_of_week + ' ' + command + '\n')
        output.close()
        os.chown(cron_file, 'crontab')

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)
        window.set_border_width(60)

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()


        #self.text = gtk.Entry()
        #self.text.set_text("hello")
        #vbox.pack_start(self.text, True, True, 0)

        self.entry1 = gtk.Entry()
        self.entry1.set_text('minute')
        vbox.pack_start(self.entry1, True, True, 0)

        self.entry2 = gtk.Entry()
        self.entry2.set_text('hour')
        vbox.pack_start(self.entry2, True, True, 0)

        self.entry3 = gtk.Entry()
        self.entry3.set_text('day of the month')
        vbox.pack_start(self.entry3, True, True, 0)

        self.entry4 = gtk.Entry()
        self.entry4.set_text('month')
        vbox.pack_start(self.entry4, True, True, 0)

        self.entry5 = gtk.Entry()
        self.entry5.set_text('day of the week')
        vbox.pack_start(self.entry5, True, True, 0)

        self.entry6 = gtk.Entry()
        self.entry6.set_text('command')
        vbox.pack_start(self.entry6, True, True, 0)

        button = gtk.Button("Write")
        button.connect("clicked", self.write, None)
        vbox.pack_start(button, True, True, 0)
        button.connect_object("clicked", gtk.Widget.destroy, window)

        #self.text.show()
        self.entry1.show()
        self.entry2.show()
        self.entry3.show()
        self.entry4.show()
        self.entry5.show()
        self.entry6.show()
        button.show()
        window.show()

def main():
    gtk.main()

if __name__ == "__main__":
    #to run as root
    #euid = os.getuid()
    #if euid != 0:
        #print "You need root permissions"
        #args = ['sudo', sys.executable] + sys.argv + [os.environ]
        # the next line replaces the currently-running process with the sudo
        #os.execlpe('sudo', *args)
    #print 'Running. Your euid is', euid
    CronWrite()
    main()
