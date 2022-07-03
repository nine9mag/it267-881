class Movie:
    def __init__(self) -> None:
        #ตัวแปร protected ขึ้นต้นด้วย underscore 1 ครั้ง
        self._title = None
        self._year = None
        self._genre = None

    #เมธอด protected ขึ้นต้นด้วย underscore 1 ครั้ง
    def _add_movie(self,title:str,year:int,genre:str):
        self._title = title
        self._year = year
        self._genre = genre

    def _getmovie_detail(self):
        print(f'Title: {self._title}')
        print(f'Year: {self._year}')
        print(f'Genre: {self._genre}')

#อยู่ในไฟล์เดียวกันไม่ต้องimport
class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self) #super().__init__() ไม่ต้องมี self

    def add_channel(self,ch:str):
        self.channel = ch

    def _getmovie_detail(self):
        #super()._getmovie_detail()
        Movie._getmovie_detail(self)
        print(f'Channel: {self.channel}')


#สร้าง obj
if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie('Thor Love and Thunder',2022,'Fantasy')
    m1.add_channel('Disney Plus')
    m1._getmovie_detail() #เรียกใช้ของ Documentary 