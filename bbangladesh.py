from tkinter import *
from PIL import ImageTk,Image
#Window
root=Tk()
root.title("Beautiful Bangladesh")
root.iconbitmap("logo/b.ico")
#root.geometry('3000x350')
#images
i1=ImageTk.PhotoImage(Image.open("pic/02.jpg"))
i2=ImageTk.PhotoImage(Image.open("pic/01.jpg"))
i3=ImageTk.PhotoImage(Image.open("pic/03.jpg"))
i4=ImageTk.PhotoImage(Image.open("pic/04.jpg"))
i5=ImageTk.PhotoImage(Image.open("pic/05.jpg"))
i6=ImageTk.PhotoImage(Image.open("pic/06.jpg"))
i7=ImageTk.PhotoImage(Image.open("pic/07.jpg"))
i8=ImageTk.PhotoImage(Image.open("pic/08.jpg"))
i9=ImageTk.PhotoImage(Image.open("pic/09.jpg"))
i10=ImageTk.PhotoImage(Image.open("pic/10.jpg"))

i11=ImageTk.PhotoImage(Image.open("pic/11.jpg"))
i12=ImageTk.PhotoImage(Image.open("pic/12.jpg"))
i13=ImageTk.PhotoImage(Image.open("pic/13.jpg"))
i14=ImageTk.PhotoImage(Image.open("pic/14.jpg"))
i15=ImageTk.PhotoImage(Image.open("pic/15.jpg"))
i16=ImageTk.PhotoImage(Image.open("pic/16.jpg"))
i17=ImageTk.PhotoImage(Image.open("pic/17.jpg"))
i18=ImageTk.PhotoImage(Image.open("pic/18.jpg"))
i19=ImageTk.PhotoImage(Image.open("pic/19.jpg"))
i20=ImageTk.PhotoImage(Image.open("pic/20.jpg"))

i21=ImageTk.PhotoImage(Image.open("pic/21.jpg"))
i22=ImageTk.PhotoImage(Image.open("pic/22.jpg"))
i23=ImageTk.PhotoImage(Image.open("pic/23.jpg"))
i24=ImageTk.PhotoImage(Image.open("pic/24.jpg"))
i25=ImageTk.PhotoImage(Image.open("pic/25.jpg"))
i26=ImageTk.PhotoImage(Image.open("pic/26.jpg"))
i27=ImageTk.PhotoImage(Image.open("pic/27.jpg"))
i28=ImageTk.PhotoImage(Image.open("pic/28.jpg"))
i29=ImageTk.PhotoImage(Image.open("pic/29.jpg"))
i30=ImageTk.PhotoImage(Image.open("pic/30.jpg"))

i31=ImageTk.PhotoImage(Image.open("pic/31.jpg"))
i32=ImageTk.PhotoImage(Image.open("pic/32.jpg"))
i33=ImageTk.PhotoImage(Image.open("pic/33.jpg"))
i34=ImageTk.PhotoImage(Image.open("pic/34.jpg"))
i35=ImageTk.PhotoImage(Image.open("pic/35.jpg"))
i36=ImageTk.PhotoImage(Image.open("pic/36.jpg"))
i37=ImageTk.PhotoImage(Image.open("pic/37.jpg"))
i38=ImageTk.PhotoImage(Image.open("pic/38.jpg"))
i39=ImageTk.PhotoImage(Image.open("pic/39.jpg"))
i40=ImageTk.PhotoImage(Image.open("pic/40.jpg"))

i41=ImageTk.PhotoImage(Image.open("pic/41.jpg"))

#list
lista=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,
i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,
i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
i41]


#starter
l1=Label(root,image=i1)
l1.grid(row=0,column=0,columnspan=3)
#Fnction
def forword(number):
	global l1,fb,bb
	l1.grid_forget()
	l1=Label(image=lista[number-1])
	fb=Button(root,text=">>",command=lambda:forword(number+1))
	bb=Button(root,text="<<",command=lambda:back(number-1))

	if number==41:
		fb=Button(root,text=">>",state=DISABLED)

	l1.grid(row=0,column=0,columnspan=3)
	bb.grid(row=1,column=0)
	fb.grid(row=1,column=2)


def back(number):
	global l1,fb,bb
	l1.grid_forget()
	l1=Label(image=lista[number-1])
	fb=Button(root,text=">>",command=lambda:forword(number+1))
	bb=Button(root,text="<<",command=lambda:back(number-1))

	if number==1:
		Bb=Button(root,text="<<",state=DISABLED)

	l1.grid(row=0,column=0,columnspan=3)
	bb.grid(row=1,column=0)
	fb.grid(row=1,column=2)
#BUTTON
bb=Button(root,text="<<",command=back,state=DISABLED)
bb.grid(row=1,column=0)

eb=Button(root,text="Exit",command=root.quit)
eb.grid(row=1,column=1)

fb=Button(root,text=">>",command=lambda:forword(2))
fb.grid(row=1,column=2)
root.mainloop()
