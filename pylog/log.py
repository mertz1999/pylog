from colorama import Fore, Style, init, Back
from datetime import datetime
import os 

# Initialize colorama
init(autoreset=True)


class Log():
    def __init__(self, save=False, output_log='log') -> None:
        self.sep = Fore.WHITE + " | "

        # output logging
        self.save = save
        self.output_log = output_log
        if not os.path.exists(output_log):
            os.makedirs(output_log)


    def info(self,message):
        print(self.get_time() + Fore.GREEN + "INFO\t" + self.sep + Style.BRIGHT + message)
        self.write(self.get_time(color=False) + "INFO\t" + " | " + message)
    
    def warning(self,message):
        print(self.get_time() + Fore.YELLOW + "WARN\t" + self.sep + Style.BRIGHT + message)
        self.write(self.get_time(color=False) + "WARN\t" + " | " + message)
    
    def error(self,message):
        print(self.get_time() + Fore.RED + "FAUL\t" + self.sep + Style.BRIGHT + message)
        self.write(self.get_time(color=False) + "FAUL\t" + " | " + message)

    def get_time(self, color=True):
        now = datetime.now()
        if color:
            date_str = Fore.BLUE + now.strftime("%Y-%m-%d") + "  " + now.strftime("%H:%M:%S") + self.sep
        else:
            date_str = now.strftime("%Y-%m-%d") + "  " + now.strftime("%H:%M:%S") + " | "
        return date_str
    
    # Write on log folder
    def write(self, message):
        if self.save:
            file_name = datetime.now().strftime("%Y-%m-%d")
            file_ = open(os.path.join(self.output_log, file_name),'a')
            file_.write(message+'\n')
            file_.close()


