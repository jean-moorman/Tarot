day = 12
month = 1
year = 2000

arcana = []
arcana.append("The Fool")
arcana.append("The Magician")
arcana.append("The High Priestess")
arcana.append("The Empress")
arcana.append("The Emperor")
arcana.append("The Pope")
arcana.append("The Lovers")
arcana.append("The Chariot")
arcana.append("Justice")
arcana.append("The Hermit")
arcana.append("The Wheel of Fortune")
arcana.append("Strength")
arcana.append("The Hanged Man")
arcana.append("Death")
arcana.append("Temperance")
arcana.append("The Devil")
arcana.append("The Tower")
arcana.append("The Star")
arcana.append("The Moon")
arcana.append("The Sun")
arcana.append("Judgement")
arcana.append("The World")

def red(num):
    if num < 22:
        return num
    if num == 22:
        return 0
    sum, newNum = 0, num
    while newNum // 10 > 0 or newNum > 0:
        sum += newNum % 10
        #print("Added ", newNum % 10, " to sum.")
        newNum = newNum // 10
        #print("newNum: ", newNum)
    return red(sum)

def redv2(num): #for house 8 calculations
    if num < 10 or num == 11 or num == 22:
        return num
    sum, newNum = 0, num
    while newNum // 10 > 0 or newNum > 0:
        sum += newNum % 10
        #print("Added ", newNum % 10, " to sum.")
        newNum = newNum // 10
        #print("newNum: ", newNum)
    return redv2(sum)

houses = [None]*13
houses[1] = red(day)
houses[2] = month
houses[3] = red(year)
houses[4] = red(houses[1] + houses[2] + year)
houses[5] = red(houses[1] + houses[2] + houses[3] + houses[4])

houses[6] = red(houses[1] + houses[2])
houses[7] = red(abs(houses[3] - houses[2]))
houses[8] = red(houses[6] + redv2(2021))

houses[9] = red(houses[6] + houses[7])
houses[10] = 0 if houses[9] == 0 else 22 - houses[9]
houses[11] = red(houses[7] + houses[3] + houses[10])
houses[12] = red(houses[4] + houses[2] + houses[6])

houses[0] = red(houses[3] + houses[2] + houses[4] + houses[5] + houses[5] + houses[9] + houses[1] + houses[11] + houses[12])

for h in range(len(houses)):
    print("House #%d: "%h, arcana[houses[h]])