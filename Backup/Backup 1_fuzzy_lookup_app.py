import pandas as pd
from rapidfuzz import fuzz, process
from tkinter import Tk, Label, Button, filedialog, messagebox, ttk, StringVar, Entry, Frame
import chardet
import os
import threading
import itertools
import time

ICON_PATH = "CG_App_Icon.ico"


class FuzzyMatcherApp:
    def __init__(self, master):
        self.master = master
        master.title("Fuzzy Company Matcher (Desktop App)")
        master.geometry("1280x720")
        try:
            master.iconbitmap(ICON_PATH)
        except Exception as e:
            print(f"Warning: Could not load icon: {e}")

        self.df1 = None
        self.df2 = None
        self.results_df = None
        self.tree = None
        self.tree_container = None
        self.loader_running = False

        self.label = Label(master, text="Welcome to the Fuzzy Lookup App by Christian G.", font=("Helvetica", 16, "bold"), justify='center')
        self.label.pack(pady=(15, 5))

        self.sub_label = Label(master, text="\nCompare two company lists and export reviewed matches.", font=("Helvetica", 13), justify='center')
        self.sub_label.pack(pady=(0, 10))

        self.file1_button = Button(master, text="Select File 1", command=self.load_file1)
        self.file1_button.pack(pady=5)
        self.file1_label = Label(master, text="File 1: Not selected", font=("Helvetica", 10))
        self.file1_label.pack(pady=2)

        self.file2_button = Button(master, text="Select File 2", command=self.load_file2)
        self.file2_button.pack(pady=5)
        self.file2_label = Label(master, text="File 2: Not selected", font=("Helvetica", 10))
        self.file2_label.pack(pady=2)

        self.compare_button = Button(master, text="Compare Files", command=self.start_comparison, state='disabled')
        self.compare_button.pack(pady=10)

        self.export_button = Button(master, text="Export Results as CSV", command=self.export_results, state='disabled')
        self.export_button.pack(pady=5)

        # Reset button added
        self.reset_button = Button(master, text="Reset / Compare New", command=self.reset_app)
        self.reset_button.pack(pady=5)

        self.search_var = StringVar()
        self.search_entry = Entry(master, textvariable=self.search_var)
        self.search_entry.pack(pady=5)
        self.search_entry.insert(0, "Type to filter results...")
        self.search_entry.bind('<KeyRelease>', self.filter_results)

        self.progress_label = Label(master, text="")
        self.progress_label.pack(pady=5)

    def detect_encoding(self, filepath):
        with open(filepath, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
        return result['encoding']

    def load_file1(self):
        try:
            path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if path:
                encoding = self.detect_encoding(path)
                self.df1 = pd.read_csv(path, encoding=encoding)
                self.file1_label.config(text=f"File 1: {os.path.basename(path)}")
                messagebox.showinfo("Success", f"Loaded File 1: {os.path.basename(path)}")
                self.check_ready()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading File 1:\n{str(e)}")

    def load_file2(self):
        try:
            path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if path:
                encoding = self.detect_encoding(path)
                self.df2 = pd.read_csv(path, encoding=encoding)
                self.file2_label.config(text=f"File 2: {os.path.basename(path)}")
                messagebox.showinfo("Success", f"Loaded File 2: {os.path.basename(path)}")
                self.check_ready()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading File 2:\n{str(e)}")

    def check_ready(self):
        if self.df1 is not None and self.df2 is not None:
            self.compare_button.config(state='normal')

    def start_comparison(self):
        threading.Thread(target=self.compare_files).start()
        threading.Thread(target=self.spinner).start()

    def spinner(self):
        self.loader_running = True
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if not self.loader_running:
                break
            self.progress_label.config(text=f"Processing... {c}")
            time.sleep(0.1)

    def compare_files(self):
        company_names_2 = self.df2['Company Name'].astype(str).tolist()
        websites_2 = self.df2['Website'].astype(str).tolist()

        results = []
        total = len(self.df1)

        for i, (_, row1) in enumerate(self.df1.iterrows(), 1):
            self.progress_label.config(text=f"Checking {i}/{total} ({int((i/total)*100)}%) • Matching...")
            self.master.update_idletasks()

            company_1 = str(row1['Company Name'])
            website_1 = str(row1['Website'])

            best_company, comp_score, comp_index = process.extractOne(
                company_1, company_names_2, scorer=fuzz.token_sort_ratio)

            best_website, web_score, web_index = process.extractOne(
                website_1, websites_2, scorer=fuzz.token_sort_ratio)

            avg_score = (comp_score + web_score) / 2

            best_row2 = self.df2.iloc[comp_index if comp_score >= web_score else web_index]

            domain_exact = website_1.strip().lower() == str(best_row2['Website']).strip().lower()
            company_exact = company_1.strip().lower() == str(best_row2['Company Name']).strip().lower()
            domain_fuzzy = fuzz.token_sort_ratio(website_1, str(best_row2['Website'])) >= 90
            company_fuzzy = fuzz.token_sort_ratio(company_1, str(best_row2['Company Name'])) >= 90

            exclude = domain_exact and company_exact
            review = domain_fuzzy or company_fuzzy

            results.append({
                "Company Name (File 1)": company_1,
                "Website (File 1)": website_1,
                "Matched Company Name (File 2)": best_row2['Company Name'],
                "Matched Website (File 2)": best_row2['Website'],
                "Domain Exact Match": domain_exact,
                "Company Exact Match": company_exact,
                "Domain Fuzzy Match": domain_fuzzy,
                "Company Fuzzy Match": company_fuzzy,
                "Fuzzy Match Score": avg_score,
                "Exclude": exclude,
                "Review": review
            })

        self.results_df = pd.DataFrame(results)
        self.loader_running = False
        self.progress_label.config(text="Done!")
        self.show_results()
        self.export_button.config(state='normal')

    def show_results(self):
        if self.tree_container:
            self.tree_container.destroy()

        self.tree_container = Frame(self.master)
        self.tree_container.pack(expand=True, fill='both')

        self.tree = ttk.Treeview(self.tree_container)
        self.tree.pack(expand=True, fill='both')

        self.tree["columns"] = list(self.results_df.columns)
        self.tree["show"] = "headings"

        for col in self.results_df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='w', width=150)

        for _, row in self.results_df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def filter_results(self, event):
        if self.results_df is not None and self.tree is not None:
            search_term = self.search_var.get().lower()
            for row in self.tree.get_children():
                self.tree.delete(row)

            for _, row in self.results_df.iterrows():
                row_values = [str(value).lower() for value in row]
                if any(search_term in value for value in row_values):
                    self.tree.insert("", "end", values=list(row))

    def reset_app(self):
        self.df1 = None
        self.df2 = None
        self.results_df = None
        self.file1_label.config(text="File 1: Not selected")
        self.file2_label.config(text="File 2: Not selected")
        self.progress_label.config(text="")
        self.compare_button.config(state='disabled')
        self.export_button.config(state='disabled')
        self.search_entry.delete(0, 'end')
        self.search_entry.insert(0, "Type to filter results...")
        if self.tree:
            self.tree.destroy()
            self.tree = None
        if self.tree_container:
            self.tree_container.destroy()
            self.tree_container = None

    def export_results(self):
        if self.results_df is not None:
            try:
                file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if file_path:
                    self.results_df.to_csv(file_path, index=False)
                    messagebox.showinfo("Success", f"Results exported to: {file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Could not export CSV: {str(e)}")


if __name__ == "__main__":
    print("Launching GUI...")
    root = Tk()
    app = FuzzyMatcherApp(root)
    root.mainloop()
