#game_now.py (a princess gathering flowers)
# Xinyan Xiang
# a python game that uses arrow keys to move a pricness so that the princess can gather all flowers
# graphics.py is in the same directory as this file.

from graphics import*
from random import*
#queen class
class queen:
    def __init__(self, x_queen, y_queen, attribute, win):
        self.princess = Image(Point(x_queen,y_queen), attribute)
        self.image = self.princess.draw(win)
        self.rec = Rectangle(Point(x_queen-25,y_queen-39.5), Point(x_queen+25,y_queen+39.5))
        # self.rec.draw(win)
    def movequeen(self,key,win):
        if key == 'Up':
            self.image.move(0, 15)
            self.rec.move(0, 15)
        elif key == 'Down':
            self.image.move(0, -15)
            self.rec.move(0, -15)
        elif key == 'Right':
            self.image.move(15, 0)
            self.rec.move(15, 0)
        elif key == 'Left':
            self.image.move(-15, 0)
            self.rec.move(-15, 0)
    def not_move_queen(self,key,win,direction):
        if direction == "Up":
            if key == 'Up':
                self.image.move(0, 0)
                self.rec.move(0, 0)
            elif key == 'Down':
                self.image.move(0, -15)
                self.rec.move(0, -15)
            elif key == 'Right':
                self.image.move(15, 0)
                self.rec.move(15, 0)
            elif key == 'Left':
                self.image.move(-15, 0)
                self.rec.move(-15, 0)
        elif direction == "Down":
            if key == 'Up':
                self.image.move(0, 15)
                self.rec.move(0, 15)
            elif key == 'Down':
                self.image.move(0, 0)
                self.rec.move(0, 0)
            elif key == 'Right':
                self.image.move(15, 0)
                self.rec.move(15, 0)
            elif key == 'Left':
                self.image.move(-15, 0)
                self.rec.move(-15, 0)
        elif direction == "Right":
            if key == 'Up':
                self.image.move(0, 15)
                self.rec.move(0, 15)
            elif key == 'Down':
                self.image.move(0, -15)
                self.rec.move(0, -15)
            elif key == 'Right':
                self.image.move(0, 0)
                self.rec.move(0, 0)
            elif key == 'Left':
                self.image.move(-15, 0)
                self.rec.move(-15, 0)
        elif direction == "Left":
            if key == 'Up':
                self.image.move(0, 15)
                self.rec.move(0, 15)
            elif key == 'Down':
                self.image.move(0, -15)
                self.rec.move(0, -15)
            elif key == 'Right':
                self.image.move(15, 0)
                self.rec.move(15, 0)
            elif key == 'Left':
                self.image.move(0, 0)
                self.rec.move(0, 0)
            
    def getcenter(self):
        return self.rec.getCenter()

    def undraw_queen(self):
        self.image.undraw()

    def overlapping(self,flower):
        x_flower_left = flower.getFlower_x()-15
        x_flower_right = flower.getFlower_x()+15
        y_flower_left = flower.getFlower_y()-14
        y_flower_right = flower.getFlower_y()+14
        x_queen_left = self.getcenter().getX()-25
        x_queen_right = self.getcenter().getX()+25
        y_queen_left = self.getcenter().getY()-39.5
        y_queen_right = self.getcenter().getY()+39.5
        #if the flower overlaps the princess, it will return False. Otherwise, it will return True.
        if x_flower_left <= x_queen_left and x_flower_right <= x_queen_left:
            return True
        if x_flower_left >= x_queen_left and x_flower_right >= x_queen_right:
            return True
        if y_flower_left >= y_queen_right and y_flower_right >= y_queen_right:
            return True
        if y_flower_left <= y_queen_left and y_flower_right <= y_queen_left:
            return True
        else:
            return False
    #if the monster overlaps the princess, it will return False. Otherwise, it will return True.
    def overlapping_monster(self,monster):
        x_monster_left = monster.getMonster_x()-15
        x_monster_right = monster.getMonster_x()+15
        y_monster_left = monster.getMonster_y()-15
        y_monster_right = monster.getMonster_y()+20
        x_queen_left = self.getcenter().getX()-25
        x_queen_right = self.getcenter().getX()+25
        y_queen_left = self.getcenter().getY()-31.5
        y_queen_right = self.getcenter().getY()+31.5
        if x_monster_left <= x_queen_left and x_monster_right <= x_queen_left:
            return True
        if x_monster_left >= x_queen_left and x_monster_right >= x_queen_right:
            return True
        if y_monster_left >= y_queen_right and y_monster_right >= y_queen_right:
            return True
        if y_monster_left <= y_queen_left and y_monster_right <= y_queen_left:
            return True
        else:
            return False

# flower class
class flowers_class:
    def __init__(self, x, y , win):
        self.x = x
        self.y = y
        self.flowers = Image(Point(self.x, self.y), "f.png")
        self.flowers.draw(win)
        self.rec_f = Rectangle(Point(self.x-15,self.y-14), Point(self.x+15,self.y+14))
        # self.rec_f.draw(win)

    def un_draw_flowers(self):
        self.flowers.undraw()

    def getFlower_rec(self):
        return self.rec_f

    def getFlower_x(self):
        return self.x

    def getFlower_y(self):
        return self.y

# monster class
class monster_class:
    def __init__(self, x, y , win):
       self.x = x
       self.y = y
       self.monsters = Image(Point(self.x, self.y), "m.png")
       self.monsters.draw(win)
       self.rec_m = Rectangle(Point(self.x-15,self.y-20), Point(self.x+15,self.y+20))
       # self.rec_m.draw(win)

    def getMonster_rec(self):
        return self.rec_m

    def getcenter(self):
        return self.rec_m.getCenter()

    def getMonster_x(self):
        return self.rec_m.getCenter().getX()

    def getMonster_y(self):
        return self.rec_m.getCenter().getY()

    def move_monster_right(self,win):
        for i in range(3):
            self.monsters.move(5,0)
            self.rec_m.move(5,0)

    def move_monster_left(self,win):
        for i in range(3):
            self.monsters.move(-5,0)
            self.rec_m.move(-5,0)

    def monster_undraw(self):
        self.monsters.undraw()
        self.rec_m.undraw()

# call monster class and flower class to create flowers and monsters
def create_more_obstacles(win, change1, change2):
    locations = []
    obstacles_1 = []
    obstacles_2 = []
    # create flowers
    for i in range(10):
        row = randint(change1,change2)
        col = randint(0,8)
        location = [col*60+20, row*60+20]
        x = col*60+20
        y = row*60+20
        if location not in locations and x != 480 and y != 555:
            locations.append(location)
            flower1 = flowers_class(x, y, win)
            obstacles_1.append(flower1)
    #create monsters
    for i in range(8):
         row = randint(0,7)
         col = randint(change1,change2)
         location_2 = [col*60+20, row*60+20]
         x_2 = col*60+20
         y_2 = row*60+20
         if location_2 not in locations and x_2 != 480 and y_2 != 555:
              locations.append(location_2)
              monster1 = monster_class(x_2, y_2, win)
              obstacles_2.append(monster1)
    # return a list of flowers and a list of monsters in a tuple form.
    return (obstacles_1, obstacles_2)
# scree design before the game
def opendesign(win):
    message_click = Text(Point(280,150), "Click to play")
    message_click.setSize(28)
    message_click.setTextColor(color_rgb(51,187,255))
    message_click.draw(win)

    message_method = Text(Point(70,580), "How to play?")
    message_method.setSize(21)
    message_method.setTextColor(color_rgb(51,187,255))
    message_method.draw(win)

    message_key = Image(Point(80,500), "key.png")
    message_key.draw(win)

    message_move = Text(Point(360,500), "Use the keyboard to move the princess")
    message_move.setSize(21)
    message_move.setTextColor(color_rgb(51,187,255))
    message_move.draw(win)

    message_alert_monster = Text(Point(380,450), "Don't collide with monsters! They will eat you!")
    message_alert_monster.setSize(21)
    message_alert_monster.setTextColor(color_rgb(255,102,128))
    message_alert_monster.draw(win)

    message_alert_flower = Text(Point(300,350),  "Enjoy gathering flowers !")
    message_alert_flower.setSize(28)
    message_alert_flower.setTextColor(color_rgb(255,102,128))
    message_alert_flower.draw(win)
    p_mouse = win.getMouse()
    # the second page before the game: draw three princesses
    if p_mouse != None:
        rec_in_main = Rectangle(Point(0,0),Point(600,600))
        rec_in_main.setFill(color_rgb(255,230,234))
        rec_in_main.draw(win)
        rec_in_main.setOutline(color_rgb(255,230,234))
        princess_a = Image(Point(100,300), "ca.png")
        princess_a.draw(win)
        princess_b = Image(Point(300,300), "ba.png")
        princess_b.draw(win)
        princess_c = Image(Point(500,300), "oa.png")
        princess_c.draw(win)
        message_choose = Text(Point(300,550),"Type a, b, or c to choose your princess!")
        message_choose.setSize(23)
        message_choose.setTextColor(color_rgb(255,128,170))
        message_choose.draw(win)
        message_a = Text(Point(100,140),"a")
        message_a.setSize(23)
        message_a.setTextColor(color_rgb(255,128,149))
        message_a.draw(win)
        message_b = Text(Point(300,140),"b")
        message_b.setSize(23)
        message_b.setTextColor(color_rgb(255,128,149))
        message_b.draw(win)
        message_c = Text(Point(530,140),"c")
        message_c.setSize(23)
        message_c.setTextColor(color_rgb(255,128,149))
        message_c.draw(win)
        # get a key from a user: choose the princess he or she wants to play
        k_type = win.getKey()
        while k_type != "a" and k_type != "b" and k_type != "c":
            k_type = win.getKey()
        if k_type == "a":
            princess_choice = "c.png"
        elif k_type == "b":
            princess_choice = "b.png"
        elif k_type == "c":
            princess_choice = "o.png"
        # after finishing choosing the princess, draw a rectangle to cover all things before
        if k_type == "a" or k_type == "b" or k_type == "c":
            rec_in_main2 = Rectangle(Point(0,0),Point(600,600))
            rec_in_main2.setFill("white")
            rec_in_main2.setOutline("white")
            rec_in_main2.draw(win)
        # return user's choice
        return princess_choice
# a function that asks the user whether he or she wants to play agian or not
def play_more(win):
    mouse_again = None
    key_again = None
    win.checkMouse()
    win.checkKey()
# if user clicks, the game will continue. if the user types 'q', the game will be quitted.
    while not mouse_again and key_again != "q":
        mouse_again = win.checkMouse()
        key_again = win.checkKey()
    if mouse_again != None:
       return True
    return False

def main():
    win = GraphWin("game", 600,600)
    win.setCoords(0,0,600,600)
    play_more_game = True
    while play_more_game:
        rec_background = Rectangle(Point(0,0),Point(600,600))
        rec_background.setFill(color_rgb(204,255,153))
        rec_background.draw(win)
        pchoice = opendesign(win)
        ob = create_more_obstacles(win,0,8)
        ob_flowerss = ob[0]
        ob_monsterss = ob[1]
        ob_flower_number = len(ob_flowerss)
        attribute = pchoice
        qu = queen(480,565,attribute,win)
        # record user's score and flowers he or she has gathered
        score = 0
        flower_gathering = 0
        num_flower = Text(Point(85,580), "number of flowers:  ")
        num_flower.setSize(18)
        num_flower.setTextColor(color_rgb(255,128,149))
        num_flower.draw(win)
        num_flower_score = Text(Point(160,580), str(score))
        num_flower_score.setSize(18)
        num_flower_score.setTextColor(color_rgb(255,128,149))
        num_flower_score.draw(win)
        e_monster = True
        while e_monster:
            key = win.checkKey()
            # make sure that the princess is in the screen
            if qu.getcenter().getY() + 39.5 >= 605 and qu.getcenter().getX() - 25 >= 0 and qu.getcenter().getX() + 25 <= 600:
                qu.not_move_queen(key,win,"Up")
            elif qu.getcenter().getY() - 39.5 <= 0 and qu.getcenter().getX() - 25 >= 0 and qu.getcenter().getX() + 25 <= 600:
                qu.not_move_queen(key,win,"Down")
            elif qu.getcenter().getX() - 25 <= 0:
                qu.not_move_queen(key,win,"Left")
            elif qu.getcenter().getX() + 25 >= 600:
                qu.not_move_queen(key,win,"Right")
    
            else:
                qu.movequeen(key,win)
            for ob_flower in ob_flowerss:
                e = qu.overlapping(ob_flower)
                if e == False:
                    ob_flower.un_draw_flowers()
                    ob_flowerss.remove(ob_flower)
                    score = score + 1
                    flower_gathering = flower_gathering + 1
                    # update the user's score and number of flowers
                    num_flower_score.undraw()
                    num_flower_score.setText(str(score))
                    num_flower_score.draw(win)
            # move all monsters at the same time and move them randomly
            move_direction = randint(1,4)
            for ob_monster in ob_monsterss:
                #make sure that the monster will not move outside of the screen
                if move_direction % 2 == 0 and ob_monster.getMonster_x() <= 580:
                    ob_monster.move_monster_right(win)
                    # check whether user collides with a monster or whether they have gathered all flowers
                    # if the user collides with the monster or have gathered all flowers, the game end.
                    if not qu.overlapping_monster(ob_monster) or flower_gathering == ob_flower_number:
                        e_monster = False
                        break
                #make sure that the monster will not move outside of the screen
                elif move_direction % 2 == 1 and ob_monster.getMonster_x() >= 40:
                    ob_monster.move_monster_left(win)
                    if not qu.overlapping_monster(ob_monster) or flower_gathering == ob_flower_number:
                        e_monster = False
                        break
        # after the game ends, the screen will be updated.
        # if the user collides with the monster:
        if flower_gathering < ob_flower_number:
            rec_end = Rectangle(Point(0,0),Point(600,600))
            rec_end.setFill(color_rgb(255,230,234))
            rec_end.setOutline("white")
            rec_end.draw(win)
            message_end = Text(Point(300,400), "Oh no! The monster eats you!")
            message_end.setSize(23)
            message_end.setTextColor(color_rgb(51,187,255))
            message_end.draw(win)
            message_end_click = Text(Point(300,300), "type 'q' to quit or click to play again ")
            message_end_click.setSize(23)
            message_end_click.setTextColor(color_rgb(51,187,255))
            message_end_click.draw(win)
        # if the user has gathered all the flowers

        else:
            rec_end = Rectangle(Point(0,0),Point(600,600))
            rec_end.setFill(color_rgb(255,230,234))
            rec_end.setOutline("white")
            rec_end.draw(win)
            message_end = Text(Point(300,400), "Good job! You have successfully gathered all flowers!")
            message_end.setSize(23)
            message_end.setTextColor(color_rgb(51,187,255))
            message_end.draw(win)
            message_end_click = Text(Point(300,300), "type 'q' to quit or click to play again ")
            message_end_click.setSize(23)
            message_end_click.setTextColor(color_rgb(51,187,255))
            message_end_click.draw(win)
        # check whether the user wants to play agagin or not
        if win.isOpen():
            play_more_game = play_more(win)



    # win.getMouse()


main()
