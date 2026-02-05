class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def dispaly_book(self):
        print("Title is",self.title)  
        print("Author is",self.author)  

class issued_book(book):
    def __init__(self, title, author,iss_to,iss_date):
        self.iss_to=iss_to
        self.iss_date=iss_date
        super().__init__(title, author)
    def issued_book_details(self):
        super().dispaly_book()
        print("Issued to",self.iss_to)     
        print("Issued on",self.iss_date)

obj=issued_book("Python",'Jhon',"Preetham",'4th Feb')
obj.issued_book_details()