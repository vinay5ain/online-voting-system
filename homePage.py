import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin

# ================= THEME =================
BG = "#0f172a"
CARD = "#1e293b"
BTN = "#3b82f6"
BTN_HOVER = "#2563eb"
TEXT = "#e5e7eb"
MUTED = "#94a3b8"


# ================= BUTTONS =================
def styled_button(parent, text, command):
    btn = Button(
        parent, text=text, command=command,
        bg=BTN, fg="white",
        font=("Segoe UI", 12, "bold"),
        bd=0, padx=25, pady=12,
        cursor="hand2", activebackground=BTN_HOVER
    )
    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN))
    return btn


def nav_button(parent, text, command):
    btn = Button(
        parent, text=text, command=command,
        bg=BG, fg=TEXT, bd=0,
        font=("Segoe UI", 11),
        cursor="hand2"
    )
    btn.bind("<Enter>", lambda e: btn.config(fg=BTN))
    btn.bind("<Leave>", lambda e: btn.config(fg=TEXT))
    return btn


# ================= CLEAR SCREEN =================
def clear_screen(root):
    for widget in root.winfo_children():
        widget.destroy()


# ================= COMMON PAGE =================
def show_page(root, title, content):
    clear_screen(root)

    root.configure(bg=BG)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Navbar
    nav = Frame(root, bg=BG)
    nav.grid(row=0, column=0, sticky="ew", padx=20, pady=15)

    nav_button(nav, "🏠 Home", lambda: Home(root)).pack(side=LEFT, padx=10)

    # Content
    main = Frame(root, bg=BG)
    main.grid(row=1, column=0, sticky="nsew")

    card = Frame(main, bg=CARD, padx=60, pady=50)
    card.place(relx=0.5, rely=0.5, anchor="center")

    Label(card, text=title,
          font=("Segoe UI", 26, "bold"),
          bg=CARD, fg=TEXT).pack(pady=(0, 20))

    Label(card, text=content,
          font=("Segoe UI", 12),
          bg=CARD, fg=TEXT,
          justify=LEFT, wraplength=700).pack(pady=10)

    styled_button(card, "⬅ Back to Home",
                  lambda: Home(root)).pack(pady=25)


# ================= PAGES =================
def About(root):
    show_page(
        root,
        "About Project",
        "Online Voting System\n\n"
        "A modern and secure desktop application\n"
        "developed for academic use.\n\n"
        "🎓 Modern College of Professional Studies\n\n"
        "👩‍💻 Team Members:\n"
        "• Vishakha\n"
        "• Prashant\n"
        "• Abhay"
    )


def Service(root):
    show_page(
        root,
        "Services",
        "⭐ Services Provided\n\n"
        "• Secure voter authentication\n"
        "• Admin-controlled elections\n"
        "• One vote per voter\n"
        "• Fast & reliable system\n"
        "• Clean and user-friendly UI"
    )


def Review(root):
    show_page(
        root,
        "Review",
        "✔ Simple interface\n"
        "✔ Smooth voting experience\n"
        "✔ Secure & efficient\n\n"
        "Overall Rating: ⭐⭐⭐⭐☆ (4/5)"
    )


# ================= HOME =================
def Home(root):
    clear_screen(root)
    root.configure(bg=BG)
    root.title("Online Voting System")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Navbar
    nav = Frame(root, bg=BG)
    nav.grid(row=0, column=0, sticky="ew", padx=20, pady=15)

    nav_button(nav, "🏠 Home", lambda: Home(root)).pack(side=LEFT, padx=10)
    nav_button(nav, "ℹ About", lambda: About(root)).pack(side=LEFT, padx=10)
    nav_button(nav, "🛠 Services", lambda: Service(root)).pack(side=LEFT, padx=10)
    nav_button(nav, "⭐ Review", lambda: Review(root)).pack(side=LEFT, padx=10)

    # Main area
    main = Frame(root, bg=BG)
    main.grid(row=1, column=0, sticky="nsew")

    card = Frame(main, bg=CARD, padx=70, pady=55)
    card.place(relx=0.5, rely=0.5, anchor="center")

    Label(card, text="Online Voting System",
          font=("Segoe UI", 30, "bold"),
          bg=CARD, fg=TEXT).pack(pady=(0, 10))

    Label(card, text="Secure • Reliable • Modern",
          font=("Segoe UI", 13),
          bg=CARD, fg=MUTED).pack(pady=(0, 35))

    styled_button(card, "Admin Login",
                  lambda: AdmLogin(root, card)).pack(pady=10)

    styled_button(card, "Voter Login",
                  lambda: voterLogin(root, card)).pack(pady=10)

    styled_button(card, "New Window",
                  lambda: sb_p.call("start python homePage.py", shell=True)).pack(pady=10)


# ================= MAIN =================
def new_home():
    root = Tk()
    root.state("zoomed")
    root.minsize(900, 600)
    Home(root)
    root.mainloop()


if __name__ == "__main__":
    new_home()
