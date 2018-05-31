#curses_menu_submenu.py
import curses                                                                
from curses import panel                                                     

class Menu(object):                                                          

    def __init__(self, items, stdscreen):                                    
        self.window = stdscreen.subwin(0,0)                                  
        self.window.keypad(1)                                                
        self.panel = panel.new_panel(self.window)                            
        #self.panel.hide()                                                    
        panel.update_panels()                                                

        self.position = 0                                                    
        self.items = items                                                   
#       append exit in mainmenu and submenu
        self.items.append(('exit','exit'))                                   

    #set up position bounderies
    def navigate(self, n):                                                   
        #position is a number that compares itself with the index of the window set
        #in this program when position == index number it wil reverse text color line 43
        self.position += n                                                   
#       move down until end of index
        if self.position < 0:                                                
            #do not move under index stop when position hits 0
            self.position = 0                                                
        elif self.position >= len(self.items):                               
            #makes the cursor stay at the end
            #if you change value 1 to 4 (end of items) it resets position
            self.position = len(self.items)-1                                

    def display(self):                                                       
        self.panel.top()                                                     
        self.panel.show()                                                    
        self.window.clear()                                                  

        while True:                                                          
            self.window.refresh()                                            
            curses.doupdate()                                                
            for index, item in enumerate(self.items):                        
                #highlight panel
                if index == self.position:                                   
                    #A_REVERSE will reverse colors
                    mode = curses.A_REVERSE                                  
                else:                                                        
                    mode = curses.A_NORMAL                                   

                #sets up windows index and name
                msg = '%d. %s' % (index, item[0])                            
                #posy posx message color
                self.window.addstr(1+index, 0, msg, mode)                    

            #navigate up and down
            key = self.window.getch()                                        
            #confirm with enter
            if key in [curses.KEY_ENTER, ord('\n')]:                         
                #if cursor is standing on submenu go inside the submenu
                if self.position == len(self.items)-1:  #-1 submenu one to last
                    #pass
                    break                                                    
                else:                                                        
                    self.items[self.position][1]()                           

            #change position variable number with the bounderies given by navigate()
            elif key == curses.KEY_UP:                                       
                self.navigate(-1)                                            
            elif key == curses.KEY_DOWN:
                self.navigate(1)                                             

#??
#        self.window.clear()                                                  
#        self.panel.hide()                                                    
#        panel.update_panels()                                                
#        curses.doupdate()

class MyApp(object):                                                         

    def __init__(self, stdscreen):                                           
        self.screen = stdscreen                                              
        curses.curs_set(0)                                                   

        #submenu_items will replace Menu(self, items)
        submenu_items = [                                                    
                ('beep', curses.beep),                                       
                ('flash', curses.flash)                                      
                ]                                                            
        submenu = Menu(submenu_items, self.screen)                           

        #main_menu_items will replace Menu(self, items)
        main_menu_items = [                                                  
                ('beep', curses.beep),                                       
                ('flash', curses.flash),                                     
                ('submenu', submenu.display)                                 
                ]                                                            
        main_menu = Menu(main_menu_items, self.screen)                       
        main_menu.display()                                                  

if __name__ == '__main__':                                                       
    curses.wrapper(MyApp)   

