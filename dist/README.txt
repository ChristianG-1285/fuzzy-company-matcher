===========================================
Fuzzy Company Matcher - Desktop App (v1.2)
===========================================

🛠 Developed by: Christian G.
📅 Version: 1.2
📂 App Folder: fuzzy_lookup_app

This is a standalone Windows desktop tool for comparing two company lists with fuzzy logic.
It matches company names and websites across two CSV files, and highlights both exact and approximate matches.

---------------------------------------------------------
📦 FILES INCLUDED
---------------------------------------------------------
✔ fuzzy_lookup_app.exe               ← The desktop app (double-click to run)
✔ CG_App_Icon.ico                   ← App icon used in window and packaging
✔ README.txt                        ← You're reading it!

All files should remain inside the same `fuzzy_lookup_app` folder.

---------------------------------------------------------
🚀 HOW TO USE THE APP
---------------------------------------------------------
1. Double-click `fuzzy_lookup_app.exe` to open the app.
   - A welcome screen with a clean blue-white UI will appear.
   - The app is a native desktop window, no internet required.

2. Click **“Select File 1”** to choose your first CSV file.
   - File must contain columns: `Company Name`, `Website`

3. Click **“Select File 2”** to choose the second file.
   - Same format required.

4. Click **“Compare Files”**.
   - The app compares companies and websites using fuzzy logic.
   - Matches will be previewed in a scrollable, searchable table.

5. You’ll be prompted to **save the results as a CSV**.
   - Output includes:
     - Company info from both files
     - Exact and fuzzy match indicators
     - Match score
     - Auto-tagged “Exclude” and “Review” flags

---------------------------------------------------------
📂 INPUT FILE FORMAT
---------------------------------------------------------
• File type: `.csv` only (not `.xlsx`)
• Column headers must be exactly:
    → Company Name
    → Website
• Avoid merged cells or blank rows.

---------------------------------------------------------
✨ WHAT'S NEW IN v1.2
---------------------------------------------------------
✔ Animated progress bar with % complete and ETA
✔ Total items processed and total time displayed
✔ Fully scrollable horizontal + vertical result table
✔ Auto-clearing search field with gray placeholder
✔ Blue/Black/White UI color theme for a polished look
✔ Footer added: “Developed by Christian G. — June 16, 2025 • Version 1.2”
✔ Bug fix: Prevent freezing after processing ends

---------------------------------------------------------
🎨 DESIGN NOTES
---------------------------------------------------------
• Desktop-native interface built with Tkinter
• Uses RapidFuzz for accurate fuzzy matching
• Responsive scrollable table view
• Clean, modern color scheme
• CG icon included in app window

---------------------------------------------------------
💬 SUPPORT / FEEDBACK
---------------------------------------------------------
For updates, bugs, or feature requests,
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

v1.2 - UX and design refinements:
    • Progress bar and timing
    • UI color theme
    • Placeholder search bar
    • Scroll improvements
    • Footer versioning
