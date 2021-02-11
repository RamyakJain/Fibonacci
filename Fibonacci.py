from tkinter import * 
root = Tk()
root.title("Fibonacci")
root.geometry("500x400")

label_series = Label(root, text = "Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)


def Fibonacci():
    number = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter<=number):
        label_series['text']+=str(sum)+" "
        counter = counter+1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_flower['text']="Flower Is Fully Blossemed"
        label_spiral['text']="Spiral In Right Direction are: "+str(first_no)+" | "+"Spiral In Left Direction are: "+str(second_no)+" | "+"Total Spiral are: "+str(sum)

btn = Button(root,text = "Show Fibonacci Series",command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()       