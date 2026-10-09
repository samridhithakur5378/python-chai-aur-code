
import json
# JSON stands for JavaScript Object Notation. It's a format used to store and exchange data. Python can easily convert its lists and dictionaries into JSON and back again.

def load_data():#Purpose: Retrieve previously saved videos.
  try:
    with open('youtube.txt','r') as file:
       test = json.load(file)
       return test
  except FileNotFoundError:
    return []


def save_data_helper(videos):
  with open('youtube.txt','w') as file:
    json.dump(videos,file)#json.dump() is used to take Python data and write it into a file in JSON format.
    

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos, start=1):
      print(f"{index}.{video['name']},Duration:{video['time']}") 
    print("\n")
    print("*"*70)

def add_videos(videos):
  name= input("enter video name:")
  time=input("enter video time: ")
  videos.append({'name':name,'time':time})#adds a new item to the end 
  save_data_helper(videos)

def update_videos(videos):
  list_all_videos(videos)
  index=int(input("enter the video number to update"))
  if 1<=index <= len(videos):
    name=input("enter the new video name:")
    time=input("enter the new video time:")
    videos[index - 1] = {'name':name,'time':time}
    save_data_helper(videos)
  else:
    print("invalid index selected")

def delete_videos(videos):
  list_all_videos(videos)
  index=int(input("enter the video number to be deleted"))

  if 1<= index <=len(videos):
    del videos[index-1]
    save_data_helper(videos)
  else:
    print('invalid video index selected')

def main():
    videos=load_data()#file mein ja ke data load karega
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List a favourite videos")
        print("2. Add a  youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice=input("Enter your choice")
        print(videos)

        match choice:#This is Python's match...case statement, which lets you execute different code depending on the value of a variable.
          case'1':
            list_all_videos(videos)
          case'2':
            add_videos(videos)
          case'3':
            update_videos(videos)
          case'4':
            delete_videos(videos)
          case'5':
            break
          case _:
              print("Invalid Choice")

if __name__ == "__main__":
  main()


 