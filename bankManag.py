import tkinter as tk
from tkinter import messagebox

accounts = []

# Load the accounts from the "comptes.txt" file
with open('C:\\Users\\ce pc\\Desktop\\Tkinter\\Bank Management\\comptes.txt', 'r') as f:
    for line in f:
        # Split the line into fields
        fields = line.strip().split(',')
        # Check if the fields list has at least 4 elements
        if len(fields) >= 4:
            balance = fields[3].rstrip(';')
            account = {'password': fields[0], 'last_name': fields[1],
                       'first_name': fields[2], 'balance': int(balance)}
            # Add the account to the list of accounts
            accounts.append(account)

# Create the main window
window1 = tk.Tk()
window1.title('Gestion Bank')
window1.resizable(False, False)
window1.iconbitmap(
    'C:\\Users\\ce pc\\Desktop\\Tkinter\\Bank Management\\bank.ico')
window1.config(bg='#3a86ff')
w = window1.winfo_screenwidth()
h = window1.winfo_screenheight()
window1.geometry(f'600x500+{(w-600) // 2}+{(h-500) // 2}')

# Create the widgets in the main window
title = tk.Label(window1, text='BANQUE',
                 font=('Arial', 20), fg='#fff', bg='#3a86ff')
title.place(x=30, y=30)

frame = tk.Frame(window1, width="500", height="350",
                 bg='#fff', borderwidth=2, relief='solid')
frame.place(x=50, y=100)

arabicLable = tk.Label(frame, text='المرجو إدخال رقمكم السري',
                       font=('Arial', 18, 'bold'), bg='#fff')
arabicLable.place(x=130, y=50)

franceLable = tk.Label(frame, text='Entrez votre code confidentiel S.V.P', font=(
    'Arial', 18, 'bold'), bg='#fff')
franceLable.place(x=37, y=100)

password_entry = tk.Entry(frame, font=('Arial', 20), width="25",
                          justify='center', borderwidth=1, relief='solid', show='X')
password_entry.place(x=60, y=170)

validate_button = tk.Button(frame, text='Valider', width="17", fg='white', bg='#3a86ff', font=(
    'Arial', 16), cursor='hand2', command=lambda: validate_password(password_entry))
validate_button.place(x=140, y=240)


def validate_password(password_entry):
    # Get the password entered by the user
    password = password_entry.get()
    # Check if the password matches any of the passwords in the accounts list
    for account in accounts:
        if password == account['password']:
            window1.withdraw()
            show_compte_window(account, password_entry)
            break
    else:
        tk.messagebox.showerror('Erreur', 'Mot de passe incorrect')


def show_compte_window(acc, password_entry):
    global account
    account = acc

    wndCompte = tk.Toplevel()
    wndCompte.title('Gestion Bank')
    wndCompte.resizable(False, False)
    wndCompte.iconbitmap(
        'C:\\Users\\ce pc\\Desktop\\Tkinter\\Bank Management\\bank.ico')
    wndCompte.config(bg='#3a86ff')
    w = wndCompte.winfo_screenwidth()
    h = wndCompte.winfo_screenheight()
    wndCompte.geometry(f'600x500+{(w-600) // 2}+{(h-500) // 2}')

    # Create a StringVar to hold the selected amount
    selected_amount = tk.StringVar()

    title = tk.Label(wndCompte, text='إختر المبلغ المطلوب\nChoisissez le montant souhaité', font=(
        'Arial', 20, 'bold'), bg='#3a86ff', fg='#fff')
    title.pack(pady=20)

    def handle_amount_selection(amount, password_entry):
        # Find the account associated with the entered password
        for acc in accounts:
            if acc['password'] == account['password']:
                # Check if the account has enough balance to withdraw the selected amount
                if acc['balance'] >= amount:
                    # Subtract the selected amount from the balance of the account
                    acc['balance'] -= amount
                    # Update the "comptes.txt" file with the new balance
                    with open('C:\\Users\\ce pc\\Desktop\\Tkinter\\Bank Management\\comptes.txt', 'w') as f:
                        for a in accounts:
                            f.write(
                                f"{a['password']},{a['last_name']},{a['first_name']},{a['balance']};\n")
                    wndCompte.withdraw()
                    show_checkout_window()
                    break
                else:
                    # If the account balance is insufficient, display an error message
                    tk.messagebox.showerror('Erreur', 'Solde insuffisant')
                    break
        else:
            # If the password is incorrect, display an error message
            tk.messagebox.showerror('Erreur', 'Mot de passe incorrect')

    def show_checkout_window():
        wndOut = tk.Toplevel()
        wndOut.title('Checkout')
        wndOut.resizable(False, False)
        wndOut.iconbitmap(
            'C:\\Users\\ce pc\\Desktop\\Tkinter\\Bank Management\\bank.ico')
        wndOut.config(bg='#3a86ff')
        w = wndOut.winfo_screenwidth()
        h = wndOut.winfo_screenheight()
        wndOut.geometry(f'600x500+{(w-600) // 2}+{(h-500) // 2}')

        messag = tk.Label(wndOut, text=' :تم سحب مبلغ\nUn montant a ete preleve: ', font=(
            'Arial', 20, 'bold'), bg='#3a86ff', fg='#fff')
        messag.pack(pady=190)

        wndOut.mainloop()

    btnprix1 = tk.Button(wndCompte, text='100 Dh', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(100, password_entry))
    btnprix1.place(x=0, y=100)

    btnprix2 = tk.Button(wndCompte, text='300 Dh', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(300, password_entry))
    btnprix2.place(x=0, y=200)

    btnprix3 = tk.Button(wndCompte, text='500 Dh', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(500, password_entry))
    btnprix3.place(x=0, y=300)

    autreSer = tk.Button(wndCompte, text='خدمات أخرى\nAutres services', width="18", height=2,
                         fg='black', bg='#fff', font=('Arial', 16, 'bold'), cursor='hand2', compound='top')
    autreSer.place(x=0, y=400)

    btnprix4 = tk.Button(wndCompte, text='1000 Dh', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(1000, password_entry))
    btnprix4.place(x=400, y=100)

    btnprix5 = tk.Button(wndCompte, text='2000 Dh', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(2000, password_entry))
    btnprix5.place(x=400, y=200)

    btnprix6 = tk.Button(wndCompte, text='5000 Dh', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(5000, password_entry))
    btnprix6.place(x=400, y=300)

    btnprix7 = tk.Button(wndCompte, text='Autre montant', width="18", height=2, fg='black', bg='#fff', font=(
        'Arial', 16, 'bold'), cursor='hand2', command=lambda: handle_amount_selection(0, password_entry))
    btnprix7.place(x=400, y=400)

    wndCompte.mainloop()


window1.mainloop()
