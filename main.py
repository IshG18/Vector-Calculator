import customtkinter as ctk


class VectorCalc():
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("Vector Calculator <3")

#Defining Grid blank system
        root.grid_columnconfigure((0,1,2,3,4), weight=1)
        root.grid_rowconfigure((0,1,2,3,4,5,6,6), weight=1)
        #sets a 5x8 grid

        frame = ctk.CTkFrame(root, height=115)
        entry1 = ctk.CTkEntry(root, placeholder_text="Input for vector, seperated by a space")
        btn_1 = ctk.CTkButton(root, text="Button1")
        btn_2 = ctk.CTkButton(root, text="Button2")
        btn_3 = ctk.CTkButton(root, text="Button3")

        text2 = ctk.CTkLabel(root, text="CTkLabel1", fg_color="transparent", text_color="grey")
        entry2 = ctk.CTkEntry(root)

        btn_4 = ctk.CTkButton(root, text="4")
        btn_5 = ctk.CTkButton(root, text="5")
        btn_6 = ctk.CTkButton(root, text="6")
        btn_7 = ctk.CTkButton(root, text="6")
        btn_8 = ctk.CTkButton(root, text="8")

        btn_9 = ctk.CTkButton(root, text="9")
        btn_10 = ctk.CTkButton(root, text="10")
        btn_11 = ctk.CTkButton(root, text="11")
        btn_12 = ctk.CTkButton(root, text="12")
        btn_13 = ctk.CTkButton(root, text="13")

        btn_14 = ctk.CTkButton(root, text="14")
        btn_15 = ctk.CTkButton(root, text="15")
        btn_16 = ctk.CTkButton(root, text="16")
        btn_17 = ctk.CTkButton(root, text="17")
        btn_18 = ctk.CTkButton(root, text="18")

        frame.grid(row=0, column=1, pady=2, sticky="nsew", columnspan=3)
        entry1.grid(row=1, column=0, pady=2, sticky="ew", columnspan=5)
        btn_1.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")
        btn_2.grid(row=2, column=2, padx=15, pady=15, sticky="nsew")
        btn_3.grid(row=2, column=3, padx=15, pady=15, sticky="nsew")

        text2.grid(row=3, column=0, padx=5, sticky="ew")
        entry2.grid(row=3, column=1, padx=10, pady=5, sticky="nsew", columnspan=3)

        btn_4.grid(row=4, column=0, padx=10, pady=10, sticky="ns")
        btn_5.grid(row=4, column=1, padx=10, pady=10, sticky="ns")
        btn_6.grid(row=4, column=2, padx=10, pady=10, sticky="ns")
        btn_7.grid(row=4, column=3, padx=10, pady=10, sticky="ns")
        btn_8.grid(row=4, column=4, padx=10, pady=10, sticky="ns")

        btn_9.grid(row=5, column=0, padx=10, pady=10, sticky="ns")
        btn_10.grid(row=5, column=1, padx=10, pady=10, sticky="ns")
        btn_11.grid(row=5, column=2, padx=10, pady=10, sticky="ns")
        btn_12.grid(row=5, column=3, padx=10, pady=10, sticky="ns")
        btn_13.grid(row=5, column=4, padx=10, pady=10, sticky="ns")

        btn_14.grid(row=6, column=0, padx=10, pady=10, sticky="ns")
        btn_15.grid(row=6, column=1, padx=10, pady=10, sticky="ns")
        btn_16.grid(row=6, column=2, padx=10, pady=10, sticky="ns")
        btn_17.grid(row=6, column=3, padx=10, pady=10, sticky="ns")
        btn_18.grid(row=6, column=4, padx=10, pady=10, sticky="ns")

        blankspace = ctk.CTkLabel(root, text="")
        blankspace.grid(row=7)
        
        
if __name__ == "__main__": 
    root = ctk.CTk()
    vector_calculator = VectorCalc(root)
    root.mainloop()