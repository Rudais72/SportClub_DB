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

# Initialize main window
root = tk.Tk()
root.title("SPORT CLUB MANAGER")
root.geometry("1024x720")
root.minsize(840, 560)

# ---------------------------------------------------------
# Theme & Color Palette Constants (Modern Grey + Colorful Accents)
# ---------------------------------------------------------
BG_COLOR = "#313338"       # Modern neutral grey (Background)
SURFACE_COLOR = "#3b3f45"  # Lighter grey (Cards, tables, notebook)
PRIMARY_COLOR = "#3b82f6"  # Vivid blue for primary actions
PRIMARY_HOVER = "#60a5fa"  # Lighter blue for hover
TEXT_COLOR = "#f4f4f5"     # Near-white for clear readability
MUTED_TEXT = "#9ca3af"     # Medium grey for secondary text
BORDER_COLOR = "#4b5058"   # Subtle border grey
INPUT_BG = "#202225"       # Dark input field background

# Colorful accent per action button: text -> (style key, base color, hover color)
ACCENTS = {
    "Add client":        ("blue",   "#3b82f6", "#2563eb"),
    "Update client":     ("indigo", "#6366f1", "#4f46e5"),
    "Delete client":     ("red",    "#ef4444", "#dc2626"),
    "Add trainer":       ("green",  "#10b981", "#059669"),
    "Update trainer":    ("teal",   "#14b8a6", "#0d9488"),
    "Delete trainer":    ("red",    "#ef4444", "#dc2626"),
    "Add class":         ("purple", "#8b5cf6", "#7c3aed"),
    "Update class":      ("violet", "#a78bfa", "#8b5cf6"),
    "Delete class":      ("red",    "#ef4444", "#dc2626"),
    "Add membership":    ("amber",  "#f59e0b", "#d97706"),
    "Update membership": ("orange", "#f97316", "#ea580c"),
    "Delete membership": ("red",    "#ef4444", "#dc2626"),
    "Add schedule":      ("cyan",   "#06b6d4", "#0891b2"),
    "Update schedule":   ("sky",    "#0ea5e9", "#0284c7"),
    "Delete schedule":   ("red",    "#ef4444", "#dc2626"),
    "Add booking":       ("lime",   "#84cc16", "#65a30d"),
    "Update booking":    ("grass",  "#22c55e", "#16a34a"),
    "Delete booking":    ("red",    "#ef4444", "#dc2626"),
    "Add payment":       ("pink",   "#ec4899", "#db2777"),
    "Update payment":    ("rose",   "#f43f5e", "#e11d48"),
    "Delete payment":    ("red",    "#ef4444", "#dc2626"),
    "Add equipment":     ("brown",  "#a16207", "#854d0e"),
    "Update equipment":  ("stone",  "#78716c", "#57534e"),
    "Delete equipment":  ("red",    "#ef4444", "#dc2626"),
}

root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use('clam')

style.configure(".", background=BG_COLOR, foreground=TEXT_COLOR, font=("Segoe UI", 10))
style.configure("TFrame", background=BG_COLOR)
style.configure("Header.TLabel", font=("Georgia", 26, "bold italic"), foreground=TEXT_COLOR, background=BG_COLOR,
                anchor="center")
style.configure("Subtitle.TLabel", font=("Segoe UI", 10), foreground=MUTED_TEXT, background=BG_COLOR,
                anchor="center")

# Standard Button Styling (neutral grey, modern flat look)
style.configure("TButton",
                background="#4b5058",
                foreground=TEXT_COLOR,
                borderwidth=0,
                focusthickness=0,
                padding=(14, 9),
                font=("Segoe UI", 9, "bold"))
style.map("TButton",
          background=[('active', '#5a606a'), ('pressed', '#202225')],
          foreground=[('disabled', MUTED_TEXT)])

# Colorful Accent Button Styling — one vivid color per action
for _text, (_key, _base, _hover) in ACCENTS.items():
    _style_name = f"Accent.{_key}.TButton"
    style.configure(_style_name,
                    background=_base,
                    foreground="#ffffff",
                    borderwidth=0,
                    focusthickness=0,
                    padding=(8, 8),
                    font=("Segoe UI", 10, "bold"))
    style.map(_style_name,
              background=[('active', _hover), ('pressed', '#202225')],
              foreground=[('active', '#ffffff'), ('pressed', '#ffffff'), ('disabled', '#ffffff')])

# Primary Accent Button Styling (blue — used for modal Submit)
style.configure("Primary.TButton",
                background=PRIMARY_COLOR,
                foreground="#ffffff",
                borderwidth=0,
                focusthickness=0,
                padding=(14, 9),
                font=("Segoe UI", 9, "bold"))
style.map("Primary.TButton",
          background=[('active', PRIMARY_HOVER), ('pressed', '#202225')],
          foreground=[('active', '#ffffff')])

# Notebook & Tabs Styling (modern flat tabs with blue selection)
style.configure("TNotebook", background=BG_COLOR, borderwidth=0, tabmargins=(0, 0, 0, 8))
style.configure("TNotebook.Tab",
                background=SURFACE_COLOR,
                foreground=MUTED_TEXT,
                padding=[18, 10],
                borderwidth=0,
                font=("Segoe UI", 10, "bold"))
style.map("TNotebook.Tab",
          background=[('selected', PRIMARY_COLOR), ('active', '#4b5058')],
          foreground=[('selected', '#ffffff'), ('active', TEXT_COLOR)])

# Wrapping Table Styling (header + cells are labels, so long text can wrap)
style.configure("Table.TFrame", background=SURFACE_COLOR)
style.configure("TableHeading.TLabel",
                background="#202225",
                foreground=TEXT_COLOR,
                borderwidth=0,
                relief="flat",
                font=("Segoe UI", 10, "bold"),
                padding=(8, 8))
style.configure("TableCell.TLabel",
                background=SURFACE_COLOR,
                foreground=TEXT_COLOR,
                borderwidth=0,
                relief="flat",
                font=("Segoe UI", 10),
                padding=(8, 6))

# Scrollbar Styling (thin, blends with surface)
style.configure("Vertical.TScrollbar",
                background="#4b5058",
                troughcolor=BG_COLOR,
                borderwidth=0,
                arrowsize=12)
style.map("Vertical.TScrollbar", background=[('active', '#5a606a')])

# Entry Field Styling (dark fields with subtle borders)
style.configure("TEntry",
                fieldbackground=INPUT_BG,
                foreground=TEXT_COLOR,
                borderwidth=1,
                insertcolor=TEXT_COLOR,
                padding=(6, 6))
style.map("TEntry",
          bordercolor=[('focus', PRIMARY_COLOR), ('!focus', BORDER_COLOR)])

# Combobox Styling (table selector dropdown)
root.option_add("*TCombobox*Listbox.background", SURFACE_COLOR)
root.option_add("*TCombobox*Listbox.foreground", TEXT_COLOR)
root.option_add("*TCombobox*Listbox.selectBackground", PRIMARY_COLOR)
root.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")
style.configure("TCombobox",
                fieldbackground=INPUT_BG,
                background="#4b5058",
                foreground=TEXT_COLOR,
                borderwidth=1,
                arrowcolor=TEXT_COLOR,
                padding=(8, 6))
style.map("TCombobox",
          bordercolor=[('focus', PRIMARY_COLOR), ('!focus', BORDER_COLOR)],
          fieldbackground=[('readonly', INPUT_BG)],
          foreground=[('readonly', TEXT_COLOR)])

# ---------------------------------------------------------
# Wrapping Table Widget (columns share the whole width and
# long text wraps onto several lines)
# ---------------------------------------------------------
class WrapTable(ttk.Frame):
    PAD = 16      # horizontal padding inside each cell
    MIN_COL = 70  # a column can never be narrower than this

    def __init__(self, master):
        super().__init__(master, style="Table.TFrame")
        self.headers = []
        self.rows = []

        scroll = ttk.Scrollbar(self, orient="vertical", style="Vertical.TScrollbar")
        scroll.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self, bg=SURFACE_COLOR, highlightthickness=0, bd=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.canvas.yview)

        self.inner = ttk.Frame(self.canvas, style="Table.TFrame")
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
            head = ttk.Label(self.inner, text=h, style="TableHeading.TLabel", anchor="w")
            head.grid(row=0, column=c, sticky="nsew")
        self._layout()

    def set_rows(self, rows):
        self.rows = [list(row) for row in rows]
        # remove old cells (everything below the header row)
        for child in self.inner.winfo_children():
            if child.grid_info() and child.grid_info()["row"] > 0:
                child.destroy()
        for r, row in enumerate(self.rows, start=1):
            for c in range(len(self.headers)):
                text = str(row[c]) if c < len(row) else ""
                cell = ttk.Label(self.inner, text=text, style="TableCell.TLabel", anchor="nw")
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

# ---------------------------------------------------------
# Main UI Layout
# ---------------------------------------------------------
main_frame = ttk.Frame(root, padding=24)
main_frame.pack(fill="both", expand=True)

# App Title Header (centered logo + subtitle)
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill="x", pady=(0, 16))
ttk.Label(header_frame, text="S P O R T   C L U B   M A N A G E R",
          style="Header.TLabel").pack(fill="x")
ttk.Label(header_frame, text="SQL Database on SQLite  ·  Sport Club Management System",
          style="Subtitle.TLabel").pack(fill="x", pady=(4, 0))

# ---------------------------------------------------------
# Action Toolbar (created & packed BEFORE the table view so it
# always keeps its space when the window is resized —
# the table shrinks instead of hiding the buttons)
# ---------------------------------------------------------
bar = ttk.Frame(main_frame)
bar.pack(side="bottom", fill="x", pady=(12, 0))

action_buttons = []
for text, (func, fields, count) in ACTIONS.items():
    style_key, _, _ = ACCENTS[text]
    btn = ttk.Button(bar, text=text, style=f"Accent.{style_key}.TButton",
                     command=lambda t=text, a=(func, fields, count): open_form(t, *a))
    action_buttons.append(btn)

BTN_GAP = 4  # matches padx between buttons


def relayout_buttons(event=None):
    """Flows the action buttons onto multiple rows when the window is too narrow."""
    width = bar.winfo_width()
    if width < 50:
        return
    rows, current, x = [], [], 0
    for btn in action_buttons:
        w = btn.winfo_reqwidth()
        need = w if not current else w + BTN_GAP
        if current and x + need > width:
            rows.append(current)
            current, x = [btn], w
        else:
            current.append(btn)
            x += need
    if current:
        rows.append(current)
    for r, row in enumerate(rows):
        for c, btn in enumerate(row):
            btn.grid(row=r, column=c, padx=(0, BTN_GAP), pady=4, sticky="ew")
    for col in range(max(len(r) for r in rows)):
        bar.columnconfigure(col, weight=1)


bar.bind("<Configure>", relayout_buttons)

# ---------------------------------------------------------
# Table Selector (single dropdown) & Table View
# ---------------------------------------------------------
table_bar = ttk.Frame(main_frame)
table_bar.pack(fill="x", pady=(0, 12))

table_var = tk.StringVar(value=list(TABLES.keys())[0])
table_selector = ttk.Combobox(table_bar, textvariable=table_var,
                              values=list(TABLES.keys()),
                              state="readonly", width=26,
                              font=("Segoe UI", 11, "bold"))
table_selector.pack(side="left", ipady=2)

table_container = ttk.Frame(main_frame)
table_container.pack(fill="both", expand=True, pady=(0, 16))

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
    win.geometry("440x480")
    win.resizable(False, False)
    win.transient(root)
    win.grab_set()
    win.configure(bg=BG_COLOR)

    form_frame = ttk.Frame(win, padding=24)
    form_frame.pack(fill="both", expand=True)

    ttk.Label(form_frame, text=title, font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=2, sticky="w",
                                                                          pady=(0, 16))

    converters = {int: int, float: float, str: str}
    entries = []
    for i, (question, kind) in enumerate(fields, start=1):
        ttk.Label(form_frame, text=question).grid(row=i, column=0, sticky="w", pady=6)
        entry = ttk.Entry(form_frame, width=28)
        entry.grid(row=i, column=1, sticky="ew", pady=6, padx=(12, 0))
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

    # Action Buttons Inside Modal
    btn_frame = ttk.Frame(form_frame)
    btn_frame.grid(row=len(fields) + 1, column=0, columnspan=2, sticky="e", pady=(24, 0))

    ttk.Button(btn_frame, text="Cancel", command=win.destroy).pack(side="right", padx=(8, 0))
    ttk.Button(btn_frame, text="Submit", style="Primary.TButton", command=submit).pack(side="right")

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
