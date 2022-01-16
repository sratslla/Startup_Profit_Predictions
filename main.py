import tkinter as tk
import pandas as pd
app = tk.Tk()
app.geometry('350x250')
app.title('Price Predictor')
mod = pd.read_pickle('startup.pkl')

spend = tk.Variable(app)
admin = tk.Variable(app)
marketing_spend = tk.Variable(app)
state = tk.Variable(app)
profit = tk.Variable(app)

tk.Label(app,text='spend:    ',font=('Arial',15)).place(x=10,y=20)
tk.Label(app,text='admin: ',font=('Arial',15)).place(x=10,y=50)
tk.Label(app,text='marketing_spend:     ',font=('Arial',15)).place(x=10,y=80)
tk.Label(app,text='state:',font=('Arial',15)).place(x=10,y=110)
tk.Label(app,textvariable=profit,font=('Arial',15),fg='red').place(x=110,y=200)

tk.Entry(app,textvariable=spend,width=15,font=('Arial',15)).place(x=130,y=20)
tk.Entry(app,textvariable=admin,width=15,font=('Arial',15)).place(x=130,y=50)
tk.Entry(app,textvariable=marketing_spend,width=15,font=('Arial',15)).place(x=130,y=80)
tk.Entry(app,textvariable=state,width=15,font=('Arial',15)).place(x=130,y=110)


def prediction():
    global spend, admin, state, marketing_spend
    a = eval(spend.get())
    b = eval(admin.get())
    c = eval(marketing_spend.get())
    d = str(state.get())
    query = [[a, b, c]]
    profit.set(round(mod.predict(query)[0],0))

tk.Button(app, text='Predict', font=('Arial',15),bg='white', command=prediction).place(x=110,y=160)

app.mainloop()