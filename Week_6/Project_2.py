import tkinter as tk
from tkinter import messagebox, StringVar
from tkinter import *

def button_click():

    messagebox.showinfo("PAU Admission Portal", "Welcome to the PAU admissions portal. \nLet's proceed.")

root = tk.Tk()
root.title("JAMB Admission Portal")
root.geometry("500x300")
root.config(bg = "Green")
root.iconbitmap("C:\\Users\\there\\OneDrive\\Desktop\\tracyjamesCOS102\\Week_6\\OIP.jpeg")

label = tk.Label(root, text = "Input your JAMB score, \nyour department of choice, \nand the number of credits from your O Levels.")
label.pack()
label.config(fg = "White", bg = "Green")

score = tk.Label(root, text = "Your JAMB Score")
score.pack()
score.config(fg = "White", bg = "Green")
score_input = tk.Entry(root)
score_input.pack()

department = tk.Label(root, text = "Department")
department.pack()
department.config(fg = "White", bg = "Green")
department_input = tk.Entry(root)
department_input.pack()

def process():
    score = int(score_input.get())
    department = department_input.get()

    for department in "Computer Science":
        
        if score >= 250:
            messagebox.showinfo("Interview", "Let us proceed to the interview.")

            interview = tk.Tk()
            interview.title("JAMB Interview Stream")
            interview.geometry("500x400")
            interview.config(bg = "Green")
            interview.iconbitmap("C:\\Users\\there\\OneDrive\\Desktop\\tracyjamesCOS102\\Week_6\\OIP.jpeg")

            def submit(interview, text):
                 label_1 = submit(interview, text = grade.get())
                 label_1.pack()

            interview_label = tk.Label(interview, text = "Welcome to interview stream. \nWe will simply ask a few questions to proceed with you application. \nLet's proceed.")
            interview_label.pack()
            interview_label.config(fg = "White", bg = "Green")
            
            grade_options = {
                "A",
                "B",
                "C",
                "D",
                "E",
                "F"
            }

            grade = StringVar()
            grade.set(grade_options[0])

            maths_label = tk.Label(interview, text = "Mathematics")
            maths_label.pack()
            maths_label.config(fg = "White", bg = "Green")
            maths = OptionMenu(interview, grade, *grade_options)
            maths.pack()

            english_label = tk.Label(interview, text = "English")
            english_label.pack()
            english_label.config(fg = "White", bg = "Green")
            english = OptionMenu(interview, grade, *grade_options)
            english.pack()

            biology_label = tk.Label(interview, text = "Biology")
            biology_label.pack()
            biology_label.config(fg = "White", bg = "Green")
            biology = OptionMenu(interview, grade, *grade_options)
            biology.pack()

            chemistry_label = tk.Label(interview, text = "Chemistry")
            chemistry_label.pack()
            chemistry_label.config(fg = "White", bg = "Green")
            chemistry = OptionMenu(interview, grade, *grade_options)
            chemistry.pack()

            physics_label = tk.Label(interview, text  = "Physics")
            physics_label.pack()
            physics_label.config(fg = "White", bg = "Green")
            physics = OptionMenu(interview, grade, *grade_options)
            physics.pack()

            submission = tk.Button(interview, text = "Submit", command = submit)
            submission.pack()

            admitted = []
            notadmitted = []

            if maths and english and biology and chemistry and physics == ("A" or "B" or "C"):
                    messagebox.showinfo("Accepted", "Congratulations! \nYou are eligible for an admission.")

                    admitted.append(maths)
                    admitted.append(english)
                    admitted.append(biology)
                    admitted.append(chemistry)
                    admitted.append(physics)
                    admitted.append(interview)
                    ("student information: , admitted")


            elif maths and english and biology and chemistry and physics == ("D" or "E" or "F"):
                    messagebox.showinfo("Rejected", "Unfortunately, you are not ineligible for an admission.")

                    notadmitted.append(maths)
                    notadmitted.append(english)
                    notadmitted.append(biology)
                    notadmitted.append(chemistry)
                    notadmitted.append(physics)
                    notadmitted.append(interview)
                    ("student information: , not admitted")

            interview.mainloop()
        
        elif score < 250:
            messagebox.showinfo("Application Rejected", "Sadly, you don't qualify for an interview.")
       
        else:
            messagebox.showerror("Error", "There seems to be a problem with your input. \nDo well to correct it.")
        
        break
    
    for department in "Mass Communication":
        
        if score >= 230:
            messagebox.showinfo("Interview", "Let us proceed to the interview.")

            interview = tk.Tk()
            interview.title("JAMB Interview Stream")
            interview.geometry("300x300")
            interview.config(bg = "Green")
            interview.iconbitmap("C:\\Users\\there\\OneDrive\\Desktop\\tracyjamesCOS102\\Week_6\\OIP.jpeg")
            
            def submit(interview, text):
                 label_1 = submit(interview, text = grade.get())
                 label_1.pack()
                 
            interview_label = tk.Label(interview, text = "Welcome to interview stream. \nWe will simply ask a few questions to proceed with you application. \nLet's proceed.")
            interview_label.pack()
            interview_label.config(fg = "White", bg = "Green")

            grade_options = [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F"
            ]

            grade = StringVar()
            grade.set(grade_options[0])

            maths_label = tk.Label(interview, text = "Mathematics")
            maths_label.pack()
            maths_label.config(fg = "White", bg = "Green")
            maths = OptionMenu(interview, grade, *grade_options)
            maths.pack()

            english_label = tk.Label(interview, text = "English")
            english_label.pack()
            english_label.config(fg = "White", bg = "Green")
            english = OptionMenu(interview, grade, *grade_options)
            english.pack()

            biology_label = tk.Label(interview, text = "Biology")
            biology_label.pack()
            biology_label.config(fg = "White", bg = "Green")
            biology = OptionMenu(interview, grade, *grade_options)
            biology.pack()

            literature_label = tk.Label(interview, text = "Literature-in-English")
            literature_label.pack()
            literature_label.config(fg = "White", bg = "Green")
            literature = OptionMenu(interview, grade, *grade_options)
            literature.pack()

            government_label = tk.Label(interview, text = "Government")
            government_label.pack()
            government_label.config(fg = "White", bg = "Green")
            government = OptionMenu(interview, grade, *grade_options)
            government.pack()

            if maths and english and biology and literature and government == ("A" or "B" or "C"):
                messagebox.showinfo("Accepted", "Congratulations! \nYou are eligible for an admission.")

                admitted.append(maths)
                admitted.append(english)
                admitted.append(biology)
                admitted.append(literature)
                admitted.append(government)
                admitted.append(interview)
                ("student information: , admitted")

            elif maths and english and biology and literature and government == ("D" or "E" or "F"):
                messagebox.showinfo("Rejected", "Unfortunately, you are not ineligible for an admission.")

                notadmitted.append(maths)
                notadmitted.append(english)
                notadmitted.append(biology)
                notadmitted.append(literature)
                notadmitted.append(government)
                notadmitted.append(interview)
                ("student information: , not admitted")


            submission = tk.Button(interview, text = "Submit", command = submit)
            submission.pack()

            interview.mainloop()
        
        elif score < 230:
            messagebox.showinfo("Application Rejected", "Sadly, you don't qualify for an interview.")
        
        else:
            messagebox.showerror("Error", "There seems to be a problem with your input. \nDo well to correct it.")
        
        break

proceed = tk.Button(root, text = "Continue", command = process)
proceed.pack()

root.mainloop()