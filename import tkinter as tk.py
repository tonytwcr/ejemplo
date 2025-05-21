import tkinter as tk
import requests 

def openSearch():
    button1.config(state="active")
    print("Hola Daniel!")

def searchPokemon(quantity):

    urlPokemon = "https://pokeapi.co/api/v2/pokemon"
    print(f"Este es el id: https://pokeapi.co/api/v2/pokemon/1/".replace(urlPokemon,"").replace("/", ""))

    number.set("")

    url = "https://pokeapi.co/api/v2/pokemon"
    params = {
        "limit": quantity,
        "offset": 0
    }

    response = requests.get(url=url, params=params)

    if response.ok:
        data = response.json()
        print(data['results'])

        for value in data['results']:
            for key, value in value.items():
                print(value)

    else:
        print("Error", response.status_code)


    print("Hola T!")
    print(quantity)

def searchScreen():
    search = tk.Toplevel()
    search.title("Búsqueda de Pokémons")
    search.geometry("500x200")

    global number

    number = tk.StringVar()
    quantity = tk.Entry(search, width=30, textvariable=number)
    quantity.pack()

    searchButton = tk.Button(search, text="Buscar", width=30, command=lambda: searchPokemon(quantity.get().strip()))
    searchButton.pack()

    search.mainloop()

def close():
    root.quit()

def main():
    global root
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Hola Mundo!")

    title = tk.Label(root, text="Poképad")
    title.pack()

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    global button1

    button1 = tk.Button(frame, width=20, text="1. Búsqueda", command=searchScreen)
    # button1.pack(padx=20, pady=5)
    button1.grid(row=1, column=0)

    button2 = tk.Button(frame, text="8. esShiny", width=20, command=searchScreen)
    # button2.pack(padx=20, pady=5)
    button2.grid(row=1, column=1)

    button3 = tk.Button(frame, text="9. Convertidor", width=20, command=close)
    button3.grid(row=2, column=1)
    
    root.mainloop()

print("Hola mundo! Daniel")



main()



