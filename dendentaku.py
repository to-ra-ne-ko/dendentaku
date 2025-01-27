import sys
sys.dont_write_bytecode = True  # do not make '__cache__'
import tkinter as tk
import my_icon  # アイコン

lisD=["."]
lisE=["+","-","*","/"]
lisA=["+","-","*","/","."]
lisALL=[ str(i) for i in range(10) ] + lisA

def clear(event):
    # テキストエリアを空にする
    # text1.delete( 0. , tk.END )
    text1.config(state='normal')
    text1.config(bg="white")
    text1.delete( 0 , tk.END )
    strtxt = "0"
    text1.insert(tk.END, strtxt )
    text1.config(state="readonly")

def call(event,name): # 数字用
    # text1.delete( 0. , tk.END ) #text=0.0 entry=0
    text1.config(state='normal')
    text1.config(bg="white")
    str1=text1.get()
    if len(str1)==1 and str1=="0":
        text1.delete( 0 , tk.END )
    text1.insert(tk.END, name )
    text1.config(state="readonly")

def call_2(event,name): # 演算子用
    text1.config(state='normal')
    text1.config(bg="white")
    # ボタンを押して一つ前が演算子で
    # なかったらテキストエリアに表示する
    # text1.delete( 0. , tk.END ) #text=0.0 entry=0
    str1=text1.get()
    if name=='.':
        if str1.count(name)>1:
            text1.config(bg="yellow")
        elif str1[-1] in lisA:
            text1.config(bg="yellow")
        elif name in str1 and [ lisE[i] in str1  for i in range(len(lisE)) ].count(True)==0:
            text1.config(bg="yellow")
        else:
            text1.insert(tk.END, name )
    elif str1[-1].isnumeric():
        # print(str1[-1])
        text1.insert(tk.END, name )
    else:
        result=str1[:-1] + name
        text1.delete( 0 , tk.END )
        strtxt = result
        text1.insert(tk.END, strtxt )
    text1.config(state="readonly")

def c_call(event,name):
    text1.config(state='normal')
    text1.config(bg="white")
    text1.delete( 0 , tk.END )
    text1.insert(tk.END, name )
    text1.config(state="readonly")

def del_1word(event):
    text1.config(state='normal')
    text1.config(bg="white")

    str1=text1.get()
    if len(str1)==0:
        pass
    elif len(str1)==1:
        text1.delete( 0 , tk.END )
        strtxt = 0
        text1.insert(tk.END, strtxt )
        pass
    else:
        result=str1[:-1]
        text1.delete( 0 , tk.END )
        strtxt = result
        text1.insert(tk.END, strtxt )
    text1.config(state="readonly")

def den_calc(event):
    text1.config(state='normal')
    text1.config(bg="white")
    # 式を取得して画面に計算結果を出す
    str1=text1.get()
    x = [ str1[i] in lisALL for i in range(len(str1)) ].count(False)
    if  x > 0:
        print(f"False Num = {x}")
        text1.config(bg="white")
        strtxt = 'SyntaxError. Press "C" button.'
        text1.delete( 0 , tk.END )
        text1.insert(tk.END, strtxt )
        text1.config(state="readonly")
        return

    print(f"str1={str1}") # テキストエリアの式を表示
    print(type(str1))     # 文字列型
    try:
        result=eval(str1) # 演算(try必須)
        text1.delete( 0 , tk.END )
        strtxt = result
        text1.insert(tk.END, strtxt )
    except(ZeroDivisionError) :
        text1.config(bg="red")
        text1.delete( 0 , tk.END )
        strtxt = "ZeroDivisionError"
        text1.insert(tk.END, strtxt )
    except(SyntaxError) :
        text1.config(bg="red")
        text1.delete( 0 , tk.END )
        strtxt = "SyntaxError"
        text1.insert(tk.END, strtxt )
    finally:
        pass
    text1.config(state="readonly")

root=tk.Tk()
photo = my_icon.get_photo_image4icon()  # PhotoImageオブジェクトの作成
root.iconphoto(False, photo)           # アイコンの設定
root.configure(bg="lightgray")
ttext = "電々卓"
root.title(ttext)
gx,gy=270,365
root.minsize(gx,gy)

# text1=tk.Text(root,bg="white")
# text1.delete( 0. , tk.END )
# strtxt = ""
# text1.insert(tk.END, strtxt )
# text1.place(x=30,y=30,width=150,height=30)

# text1=tk.Entry(root,bg="white",justify="center",state='disabled')
text1=tk.Entry(root,bg="white",justify="center")
strtxt = "0"
text1.insert(tk.END, strtxt )
text1.place(x=30,y=20,width=210,height=30)
text1.configure(state="readonly")

button_cat=tk.Button(root,text="🐱",bg="gray",fg="white")
button_cat.bind("<1>", lambda event:c_call(event,"にゃー") )
button_cat.place(x=30,y=65,width=35,height=35)

button_dog=tk.Button(root,text="🐶",bg="gray",fg="white")
button_dog.bind("<1>", lambda event:c_call(event,"わんわん") )
button_dog.place(x=90,y=65,width=35,height=35)

button_bs=tk.Button(root,text="BS",bg="yellow")
button_bs.bind("<1>", lambda event:del_1word(event) )
button_bs.place(x=150,y=65,width=35,height=35)

button_clear=tk.Button(root,text="C",bg="yellow")
button_clear.bind("<1>", lambda event:clear(event) )
button_clear.place(x=210,y=65,width=35,height=35)

button_7=tk.Button(root,text="7",bg="lightgray")
button_7.bind("<1>", lambda event:call(event,"7") )
button_7.place(x=30,y=125,width=35,height=35)

button_8=tk.Button(root,text="8",bg="lightgray")
button_8.bind("<1>", lambda event:call(event,"8") )
button_8.place(x=90,y=125,width=35,height=35)

button_9=tk.Button(root,text="9",bg="lightgray")
button_9.bind("<1>", lambda event:call(event,"9") )
button_9.place(x=150,y=125,width=35,height=35)

button_slash=tk.Button(root,text="/",bg="white")
button_slash.bind("<1>", lambda event:call_2(event,"/") )
button_slash.place(x=210,y=125,width=35,height=35)

button_4=tk.Button(root,text="4",bg="lightgray")
button_4.bind("<1>", lambda event:call(event,"4") )
button_4.place(x=30,y=185,width=35,height=35)

button_5=tk.Button(root,text="5",bg="lightgray")
button_5.bind("<1>", lambda event:call(event,"5") )
button_5.bind("<2>", lambda event:c_call(event,"Have A Nice Day!!") )
button_5.place(x=90,y=185,width=35,height=35)

button_6=tk.Button(root,text="6",bg="lightgray")
button_6.bind("<1>", lambda event:call(event,"6") )
button_6.place(x=150,y=185,width=35,height=35)

button_mul=tk.Button(root,text="x",bg="white")
button_mul.bind("<1>", lambda event:call_2(event,"*") )
button_mul.place(x=210,y=185,width=35,height=35)

button_1=tk.Button(root,text="1",bg="lightgray")
button_1.bind("<1>", lambda event:call(event,"1") )
button_1.place(x=30,y=245,width=35,height=35)

button_2=tk.Button(root,text="2",bg="lightgray")
button_2.bind("<1>", lambda event:call(event,"2") )
button_2.place(x=90,y=245,width=35,height=35)

button_3=tk.Button(root,text="3",bg="lightgray")
button_3.bind("<1>", lambda event:call(event,"3") )
button_3.place(x=150,y=245,width=35,height=35)

button_sub=tk.Button(root,text="-",bg="white")
button_sub.bind("<1>", lambda event:call_2(event,"-") )
button_sub.place(x=210,y=245,width=35,height=35)

button_0=tk.Button(root,text="0",bg="lightgray")
button_0.bind("<1>", lambda event:call(event,"0") )
button_0.place(x=30,y=305,width=35,height=35)

button_dot=tk.Button(root,text=".",bg="lightgray")
button_dot.bind("<1>", lambda event:call_2(event,".") )
button_dot.place(x=90,y=305,width=35,height=35)

button_eql=tk.Button(root,text="=",bg="white")
button_eql.bind("<1>", den_calc )
button_eql.place(x=150,y=305,width=35,height=35)

button_pls=tk.Button(root,text="+",bg="white")
button_pls.bind("<1>", lambda event:call_2(event,"+") )
button_pls.place(x=210,y=305,width=35,height=35)

root.mainloop()
