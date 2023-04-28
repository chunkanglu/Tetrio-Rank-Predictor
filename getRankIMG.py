from PIL import Image

def rank_img(rank_num):
    if (rank_num == 1):
        image = Image.open('RankImages/d.png')
    elif (rank_num == 2):
        image = Image.open('RankImages/c.png')
    elif (rank_num == 3):
        image = Image.open('RankImages/b.png')
    elif (rank_num == 4):
        image = Image.open('RankImages/a.png')
    elif (rank_num == 5):
        image = Image.open('RankImages/s.png')
    elif (rank_num == 6):
        image = Image.open('RankImages/ss.png')
    elif (rank_num == 7):
        image = Image.open('RankImages/u.png')
    elif (rank_num == 8):
        image = Image.open('RankImages/x.png')
    
    return image

