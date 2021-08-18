import tkinter as tk
from PIL import Image, ImageTk
from weather_api import weather_information


def open_weather_icon(icon):
   # set current weather icon
   size = int(information_frame.winfo_height()*0.30)
   img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
   weather_icon.delete("all")
   weather_icon.create_image(0,0, anchor='nw', image=img)
   weather_icon.image = img

def get_weather_info(city_name):
   #set current weather info
   weather_report = weather_information(city_name)
   result['text']= weather_report[0]
   weather_icon_name = weather_report[1]
   open_weather_icon(weather_icon_name)

#basic settings of Weather App windows
app = tk.Tk()
canvas = tk.Canvas(app, height=550, width=650)
canvas.pack()
app.resizable(False, False)
app.title('Weather App')

#set background image
background_image = tk.PhotoImage(file='background-image.png')
background_image_lebel = tk.Label(app, image=background_image)
background_image_lebel.place(relwidth=1,relheight= 1

)


# Heading of the app

Heading = tk.Label(app,
            text= "Weather Information",
            font=('Poor Richard', 26, 'bold'),
            bg = '#ffff99',
            bd = 2)

Heading.place(relwidth= 1)

#input frame

frame = tk.Frame(app, bg = 'skyblue', bd= 7)
frame.place(x=85, y=80, relwidth=0.75, relheight= 0.1)

#input TextBox
textbox = tk.Entry(frame, font=('Courler', 16))
textbox.place(relwidth= 0.65, relheight= 1)

#submit button
submit_button = tk.Button(frame,
               text = 'Search Weather',
            font=('Calibri ', 11, 'bold'),
            command=lambda : get_weather_info(textbox.get()))

submit_button.place(x=360, relwidth=0.25, relheight= 1)


#Information frame
information_frame = tk.Frame(app, bg="skyblue", bd =6)
information_frame.place(x=85, y=200, relwidth=0.75, relheight=0.55)

result = tk.Label(information_frame,
            font=('Courlier', 14),
            anchor='nw',
            justify='left',
            bg='white',
            bd= 4)
result.place(relwidth=1 , relheight=1 )

# canvas for weather icon
weather_icon =tk.Canvas(result, bg='white', bd= 0, highlightthickness=0)
weather_icon.place(relx= 0.75, relwidth= 1, relheight=0.5)





app.mainloop()