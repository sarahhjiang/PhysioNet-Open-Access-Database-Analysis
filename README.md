# Physionet Demographics Reporting

Usage:

The jupyter notebook file final.ipynb (SJ) contains all necessary packaging and cleaning for the data to run analysis and generate figures. Install all necessary packages in local environment before running cells.

All cleaned data is contained within "final_data.csv", so you should be able to run all cells immediately.


Archive contains:
1. Past generated figures (SJ)
2. Large databases pulled down from PhysioNet -- used to parse out gender, age, race, ethnicity information from individual header files.
3. Python scripts (SJ) to parse the above demographics information from various .csv, .txt, and .hea files with different data storage formats (primarily using regex matching)
4. Jupyter notebook (SJ) file to parse out above demographics information from singular summary .csv files 