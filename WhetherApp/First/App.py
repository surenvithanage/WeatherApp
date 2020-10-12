import tkinter as tk
import requests

def init():
    print('Application running successfully.........')

def testfun(city):
    print('Entered keyword : ',city)

def formatjson(wjson):
    name = wjson['name']
    description = wjson['weather'][0]['description']
    temp = wjson['main']['temp']

    return str(name) +' , '+str(description) +' , ' + str(temp)

def getwhe(city):
    whether_Key = '900caba2e7325400561b4ed08db0b98e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':whether_Key,'q':city,'units':'imperial'}
    response = requests.get(url,params=params)
    # print(response.json())
    wjson = response.json()

    showlabel['text'] = formatjson(wjson)

    # print(wjson['name'])
    # print(wjson['weather'][0]['description'])
    # print(wjson['main']['temp'])


# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

root = tk.Tk()
//Adding canvas and frame
canvas = tk.Canvas(root , height=600,width=600).pack()
frame = tk.Frame(root,bg='#A9CCE3')
frame.place(relwidth=1,relheight = 1)

button = tk.Button(frame,text='Get Whether' , command=lambda:getwhe(city.get()))
button.place(relx=0.5,rely=0.3,relwidth=0.2,relheight=0.05)

# button.grid(row=3,column = 2)

# label = tk.Label(frame,text ='this is a label',bg = 'yellow') #just a label
# label.grid(row=2,column=3)

city = tk.Entry(frame,bg = 'white')  #text input
city.place(relx=0.28,rely=0.3,relwidth=0.2,relheight=0.05)

showlabel = tk.Label(frame,bg = 'white',anchor='nw',justify='left')  #text input
showlabel.place(relx=0.28,rely=0.4,relwidth=0.425,relheight=0.4)

root.mainloop()
