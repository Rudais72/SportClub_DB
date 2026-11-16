# app.py
import tkinter as tk
from tkinter import ttk, messagebox
from functions import (
    get_clients, add_client, update_client, delete_client,
    get_trainers, add_trainer, update_trainer, delete_trainer,
    get_group_classes, add_group_class, update_group_class, delete_group_class,
    get_memberships, add_membership, update_membership, delete_membership,
    get_schedules, add_schedule, update_schedule, delete_schedule,
    get_bookings, add_booking, update_booking, delete_booking,
    get_payments, add_payment, update_payment, delete_payment,
    get_equipment, add_equipment, update_equipment, delete_equipment
)

class SportClubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sporta Kluba Vadības Sistēma")
        self.root.geometry("1000x700")

        # Notebook (Tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Izveido cilnes visām 8 tabulām ar pilnu CRUD atbalstu
        self.setup_tab(
            "Klienti", 
            get_clients, 
            [("Vārds", "vards"), ("Uzvārds", "uzvārds"), ("Tālrunis", "tālrunis"), ("E-pasts", "epasts"), ("Reģ. datums", "registracijas_datums")],
            lambda vals: add_client(vals[0], vals[1], vals[2], vals[3], vals[4]),
            lambda id_, vals: update_client(id_, vals[0], vals[1], vals[2], vals[3], vals[4]),
            delete_client
        )

        self.setup_tab(
            "Treneri", 
            get_trainers, 
            [("Vārds", "vards"), ("Uzvārds", "uzvārds"), ("Tālrunis", "tālrunis"), ("Specializācija", "specializacija"), ("Pieņemšanas datums", "pieņemšanas_datums")],
            lambda vals: add_trainer(vals[0], vals[1], vals[2], vals[3], vals[4]),
            lambda id_, vals: update_trainer(id_, vals[0], vals[1], vals[2], vals[3], vals[4]),
            delete_trainer
        )

        self.setup_tab(
            "Nodarbības", 
            get_group_classes, 
            [("Nosaukums", "nosaukums"), ("Apraksts", "apraksts"), ("Ilgums (min)", "ilgums_minutēs")],
            lambda vals: add_group_class(vals[0], vals[1], int(vals[2])),
            lambda id_, vals: update_group_class(id_, vals[0], vals[1], int(vals[2])),
            delete_group_class
        )

        self.setup_tab(
            "Abonementi", 
            get_memberships, 
            [("Klienta ID", "klienta_id"), ("Veids", "abonementa_veids"), ("Sākuma datums", "sakuma_datums"), ("Beigu datums", "beigu_datums")],
            lambda vals: add_membership(int(vals[0]), vals[1], vals[2], vals[3]),
            lambda id_, vals: update_membership(id_, int(vals[0]), vals[1], vals[2], vals[3]),
            delete_membership
        )

        self.setup_tab(
            "Grafiks", 
            get_schedules, 
            [("Nodarbības ID", "nodarbibas_id"), ("Trenera ID", "trenera_id"), ("Datums un laiks", "datums_laiks"), ("Telpa", "telpa")],
            lambda vals: add_schedule(int(vals[0]), int(vals[1]), vals[2], vals[3]),
            lambda id_, vals: update_schedule(id_, int(vals[0]), int(vals[1]), vals[2], vals[3]),
            delete_schedule
        )

        self.setup_tab(
            "Rezervācijas", 
            get_bookings, 
            [("Klienta ID", "klienta_id"), ("Grafika ID", "grafika_id"), ("Rezervācijas datums", "rezervacijas_datums")],
            lambda vals: add_booking(int(vals[0]), int(vals[1]), vals[2]),
            lambda id_, vals: update_booking(id_, int(vals[0]), int(vals[1]), vals[2]),
            delete_booking
        )

        self.setup_tab(
            "Maksājumi", 
            get_payments, 
            [("Klienta ID", "klienta_id"), ("Summa", "summa"), ("Maksājuma datums", "maksajuma_datums"), ("Veids", "maksajuma_veids")],
            lambda vals: add_payment(int(vals[0]), float(vals[1]), vals[2], vals[3]),
            lambda id_, vals: update_payment(id_, int(vals[0]), float(vals[1]), vals[2], vals[3]),
            delete_payment
        )

        self.setup_tab(
            "Inventārs", 
            get_equipment, 
            [("Nosaukums", "nosaukums"), ("Daudzums", "daudzums"), ("Stāvoklis", "stāvoklis"), ("Iegādes datums", "iegades_datums")],
            lambda vals: add_equipment(vals[0], int(vals[1]), vals[2], vals[3]),
            lambda id_, vals: update_equipment(id_, vals[0], int(vals[1]), vals[2], vals[3]),
            delete_equipment
        )

    def setup_tab(self, title, fetch_func, fields, add_func, update_func, delete_func):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)

        # Formas rāmītis datu ievadei un rediģēšanai
        form_frame = ttk.LabelFrame(frame, text=" Ieraksta pārvaldība ")
        form_frame.pack(fill="x", padx=10, pady=10)

        entries = {}
        for i, (label_text, key) in enumerate(fields):
            lbl = ttk.Label(form_frame, text=label_text)
            lbl.grid(row=i//3, column=(i%3)*2, padx=5, pady=5, sticky="w")
            ent = ttk.Entry(form_frame)
            ent.grid(row=i//3, column=(i%3)*2 + 1, padx=5, pady=5, sticky="ew")
            entries[key] = ent

        selected_id_var = tk.StringVar(value="")

        # Tabulas rāmītis
        table_frame = ttk.Frame(frame)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        tree = ttk.Treeview(table_frame, selectmode="browse")
        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        def refresh_data():
            for item in tree.get_children():
                tree.delete(item)
            rows = fetch_func()
            if rows:
                keys = rows[0].keys()
                tree["columns"] = list(keys)
                tree["show"] = "headings"
                for key in keys:
                    tree.heading(key, text=key.capitalize())
                    tree.column(key, width=130, anchor="w")

                for row in rows:
                    tree.insert("", tk.END, values=list(row))
            selected_id_var.set("")
            clear_form()

        def clear_form():
            selected_id_var.set("")
            for ent in entries.values():
                ent.delete(0, tk.END)

        def on_row_select(event):
            selected_item = tree.selection()
            if selected_item:
                item_values = tree.item(selected_item, "values")
                if item_values:
                    selected_id_var.set(item_values[0])
                    # Aizpilda ievades laukus ar atlasītās rindas datiem (izlaižot ID)
                    for idx, key in enumerate([k for _, k in fields]):
                        entries[key].delete(0, tk.END)
                        if idx + 1 < len(item_values):
                            entries[key].insert(0, str(item_values[idx + 1]))

        tree.bind("<<TreeviewSelect>>", on_row_select)

        def on_add():
            try:
                vals = [entries[key].get() for _, key in fields]
                add_func(vals)
                messagebox.showinfo("Veiksmīgi", "Ieraksts pievienots!")
                refresh_data()
            except Exception as e:
                messagebox.showerror("Kļūda", f"Neizdevās pievienot: {e}")

        def on_update():
            rec_id = selected_id_var.get()
            if not rec_id:
                messagebox.showwarning("Brīdinājums", "Lūdzu, izvēlies ierakstu tabulā, ko rediģēt!")
                return
            try:
                vals = [entries[key].get() for _, key in fields]
                update_func(rec_id, vals)
                messagebox.showinfo("Veiksmīgi", "Ieraksts atjaunināts!")
                refresh_data()
            except Exception as e:
                messagebox.showerror("Kļūda", f"Neizdevās atjaunināt: {e}")

        def on_delete():
            rec_id = selected_id_var.get()
            if not rec_id:
                messagebox.showwarning("Brīdinājums", "Lūdzu, izvēlies ierakstu tabulā, ko dzēst!")
                return
            if messagebox.askyesno("Apstiprinājums", "Vai tiešām vēlies dzēst šo ierakstu?"):
                try:
                    delete_func(rec_id)
                    messagebox.showinfo("Veiksmīgi", "Ieraksts izdzēsts!")
                    refresh_data()
                except Exception as e:
                    messagebox.showerror("Kļūda", f"Neizdevās izdzēst: {e}")

        # Pogas
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=(len(fields)//3)+1, column=0, columnspan=6, pady=10)

        btn_add = ttk.Button(btn_frame, text="Pievienot", command=on_add)
        btn_add.pack(side="left", padx=5)

        btn_update = ttk.Button(btn_frame, text="Saglabāt izmaiņas (Rediģēt)", command=on_update)
        btn_update.pack(side="left", padx=5)

        btn_delete = ttk.Button(btn_frame, text="Dzēst izvēlēto", command=on_delete)
        btn_delete.pack(side="left", padx=5)

        btn_clear = ttk.Button(btn_frame, text="Notīrīt laukus", command=clear_form)
        btn_clear.pack(side="left", padx=5)

        btn_refresh = ttk.Button(frame, text="Atjaunot sarakstu", command=refresh_data)
        btn_refresh.pack(pady=5)

        refresh_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = SportClubApp(root)
    root.mainloop()