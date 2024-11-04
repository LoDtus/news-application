from tkinter import *
from views.ItemPost import *
import controllers.GET as GET

def Content(master, movePage, Post):
    content = Frame(master)
    content.pack(side="top", fill='x', expand=True)
    
    def refeshPage():
        result = GET.getAllPost()
        
        if result:
            for widget in content.winfo_children():
                widget.destroy()

            posts = []
            for i in range(len(result)):
                posts.append({
                    "id": result[i]['id'],
                    "title": result[i]['title'],
                    "thumbnail": result[i]['thumbnail'],
                    "createdAt": result[i]['creationDate']
                })

            rows = {True: (len(posts)/3), False: ((len(posts) // 3) + 1)} [len(posts) % 3 == 0]
            index = 0
            for i in range(int(rows)):
                frame_perRow = Frame(content)
                frame_perRow.pack(expand=True, fill='x', anchor="w")
                
                for j in range(3):
                    if (index < len(result)):
                        item = ItemPost(
                            frame_perRow,
                            master,
                            movePage,
                            Post,
                            posts[index]['id'], 
                            posts[index]['title'], 
                            posts[index]['thumbnail'],
                            posts[index]['createdAt']
                        )
                        index += 1
                    else:
                        break

            for widget in content.winfo_children():
                for item in widget.winfo_children():
                    if hasattr(item, 'update_image'):
                        item.update_image(300)
        master.after(5000, refeshPage)
    
    refeshPage()
    return content