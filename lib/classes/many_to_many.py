class Article:
    def __init__(self, author, magazine, title):

        if not isinstance(author,Author):
            raise TypeError("author must be of type Author")
        if not isinstance(magazine,Magazine):
            raise TypeError("magazine must be of type Magazine")
        

        self._author = author
        self._magazine = magazine
        self.title = title

    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine

    
    @magazine.setter
    def magazine(self,new_magazine):
        if not isinstance(new_magazine,Magazine):
            raise TypeError("magazine must be of type Magazine")
        self._magazine = new_magazine


    @author.setter
    def author(self,new_author):
        if not isinstance(new_author,Author):
            raise TypeError("author must be of type Author")
        self._author = new_author

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def display_info(self):
       print(f"This is {self.name}")

    def articles(self):
        return self._articles



    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self,magazine,title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        categories =  list({magazine.topic for magazine in self.magazines()})

        if categories:
            return categories
        else:
            return None
         
   

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):

        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)


    def display_info(self):
        print(f"it is a {self.name} magazine in the {self.category} category.")

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if self._articles:
            return [article.title for article in self._articles]
        return None

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author,0) + 1

            authors_with_more_than_two_articles = [
                author for author, count in author_count.items() if count > 2
            ]
            return authors_with_more_than_two_articles if authors_with_more_than_two_articles else None


     
    @classmethod
    def top_publisher(cls):
            if not cls._all_magazines:
                return None
            return max(cls._all_magazines,key=lambda magazine: len(magazine._articles),default=None)

#Test cases
magazine1 = Magazine("Tech world","Technolgy")
magazine2 = Magazine("Daily Nation","Newspaper")


author1 = Author("Carry Bradshaw")
author1.add_article(magazine1,"Ai Advancements")
author1.add_article(magazine1,"Tech for All")
author1.add_article(magazine2,"Daily Insigths")
author1.add_article(magazine1,"Ai in 2024")


print("Article Titles for Tech world:",magazine1.article_titles())

print("Contributing Authors for Tech World:",magazine1.contributing_authors())
top_magazine = Magazine.top_publisher()

print("Top Publisher:",top_magazine.name if top_magazine else "None")

