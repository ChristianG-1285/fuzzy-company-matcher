===========================================
Fuzzy Company Matcher - Desktop App (v1.1)
===========================================

🛠 Developed by: Christian G.
📅 Version: 1.1
📂 App Folder: fuzzy_lookup_app

This is a standalone Windows desktop tool for comparing two company lists with fuzzy logic.
It matches company names and websites across two CSV files, and highlights both exact and approximate matches.

---------------------------------------------------------
📦 FILES INCLUDED
---------------------------------------------------------
✔ fuzzy_lookup_app.exe               ← The desktop app (double-click to run)
✔ CG_App_Icon.ico                   ← App icon used in window and packaging
✔ Welcome Screen.png                ← Splash screen on startup
✔ README.txt                        ← You're reading it!

All files should remain inside the same `fuzzy_lookup_app` folder.

---------------------------------------------------------
🚀 HOW TO USE THE APP
---------------------------------------------------------
1. Double-click `fuzzy_lookup_app.exe` to open the app.
   - A welcome screen with branding will appear briefly.
   - A native Windows window will launch (no browser needed).

2. Click **“Select File 1”** to choose your first CSV file.
   - File must contain columns: `Company Name`, `Website`

3. Click **“Select File 2”** to choose the second file.
   - Same format required.

4. Click **“Compare and Generate CSV”**.
   - The app compares companies and websites using fuzzy logic.
   - Matched records will be shown in the window.

5. You’ll be prompted to **save the result CSV file**.
   - Output includes:
     - Company info from both files
     - Exact and fuzzy match flags
     - Match score
     - “Exclude” and “Review” logic

---------------------------------------------------------
📂 INPUT FILE FORMAT
---------------------------------------------------------
• File type: `.csv` only (not `.xlsx`)
• Column headers must be exactly:
    → Company Name
    → Website
• Avoid merged cells or blank rows.

---------------------------------------------------------
🎨 DESIGN NOTES
---------------------------------------------------------
• Desktop-native interface built with Tkinter
• Uses RapidFuzz for fast fuzzy matching
• Displays results in a scrollable table
• Custom welcome screen with blue theme
• App window features a CG icon

---------------------------------------------------------
💬 SUPPORT / FEEDBACK
---------------------------------------------------------
For updates, bugs, or enhancements,
please contact: [your email or preferred contact]

---------------------------------------------------------
📌 VERSION HISTORY
---------------------------------------------------------
v1.0 - Initial Streamlit-based version (browser app)
v1.1 - Desktop version with:
    • Native GUI
    • Custom icon
    • Welcome splash screen
    • Faster matching via RapidFuzz
