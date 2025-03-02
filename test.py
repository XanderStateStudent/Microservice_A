



message = input("Type alert message: ")

pipeline = open("pipeline.txt", 'w')


pipeline.write(message)

pipeline.close()