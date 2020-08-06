--- 2 ---

Used to figure out which color LED was the best for future experiments.
Blue was chosen for its brightness, which would eliminate most interference.
NONBLIND.

--- SPECS ---

Every Red, White, and Blue LED was scanned 3 times.

--- DETAILS ---

/Raw Data
    Contains raw spectra files (*.csv)
/Spectrometer Data
    The spectra files from PASCO (*.sp)
/Processed Data
    Contains the Unscrambler file (PCA Analysis.unsb) as well as some charts to go with it (*.csv)
/Master Files
    masterfile.csv (Combination of all files in "/Raw Data")
    masterfilegen.py (Due to the size of the dataset, a small python script was created to merge
                      all the files into one. When ran, it will regenerate masterfile.csv)