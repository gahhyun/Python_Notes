import turtle
t = turtle.Turtle()
t.shape('turtle')

s = turtle.textinput("", "이름을 입력하시오")
t.write("인녕하세요" +s+"님, 거북이 인사드립니다")

turtle.exitonclick()