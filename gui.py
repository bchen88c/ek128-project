import tkinter as tk
import cryptosystem
private, public = cryptosystem.keyPair().generate(cryptosystem.curves().nist256) #As of now, I made the keypair at startup, it doesn't regenerate during GUI use

class Application(tk.Frame):                                                        #Main application
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.showKeyPair()                                                          #these are the buttons for encode/decode/showkey
        self.encodeButton()
        self.decodeButton()
       
    def showKeyPair(self):                                                          
        self.showPublicKeyButton = tk.Button(self,text="Show Public Key (point)",command=self.showPublicKey)
        self.showPublicKeyButton.grid(row=8,column=0)
        self.QUIT = tk.Button(self, text="QUIT", fg="red", bg='white',command=root.destroy)         #quit button. is arbitrarily in keypair button
        self.QUIT.grid(row=0,column=0)
        self.showPrivateKeyButton = tk.Button(self,text="Show Private Key (number)",command=self.showPrivateKey)
        self.showPrivateKeyButton.grid(row=8,column=1)

    def showPublicKey(self):                                                           #originally intended to generate keypair via button, now it does it on startup
       #cryptosystem.keyPair().generate(cryptosystem.curves.nist256)
       self.printPublicLabel=tk.Text(self,height=3)                                 #Shows Public key (a point)
       self.printPublicLabel.insert(1.0,public)
       self.printPublicLabel.grid(row=9,column=0)
       #print(public,private)

    def showPrivateKey(self):                                                       #Shows private key (it is an integer)
        self.printPrivateLabel=tk.Text(self,height=3)
        self.printPrivateLabel.insert(1.0,private)
        self.printPrivateLabel.grid(row=9,column=1)

    def encodeButton(self):                                                             #Encode button
        self.encode = tk.Button(self,text='encode message',command=self.encodeMessage)
        self.encode.grid(row=1,column=0) 
        self.encodeentry=tk.Entry(self)
        self.encodeentry.grid(row=1,column=1)


    def decodeButton(self):                                                             #Asks for entries from the encoded message; a point and a number
        self.decode = tk.Button(self,text="decode message",command=self.decodeMessage)
        self.decode.grid(row=6,column=0)
        self.decodeentryPointX=tk.Entry(self)
        self.decodeentryPointX.grid(row=6,column=1)
        self.decodeentryPointY=tk.Entry(self)
        self.decodeentryPointY.grid(row=6,column=2)
        self.decodeentryNumber=tk.Entry(self)
        self.decodeentryNumber.grid(row=6,column=3)


    def encodeMessage(self):
        self.test=cryptosystem.Encoder().encode(cryptosystem.publicKey(public),cryptosystem.curves().nist256,self.encodeentry.get()) #takes input string and encodes it
        self.printEncode=tk.Text(self, height=3)
        self.printEncode.insert(1.0,self.test)
        self.printEncode.grid(row=2,column=0)
        self.printToDo=tk.Label(self,text="Copy each component of the point\ninto the first two boxes next to decode,\ncopy the third number into the third slot")
        self.printToDo.grid(row=2,column=1)

    def decodeMessage(self):
        self.printDecode=tk.Label(self)
        QQQ=([int(self.decodeentryPointX.get()),int(self.decodeentryPointY.get())],int(self.decodeentryNumber.get()))   #takes inputted numbers and makes it into a tuple for cryptosystem digestion
        self.printDecode["text"] = 'Your message is:','\n', cryptosystem.Encoder().decode(cryptosystem.privateKey(private),cryptosystem.curves().nist256,QQQ) #decodes
        self.printDecode.grid(row=7,column=0)

#PROBLEM. self.decodeentry.get() returns a tuple-like string, we need to input a tuple for cryptosystem

root = tk.Tk()
root.title('ECC GUI')
app = Application(master=root)


app.mainloop()
