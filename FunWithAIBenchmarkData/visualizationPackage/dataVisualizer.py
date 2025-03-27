# File Name : dataVisualizer.py
# Student Name: Dylan Sams, Liam Vasey, Matthew Boutros
# email:  samsds@mail.uc.edu, vaseylh@mail.uc.edu, boutromw@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS 4010 001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment is about displaying an image of our team name and creating a visualization of the data using modularity.

# Brief Description of what this module does: This module reads AI benchmark data from a CSV file, generates bar chart when called by main
# Citations: We used chatgpt.com and chat.deepseek.com as our models

# Anything else that's relevant: Must pip install pandas and matplotlib
import csv
import pandas as pd
import matplotlib.pyplot as plt

def visualize_ai_scores_by_manufacturer():
    try:
        df = pd.read_csv('visualizationPackage/AI-Benchmarks.csv')  # Make sure this path is correct
        df = df[['Chipset Manufacturer', 'AI Score']].dropna()

        # Group by manufacturer and calculate average
        avg_scores = df.groupby('Chipset Manufacturer')['AI Score'].mean().sort_values(ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        avg_scores.plot(kind='bar')
        plt.title('Average AI Score by Chipset Manufacturer')
        plt.xlabel('Chipset Manufacturer')
        plt.ylabel('Average AI Score')
        plt.tight_layout()
        plt.show()
    
    except Exception as e:
        print(f"Error in visualize_ai_scores_by_manufacturer: {e}")
