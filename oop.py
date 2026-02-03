class Instagram:
    def __init__(self,title, description,Creator_name,Location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.comments = []
        self.Creator_name = Creator_name
        self.Location = Location
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def display_comments(self):
        print("The commments are")
        for comment in self.comments:
            print('-',comment)
    def add_comment(self,comment):
        self.comments.append(comment) 
    def delete_comment(self):
        if len(self.comments)==0:
            print('No comments yet')
        else:
            temp=self.comments.pop() 
            print("\nThe Comment deleted is",temp)         
    def display_Creator_name(self):
        print("The Creator_name is",self.Creator_name)
    def display_Location(self):
        print("The Location is",self.Location)
        

reel1=Instagram("dancing","dancing with friends","Preetham","Hassan")# 0
reel1.disliked() #0
reel1.liked() #1


reel2=Instagram("finance minister conference","finance minister conference with friends","khushi","Mysuru")
reel1.liked() #2
# 0


reel1.add_comment('hi')
reel1.add_comment('gud')
reel1.display_comments()
reel1.display_Location()
reel1.display_Creator_name()
reel1.delete_comment()
reel1.display_comments()
