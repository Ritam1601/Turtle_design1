import turtle as t
import colorsys as c
t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
t.color('black')
t.hideturtle()
for j in range(10):
	for k in range(15):
		for i in range(2):
			t.pencolor(c.hsv_to_rgb((j)/40,i/2,1))
			t.circle(200-j*4,90)
			t.lt(90)
		t.circle(1,24)
t.penup()
t.lt(90)
t.fd(1)
t.pendown()
for i in range (4):
	for i in range(18):
		t.pencolor(c.hsv_to_rgb(i/18,1,1))
		t.penup()
		t.fd(250)
		t.rt(90)
		t.pendown()
		for i in range(2):
			t.fd(250)
			t.rt(90)
		t.penup()
		t.fd(250)
		t.rt(90)
		t.rt(20)
	t.rt(5)
t.exitonclick()

