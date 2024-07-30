import tkinter as tk
frame = tk.Tk()
frame.title("Primes")
frame.geometry('420x200')
inputtxt = tk.Text(frame, height=5, width=20)
inputtxt.pack()

def getInput():
    inp = int(inputtxt.get(1.0, "end-1c"))
    lbl.config(text=f"Is {inp} prime? {str(is_prime(inp))}")

printButton = tk.Button(frame,
                        text = "Calculate",
                        command = getInput)
printButton.pack()

lbl = tk.Label(frame, text="")
lbl.pack()
lbl2 = tk.Label(frame, text="")
lbl2.pack()

def is_prime(number):
    i = 3
    composite = False
    if (number % 2 == 0) and (number != 2):
        return False
    while i**2 < number:
        if number % i == 0:
            lbl2.config(text=f"{number} is {number/i} * {i}")
            composite = True
            break
        i += 2
    if composite:
        return False
    else:
        return True


frame.mainloop()

