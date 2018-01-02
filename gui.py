from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import nltk
from nltk.corpus import wordnet as wn
import PlagueX_2_0_main
import PlagueX_2_0_main_custom
import PlagueX_2_0_concept_corpus
import webbrowser
import os
class Gui:
        
    def page1(self):
        self.inputfiles = []
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        var1.set(1)
        
        
        
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 200)
        data_frame.pack(side = "top")

        
        
        E1 = Entry(data_frame)
        E2 = Entry(data_frame)
        E3 = Entry(data_frame)
        E4 = Entry(data_frame)
        self.input_1 = ""
        self.input_2 = ""
        self.input_3 = ""
        
        def a1():
            self.input_1 = str(filedialog.askdirectory(initialdir = "D:\\CS\\px\\Test Cases\\", parent=window,title='Choose Folder'))
            print(self.input_1)
            
        def a2():
            self.input_2 = ((str(filedialog.askopenfilename(initialdir = "D:\\CS\\px\\Test Cases\\", parent=window,title='Choose a file'))),)
            print(self.input_2)
        def a3():
            self.input_3 = filedialog.askopenfilenames(initialdir = "D:\\CS\\px\\Test Cases\\", parent=window,title='Choose files')
            print(self.input_3)
            
        button_1 = Button(data_frame, text = "Select Folder", fg = "#2c3e50", bg = "#ecf0f1", font = ("Helvetica 9 bold"), command =a1 , width = 22)
        button_2 = Button(data_frame, text = "Select Query", fg = "#2c3e50", bg = "#ecf0f1", font = ("Helvetica 9 bold"), command =a2 )
        button_3 = Button(data_frame, text = "Select Data", fg = "#2c3e50", bg = "#ecf0f1", font = ("Helvetica 9 bold"), command =a3 ) 
        def b1():
            button_1['state'] = "normal"
            button_2['state'] = "disabled"
            button_3['state'] = "disabled"
            E1['state'] = "disabled"
            E2['state'] = "disabled"
            E3['state'] = "disabled"
            E4['state'] = "disabled"
        def b2():
            button_1['state'] = "disabled"
            button_2['state'] = "normal"
            button_3['state'] = "normal"
            E1['state'] = "disabled"
            E2['state'] = "disabled"
            E3['state'] = "disabled"
            E4['state'] = "disabled"
        def b3():
            button_1['state'] = "disabled"
            button_2['state'] = "disabled"
            button_3['state'] = "disabled"
            E1['state'] = "normal"
            E2['state'] = "normal"
            E3['state'] = "normal"
            E4['state'] = "normal"
        R1 = Radiobutton(data_frame, text="All Documents in: ", variable=var1, value=1,bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 10 bold"), command = b1)
        R1.invoke()
        R1.select()
        R1.grid(row = 0, column = 0, sticky = W)
 
        R2 = Radiobutton(data_frame, text="Test Cases:", variable=var1, value=2,bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 10 bold"), command = b2)
        R2.grid(row = 1, column = 0, sticky = W)

        R3 = Radiobutton(data_frame, text="Custom Text:", variable=var1, value=3,bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 10 bold"), command = b3)
        
        
        
        button_1.grid(row = 0, column = 1, columnspan = 2, sticky = W , pady = 5, padx = 2)
        button_2.grid(row = 1, column = 1, sticky = W , pady = 5, padx = 2)
        button_3.grid(row = 1, column = 2, sticky = W , pady = 5, padx = 2)
        R3.grid(row = 2, column = 0 , sticky = W)
        E1.grid(row = 2, column = 1, columnspan = 2 , sticky = W , pady = 5, padx = 2)
        E2.grid(row = 3, column = 1, columnspan = 2 , sticky = W , pady = 5, padx = 2)
        E3.grid(row = 4, column = 1, columnspan = 2 , sticky = W , pady = 5, padx = 2)
        E4.grid(row = 5, column = 1, columnspan = 2 , sticky = W , pady = 5, padx = 2)
        def process():
            print(var1.get())
            print(self.input_1)
            print(self.input_2)
            print(self.input_3)
            if var1.get() == 1:
                self.data = PlagueX_2_0_main.main(1,self.input_1)
            if var1.get() == 2:
                self.data = PlagueX_2_0_main.main(2,self.input_2+self.input_3)
            if var1.get() == 3:
                self.data = PlagueX_2_0_main.main(3,(E1.get(),E2.get(),E3.get(),E4.get()))
            webbrowser.open_new("output.txt")
        def hood():
            data = PlagueX_2_0_main_custom.main(E1.get(),E2.get(),E3.get(),E4.get())
            self.tokens = data[0]
            self.nounset = data[1]
            self.concepts = data[2]
            self.scores = data[3]
            self.d1 = E1.get()
            self.d2 = E2.get()
            self.d3 = E3.get()
            self.d4 = E4.get()
            webbrowser.open_new("output.txt")
            window.destroy()
            self.page2()

        footer = Frame(main_frame, width = 600, height = 70, bg = "#ecf0f1")
        button1 = Button(footer, text = "Under the Hood", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 8, command = hood)
        button1.pack(side = "left")
        button2 = Button(footer, text = "Get Results", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") ,pady = 8, command = process )
        button2.pack(side = "right")

        footer.pack_propagate(0)
        footer.pack(side = "bottom")
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
    def page2(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5, width = 600,height = 500)
        data_frame.pack_propagate(0)
        data_frame.pack(side = "top")
        
        next_frame = Frame(main_frame, bg = "#ecf0f1", pady = 2 )
        next_frame.pack(side = "top")
        
        
        label1 = Label (data_frame, text = "Tokenized Text", width = 20, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 14 bold"))
        label1.pack(anchor = "nw")
        label2 = Label (data_frame, text = str(self.d1), wraplength = 500, bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 11 bold"))
        label2.pack(anchor = "nw",pady = 10)
        text1 = Label (data_frame, text = str(self.tokens[0]),wraplength = 500, bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text1.pack(anchor = "nw",pady = 3)
        label3 = Label (data_frame, text = str(self.d2), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label3.pack(anchor = "nw",pady = 10)
        text2 = Label (data_frame, text = str(self.tokens[1]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text2.pack(anchor = "nw",pady = 3)
        label4 = Label (data_frame, text = str(self.d3), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label4.pack(anchor = "nw",pady = 10)
        text3 = Label (data_frame, text = str(self.tokens[2]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text3.pack(anchor = "nw",pady = 3)
        label5 = Label (data_frame, text = str(self.d4), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label5.pack(anchor = "nw",pady = 10)
        text4 = Label (data_frame, text = str(self.tokens[3]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text4.pack(anchor = "nw",pady = 3)
        
        def next():
            window.destroy()
            self.page3()
            
        
        
        footer = Frame(main_frame, width = 600, height = 120, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)
        
        inspectlabel = Label(footer, text = "Inspect Integrity:", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 8)
        inspectlabel.pack(anchor = "nw")
        
        button2 = Button(next_frame, text = "NEXT", width = 8, bd = 5, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 12 bold") , command = next)
        button2.pack(anchor = "center", pady =8)
        
        E1 = Entry(footer)
        E1.pack(anchor = "center")
        ttext = StringVar()
        def np():
            pos = nltk.word_tokenize(E1.get())
            tokenized_text = nltk.pos_tag(pos)
            ttext.set(tokenized_text)
        
        button2 = Button(footer, text = "Get Tokens", width = 10, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , command = np )
        button2.pack(anchor = "center", pady = 4)
        text4 = Label (footer, textvariable = ttext, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 9"))
        text4.pack(anchor = "center",pady = 3)
        
        
        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
        
        
        
        
    def page3(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5)
        data_frame.pack(side = "top")
        
        label1 = Label (data_frame, text = "Concept Corpus", width = 20, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 14 bold"))
        label1.pack(anchor = "nw")
        label2 = Label (data_frame, text = "Nouns Set", bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label2.pack(anchor = "nw",pady = 10)
        
        text1 = Label (data_frame, text = str(self.nounset), wraplength=200, bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text1.pack(anchor = "nw",pady = 3)
        
        label2 = Label (data_frame, text = "Reduced Concepts", bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label2.pack(anchor = "nw",pady = 10)
        
        text1 = Label (data_frame, text = str(self.concepts), wraplength=200, bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text1.pack(anchor = "nw",pady = 3)
        
        def next():
            window.destroy()
            self.page4()
            
        def hood():
            top = Toplevel()
            top.title("Data Analysis")
            main_frame = Frame(top, width = 600, height = 800)
            header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
            header.pack_propagate(0)
            header.pack(side = "top")
            load = Image.open("logo.png")
            render = ImageTk.PhotoImage(load)

                # labels can be text or images
            img = Label(header, image=render, borderwidth = 0, highlightthickness =0)  
            img.image = render
            img.place(x=0, y=0)

            var1 = IntVar()
            data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 200)
            data_frame.pack(side = "top")
            def dataset():
                webbrowser.open_new("Data\Concept_Corpus\PlagueX_SynAnts.txt")
            button1 = Button(data_frame, text = "Dataset", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 12 bold") , pady = 8, command = dataset)
            button1.pack(anchor = "n", pady = 10)
            button2 = Button(data_frame, text = "Classifier Results", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 12 bold") , pady = 8, command = lambda: os.startfile('Data\Concept_Corpus\Results'))
            button2.pack(anchor ="n" , pady = 10)
            semframe = Frame(data_frame, bg = "#ecf0f1")
            semframe.pack(anchor = "center")
            path_frame = Frame(semframe, bg = "#ecf0f1", bd = 2, relief = "groove")
            lch_frame = Frame(semframe, bg = "#ecf0f1", bd = 4, relief = "ridge")
            wup_frame = Frame(semframe, bg = "#ecf0f1", bd = 2, relief = "groove")
            path_frame.pack(side = "left", pady = 8, padx = 3)
            lch_frame.pack(side = "left",pady = 8, padx = 3)
            wup_frame.pack(side = "left", pady = 8, padx = 3)
            
            text1 = Label (path_frame, text = "Path Similarity", fg = "#c0392b", bg = "#ecf0f1", font = ("Helvetica 14 bold"))
            text1.pack(side = "top",pady = 8, padx = 3)
            button3 = Button(path_frame, text = "ROC", width = 5, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , pady = 8, command = lambda: webbrowser.open_new("Data\Concept_Corpus\D_results\path_ROC_fin.jpg") )
            button3.pack(side = "top", pady = 10)
            text2 = Label (lch_frame, text = "LCH Similarity", fg = "#c0392b", bg = "#ecf0f1", font = ("Helvetica 14 bold"))
            text2.pack(side = "top",pady = 8, padx = 3)
            button4 = Button(lch_frame, text = "ROC", width = 5, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , pady = 8, command = lambda: webbrowser.open_new("Data\Concept_Corpus\D_results\lch_ROC_fin.jpg"))
            button4.pack(side = "top", pady = 10)
            text3 = Label(wup_frame, text = "WUP Similarity", fg = "#c0392b", bg = "#ecf0f1", font = ("Helvetica 14 bold"))
            text3.pack(side = "top",pady = 8, padx = 3)
            button6 = Button(wup_frame, text = "ROC", width = 5, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , pady = 8, command = lambda: webbrowser.open_new("Data\Concept_Corpus\D_results\wup_ROC_fin.jpg"))
            button6.pack(side = "top", pady = 10)
            button5 = Button(lch_frame, text = "True Positive - True Negative", width = 30, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 9 bold") , pady = 8, command = lambda: webbrowser.open_new("Data\Concept_Corpus\D_results\LCH.png"))
            button5.pack(side = "top", ipady = 5,padx = 10, pady = 19)
            


            footer = Frame(main_frame, width = 600, height = 70, bg = "#ecf0f1")
#            button1 = Button(footer, text = "Under the Hood", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 8, command = hood)
#            button1.pack(side = "left")
#            button2 = Button(footer, text = "Get Results", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") ,pady = 8, command = hood )
#            button2.pack(side = "right")
            footer.pack_propagate(0)
            footer.pack(side = "bottom")
            main_frame.pack_propagate(0)
            main_frame.pack()

        
        footer = Frame(main_frame, width = 600, height = 170, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)
        nfooter = Frame(footer, bg = "#c0392b")
        nfooter.pack(anchor = "n")
        mfooter = Frame(footer, bg = "#c0392b")
        mfooter.pack(anchor = "n")
        button1 = Button(mfooter, text = "Under the Hood", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 12 bold") , pady = 8, command = hood)
        button1.pack(side = "left", padx = 5)
        button2 = Button(mfooter, text = "Next", width = 10, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") ,pady = 8, command = next )
        button2.pack(side = "right", padx = 5)
        inspectlabel = Label(nfooter, text = "Inspect Integrity: (Threshold = 2.029)", width = 30, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 11 bold") , pady = 8)
        inspectlabel.pack(anchor = "nw")
        E1 = Entry(nfooter)
        E1.pack(anchor = "center")
        E2 = Entry(nfooter)
        E2.pack(anchor = "center")
        
        ttext = StringVar()
        def checksim(synset1,synset2):
            score = 0
            for syn1 in synset1:
                for syn2 in synset2:
                    try:
                        ns = wn.lch_similarity(syn1,syn2)
                    except:
                        ns = 0
        #            ns = wn.wup_similarity(syn1,syn2)
                    if isinstance(ns, float):
                        if ns > score:
                            score = ns

    
            return(score)
        def np():
            w1 = E1.get()
            w2 = E2.get()
            score = checksim(wn.synsets(w1),wn.synsets(w2))
            print(score)
            ttext.set(score)
        
        
        button2 = Button(nfooter, text = "Check Concept Match", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , command = np )
        button2.pack(anchor = "center", pady = 4)
        text4 = Label (nfooter, textvariable = ttext, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 9"))
        text4.pack(anchor = "center",pady = 3)

        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
        
    
    
    def page4(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5)
        data_frame.pack(side = "top")
        
        label1 = Button(data_frame, text = "Scope-Extender \n Algorithm ", width = 20, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 24 bold"), command = lambda: webbrowser.open_new("Data\Comp.mp4"))
        label1.pack(anchor = "center", pady = 80)
        
                
        def next():
            window.destroy()
            self.page5()
            
        footer = Frame(main_frame, width = 600, height = 120, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)
        button2 = Button(main_frame, text = "NEXT", width = 8, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 6, command = next)
        button2.pack(side = "bottom", pady =8)

        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
        
    def page5(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5)
        data_frame.pack(side = "top")
        
        label1 = Label (data_frame, text = "Scope-Extender \n Results ", width = 30, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 14 bold"))
        label1.pack(anchor = "center", pady = 80)
        mainstring = ""
        
        for comb in self.scores:
            for score in comb:
            
                try:
                    mainstring+=str(score[0])
                    mainstring+="\n"
                    mainstring+="\n"
                    mainstring+=str(score[1])
                    mainstring+="\n"
                    mainstring+="\n"
                    mainstring+="\n"
                    mainstring+="\n"
                except:
                    mainstring += ""
        text0 = Text(data_frame, font = ("Helvetica 9"))
        text0.insert(INSERT,mainstring)
        text0.pack(side = "top")
            
                
        def next():
            window.destroy()
            self.page6()
            
        footer = Frame(main_frame, width = 600, height = 80, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)
        button2 = Button(main_frame, text = "NEXT", width = 8, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 6, command = next)
        button2.pack(side = "bottom", pady =8)

        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
    def page6(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5)
        data_frame.pack(side = "top")

            
        label1 = Button(data_frame, text = "Local Analysis \n and Scoring Algorithm ", width = 20, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 24 bold"), command = lambda: webbrowser.open_new("Data\Comp2.mp4"))
        label1.pack(anchor = "center", pady = 80)
        
        mainstring = ""
        
        for comb in self.scores:
            for score in comb:
            
                try:
                    mainstring+=str(score[0])
                    mainstring+="\n"
                    mainstring+="\n"
                    mainstring+=str(score[1])
                    mainstring+="\n"
                    mainstring+=str(score[2])
                    mainstring+="\n"
                    mainstring+="\n"
                    mainstring+="\n"
                    mainstring+="\n"
                except:
                    mainstring += ""
        text0 = Text(data_frame, font = ("Helvetica 9"))
        text0.insert(INSERT,mainstring)
        text0.pack(side = "top")
        
        
        
        
        def hood():
            top = Toplevel()
            top.title("POS Weightage")
            main_frame = Frame(top, width = 600, height = 800)
            header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
            header.pack_propagate(0)
            header.pack(side = "top")
            load = Image.open("logo.png")
            render = ImageTk.PhotoImage(load)

                # labels can be text or images
            img = Label(header, image=render, borderwidth = 0, highlightthickness =0)  
            img.image = render
            img.place(x=0, y=0)

            var1 = IntVar()
            data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 200)
            data_frame.pack(side = "top")
            button1 = Button(data_frame, text = "Dataset", width = 40, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 15 bold") , pady = 8, command = lambda: webbrowser.open_new("Data\Mini_Corpus\Data_0_90.txt"))
            button1.pack(anchor = "n", pady = 30)
            button2 = Button(data_frame, text = "POS Weights Generation", width = 40, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 15 bold") , pady = 8, command = lambda: os.startfile('Data\Mini_Corpus\Analysis.py'))
            button2.pack(anchor ="s" , pady = 30)
            


            footer = Frame(main_frame, width = 600, height = 70, bg = "#ecf0f1")
#            button1 = Button(footer, text = "Under the Hood", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 8, command = hood)
#            button1.pack(side = "left")
#            button2 = Button(footer, text = "Get Results", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") ,pady = 8, command = hood )
#            button2.pack(side = "right")
            footer.pack_propagate(0)
            footer.pack(side = "bottom")
            main_frame.pack_propagate(0)
            main_frame.pack()

        
        
        
        
        button2 = Button(data_frame, text = "Under the hood: POS Weights", width = 30, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 6, command = hood)
        button2.pack(side = "bottom", pady =8)
            
        footer = Frame(main_frame, width = 600, height = 50, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)

        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
a = Gui()
a.page1()
    