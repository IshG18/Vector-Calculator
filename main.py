from myvect import Vector
import customtkinter as ctk
ctk.set_appearance_mode("dark")

class VectorCalc():
    history_dict = {}
    history_cnt = 1
    history_window = None

    #class for holding and handling vector variables 
    class VectorViewFrame(ctk.CTkScrollableFrame):

        def __init__(self, root, *args, **kwargs):
            super().__init__(root, *args, **kwargs)
            self.vectDict = {}
            self.lastStr = " "
            self.count = 1
            guideLabel = ctk.CTkLabel(self, text="# Added vectors will appear here", text_color="gray")
            guideLabel.grid(row=0)
            self.guideId = guideLabel.winfo_id()

    #Defining update, del, and plug-in funcs
        def add(self, entry):
            vectorStr = entry.get().split(",")
            vectLis = []
            try:
                if entry.get() == self.lastStr:
                    raise ValueError()
                for i in vectorStr:
                    if '.' in  i:
                        vectLis.append(float(i))
                    else:
                        vectLis.append(int(i))
                        
                vector = Vector(vectLis)    
                self.vectDict.update({f"v{self.count}": (vector, round(self.length(vector), 4))})
                label = ctk.CTkLabel(self, text=f"v{self.count}: {vector}\t|𝑣| = {round(self.length(vector), 4)}") #ad lenght to dictionary, so it shows when you delete something
                label.grid(row=self.count, sticky="w")
                self.lastStr = entry.get()
                self.count += 1
            except ValueError:
                entry.delete(-1, "end")
                entry.insert(-1, f"Err: {vectorStr}")

        def delLast(self):
            try:
                self.vectDict.popitem()
                self.count = 1
            except KeyError:
                return
            
            for widget in self.winfo_children():
                if widget.winfo_id() != self.guideId:
                    widget.destroy()

        #Adding back each label for each vector
            for name, (vect, length) in self.vectDict.items():
                label = ctk.CTkLabel(self, text=f"{name}: {vect}\t\t|𝑣| = {length}")
                label.grid(row=self.count, sticky="w")
                self.count += 1

        def plugIn(self, entry, varEntry):
            varName = varEntry.get()
            #check for a match in dict
            if varName in self.vectDict:
                result = varName
            else:
                result = "unknown"

            varEntry.delete(-1, "end")
            entry.insert("end", result)

        def length(self, v):
            v = v.nums
            sum = 0
            for n in v:
                sum += n*n
            return sum**.5

    class HistoryWindow(ctk.CTkToplevel):

        def __init__(self, parent, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.ref = parent
            self.geometry("350x500+100+100")
            self.title("History")

            self.grid_rowconfigure((0,1,2), weight=1)
            self.grid_columnconfigure((0,1,2), weight=1)

            self.hd = VectorCalc.history_dict
            self.scrFrame = ctk.CTkScrollableFrame(self, fg_color="#242424", corner_radius=0)
            self.scrFrame.grid(row=0, column=0, sticky="nsew", pady=(0, 100), columnspan=3, rowspan=2)

            self.selected = ctk.CTkEntry(self, placeholder_text="Click a checkbox", state="disabled")
            self.addbtn = ctk.CTkButton(self, text="Select", command=lambda: self.addEqu(self.selected.get()))
            
            check_var = ctk.StringVar(value=1)

            for item, key in self.hd.items():
                textStr = f'{item}  =  {key[1]}'
                box = ctk.CTkCheckBox(self.scrFrame, corner_radius=10, text=textStr, text_color="#dce4ee", checkbox_width=12, checkbox_height=12,
                variable=check_var, onvalue=1, offvalue=0, height=60, font=(None,16), hover=True, hover_color="#7d8185")
                box.configure(command=lambda cb=box:self.clicked(cb, key[2] if len(key) == 3 else None))
                box.pack(side="top", anchor='w', padx=(30,0))
                box.pack_configure(pady=(50,20) if key[0] == 1 else (0,20))
            
            self.selected.grid(row=1, column=1, columnspan=1, sticky='new', padx=(20,0), pady=(350,0))
            self.addbtn.grid(row=2, column=1, columnspan=1, sticky='new', padx=(20,0), pady=(0,10))

        #Keybinds
            self.bind("<Return>", lambda event: self.addEqu(self.selected.get()))
            self.bind("<Escape>", lambda event: self.destroy())

        def clicked(self, checkbox, t=None):
            for widget in self.scrFrame.winfo_children():
                if widget != checkbox and 'checkbox' in widget.winfo_pathname(widget.winfo_id()):
                    widget.deselect()

            self.selected.configure(state="normal")
            insert_text = checkbox.cget("text").split('=')[1] if t in ('d', 'p') else checkbox.cget("text").split('=')[0]
            self.selected.delete(-1, "end")
            self.selected.insert("end", insert_text)

            self.selected.configure(state="disabled")

        def addEqu(self, text):
            self.ref.entryAdd(text, True)

        def updtFrame(self, text, tup):
            check_var = ctk.StringVar(value=1)
            textStr = f'{text} = {tup[1]}'
            box = ctk.CTkCheckBox(self.scrFrame, corner_radius=10, text=textStr, text_color="#dce4ee", checkbox_width=12, checkbox_height=12,
            variable=check_var, onvalue=1, offvalue=0, height=60, font=(None,16),hover=True, hover_color="#7d8185")
            box.configure(command=lambda cb=box:self.clicked(cb, tup[2] if len(tup) == 3 else None))
            box.pack(side="top", anchor='w', padx=(30,0))

    def __init__(self, root):
        root.geometry("410x550+700+50")
        root.title("Vector Calculator <3")
        root.resizable(False, False)

    #Defining Grid system (5x8 Grid)
        root.grid_columnconfigure((0,1,2,3,4), weight=1)
        root.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)

    #Frame, Vector Entry
        frame = self.VectorViewFrame(root, height=115)
        self.inputArea = ctk.CTkEntry(root)
        
    #Var Entry, Buttons
        vectorEntry = ctk.CTkEntry(root, placeholder_text="Input for vector, number(s) seperated by comma")
        frame.grid(row=0, column=1, pady=2, sticky="nsew", columnspan=3)
        vectorEntry.grid(row=1, column=0, pady=2, sticky="ew", columnspan=5)

        var_entry = ctk.CTkEntry(root, width=40)
        btn_1 = ctk.CTkButton(root, text="Add", command=lambda: frame.add(vectorEntry))
        btn_2 = ctk.CTkButton(root, text="Delete", command=lambda: frame.delLast())
        btn_3 = ctk.CTkButton(root, text="Plug-In", command=lambda: frame.plugIn(self.inputArea, var_entry))
        var_entry.grid(row=2, column=4, pady=15, sticky="w")
        btn_1.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")
        btn_2.grid(row=2, column=2, padx=15, pady=15, sticky="nsew")
        btn_3.grid(row=2, column=3, padx=15, pady=15, sticky="nsew")

    #Var Entry
        guide2 = ctk.CTkLabel(root, text="Calculate:", fg_color="transparent", text_color="grey")
        guide2.grid(row=3, column=0, padx=5, sticky="ew")
        self.inputArea.grid(row=3, column=1, padx=10, pady=5, sticky="nsew", columnspan=3)

    #Buttons
        btn_4 = ctk.CTkButton(root, text="0", command=lambda: self.entryAdd("0"))
        btn_5 = ctk.CTkButton(root, text="1", command=lambda: self.entryAdd("1"))
        btn_6 = ctk.CTkButton(root, text="2", command=lambda: self.entryAdd("2"))
        btn_7 = ctk.CTkButton(root, text="3", command=lambda: self.entryAdd("3"))
        btn_8 = ctk.CTkButton(root, text="AC", command=lambda: self.inputArea.delete(-1, "end"))
        btn_9 = ctk.CTkButton(root, text="4", command=lambda: self.entryAdd("4"))
        btn_10 = ctk.CTkButton(root, text="5", command=lambda: self.entryAdd("5"))
        btn_11 = ctk.CTkButton(root, text="6", command=lambda: self.entryAdd("6"))
        btn_12 = ctk.CTkButton(root, text="\u00F7", command=lambda: self.entryAdd("\u00F7"))
        btn_13 = ctk.CTkButton(root, text="+", command=lambda: self.entryAdd("+"))
        btn_14 = ctk.CTkButton(root, text="7", command=lambda: self.entryAdd("7"))
        btn_15 = ctk.CTkButton(root, text="8", command=lambda: self.entryAdd("8"))
        btn_16 = ctk.CTkButton(root, text="9", command=lambda: self.entryAdd("9"))
        btn_17 = ctk.CTkButton(root, text="\u00D7", command=lambda: self.entryAdd("\u00D7"))
        btn_18 = ctk.CTkButton(root, text="-", command=lambda: self.entryAdd("-"))
        
    #Special Buttons
        sbtn_1 = ctk.CTkButton(root, text="H", command=lambda:self.open_history())
        sbtn_2 = ctk.CTkButton(root, text="A ⦁ B", command=lambda: self.dot_p(frame, self.inputArea))
        sbtn_3 = ctk.CTkButton(root, text="D |AB|", command=lambda: self.any_dist(frame, self.inputArea))
        sbtn_4 = ctk.CTkButton(root, text=".", command=lambda: self.entryAdd("."))
        sbtn_5 = ctk.CTkButton(root, text="=", command=lambda: self.calc(frame.vectDict, self.inputArea, {}))
        
    #Grid Layout
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
        sbtn_1.grid(row=7, column=0, padx=10, pady=10, sticky="ns")
        sbtn_2.grid(row=7, column=1, padx=10, pady=10, sticky="ns")
        sbtn_3.grid(row=7, column=2, padx=10, pady=10, sticky="ns")
        sbtn_4.grid(row=7, column=3, padx=10, pady=10, sticky="ns")
        sbtn_5.grid(row=7, column=4, padx=10, pady=10, sticky="ns")

    #Keyboard Input
        root.bind("<Return>", lambda event: self.calc(frame.vectDict, self.inputArea, {}))
        root.bind("<Escape>", lambda event: root.destroy())
        root.bind("<Delete>", lambda event: self.inputArea.delete(-1, "end"))
        root.bind("<H>", lambda event: self.open_history())
        root.bind("<Shift-Alt_L>", lambda event: frame.add(vectorEntry))

    def open_history(self):
        if self.history_window is None or not self.history_window.winfo_exists():
            self.history_window = self.HistoryWindow(self)
        else:
            self.history_window.focus()  # if window exists focus it

    def updtHistory(self, text, tuple):
        self.history_dict[text] = tuple
        if self.history_window is None or not self.history_window.winfo_exists():   
            pass
        else:
            self.history_window.updtFrame(text, tuple)
        self.history_cnt += 1

    def entryAdd(self,strToAdd, delF=False):
        if delF:
            self.inputArea.delete(-1, "end")
        self.inputArea.insert("end", strToAdd)

    def ez_calc(self, x, y, operand):
        if operand == "+":
            return x + y
            
        elif operand == "\u00F7":
            return x / y

        elif operand == "-":
            return x - y

        elif operand == "\u00D7":
            return x * y

#Precedence logic for mult, div, add, and sub
    def rank(self, op1, op2): 
        if op1 == "\u00D7" or op1 == "\u00F7":
            return op1
        elif op2 == "\u00D7" or op2 == "\u00F7":
            return op2
        elif op1 == "":
            return op2
        else:
            return op1
        
    def list_find(self, lst, pos):
    #Handle negative index
        if pos < 0:
            return 0  
        try:
            lst[pos]
            return lst[pos]
        except IndexError:
            return 0

    def createDict(self, input):
        pos_dict = {}
    #Catching negative output on final answer
        try:     
            val = float(input)
            if val < 0:
                return pos_dict #will return the empty dict 
        except ValueError:
            pass # Is a valid equation or an vector

        for index, char in enumerate(input):
            if char in ('+', '-', '\u00F7', '\u00D7'):
                pos_dict[index] = char

        return pos_dict

    def calc(self, frame_dict, entry, equ_dict):
        input = entry.get()
        input = input.replace(' ', '')
        input = input.replace('*', '\u00D7')
        input = input.replace('/', '\u00F7')
        his_str = input

    #Removing lenght from frame dictionary
        vect_dict = {key: val[0] for key, val in frame_dict.items()}

        pos_dict = {}
        v_cnt = 1
        op_lis = ['+', '-', '\u00D7', '\u00F7']

        def trueop(oper):
            try:
                oper = int(oper)
                return oper
            except ValueError:
                try:
                    oper = float(oper)
                    return oper
                except ValueError:
                    return vect_dict.get(oper, equ_dict.get(oper, False))
                
        def get_equ(input, v_cnt, pos_dict):
            pd=pos_dict
            prev_op = ""
            op_pos = ""
            pdkey_lis = list(pd.keys())
            
            for key, val in pd.items():
                op = val
                r_val = self.rank(prev_op, op)
                if r_val == op and prev_op != op:  #check if its the same op to keep the precedence   
                    op_pos = key
                prev_op = r_val
            op = r_val

            s = self.list_find(pdkey_lis, (pdkey_lis.index(op_pos))-1) or 0
            e = self.list_find(pdkey_lis, pdkey_lis.index(op_pos)+1) or len(input)

            equ = input[s:e]
            adjust = 0
            negF = False
            if equ[0] in op_lis:
                if equ[0] == '-': #checks for a negative value 
                    negF = True
                equ = equ[1:]
                adjust += 1
            if equ[-1] in op_lis:
                equ = equ[:-1]

            
            try:
                oper1, oper2 = equ.split(op)
                
                if negF:    #switches neg value backk to it's original  
                    oper1 = trueop(f'-{oper1}')
                else:
                    oper1 = trueop(oper1)
                oper2 = trueop(oper2)
            except ValueError: #user entered a negative vector like '-v1' or '-'v1+v2
                return 'equ', v_cnt, pd
            
            if oper1 == False or oper2 == False:
                return "op", v_cnt, pd
            else:
                ans = self.ez_calc(oper1, oper2, op) 
                if 'e' in str(ans).lower(): #checking if it's in scientific notation
                    return "sci", v_cnt, pd
                else:
                    ans = round(ans, 4)

                if isinstance(oper1, Vector) or isinstance(oper2, Vector):
                    equStr = f'ans{v_cnt}'
                    equ_dict[equStr] = ans

                    finalStr =  input[:s+adjust]+equStr+input[e:]
                    v_cnt += 1

                else:
                    if negF:
                        finalStr = input[:s]+str(ans)+input[e:]
                    else:
                        finalStr = input[:s+adjust]+str(ans)+input[e:]
                       
            return finalStr, v_cnt, pd

        pos_dict = self.createDict(input)
        if pos_dict:
            while pos_dict:
                    input, v_cnt, pos_dict = get_equ(input, v_cnt, pos_dict)                    
                    
                #Checking for errors
                    if input == "sci":
                        entry.delete(-1, "end")
                        entry.insert("end", "Values exceed size limit")
                        break
                    elif input == "op":
                        entry.delete(-1, "end")
                        entry.insert("end", "Invalid operands")
                        break
                    elif input == "equ": 
                        entry.delete(-1, "end")
                        entry.insert("end", "Can't use negative vectors")

                    pos_dict = self.createDict(input) 
             
            if input not in ("op","sci","equ"):
                entry.delete(-1, "end")
                if input in equ_dict:
                    self.updtHistory(his_str, (self.history_cnt, equ_dict[input.strip()]))
                    entry.insert("end", equ_dict[input])
                else:
                    self.updtHistory(his_str, (self.history_cnt, input))
                    entry.insert("end", input)
            
    #Handling any other error
        else: 
            if trueop(input):
                entry.delete(-1, "end")
                entry.insert("end", f"{input}")

            else:
                entry.delete(-1, "end")
                entry.insert("end", f"Invalid Equation") 

    def collect_list(self, vdict, dtitle):  #Collects vectors, and string version
        list = []
        prompt = ctk.CTkInputDialog(title=f"{dtitle}", text="Input vectors as such: v3, v4...")
        p = prompt.get_input()
        if p != None:
            for v in p.split(","):
                v = v.strip()
                if v in vdict:
                    list.append(vdict[v])
                else:
                    return 0, p
        else:
            return 0, p

        return list, p

    def dot_p(self, vframe, entry):
        vectD = {key: val[0] for key, val in vframe.vectDict.items()}
        result, potent_err = self.collect_list(vectD, "Dot Product")
        if potent_err == None:
            entry.delete(-1, "end")
            entry.insert("end", f"Error: {potent_err}")
            return
        input = f"{potent_err.replace(' ', '').replace(',', ' ⦁ ')}"
        if result != 0 and len(result) == 2:
            v1, v2 = result
        else:
            entry.delete(-1, "end")
            entry.insert("end", f"Error: {potent_err}")
            return
        
        sum = 0
        if v1.len >= v2.len:
            rank = v1.len
            v1, v2 = v1.nums, v2.nums
        else:
            rank = v2.len
            v1, v2 = v2.nums, v1.nums
        #Changes vects to their array in order of rank

        for n in range(rank):
            try:
                sum += v1[n] * v2[n]
            except IndexError:
                sum += v1[n] * 1
        
        entry.delete(-1, "end")
        entry.insert("end", f"{sum}")
        self.updtHistory(input, (self.history_cnt, sum, 'p'))

    def any_dist(self, vframe, entry): #avg pair-wise distance d
        vectD = {key: val[0] for key, val in vframe.vectDict.items()}
        def dist(v1, v2): #straight-line method
            square_eud_dist = 0
            if v1.len >= v2.len:
                rank = v1.len
                v1, v2 = v1.nums, v2.nums
            else:
                rank = v2.len
                v1, v2 = v2.nums, v1.nums

            for n in range(rank):
                try:
                    square_eud_dist += (v1[n]-v2[n])*(v1[n]-v2[n]) #squaring
                except IndexError:
                    square_eud_dist += (v1[n]-0)*(v1[n]-0) 

            return square_eud_dist**0.5

        result, potent_err = self.collect_list(vectD, "Distance of Vectors")
        if potent_err == None:
            entry.delete(-1, "end")
            entry.insert("end", f"Error: {potent_err}")
            return
        input = f"Dist({potent_err.replace(' ', '').replace(',', ' ')})"

        if result != 0:
            if len(result) == 2:
                ans = round(dist(*result),4)
            elif len(result) > 2:
                sum = 0
                pairs = 0
                args = result
                for vnum in range(len(args)-1):
                    for i in range(vnum, len(args)-1):
                        sum += dist(args[vnum], args[i+1])
                        pairs+=1
                ans = round((sum/pairs),4)
            entry.delete(-1, "end")
            entry.insert("end", str(ans))
            self.updtHistory(input, (self.history_cnt, ans, 'd'))
        else:
            entry.delete(-1, "end")
            entry.insert("end", f"Vector Error: {potent_err}")
            return


if __name__ == "__main__":
    root = ctk.CTk()
    vectorCalculator = VectorCalc(root)
    root.mainloop()