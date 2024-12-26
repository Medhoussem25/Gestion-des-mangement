import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import os  
import re

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee management system V 1.0")
        self.root.geometry("400x486")
        self.root.resizable(True, True)

        # choisir chemin
        self.project_path = os.path.dirname(os.path.abspath(__file__))

        # icon de projet
        icon_path = os.path.join(self.project_path, "recruitment.png")
        self.icon_image = ImageTk.PhotoImage(file=icon_path)
        self.root.iconphoto(False, self.icon_image)

        # title
        self.title_label = tk.Label(self.root, text="Système de gestion des employés", font=('Calibri', 19, 'bold'), bg='#2c3e50', fg='white')
        self.title_label.pack(pady=10)

        # upload et afficher photo
        image_path = os.path.join(self.project_path, "manager.png")
        self.image = Image.open(image_path).resize((100, 100), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.pack(pady=5)

        # frame champs
        self.fields_frame = tk.Frame(self.root, bg='#2c3e50')
        self.fields_frame.pack(pady=20)

        # champs nom d'utulisateur
        self.username_label = tk.Label(self.fields_frame, text="Nom d'utilisateur:", font=('Calibri', 12), bg='#2c3e50', fg='white')
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.fields_frame, font=('Calibri', 12))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # champs password
        self.password_label = tk.Label(self.fields_frame, text="Mot de passe:", font=('Calibri', 12), bg='#2c3e50', fg='white')
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.fields_frame, show='*', font=('Calibri', 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # مربع الاختيار لإظهار كلمة المرور
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(
            self.root,
            text="Afficher le mot de passe",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            font=('Calibri', 10)
        )
        self.show_password_checkbox.pack(pady=5)

        # boutton login
        self.login_button = tk.Button(self.root, text='Connexion', command=self.login, bg='#3498db', fg='white', font=('Calibri', 12, 'bold'))
        self.login_button.pack(pady=10)

        # boutton dev info
        self.dev_info_button = tk.Button(self.root, text='Infos Développeur', command=self.show_dev_info, bg='#e67e22', fg='white', font=('Calibri', 10))
        self.dev_info_button.pack(pady=5)
   
    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show='')  # afficher password
        else:
            self.password_entry.config(show='*')  # masque password

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123":
            messagebox.showinfo("Connexion réussie", "Bienvenue dans l'application!")
            self.root.withdraw()  
            self.open_employee_management()  
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")
            
    def show_dev_info(self):
      messagebox.showinfo("Infos Développeur", "Développé par HoussemBouagal\nVersion: 1.0\nContact: mouhamedhoussem813@gmail.com")
    
    def open_employee_management(self):
        # Connect to SQLite database
        self.conn = sqlite3.connect('employees.db')
        self.create_table()  # Create table if not exists
        
        # Employee management window
        self.emp_root = tk.Toplevel(self.root)
        self.emp_root.title('Système de Gestion des Employés')
        self.emp_root.geometry('798x560')
        self.emp_root.resizable(True, True)
        
        # Use image as window icon
        self.emp_root.iconphoto(False, self.icon_image)
        
        # Entry frame
        entries_frame = tk.Frame(self.emp_root, bg='#2c3e50')
        entries_frame.pack(side=tk.LEFT, fill=tk.Y)
        title = tk.Label(entries_frame, text="Gestion de Employés", font=('Calibri', 18, 'bold'), bg='red', fg='white')
        title.pack(pady=10)
        
        # Function to create a Label and Entry
        def create_label_entry(parent, text, row):
            label = tk.Label(parent, text=text, font=('Calibri', 12), bg='#2c3e50', fg='white')
            label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
            entry = tk.Entry(parent, font=('Calibri', 12))
            entry.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
            return entry
        
        # Entry fields
        entries_grid = tk.Frame(entries_frame, bg='#2c3e50')
        entries_grid.pack(fill=tk.BOTH, expand=True)
        self.txtName = create_label_entry(entries_grid, "Nom", 0)
        self.txtJob = create_label_entry(entries_grid, "Poste", 1)
        self.gender_label = tk.Label(entries_grid, text="Genre", font=('Calibri', 12), bg='#2c3e50', fg='white')
        self.gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.txtGender = ttk.Combobox(entries_grid, font=('Calibri', 12), values=["Masculin", "Féminin"])
        self.txtGender.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.txtAge = create_label_entry(entries_grid, "Âge", 3)
        self.txtEmail = create_label_entry(entries_grid, "E-mail", 4)
        self.txtMobile = create_label_entry(entries_grid, "Téléphone", 5)
        self.txtAddress = create_label_entry(entries_grid, "Adresse", 6)
        
        # Buttons frame
        buttons_frame = tk.Frame(entries_frame, bg='#2c3e50', bd=1, relief=tk.SOLID)
        buttons_frame.pack(pady=20)
        
        # CRUD buttons
        tk.Button(buttons_frame, text="Ajouter", font=('Calibri', 12), bg='#1abc9c', fg='white', width=15, command=self.add_employee).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(buttons_frame, text="Supprimer", font=('Calibri', 12), bg='#e74c3c', fg='white', width=15, command=self.delete_employee).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(buttons_frame, text="Mettre à jour", font=('Calibri', 12), bg='#3498db', fg='white', width=15, command=self.update_employee).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(buttons_frame, text="Effacer", font=('Calibri', 12), bg='#f39c12', fg='white', width=15, command=self.clear_entries).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(buttons_frame, text="Dashboard", font=('Calibri', 12), bg='#9b59b6', fg='white', width=15, command=self.open_dashboard).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(buttons_frame, text="Déconnexion", font=('Calibri', 12), bg='#e67e22', fg='white', width=15, command=self.logout).grid(row=2, column=1, padx=5, pady=5)
        
        # Treeview table to display employees
        self.tree_frame = tk.Frame(self.emp_root, bg='white')
        self.tree_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.scrollbar_x = tk.Scrollbar(self.tree_frame, orient=tk.HORIZONTAL)
        self.scrollbar_y = tk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.employee_table = ttk.Treeview(self.tree_frame, columns=("ID", "Nom", "Poste", "Genre", "Âge", "E-mail", "Téléphone", "Adresse"), 
                                           show='headings', xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_x.config(command=self.employee_table.xview)
        self.scrollbar_y.config(command=self.employee_table.yview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        for col in self.employee_table['columns']:
            self.employee_table.heading(col, text=col)
            self.employee_table.column(col, width=100)
        
        self.employee_table.pack(fill=tk.BOTH, expand=True)
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        self.show_employees()
        
    def clear_entries(self):
        self.txtName.delete(0, tk.END)
        self.txtJob.delete(0, tk.END)
        self.txtGender.set('')
        self.txtAge.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtMobile.delete(0, tk.END)
        self.txtAddress.delete(0, tk.END)

    def add_employee(self):
        name = self.txtName.get()
        job = self.txtJob.get()
        gender = self.txtGender.get()
        age = self.txtAge.get()
        email = self.txtEmail.get()
        mobile = self.txtMobile.get()
        address = self.txtAddress.get()

        # Validation
        if not name or not job or not gender or not age or not email or not mobile or not address:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
            return
        # Validate age
        if not age.isdigit() or int(age) < 0:
            messagebox.showerror("Erreur", "Âge doit être un entier non négatif.")
            return

        # Validate email and phone number
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            messagebox.showerror("Erreur", "Adresse e-mail non valide")
            return

        if not re.match(r'^\d{10}$', mobile):
            messagebox.showerror("Erreur", "Numéro de téléphone non valide")
            return
        # Check for existing email
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE email=?", (email,))
        if cursor.fetchone() is not None:
            messagebox.showerror("Erreur", "L'adresse e-mail existe déjà.")
            return
  # Check for existing numero
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE mobile=?", (mobile,))

        if cursor.fetchone() is not None:
            messagebox.showerror("Erreur", "Le numéro de téléphone existe déjà.")
            return
 # Insert new employee into the database
        cursor.execute("INSERT INTO employees (name, job, gender, age, email, mobile, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, job, gender, age, email, mobile, address))
        self.conn.commit()
        messagebox.showinfo("Succès", "Employé ajouté avec succès.")
        self.show_employees()  # Refresh the employee list

    def show_employees(self):
        # Clear the existing data in the treeview
        for item in self.employee_table.get_children():
            self.employee_table.delete(item)
        
        # Fetch employees from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees")
        for row in cursor.fetchall():
            self.employee_table.insert('', tk.END, values=row)

    def get_data(self, event):
        selected_item = self.employee_table.focus()
        values = self.employee_table.item(selected_item, 'values')
        
        # Populate the entries with the selected item data
        self.txtName.delete(0, tk.END)
        self.txtName.insert(0, values[1])  # Name
        self.txtJob.delete(0, tk.END)
        self.txtJob.insert(0, values[2])  # Job
        self.txtGender.set(values[3])  # Gender
        self.txtAge.delete(0, tk.END)
        self.txtAge.insert(0, values[4])  # Age
        self.txtEmail.delete(0, tk.END)
        self.txtEmail.insert(0, values[5])  # Email
        self.txtMobile.delete(0, tk.END)
        self.txtMobile.insert(0, values[6])  # Mobile
        self.txtAddress.delete(0, tk.END)
        self.txtAddress.insert(0, values[7])  # Address

    
    def update_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sélectionnez un employé", "Veuillez sélectionner un employé à mettre à jour.")
            return

        item_id = self.tree.item(selected_item)['values'][0]
        name = self.txtName.get()
        job = self.txtJob.get()
        gender = self.txtGender.get()
        age = self.txtAge.get()
        email = self.txtEmail.get()
        mobile = self.txtMobile.get()
        address = self.txtAddress.get()

        if self.validate_fields(name, job, gender, age, email, mobile, address):
            cursor = self.conn.cursor()
            # Check if email or mobile already exists
            cursor.execute("SELECT * FROM employees WHERE (email=? OR mobile=?) AND id!=?", (email, mobile, item_id))
            if cursor.fetchone():
                messagebox.showerror("Erreur", "Cet e-mail ou numéro de téléphone est déjà utilisé.")
                return

            cursor.execute('''
            UPDATE employees SET name=?, job=?, gender=?, age=?, email=?, mobile=?, address=? WHERE id=?
            ''', (name, job, gender, age, email, mobile, address, item_id))
            self.conn.commit()
            messagebox.showinfo("Succès", "Employé mis à jour avec succès.")
            self.clear_fields()
            self.view_employees()  # Refresh the tree view

    def delete_employee(self):
        selected_item = self.employee_table.focus()
        if not selected_item:
            messagebox.showerror("Erreur", "Sélectionnez un employé à supprimer.")
            return

        # Get email of the selected employee for deletion
        values = self.employee_table.item(selected_item, 'values')
        email = values[5]  # Assuming email is at index 5

        # Delete employee from the database
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM employees WHERE email=?", (email,))
        self.conn.commit()
        messagebox.showinfo("Succès", "Employé supprimé avec succès.")
        self.show_employees()

    def update_employee(self):
        selected_row = self.employee_table.selection()
        if selected_row:
            emp_id = self.employee_table.item(selected_row)['values'][0]
            name = self.txtName.get()
            job = self.txtJob.get()
            gender = self.txtGender.get()
            age = self.txtAge.get()
            email = self.txtEmail.get()
            mobile = self.txtMobile.get()
            address = self.txtAddress.get()

            if not name or not job or not gender or not age or not email or not mobile or not address:
                messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
                return

            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                messagebox.showerror("Erreur", "Adresse e-mail non valide")
                return

            if not re.match(r'^\d{10}$', mobile):
                messagebox.showerror("Erreur", "Numéro de téléphone non valide")
                return

            cursor = self.conn.cursor()
            
            cursor.execute("UPDATE employees SET name=?, job=?, gender=?, age=?, email=?, mobile=?, address=? WHERE id=?",
                           (name, job, gender, age, email, mobile, address, emp_id))
            self.conn.commit()
            messagebox.showinfo("Succès", "Employé mis à jour avec succès")
            self.clear_entries()
            self.show_employees()
        else:
            messagebox.showerror("Erreur", "Sélectionnez un employé à mettre à jour")

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            job TEXT NOT NULL,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            mobile TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL
        )""")
        self.conn.commit()

    def open_dashboard(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT gender, COUNT(*) FROM employees GROUP BY gender")
        data = cursor.fetchall()
        gender_counts = {gender: count for gender, count in data}
        genders = list(gender_counts.keys())
        counts = list(gender_counts.values())
        fig, ax = plt.subplots()
        bars = ax.bar(genders, counts, color=['#3498db', '#e74c3c'])  # Customize colors
        # Add title and labels
        ax.set_title('Distribution des Genres', fontsize=16, fontweight='bold')
        ax.set_xlabel('Genre', fontsize=14)
        ax.set_ylabel('Nombre', fontsize=14)
        # Adding data labels above bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for better readability
        plt.show()
    def logout(self):
        self.emp_root.destroy()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
