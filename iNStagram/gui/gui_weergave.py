__author__ = 'Freek'
__build__ = 'versie 1.0'

from iNStagram.file_io.fileio import lees_stationgegevens
from iNStagram.api_requests.app_requests import request_instagram

from tkinter import *

startscherm = Tk()
startscherm.title('Foto of video in de buurt!')
startscherm.minsize(width=790, height=600, )
startscherm.configure(bg='yellow')
infolabel = Label(startscherm, fg='blue', text='Voer een station in')
infolabel.place(x=0, y=0)

e = Entry(master=startscherm, fg='black')
e.place(x=93, y=480)

T = Text(startscherm, height=25, width=120, bg='yellow', fg='blue')
T.pack()

def weergeef_instagram_links():
    """
    Geeft de bijbehorende station dict uit de lijst van alle stations (in de NS API)
    :param stationnaam: geef ofwel kort, middel als lange stationnaam om de bijbehorende station te identificeren
    :type stationnaam: str
    :return: station dict met namen en locatie
    :rtype: dict
    """
    stationnaam = e.get()
    stations = lees_stationgegevens()
    for station in stations:
        if stationnaam in station["namen"].values():
            print("Station gevonden")
            lat, lon = station["locatie"]
            lat = float(lat)
            lon = float(lon)
            instagram_data_dict = request_instagram(lat, lon)
            for data in instagram_data_dict:
                print(data) # eerst kijken
                import datetime
                regeltekst = "%-30s %s %s %s"%(data["plaatsnaam"],datetime.datetime.fromtimestamp(data["tijd"]),data["link"],data["type"])
                T.insert(END, regeltekst + '\n')


    else:
        print("Geen station gevonden")
        # return "GEEEN STAZION"


b = Button(master=startscherm, text="Zoek naar media", width=20, height=3, bg='blue', fg='white',
           command=weergeef_instagram_links)
b.place(x=93, y=500)

startscherm.mainloop()
