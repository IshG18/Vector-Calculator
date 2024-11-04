from myvect import Vector
import customtkinter as ctk


class VectorCalc():

    #Building a class for holding and handling vector variables 
    class VectorViewFrame(ctk.CTkScrollableFrame):

        def __init__(self, root, *args, **kwargs):
            super().__init__(root, *args, **kwargs)
            self.vectDict = {}
            self.lastStr = " "
            self.count = 1
            guideLabel = ctk.CTkLabel(self, text="# Added vectors will appear here", text_color="gray")
            guideLabel.grid(row=0)
            self.guideId = guideLabel.winfo_id()

    #Defining update, del, and plug in funcs
        def add(self, entry):
            vectorStr = entry.get().split(",")
            vectLis = []
            try:
                if entry.get() == self.lastStr:
                    raise ValueError()
                for i in vectorStr:
                    isDecimal = False
                    for char in  i:
                        if char == '.':
                            isDecimal = True 
                            vectLis.append(float(i))
                            break
                    if not isDecimal:
                        vectLis.append(int(i))
                        
                vector = Vector(vectLis)    
                self.vectDict.update({f"v{self.count}": vector})
                label = ctk.CTkLabel(self, text=f"v{self.count}: {vector}")
                label.grid(row=self.count, sticky="w")
                self.lastStr = entry.get()
                self.count += 1
            except ValueError:
                entry.delete(-1, "end")
                entry.insert(-1, f"User Error: Bad or Same List Given -->{vectorStr}")

        def delLast(self):
            try:
                self.vectDict.popitem()
                #resets for reshowing labels
                self.count = 1
            except KeyError:
                print("No Vectors on Screen!")
            
            for widget in self.winfo_children():
                if widget.winfo_id() == self.guideId: #comment label
                    pass
                else:
                    widget.destroy()

        #Adding back each label for each key in dictionary
            for key in self.vectDict:
                label = ctk.CTkLabel(self, text=f"{key}: {self.vectDict[key]}")
                label.grid(row=self.count, sticky="w")
                self.count += 1

        def plugIn(self, entry, varEntry):
            varName = varEntry.get()
            #check for a match in dict
            print()
            if varName in self.vectDict.keys():
                varEntry.delete(-1, "end")
                VectorCalc.entryAdd(entry, varName)
            else:
                varEntry.delete(-1, "end")
                VectorCalc.entryAdd(entry, "unknown")


    def __init__(self, root):
        root.geometry("600x600")
        root.title("Vector Calculator <3")

    #Defining Grid system (5x8 Grid)
        root.grid_columnconfigure((0,1,2,3,4), weight=1)
        root.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)

    #Frame, Entry and related buttons
        frame = VectorCalc.VectorViewFrame(root, height=115)
        vectorEntry = ctk.CTkEntry(root, placeholder_text="Input for vector, number(s) seperated by comma")
        frame.grid(row=0, column=1, pady=2, sticky="nsew", columnspan=3)
        vectorEntry.grid(row=1, column=0, pady=2, sticky="ew", columnspan=5)

        var_entry = ctk.CTkEntry(root, width=40)
        btn_1 = ctk.CTkButton(root, text="Add", command=lambda: frame.add(vectorEntry))
        btn_2 = ctk.CTkButton(root, text="Delete", command=lambda: frame.delLast())
        btn_3 = ctk.CTkButton(root, text="Plug-In", command=lambda: frame.plugIn(inputArea, var_entry))
        var_entry.grid(row=2, column=4, pady=15, sticky="w")
        btn_1.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")
        btn_2.grid(row=2, column=2, padx=15, pady=15, sticky="nsew")
        btn_3.grid(row=2, column=3, padx=15, pady=15, sticky="nsew")

    #Entry, and functional buttons
        guide2 = ctk.CTkLabel(root, text="Calculate:", fg_color="transparent", text_color="grey")
        inputArea = ctk.CTkEntry(root)
        guide2.grid(row=3, column=0, padx=5, sticky="ew")
        inputArea.grid(row=3, column=1, padx=10, pady=5, sticky="nsew", columnspan=3)

        btn_4 = ctk.CTkButton(root, text="0", command=lambda: VectorCalc.entryAdd(inputArea, "0"))
        btn_5 = ctk.CTkButton(root, text="1", command=lambda: VectorCalc.entryAdd(inputArea, "1"))
        btn_6 = ctk.CTkButton(root, text="2", command=lambda: VectorCalc.entryAdd(inputArea, "2"))
        btn_7 = ctk.CTkButton(root, text="3", command=lambda: VectorCalc.entryAdd(inputArea, "3"))
        btn_8 = ctk.CTkButton(root, text="n/a")
        btn_4.grid(row=4, column=0, padx=10, pady=10, sticky="ns")
        btn_5.grid(row=4, column=1, padx=10, pady=10, sticky="ns")
        btn_6.grid(row=4, column=2, padx=10, pady=10, sticky="ns")
        btn_7.grid(row=4, column=3, padx=10, pady=10, sticky="ns")
        btn_8.grid(row=4, column=4, padx=10, pady=10, sticky="ns")

        btn_9 = ctk.CTkButton(root, text="4", command=lambda: VectorCalc.entryAdd(inputArea, "4"))
        btn_10 = ctk.CTkButton(root, text="5", command=lambda: VectorCalc.entryAdd(inputArea, "5"))
        btn_11 = ctk.CTkButton(root, text="6", command=lambda: VectorCalc.entryAdd(inputArea, "6"))
        btn_12 = ctk.CTkButton(root, text="n/a")
        btn_13 = ctk.CTkButton(root, text="n/a")
        btn_9.grid(row=5, column=0, padx=10, pady=10, sticky="ns")
        btn_10.grid(row=5, column=1, padx=10, pady=10, sticky="ns")
        btn_11.grid(row=5, column=2, padx=10, pady=10, sticky="ns")
        btn_12.grid(row=5, column=3, padx=10, pady=10, sticky="ns")
        btn_13.grid(row=5, column=4, padx=10, pady=10, sticky="ns")

        btn_14 = ctk.CTkButton(root, text="7", command=lambda: VectorCalc.entryAdd(inputArea, "7"))
        btn_15 = ctk.CTkButton(root, text="8", command=lambda: VectorCalc.entryAdd(inputArea, "8"))
        btn_16 = ctk.CTkButton(root, text="9", command=lambda: VectorCalc.entryAdd(inputArea, "9"))
        btn_17 = ctk.CTkButton(root, text="n/a")
        btn_18 = ctk.CTkButton(root, text="n/a")
        btn_14.grid(row=6, column=0, padx=10, pady=10, sticky="ns")
        btn_15.grid(row=6, column=1, padx=10, pady=10, sticky="ns")
        btn_16.grid(row=6, column=2, padx=10, pady=10, sticky="ns")
        btn_17.grid(row=6, column=3, padx=10, pady=10, sticky="ns")
        btn_18.grid(row=6, column=4, padx=10, pady=10, sticky="ns")

    #Special Buttons
        sbtn_1 = ctk.CTkButton(root, text="n/a")
        sbtn_2 = ctk.CTkButton(root, text="n/a")
        sbtn_3 = ctk.CTkButton(root, text="n/a")
        sbtn_4 = ctk.CTkButton(root, text="n/a")
        sbtn_5 = ctk.CTkButton(root, text="n/a")
        sbtn_1.grid(row=7, column=0, padx=10, pady=10, sticky="ns")
        sbtn_2.grid(row=7, column=1, padx=10, pady=10, sticky="ns")
        sbtn_3.grid(row=7, column=2, padx=10, pady=10, sticky="ns")
        sbtn_4.grid(row=7, column=3, padx=10, pady=10, sticky="ns")
        sbtn_5.grid(row=7, column=4, padx=10, pady=10, sticky="ns")

    def entryAdd(entry, strToAdd):
        entry.insert("end", strToAdd)

    def calculate(self, entry):
        pass


if __name__ == "__main__": 
    root = ctk.CTk()
    vectorCalculator = VectorCalc(root)
    root.mainloop()