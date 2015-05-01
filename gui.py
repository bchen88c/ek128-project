import tkinter as tk
import cryptosystem
private, public = cryptosystem.keyPair().generate(cryptosystem.curves().nist256) #As of now, I made the keypair at startup, it doesn't regenerate during GUI use

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.showKeyPair()
        self.encodeButton()
        self.decodeButton()
       
    def showKeyPair(self):
        self.showKeyButton = tk.Button(self)
        self.showKeyButton["text"] = "Show Public Key (point) and Private Key (number)"
        self.showKeyButton["command"] = self.genKeyPair
        self.showKeyButton.grid(row=300,column=0)
        self.QUIT = tk.Button(self, text="QUIT", fg="red", bg='white',command=root.destroy)
        self.QUIT.grid(row=400,column=0)

    def genKeyPair(self):
       #cryptosystem.keyPair().generate(cryptosystem.curves.nist256)
      	self.printLabel=tk.Label(self)
      	self.printLabel["text"]=(public,private)
      	self.printLabel.grid(row=800,column=0)

    def encodeButton(self):
        self.encode = tk.Button(self,text='encode message',command=self.encodeMessage)
        self.encode.grid(row=100,column=0) 
        self.encodeentry=tk.Entry(self)
        self.encodeentry.grid(row=100,column=100)

    def decodeButton(self):
        self.decode = tk.Button(self,text="decode message",command=self.decodeMessage)
        self.decode.grid(row=0,column=0)
        self.decodeentry=tk.Entry(self)
        self.decodeentry.grid(row=0,column=100)

    def encodeMessage(self):
        self.test=cryptosystem.Encoder().encode(cryptosystem.publicKey(public),cryptosystem.curves().nist256,self.encodeentry.get())
        self.printLabel=tk.Text(self, height=3)
        self.printLabel.insert(1.0,self.test)
        self.printLabel.grid(row=100,column=200)
        print(self.test) #debug
        print(type(self.test))
    def decodeMessage(self):
        self.printLabel=tk.Label(self)
        QQQ=self.decodeentry.get()
        print(QQQ) #debug
        self.printLabel["text"] = cryptosystem.Encoder().decode(cryptosystem.privateKey(private),cryptosystem.curves().nist256,QQQ)
        self.printLabel.grid(row=0,column=200)


root = tk.Tk()
root.title('ECC GUI')
app = Application(master=root)


app.mainloop()
