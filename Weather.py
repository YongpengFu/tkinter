from tkinter import *
from PIL import ImageTk, Image
import requests #get data from a API URL
import json


root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
root.geometry("400x400")
root.grid_columnconfigure(0, weight=1)
#lookup function:
def ziplookup():
    # zip.get()
    # ziplabel = Label(root, text = zip.get())
    # ziplabel.grid(row = 1, column = 0, columnspan = 2)
    '''
    loads: If you’ve pulled JSON data in from another program or 
    have otherwise obtained a string of JSON formatted data in Python, 
    you can easily deserialize that with loads(), 
    which naturally loads from a string.
    '''
    api_url = ("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&" +
    f"zipCode={zip.get()}&distance=5&API_KEY=E43174D8-5968-4CA0-A66B-7648FB700EC4")

    try:
        api_request = requests.get(api_url)
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']["Name"]
        #create label
        if category.lower() == "good":
            weather_color = "#0C0"
        elif category.lower() == "moderate":
            weather_color = "#FFFF00"
        elif category.lower() == "unhealthy for sensitive groups":
            weather_color = "#ff9900"
        elif category.lower() == "unhealthy":
            weather_color = "#FF0000"
        elif category.lower() == "very unhealthy":
            weather_color = "#990066"
        else:
            weather_color = "#660000"
        #change the color of root and label
        root.configure(background = weather_color)
        # mylabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font = ("Helvetica", 20), background = weather_color)
        mylabel.grid_forget()
        mylabel.config(bg = weather_color)
        mylabel.config(text = city + " Air Quality " + str(quality) + " " + category)
        mylabel.grid(row = 1, column = 0, columnspan = 2)
    except Exception as e:
        print("Error: " + str(e))

#create a lookup for the zipcode
zip = Entry(root)
zip.grid(row = 0, column = 0, sticky = W+E+N+S)

zipbutton = Button(root, text = "Lookup Zipcode", command = ziplookup)
zipbutton.grid(row = 0, column = 1, sticky = E)

mylabel = Label(root, font = ("Helvetica", 20))

root.mainloop()