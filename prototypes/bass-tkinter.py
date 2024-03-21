import tkinter as tk


def main():
    window = tk.Tk()

    window.geometry("1280x720")

    window.configure(bg="white")
    window.resizable(width=True, height=True)

    strings = tk.Frame(master=window)

    def check_screen_size():
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        print(screen_width)
        print(screen_height)

    c = tk.Button(master=strings, text="test", command=lambda: check_screen_size())
    c.grid(row=5, column=0)

    def g_func(fret_num):
        print(f"num: {fret_num} string: g")

    def d_func(fret_num):
        print(f"num: {fret_num} string: d")

    def a_func(fret_num):
        print(f"num: {fret_num} string: a")

    def e_func(fret_num):
        print(f"num: {fret_num} string: e")

    # G
    g_string = tk.Label(master=strings, text="G")
    g_string.grid(row=0, column=0, padx=10, pady=2)

    g_0 = tk.Button(master=strings, text="0", bg="black", fg="black", command=lambda: g_func(0), width=1, height=1)
    g_0.grid(row=0, column=1, padx=5, pady=2)

    g_1 = tk.Button(master=strings, text="1", bg="black", fg="black", command=lambda: g_func(1))
    g_1.grid(row=0, column=2, padx=5, pady=2)

    g_2 = tk.Button(master=strings, text="2", bg="black", fg="black", command=lambda: g_func(2))
    g_2.grid(row=0, column=3, padx=5, pady=2)

    g_3 = tk.Button(master=strings, text="3", bg="black", fg="black", command=lambda: g_func(3))
    g_3.grid(row=0, column=4, padx=5, pady=2)

    g_4 = tk.Button(master=strings, text="4", bg="black", fg="black", command=lambda: g_func(4))
    g_4.grid(row=0, column=5, padx=5, pady=2)

    g_5 = tk.Button(master=strings, text="5", bg="black", fg="black", command=lambda: g_func(5))
    g_5.grid(row=0, column=6, padx=5, pady=2)

    g_6 = tk.Button(master=strings, text="6", bg="black", fg="black", command=lambda: g_func(6))
    g_6.grid(row=0, column=7, padx=5, pady=10)

    g_7 = tk.Button(master=strings, text="7", bg="black", fg="black", command=lambda: g_func(7))
    g_7.grid(row=0, column=8, padx=5, pady=10)

    g_8 = tk.Button(master=strings, text="8", bg="black", fg="black", command=lambda: g_func(8))
    g_8.grid(row=0, column=9, padx=5, pady=10)

    g_9 = tk.Button(master=strings, text="9", bg="black", fg="black", command=lambda: g_func(9))
    g_9.grid(row=0, column=10, padx=5, pady=10)

    g_10 = tk.Button(master=strings, text="10", bg="black", fg="black", command=lambda: g_func(10))
    g_10.grid(row=0, column=11, padx=5, pady=10)

    g_11 = tk.Button(master=strings, text="11", bg="black", fg="black", command=lambda: g_func(11))
    g_11.grid(row=0, column=12, padx=5, pady=10)

    g_12 = tk.Button(master=strings, text="12", bg="black", fg="black", command=lambda: g_func(12))
    g_12.grid(row=0, column=13, padx=5, pady=10)

    g_13 = tk.Button(master=strings, text="13", bg="black", fg="black", command=lambda: g_func(13))
    g_13.grid(row=0, column=14, padx=5, pady=10)

    g_14 = tk.Button(master=strings, text="14", bg="black", fg="black", command=lambda: g_func(14))
    g_14.grid(row=0, column=15, padx=5, pady=10)

    g_15 = tk.Button(master=strings, text="15", bg="black", fg="black", command=lambda: g_func(15))
    g_15.grid(row=0, column=16, padx=5, pady=10)

    g_16 = tk.Button(master=strings, text="16", bg="black", fg="black", command=lambda: g_func(16))
    g_16.grid(row=0, column=17, padx=5, pady=10)

    g_17 = tk.Button(master=strings, text="17", bg="black", fg="black", command=lambda: g_func(17))
    g_17.grid(row=0, column=18, padx=5, pady=10)

    g_18 = tk.Button(master=strings, text="18", bg="black", fg="black", command=lambda: g_func(18))
    g_18.grid(row=0, column=19, padx=5, pady=10)

    g_19 = tk.Button(master=strings, text="19", bg="black", fg="black", command=lambda: g_func(19))
    g_19.grid(row=0, column=20, padx=5, pady=10)

    g_20 = tk.Button(master=strings, text="20", bg="black", fg="black", command=lambda: g_func(20))
    g_20.grid(row=0, column=21, padx=5, pady=10)

    g_21 = tk.Button(master=strings, text="21", bg="black", fg="black", command=lambda: g_func(21))
    g_21.grid(row=0, column=22, padx=5, pady=10)

    g_22 = tk.Button(master=strings, text="22", bg="black", fg="black", command=lambda: g_func(22))
    g_22.grid(row=0, column=23, padx=5, pady=10)

    g_23 = tk.Button(master=strings, text="23", bg="black", fg="black", command=lambda: g_func(23))
    g_23.grid(row=0, column=24, padx=5, pady=10)

    # D
    d_string = tk.Label(master=strings, text="D")
    d_string.grid(row=1, column=0, padx=10, pady=10)

    d_0 = tk.Button(master=strings, text="0", bg="black", fg="black", command=lambda: d_func(0))
    d_0.grid(row=1, column=1, padx=5, pady=10)

    # A
    a_string = tk.Label(master=strings, text="A")
    a_string.grid(row=2, column=0, padx=10, pady=10)

    a_0 = tk.Button(master=strings, text="0", bg="black", fg="black", command=lambda: a_func(0))
    a_0.grid(row=2, column=1, padx=5, pady=10)

    a_1 = tk.Button(master=strings, text="1", bg="black", fg="black", command=lambda:a_func(1))
    a_1.grid(row=2, column=2, padx=5, pady=10)

    # E
    e_string = tk.Label(master=strings, text="E")
    e_string.grid(row=3, column=0, padx=10, pady=10)

    e_0 = tk.Button(master=strings, text= "0", bg="black", fg="black", command=lambda: e_func(0))
    e_0.grid(row=3, column=1, padx=5, pady=10)

    e_1 = tk.Button(master=strings, text="1", bg="black", fg="black", command=lambda: e_func(1))
    e_1.grid(row=3, column=2, padx=5, pady=10)

    e_2 = tk.Button(master=strings, text="2", bg="black", fg="black", command=lambda: e_func(2))
    e_2.grid(row=3, column=3, padx=5, pady=10)

    e_3 = tk.Button(master=strings, text="3", bg="black", fg="black", command=lambda: e_func(3))
    e_3.grid(row=3, column=4, padx=5, pady=10)

    # TODO: ADD MORE STRINGS
    # TODO: ADD FUNCTIONS THAT RETRIEVE BUTTON VALUES
    # TODO: ADD CHANGE NUMBERS TO LETTERS
    # TODO: ADD CHANGE LETTERS TO NUMBERS

    strings.pack()

    # print(screen_height)
    # print(screen_width)

    window.mainloop()


if __name__ == '__main__':
    main()
