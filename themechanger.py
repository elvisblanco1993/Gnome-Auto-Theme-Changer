# Name: Gnome Auto Theme Changer
# Author: Elvis Blanco <eblanco@registrac.page>
# Description: Change bewteen your light and dark themes during the day.

import datetime
import os

#--------------------#
#--- Configuration --#
#--------------------#
time_from = "18:00"
time_to = "7:30"

light_theme = "Yaru"
dark_theme = "Yaru-dark"


#-------------------------#
#-- Program Starts Here --#
#-------------------------#

current_hour = datetime.datetime.now().hour
current_minute = datetime.datetime.now().minute
current_time = str(current_hour) + ':' + str(current_minute)
theme_change_to_light = "gsettings set org.gnome.desktop.interface gtk-theme " + light_theme
theme_change_to_dark = "gsettings set org.gnome.desktop.interface gtk-theme " + dark_theme



if current_time >= time_from and current_time <= time_to:
    # Set to dark variant
    os.system(theme_change_to_dark)
else:
    # Set to light variant
    os.system(theme_change_to_light)
