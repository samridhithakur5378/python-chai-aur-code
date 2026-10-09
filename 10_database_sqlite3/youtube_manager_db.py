import sqlite3
con=sqlite3.connect('youtube_videos.db')
cursor=con.cursor()

cursor.execute(''' 
   CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
  )
         
''')


def list_video():
   cursor.execute("SELECT * FROM videos")
   for row in cursor.fetchall():
      print(row)

def add_video(video_id,name,time):
  cursor.execute("INSERT INTO VIDEOS(name,time) values(?,?)",(name,time))
  con.commit()
  

def update_video(video_id,new_name,new_time):
  cursor.execute("UPDATE videos SET name=?, time = ? WHERE id =?",(new_name, new_time,video_id))
  con.commit()

def delete_video(video_id):
  cursor.execute("DELETE FROM videos where id=?",(video_id,))
  con.commit()



def main():
  while True:
    print("\n Youtube manager with DB")
    print("1. List videos")
    print("2. Add videos")
    print("3. Update videos")
    print("4. Delete videos")
    print("5. Exit videos")
    choice = input("enter your choice:")

    if choice =="1":
      list_video()
    elif choice =="2":
      name= input("enter the video name")
      time= input("enter the video time")
      add_video(name,time)
    elif choice == "3":
      video_id=input("enter video ID to update:")
      name=input("Enter the video name:")
      time=input("Enter the video time:")
      add_video(video_id,name,time)
    elif choice == "4":
      video_id=input("enter video ID to delete:")
      delete_video(video_id)
    elif choice == "5":
       break
    else:
      print("Invalid choice")

  con.close()




if __name__ =="__main__":
  main()

#can make better still some bugs need to debug
