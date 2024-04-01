# print ("\n" + "=========================DATABASE APPLICATION=========================" + "\n")

user_msg = """
choose operation you want
'a' => add skills
's' => show skills
'u' => update skills
'd' => delete skills 
'q' => quit programme
"""

import sqlite3

def add_skills():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS skills(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            skill TEXT NOT NULL,
            progress INTEGER NOT NULL
        )
        """)
    
    input_name = input("enter your name : ").capitalize()
    input_skill = input("enter a skill e.g(html, c++, hobits) : ")
    input_progress = int(input(f"enter progress to skill {input_skill} : "))
    
    cur.execute(f"INSERT INTO skills(name, skill, progress) VALUES('{input_name}', '{input_skill}', {input_progress})")
    db.commit()
    print(f"Hello {input_name}, your skill {input_skill} and progress {input_progress} are Added successfully")
    
    check_msg = input("Do you want to add any other items? press(yes / no) : ").lower()
    if check_msg == "yes" :
        return add_skills()
    
    elif check_msg == "no" :
        print("Programme Closed")
        db.close()
        
    else :
        print("Wrong Value, Try Again")
        return add_skills()

def show_skills():
    
    input_name = input("enter your name : ").capitalize()
    cur.execute(f"SELECT * FROM skills WHERE name = '{input_name}'")
    data = cur.fetchall()
    for row in data :
        print(row)

def update_skills():
    
    check_msg = input("which data you want to update press(name, skill or progress), press all to update all data : ").lower()
    
    if check_msg == "name" :
        input_old_name = input("Enter Your Old Name : ").capitalize()
        input_new_name = input("Enter The New Name : ").capitalize()
        cur.execute(f"UPDATE skills SET name = '{input_new_name}' WHERE name = '{input_old_name}'")
        db.commit()
        
    elif check_msg == "skill" :
        input_name = input("Enter the name whose skill you want to update: ").capitalize()
        input_new_skill = input("enter a new skill : ")
        cur.execute(f"UPDATE skills SET skill = '{input_new_skill}' WHERE name = '{input_name}'")
        db.commit()
        
    elif check_msg == "progress" :
        input_name = input("Enter the name whose skill you want to update: ").capitalize()
        input_new_progress = int(input(f"enter progress to skill '{input_new_skill}' : "))
        cur.execute(f"UPDATE skills SET progress = {input_new_progress} WHERE name = '{input_name}'")
        db.commit()
        
    elif check_msg == "all" :
        input_old_name = input("Enter Your Old Name : ").capitalize()
        input_new_name = input("Enter The New Name : ").capitalize()
        input_new_skill = input("enter a new skill : ")
        input_new_progress = int(input(f"enter progress to skill '{input_new_skill}' : "))
        cur.execute(f"UPDATE skills SET name = '{input_new_name}', skill = '{input_new_skill}', progress = {input_new_progress} WHERE name = '{input_old_name}'")
        db.commit()
        
    else :
        print("Wrong Value, Try Again")
        return update_skills()
    print("Information Updated")

def delete_skills() :
    
    check_msg = input("data will be deleted, are you sure. Write down (yes / no) :").lower()
    
    if check_msg == "yes" :
        input_name = input("enter your name : ").capitalize()
        cur.execute(f"DELETE FROM skills WHERE name = '{input_name}'")
        db.commit()
        print("Data is Deleted")
        
    elif check_msg == "no" :
        print("Operation Canceled")
        
    else :
        print("wrong value, Try Again")
        return delete_skills()

user_input = input(f"{user_msg}\n => ").lower()

operation_list = ["a", "s", "u", "d", "q"]

db = sqlite3.connect("skills_data.db")
cur = db.cursor()

if user_input in operation_list :
    
    if user_input == "a" :
        add_skills()
    elif user_input == "s" :
        show_skills()
    elif user_input == "u" :
        update_skills()
    elif user_input == "d" :
        delete_skills()
    else :
        print("programmes is closed")
else :
    print("wrong operation")

db.close()