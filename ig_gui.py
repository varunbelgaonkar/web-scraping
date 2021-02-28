from tkinter import *
from ig_analysis import get_post_links, get_post_info

root = Tk()
root.title("Instagram Profile analysis")
root.geometry("500x500")

def analyse():
	label_wait = Label(root, text = "Thanks for waiting!!", padx=10,pady=10)
	label_wait.grid(row=3,column=0, columnspan = 5)
	username = e_user.get()
	average_likes, top_5_hashtags, posts, followers, following = get_post_info(username)
	label_username = Label(root, text=username, padx=10, pady=10)
	label_likes = Label(root,text = average_likes, padx=10, pady=10)
	label_likes_msg = Label(root, text = "Average likes per post: ", padx=10, pady=10) 
	label_posts = Label(root, text = posts, padx = 10, pady = 10)
	label_followers = Label(root, text = followers, padx = 10, pady = 10)
	label_hashtags_m = Label(root, text = "Top 5 hashtags used", padx = 10, pady = 10)
	label_hashtags = Label(root, text = top_5_hashtags, padx = 10, pady = 10)

	label_username.grid(row=4, column = 0)
	label_posts.grid(row=4, column = 1)
	label_followers.grid(row=4, column=2)
	label_likes_msg.grid(row=5,column=0)
	label_likes.grid(row = 5, column = 1)
	label_hashtags_m.grid(row = 6, column = 0, columnspan = 5, sticky = "W")
	label_hashtags.grid(row = 7, column = 0, columnspan = 5, sticky = "W")


#creating widgets
label_m = Label(root, text = "Enter username of public profile only!!", 
				padx=10, pady = 10, fg = "red", font=('Ariel',15))
label_user = Label(root, text='Enter a username', 
				padx = 10, pady = 10, font=('Ariel',12))
e_user = Entry(root, width = 50, borderwidth = 5)
analyse_btn = Button(root, text='Analyse->', padx = 10, 
				pady = 10, font=('Ariel',12), command = analyse)

#placing widgets
label_m.grid(row=0, column=0, columnspan = 5)
label_user.grid(row=1, column=0)
e_user.grid(row = 1, column = 1, columnspan = 3)
analyse_btn.grid(row=2, column = 2)


root.mainloop()