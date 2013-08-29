#!/usr/bin/env python
'''

    "The Century Club" is a drinking game, and it is known by some other names
    like "Centurion". The element of luck is reduced to almost nothing, and
    there is a strong strategic component.

    The aim of the gaim is to consume 100 x 30ml shots of beer, one a minute,
    every minute, for 100 minutes. This should add up to 8 standard bottles
    of beer in the 100 minutes, which is not an obscene amount of alcohol.

'''

import gtk
import gobject

class CenturyClub:
    '''
    This is the main Century Club logic
    '''

    def __init__(self):

        # variables
        self.shot = 0

        # create a simple window with a label
        self.window = gtk.Window()
        self.window.set_size_request(400, 200)
        self.window.set_title('Century Club')
        self.window.connect('destroy', lambda wid: gtk.main_quit())
        self.window.connect('delete_event', lambda a1, a2:gtk.main_quit())
        vbox = gtk.VBox()
        self.window.add(vbox)
        self.label = gtk.Label('Counter: 0')
        self.label2 = gtk.Label('Shot: 0')
        vbox.pack_start(self.label)
        vbox.pack_start(self.label2)
        self.window.show_all()

        # register a periodic timer
        self.counter = 0
        gobject.timeout_add_seconds(1, self.callback)

    def callback(self):
        '''
        
        Timer callback

        '''

        if self.shot < 100:
            if self.counter < 60:
                self.counter += 1
            else:
                self.counter = 0
                self.shot += 1

        self.draw()

        return True

    def draw(self):
        '''
        
        Screen draw routing

        '''

        self.label.set_text('Counter: %s' %  str(self.counter))
        self.label2.set_text('Shot: %s' % str(self.shot))

if __name__ == '__main__':
    CENTURY_CLUB = CenturyClub()
    gtk.main()
