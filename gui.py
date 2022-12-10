
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import openai
import nlpcloud
import json
from os import path

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
       
        self.ventana1.resizable(0,0)
        self.ventana1.configure(bg='white')
        self.ventana1.title("Centro psicologico")
        self.ventana1.geometry("650x700")
        barraMenu = tk.Menu(self.ventana1)
        self.ventana1.config(menu=barraMenu)
        barraMenu.add_cascade(label="Consulta psicologico",command=self.ventana2)#acomodo los elementos elen  menú
        barraMenu.add_cascade(label="Asistente psicologico",command=self.ventana3 )
        barraMenu.add_cascade(label="Chat psicologo",command=self.ventana4 )
        img = ImageTk.PhotoImage(Image.open("img.png"))
        Label(self.ventana1, image=img).place(x=120, y=0)
        label2 = Label(self.ventana1, text="Centro de tratamiento contra las drogas,\n alcohol, depresión, ansiedad, obesidad.", font=("Ariel", 12),bg="white")
        label2.place(x=180, y=140)

      
        

    
        
        self.ventana1.mainloop()


    def ventana2(self):
        self.ventana_two =tk.Toplevel()
        self.ventana_two.geometry("440x650")
        self.ventana_two.title("Consulta psicologico")
        self.ventana_two.configure(bg='white')
        self.img = ImageTk.PhotoImage(Image.open("img.png"))
        Label(self.ventana_two, image=self.img).place(x=20, y=0)
        caja2 = Entry(self.ventana_two, width=40,bg="#7FC2DC")
        caja2.place(x=160, y=250)
        caja3= Entry(self.ventana_two, width=40,bg="#7FC2DC")
        caja3.place(x=160, y=300)
        
        label2 = Label(self.ventana_two, text="TEST DE EVALUCACION")
        label2.place(x=150, y=140)
        label3 = Label(self.ventana_two, text="Como te siente  : ")
        label3.place(x=50, y=250)
        label4 = Label(self.ventana_two, text="Digite un nombre: ")
        label4.place(x=50, y=300)
        

        def send1():
            client = nlpcloud.Client("distilbert-base-uncased-finetuned-sst-2-english", "e8230b07b816c5aafa386309cd3bc694236b3bd3", gpu=False, lang="en")
            dato=client.sentiment(caja2.get())
            messagebox.showinfo(title="Usuando api 1 de sentimiento", message=dato)
            
            client1 = nlpcloud.Client("nllb-200-3-3b", "e8230b07b816c5aafa386309cd3bc694236b3bd3", gpu=False)
            dato1=client1.translation(caja2.get(), source="", target="ace_Arab")
            messagebox.showinfo(title="Usuando api 2 de traductor arabe", message=dato1)
            messagebox.showinfo(title="JSON", message="SE HA GUARDADO JSON")
            users = [
                  {
                    "Nombre": "",
                    "id": "" ,
                    "Tipo_de_serivicio": "",
                    "Valor_entrada": "",
                    "Valor_salida": "",
                                                                                
                                                                                                    
                                                                                                        
             }
            ]
                                                                        
            for user in users:
                                                 
                user['Nombre'] = caja3.get()
                user['id']  =1
                user['Tipo_de_serivicio'] = "Sercicio api de sentimiento y de traductor"
                user['Valor_entrada'] = caja2.get()
                user['Valor_salida'] = dato,dato1



                                                                                                    
            my_path = 'users.json'

            if path.exists(my_path):
                with open(my_path , 'r') as file:
                    previous_json = json.load(file)
                    users = previous_json + users
                    print(chr(27)+"[1;33m"+"Se ha guardado json\n") 
                    file.close()
                                                                                
                                                                                                        
            with open(my_path , 'w') as file:
                json.dump(users, file, indent=4)
                print(chr(27)+"[1;33m"+"Se ha guardado json\n") 
                file.close()
            self.ventana2()
        send1 = Button(self.ventana_two, text="Enviar",command=send1).place(x=200, y=400)
        
                                                                                     
        
        
        

        

    def ventana3(self):
        self.ventana_three =tk.Toplevel()
        self.ventana_three.resizable(0,0)
        self.ventana_three.geometry("440x650")
        self.ventana_three.configure(bg='white')
        self.ventana_three.title("Asistente psicologico")
        self.img = ImageTk.PhotoImage(Image.open("img.png"))
        Label(self.ventana_three, image=self.img).place(x=20, y=0)
        caja3 = Entry(self.ventana_three, width=40,bg="#7FC2DC")
        caja3.place(x=160, y=250)
        
        label2 = Label(self.ventana_three, text="Generador de texto (se demorara) ")
        label2.place(x=160, y=140)
        label3 = Label(self.ventana_three, text="DIGITE UN TEXTO: ")
        label3.place(x=50, y=250)
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana_three,text="SI", variable=self.seleccion, value=1)
        self.radio1.place(x=220, y=300)
        self.radio2=tk.Radiobutton(self.ventana_three,text="NO", variable=self.seleccion, value=2)
        self.radio2.place(x=300, y=300)
        caja4= Entry(self.ventana_three, width=40,bg="#7FC2DC")
        caja4.place(x=160, y=350)
        label3 = Label(self.ventana_three, text="generar texto 2 api: ")
        label3.place(x=50, y=300)
        label4 = Label(self.ventana_three, text="Digite un nombre: ")
        label4.place(x=50, y=350)
        
            
            
        def send2():
           
           
            client = nlpcloud.Client("fast-gpt-j", "e8230b07b816c5aafa386309cd3bc694236b3bd3", gpu=True, lang="en")
            dato2=client.article_generation(caja3.get())
            messagebox.showinfo(title="Usuando api 3", message=dato2)
            if self.seleccion.get()==1:
                client2 = nlpcloud.Client("fast-gpt-j", "e8230b07b816c5aafa386309cd3bc694236b3bd3", gpu=True, lang="en")
                dato3=client2.generation(caja3.get(),
                    min_length=10,
                    max_length=50,
                    length_no_input=True,
                    remove_input=False,
                    end_sequence=None,
                    top_p=1,
                    temperature=0.8,
                    top_k=50,
                    repetition_penalty=1,
                    length_penalty=1,
                    do_sample=True,
                    early_stopping=False,
                    num_beams=1,
                    no_repeat_ngram_size=0,
                    num_return_sequences=1,
                    bad_words=None,
                    remove_end_sequence=False
                    )
                                
            messagebox.showinfo(title="Usuando api 4 Resumen", message=dato3) 
            
            messagebox.showinfo(title="JSON", message="SE HA GUARDADO JSON")
            users = [
                  {
                    "Nombre": "",
                    "id": "" ,
                    "Tipo_de_serivicio": "",
                    "Valor_entrada": "",
                    "Valor_salida": "",                                                                                                                                                                                                                                                          
             }
            ]
                                                                        
            for user in users:
                                                    
                user['Nombre'] = caja4.get()
                user['id']  =1
                user['Tipo_de_serivicio'] = "Sercicio api de generado de texto y deteccion de idioma"
                user['Valor_entrada'] = caja3.get()
                user['Valor_salida'] = dato2,dato3                                                                                            
                my_path = 'users.json'

                if path.exists(my_path):
                    with open(my_path , 'r') as file:
                        previous_json = json.load(file)
                        users = previous_json + users
                        print(chr(27)+"[1;33m"+"Se ha guardado json\n") 
                        file.close()
                                                                                    
                                                                                                            
                with open(my_path , 'w') as file:
                    json.dump(users, file, indent=4)
                    print(chr(27)+"[1;33m"+"Se ha guardado json\n") 
                    file.close()
            
        send2 = Button(self.ventana_three, text="Enviar",command=send2).place(x=200, y=500)
            
        
        

   
      
        
       
    
    def ventana4(self):
        root = Tk()
        root.title("Chat Psicologo")
        BG_GRAY = "#FFFFFF"
        BG_COLOR = "#FFFFFF"
        TEXT_COLOR = "#060606"
        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"
        # Send function
        def send():
            openai.api_key = "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"
            conversation = "AI: En que puedo ayudarte?"
            i = 1
            while (i != 0):
                question =  e.get()
                conversation += "\nHuman:" + question + "\nAI:"
                response = openai.Completion.create(
                    engine = "davinci",
                    prompt = conversation,
                    temperature = 0.9,
                    max_tokens = 150,
                    top_p = 1,
                    frequency_penalty = 0,
                    presence_penalty = 0.6,
                    stop = ["\n", " Human:", " AI:"]
                )
                answer = response.choices[0].text.strip()
                conversation += answer
                
                send = "TU -> " + e.get()
                txt.insert(END, "\n" + send)
                user = e.get().lower()
                
                if (user == question):
                    txt.insert(END, "\n" + "AI: " + answer)     
                
                e.delete(0, END)
                break
        lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Bienvenido al chat", font=FONT_BOLD, pady=10, width=20, height=1).grid(
            row=0)
        txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=70)
        txt.grid(row=1, column=0, columnspan=2)
        scrollbar = Scrollbar(txt)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar = Scrollbar(txt,orient='horizontal')   

        e = Entry(root, bg="#E3E2E2", fg=TEXT_COLOR, font=FONT, width=55)
        e.grid(row=2, column=0)

        send = Button(root, text="Enviar", font=FONT_BOLD, bg=BG_GRAY,
                    command=send).grid(row=2, column=1)

aplicacion1=Aplicacion()