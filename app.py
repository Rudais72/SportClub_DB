import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import functions as f


# Tab configuration: (column headers, getter function)
TABLES = {
    "Clients": (["ID", "First name", "Last name", "Phone", "Email", "Registered"], f.get_clients),
    "Trainers": (["ID", "First name", "Last name", "Phone", "Specialization", "Hired"], f.get_trainers),
    "Group classes": (["ID", "Name", "Description", "Duration (min)"], f.get_group_classes),
    "Memberships": (["ID", "Client ID", "First name", "Last name", "Type", "From", "To"], f.get_memberships),
    "Schedule": (["ID", "Class", "Trainer", "Date & time", "Room"], f.get_schedules),
    "Bookings": (["ID", "Client ID", "First name", "Last name", "Class", "Booked on"], f.get_bookings),
    "Payments": (["ID", "Client ID", "First name", "Last name", "Amount", "Date", "Method"], f.get_payments),
    "Equipment": (["ID", "Name", "Quantity", "Condition", "Bought"], f.get_equipment),
}

# Action button configuration: (function, [(field_label, type)], returns_count)
ACTIONS = {
    "Add client": (f.add_client, [("First name", str), ("Last name", str), ("Phone", str), ("Email", str),
                                  ("Registered (YYYY-MM-DD)", str)], False),
    "Update client": (f.update_client, [("Client ID", int), ("First name", str), ("Last name", str),
                                        ("Phone", str), ("Email", str), ("Registered (YYYY-MM-DD)", str)], True),
    "Delete client": (f.delete_client, [("Client ID", int)], True),
    "Add trainer": (f.add_trainer, [("First name", str), ("Last name", str), ("Phone", str),
                                    ("Specialization", str), ("Hired (YYYY-MM-DD)", str)], False),
    "Update trainer": (f.update_trainer, [("Trainer ID", int), ("First name", str), ("Last name", str),
                                          ("Phone", str), ("Specialization", str), ("Hired (YYYY-MM-DD)", str)], True),
    "Delete trainer": (f.delete_trainer, [("Trainer ID", int)], True),
    "Add class": (f.add_group_class, [("Name", str), ("Description", str), ("Duration (min)", int)], False),
    "Update class": (f.update_group_class, [("Class ID", int), ("Name", str), ("Description", str),
                                            ("Duration (min)", int)], True),
    "Delete class": (f.delete_group_class, [("Class ID", int)], True),
    "Add membership": (f.add_membership, [("Client ID", int), ("Type", str), ("Start (YYYY-MM-DD)", str),
                                          ("End (YYYY-MM-DD)", str)], False),
    "Update membership": (f.update_membership, [("Membership ID", int), ("Client ID", int), ("Type", str),
                                                ("Start (YYYY-MM-DD)", str), ("End (YYYY-MM-DD)", str)], True),
    "Delete membership": (f.delete_membership, [("Membership ID", int)], True),
    "Add schedule": (f.add_schedule, [("Class ID", int), ("Trainer ID", int), ("Date & time (YYYY-MM-DD HH:MM:SS)", str),
                                      ("Room", str)], False),
    "Update schedule": (f.update_schedule, [("Schedule ID", int), ("Class ID", int), ("Trainer ID", int),
                                            ("Date & time (YYYY-MM-DD HH:MM:SS)", str), ("Room", str)], True),
    "Delete schedule": (f.delete_schedule, [("Schedule ID", int)], True),
    "Add booking": (f.add_booking, [("Client ID", int), ("Schedule ID", int), ("Booked on (YYYY-MM-DD)", str)], False),
    "Update booking": (f.update_booking, [("Booking ID", int), ("Client ID", int), ("Schedule ID", int),
                                          ("Booked on (YYYY-MM-DD)", str)], True),
    "Delete booking": (f.delete_booking, [("Booking ID", int)], True),
    "Add payment": (f.add_payment, [("Client ID", int), ("Amount", float), ("Date (YYYY-MM-DD)", str),
                                    ("Method", str)], False),
    "Update payment": (f.update_payment, [("Payment ID", int), ("Client ID", int), ("Amount", float),
                                          ("Date (YYYY-MM-DD)", str), ("Method", str)], True),
    "Delete payment": (f.delete_payment, [("Payment ID", int)], True),
    "Add equipment": (f.add_equipment, [("Name", str), ("Quantity", int), ("Condition", str),
                                        ("Bought (YYYY-MM-DD)", str)], False),
    "Update equipment": (f.update_equipment, [("Equipment ID", int), ("Name", str), ("Quantity", int),
                                              ("Condition", str), ("Bought (YYYY-MM-DD)", str)], True),
    "Delete equipment": (f.delete_equipment, [("Equipment ID", int)], True),
}

# ---------------------------------------------------------
# Theme: "Vintage Club Ledger" — printed registry book.
# Cream paper, serif typography, ink-black header band,
# hairline rules, flat bordered buttons that invert on hover.
# ---------------------------------------------------------
PAPER = "#f6f1e4"        # warm cream page background
CARD = "#fdfaf1"         # slightly lighter card / table surface
INK = "#221d15"          # warm near-black ink
INK_SOFT = "#6b6252"     # faded ink for secondary text
RULE = "#c9bfa8"         # hairline rule colour
SELECT = "#1d4230"       # deep club green — single accent colour
SELECT_HOVER = "#153427"
DANGER = "#8c2f39"       # muted oxblood red — delete actions only

SERIF = ("Georgia", 11)
SERIF_SMALL = ("Georgia", 10)
SERIF_CAPS = ("Georgia", 10, "bold")
SERIF_TITLE = ("Georgia", 26, "bold")
SERIF_HEADER = ("Georgia", 12, "bold")

# Initialize main window
root = tk.Tk()
root.title("Sport Club Registry")
root.geometry("1024x720")
root.minsize(840, 560)
root.configure(bg=PAPER)

style = ttk.Style()
style.theme_use('clam')

# ---------------------------------------------------------
# Ledger-style widget styling
# ---------------------------------------------------------
style.configure(".", background=PAPER, foreground=INK, font=SERIF_SMALL)
style.configure("TFrame", background=PAPER)
style.configure("Card.TFrame", background=CARD)

# Masthead: letterspaced title above a double rule
style.configure("Masthead.TLabel", font=SERIF_TITLE, foreground=INK,
                background=PAPER, anchor="w")
style.configure("MastheadSub.TLabel", font=SERIF_CAPS, foreground=INK_SOFT,
                background=PAPER, anchor="w")
style.configure("Rule.TFrame", background=INK)

# Buttons: flat, thin ink border, cream face — invert to ink on hover.
# Delete actions are outlined in oxblood red instead.
style.configure("Ledger.TButton",
                background=CARD,
                foreground=INK,
                bordercolor=INK,
                borderwidth=1,
                relief="solid",
                focusthickness=0,
                padding=(12, 7),
                font=SERIF_CAPS)
style.map("Ledger.TButton",
          background=[('active', INK), ('pressed', INK)],
          foreground=[('active', CARD), ('pressed', CARD)])

style.configure("Danger.Ledger.TButton",
                bordercolor=DANGER,
                foreground=DANGER)
style.map("Danger.Ledger.TButton",
          background=[('active', DANGER), ('pressed', DANGER)],
          foreground=[('active', CARD), ('pressed', CARD)])

# Modal submit button: solid deep green
style.configure("Confirm.TButton",
                background=SELECT,
                foreground=CARD,
                borderwidth=0,
                focusthickness=0,
                padding=(14, 8),
                font=SERIF_CAPS)
style.map("Confirm.TButton",
          background=[('active', SELECT_HOVER), ('pressed', SELECT_HOVER)],
          foreground=[('active', CARD)])

# Combobox table selector: ruled underline field with serif text
root.option_add("*TCombobox*Listbox.background", CARD)
root.option_add("*TCombobox*Listbox.foreground", INK)
root.option_add("*TCombobox*Listbox.selectBackground", SELECT)
root.option_add("*TCombobox*Listbox.selectForeground", CARD)
style.configure("Ledger.TCombobox",
                fieldbackground=CARD,
                background=CARD,
                foreground=INK,
                bordercolor=INK,
                lightcolor=INK,
                darkcolor=INK,
                borderwidth=1,
                arrowcolor=INK,
                arrowsize=14,
                padding=(10, 6),
                font=SERIF_HEADER)
style.map("Ledger.TCombobox",
          bordercolor=[('focus', SELECT), ('!focus', INK)],
          fieldbackground=[('readonly', CARD)],
          foreground=[('readonly', INK)])

# Entry fields: paper face with ink border
style.configure("Ledger.TEntry",
                fieldbackground=CARD,
                foreground=INK,
                bordercolor=INK,
                lightcolor=RULE,
                darkcolor=RULE,
                borderwidth=1,
                insertcolor=INK,
                padding=(8, 6),
                font=SERIF_SMALL)
style.map("Ledger.TEntry", bordercolor=[('focus', SELECT), ('!focus', INK)])

# Scrollbar: slim ink thumb on paper trough
style.configure("Ledger.Vertical.TScrollbar",
                background=PAPER,
                troughcolor=PAPER,
                bordercolor=PAPER,
                arrowcolor=INK_SOFT,
                borderwidth=0,
                arrowsize=11)
style.map("Ledger.Vertical.TScrollbar",
          background=[('active', RULE), ('pressed', INK_SOFT)])

# ---------------------------------------------------------
# Wrapping Table Widget — printed ledger with an ink header
# band, zebra rows and generous cell padding
# ---------------------------------------------------------
class WrapTable(ttk.Frame):
    PAD = 16      # horizontal padding inside each cell
    MIN_COL = 70  # a column can never be narrower than this

    def __init__(self, master):
        super().__init__(master, style="Card.TFrame")
        self.headers = []
        self.rows = []

        scroll = ttk.Scrollbar(self, orient="vertical", style="Ledger.Vertical.TScrollbar")
        scroll.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self, bg=CARD, highlightthickness=0, bd=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.canvas.yview)

        self.inner = ttk.Frame(self.canvas, style="Card.TFrame")
        self._win = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.inner.bind("<Configure>",
                        lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", self._on_resize)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # ---------- public API (like Treeview: columns + rows) ----------
    def set_columns(self, headers):
        self.headers = list(headers)
        for child in self.inner.winfo_children():
            child.destroy()
        for c, h in enumerate(self.headers):
            head = ttk.Label(self.inner, text=h.upper(), style="HeadCell.TLabel", anchor="w")
            head.grid(row=0, column=c, sticky="nsew")
        self._layout()

    def set_rows(self, rows):
        self.rows = [list(row) for row in rows]
        # remove old cells (everything below the header row)
        for child in self.inner.winfo_children():
            if child.grid_info() and child.grid_info()["row"] > 0:
                child.destroy()
        for r, row in enumerate(self.rows, start=1):
            # zebra shading on even rows, like alternating ledger lines
            style = "CellEven.TLabel" if r % 2 == 0 else "CellOdd.TLabel"
            for c in range(len(self.headers)):
                text = str(row[c]) if c < len(row) else ""
                cell = ttk.Label(self.inner, text=text, style=style, anchor="nw")
                cell.grid(row=r, column=c, sticky="nsew")
        self._layout()

    # ---------- column sizing ----------
    def _on_resize(self, event=None):
        self.canvas.itemconfigure(self._win, width=event.width if event else self.canvas.winfo_width())
        self._layout()

    def _layout(self):
        if not self.headers:
            return
        avail = self.canvas.winfo_width()
        if avail < 100:  # window not drawn yet
            return
        # column weight = length of the longest record in it (max 40 chars)
        weights = []
        for c in range(len(self.headers)):
            lens = [len(self.headers[c])]
            lens += [len(str(row[c])) for row in self.rows if c < len(row)]
            weights.append(max(1, min(max(lens), 40)))
        widths = [max(self.MIN_COL, int(avail * w / sum(weights))) for w in weights]
        if sum(widths) > avail:  # minimum widths don't fit — shrink proportionally
            widths = [max(40, int(w * avail / sum(widths))) for w in widths]
        for c in range(len(self.headers)):
            self.inner.columnconfigure(c, minsize=widths[c])
            wraplength = max(20, widths[c] - self.PAD)
            for cell in self.inner.grid_slaves(column=c):
                cell.configure(wraplength=wraplength)

    def _on_mousewheel(self, event):
        if abs(event.delta) >= 120:  # Windows
            steps = -event.delta // 120
        else:                        # macOS
            steps = -event.delta
        if steps:
            self.canvas.yview_scroll(steps, "units")


# Ledger table cell styles: solid ink header band + zebra rows
style.configure("HeadCell.TLabel",
                background=INK,
                foreground=CARD,
                font=SERIF_CAPS,
                padding=(8, 9))
style.configure("CellOdd.TLabel",
                background=CARD,
                foreground=INK,
                font=SERIF_SMALL,
                padding=(8, 7))
style.configure("CellEven.TLabel",
                background="#f1ead8",
                foreground=INK,
                font=SERIF_SMALL,
                padding=(8, 7))

# ---------------------------------------------------------
# Main UI Layout
# ---------------------------------------------------------
main_frame = ttk.Frame(root, padding=28)
main_frame.pack(fill="both", expand=True)

# Masthead: title centred, table selector in the top-right corner,
# double rule beneath — like a printed ledger page
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill="x", pady=(0, 18))
header_frame.columnconfigure(0, weight=1)
header_frame.columnconfigure(2, weight=1)

table_var = tk.StringVar(value=list(TABLES.keys())[0])
table_selector = ttk.Combobox(header_frame, textvariable=table_var,
                              values=list(TABLES.keys()),
                              state="readonly", width=24,
                              style="Ledger.TCombobox")
table_selector.grid(row=0, column=2, sticky="e")

ttk.Label(header_frame, text="S P O R T   C L U B   R E G I S T R Y",
          style="Masthead.TLabel").grid(row=0, column=0, sticky="w")
ttk.Label(header_frame, text="EST. TODAY  ·  A PRINTED-STYLE REGISTRY OF MEMBERS, CLASSES & PAYMENTS",
          style="MastheadSub.TLabel").grid(row=1, column=0, sticky="w", pady=(6, 10))
ttk.Frame(header_frame, style="Rule.TFrame", height=3).grid(row=2, column=0, columnspan=3, sticky="ew")
ttk.Frame(header_frame, style="Rule.TFrame", height=1).grid(row=3, column=0, columnspan=3, sticky="ew", pady=(2, 0))

# ---------------------------------------------------------
# Left sidebar: action buttons in a fixed two-column grid
# (packed BEFORE the table view so the table shrinks instead
# of the sidebar when the window is resized)
# ---------------------------------------------------------
sidebar = ttk.Frame(main_frame)
sidebar.pack(side="left", fill="y", padx=(0, 18))

ttk.Label(sidebar, text="ACTIONS", font=SERIF_CAPS,
          foreground=INK_SOFT, background=PAPER).grid(
    row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))

for i, (text, (func, fields, count)) in enumerate(ACTIONS.items()):
    danger = text.startswith("Delete")
    btn = ttk.Button(sidebar, text=text.upper(),
                     style="Danger.Ledger.TButton" if danger else "Ledger.TButton",
                     command=lambda t=text, a=(func, fields, count): open_form(t, *a))
    btn.grid(row=1 + i // 2, column=i % 2, padx=(0, 6), pady=3, sticky="ew")

sidebar.columnconfigure(0, weight=1)
sidebar.columnconfigure(1, weight=1)

# ---------------------------------------------------------
# Table View (middle of the window, beside the sidebar)
# ---------------------------------------------------------
table_container = ttk.Frame(main_frame)
table_container.pack(side="left", fill="both", expand=True)

table = WrapTable(table_container)
table.pack(fill="both", expand=True)


def set_table_columns():
    """Applies the column headers of the currently selected table."""
    table.set_columns(TABLES[table_var.get()][0])


def on_table_selected(event=None):
    set_table_columns()
    refresh()


table_selector.bind("<<ComboboxSelected>>", on_table_selected)
set_table_columns()


def refresh():
    """Refreshes the current table view from its backend database getter."""
    getter = TABLES[table_var.get()][1]
    table.set_rows(getter())


def open_form(title, func, fields, returns_count):
    """Opens a clean, centered modal dialog window for user actions/inputs."""
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("460x520")
    win.resizable(False, False)
    win.transient(root)
    win.grab_set()
    win.configure(bg=PAPER)

    form_frame = ttk.Frame(win, padding=28)
    form_frame.pack(fill="both", expand=True)

    # Modal header: title with a single rule beneath
    ttk.Label(form_frame, text=title, font=SERIF_HEADER,
              background=PAPER, foreground=INK).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 4))
    ttk.Frame(form_frame, style="Rule.TFrame", height=1).grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 14))

    converters = {int: int, float: float, str: str}
    entries = []
    for i, (question, kind) in enumerate(fields, start=2):
        ttk.Label(form_frame, text=question, font=SERIF_SMALL,
                  background=PAPER, foreground=INK_SOFT).grid(row=i, column=0, sticky="w", pady=7)
        entry = ttk.Entry(form_frame, width=28, style="Ledger.TEntry")
        entry.grid(row=i, column=1, sticky="ew", pady=7, padx=(12, 0))
        entries.append(entry)

    form_frame.columnconfigure(1, weight=1)

    def submit(event=None):
        try:
            values = [converters[kind](e.get()) for e, (_, kind) in zip(entries, fields)]
            result = func(*values)
            refresh()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number where required.", parent=win)
            return
        except Exception as error:
            messagebox.showerror("Error", f"{type(error).__name__}: {error}", parent=win)
            return

        win.destroy()
        if returns_count and result == 0:
            messagebox.showwarning("Not found", "The specified ID was not found.", parent=root)
        else:
            if isinstance(result, list):
                messagebox.showinfo("Result", f"Retrieved {len(result)} record(s). Check database or table view.",
                                    parent=root)
            else:
                messagebox.showinfo("Success",
                                    "Done." if returns_count else f"Successfully completed. Result/ID: {result}",
                                    parent=root)

    # Action buttons inside modal
    btn_frame = ttk.Frame(form_frame)
    btn_frame.grid(row=len(fields) + 2, column=0, columnspan=2, sticky="e", pady=(26, 0))

    ttk.Button(btn_frame, text="CANCEL", style="Ledger.TButton", command=win.destroy).pack(side="right", padx=(8, 0))
    ttk.Button(btn_frame, text="SUBMIT", style="Confirm.TButton", command=submit).pack(side="right")

    win.bind("<Return>", submit)
    win.bind("<Escape>", lambda event: win.destroy())

    if entries:
        entries[0].focus_set()

    # Center modal relative to main window
    win.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (win.winfo_width() // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (win.winfo_height() // 2)
    win.geometry(f"+{x}+{y}")
    win.lift()


root.report_callback_exception = lambda *err: messagebox.showerror("Error", f"{err[0].__name__}: {err[1]}")

refresh()

if __name__ == "__main__":
    root.mainloop()
